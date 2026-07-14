# -*- coding: utf-8 -*-
"""
Siembra de datos (Mock Data) para ambos entornos.
Inyecta usuarios/productos/resenas/ordenes falsos para que los ataques de
profundidad (UC-02+) tengan datos reales que recorrer.

Autocontenido: como la copia NO incluye node_modules, el contenedor del seeder
genera el cliente Prisma de cada microservicio, crea el esquema (prisma db push)
e instala faker ANTES de ejecutar seed.js. Todo se genera dentro del contenedor
Linux para que los binarios del motor Prisma sean los correctos.

Aislado del proyecto original: cada entorno usa su propio proyecto de Docker
(COMPOSE_PROJECT_NAME en su .env) y, por tanto, su propia red y volumenes.
"""
import os, subprocess, sys, time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# entorno -> nombre de proyecto Docker (debe coincidir con su .env)
ENVS = {
    "E-commerce": "exp-vulnerable",
    "E-commerce-controles": "exp-protegido",
}

# Comando que corre DENTRO del contenedor node:18-slim (Linux).
SEED_SH = r'''set -e
echo "[seed] Instalando openssl (requerido por el motor de Prisma)..."
apt-get update -qq >/dev/null 2>&1 && apt-get install -y -qq openssl >/dev/null 2>&1
prep() {
  ms="$1"; url="$2"; kind="$3"
  echo "[seed] === $ms : npm install + prisma generate + db push ==="
  cd "/app/$ms"
  npm install --no-audit --no-fund --loglevel=error
  DATABASE_URL="$url" npx --yes prisma generate
  if [ "$kind" = "pg" ]; then
    DATABASE_URL="$url" npx --yes prisma db push --skip-generate --accept-data-loss
  else
    DATABASE_URL="$url" npx --yes prisma db push --skip-generate --accept-data-loss || echo "[seed] (mongo db push best-effort)"
  fi
}
prep ms-usuarios "$USUARIOS_DATABASE_URL" pg
prep ms-catalogo "$CATALOGO_DATABASE_URL" mongo
prep ms-resenas  "$RESENAS_DATABASE_URL"  pg
prep ms-ordenes  "$ORDENES_DATABASE_URL"  pg
echo "[seed] === root npm install (para @faker-js/faker) ==="
cd /app && npm install --no-audit --no-fund --loglevel=error
echo "[seed] === Ejecutando seed.js ==="
cd /app/seeder && node seed.js
echo "[seed] DONE OK"
'''


def run(cmd, **kw):
    return subprocess.run(cmd, **kw)


def up_databases(env_path):
    """Levanta postgres/mongo/mongo-init esperando a que esten sanos, con reintento."""
    for attempt in range(1, 4):
        r = run(["docker-compose", "up", "-d", "--wait", "--wait-timeout", "240",
                 "postgres-db", "mongo-db", "mongo-init"], cwd=env_path)
        if r.returncode == 0:
            return True
        print(f"[WARN] Las BD no quedaron sanas (intento {attempt}/3). Limpiando y esperando...")
        # Limpieza total + espera amplia: al recrear mongo demasiado rapido, el
        # archivo /data/db/mongod.lock del intento previo puede seguir tomado
        # (DBPathInUse, exitCode 100). Esperar evita esa carrera de reinicio.
        run(["docker-compose", "down", "-v", "--remove-orphans"], cwd=env_path)
        time.sleep(12)
    return False


def main():
    for env, project in ENVS.items():
        print(f"\n{'='*60}\nPreparando MOCK DATA para {env} (proyecto={project})\n{'='*60}")
        env_path = os.path.join(BASE_DIR, env)
        network = f"{project}_ecommerce-net"  # red que crea docker-compose para este proyecto

        run(["docker-compose", "down", "-v", "--remove-orphans"], cwd=env_path)

        if not up_databases(env_path):
            print(f"[ERROR] No se pudieron levantar las BD de {env}. Se omite este entorno.")
            continue

        cmd = [
            "docker", "run", "--rm", "-v", f"{env_path}:/app", "--network", network,
            "-e", "USUARIOS_DATABASE_URL=postgresql://postgres:password@postgres-db:5432/usuarios?schema=public",
            "-e", "CATALOGO_DATABASE_URL=mongodb://mongo-db:27017/catalogo?replicaSet=rs0&directConnection=true",
            "-e", "RESENAS_DATABASE_URL=postgresql://postgres:password@postgres-db:5432/resenas?schema=public",
            "-e", "ORDENES_DATABASE_URL=postgresql://postgres:password@postgres-db:5432/ordenes?schema=public",
            "node:18-slim", "bash", "-c", SEED_SH,
        ]
        r = run(cmd, cwd=env_path)
        if r.returncode == 0:
            print(f"[OK] Mock Data generada para {env}")
        else:
            print(f"[ERROR] La siembra de {env} fallo (codigo {r.returncode}).")

        run(["docker-compose", "down"], cwd=env_path)

    print("\nProceso de siembra finalizado.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[CANCELADO] Siembra interrumpida por el usuario.")
        sys.exit(1)
