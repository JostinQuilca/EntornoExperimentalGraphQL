# -*- coding: utf-8 -*-
"""
Siembra de datos (Mock Data) para ambos entornos.
Inyecta usuarios/productos/resenas falsos con el seeder de Node+Prisma para que
los ataques de profundidad (UC-02+) tengan datos reales que recorrer.

Aislado del proyecto original: cada entorno usa su propio proyecto de Docker
(COMPOSE_PROJECT_NAME en su .env) y, por tanto, su propia red.
"""
import os, subprocess, time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# entorno -> nombre de proyecto Docker (debe coincidir con su .env)
ENVS = {
    "E-commerce": "exp-vulnerable",
    "E-commerce-controles": "exp-protegido",
}

for env, project in ENVS.items():
    print(f"Preparando MOCK DATA para {env} (proyecto={project})...")
    env_path = os.path.join(BASE_DIR, env)
    network = f"{project}_ecommerce-net"  # red que crea docker-compose para este proyecto

    # Levantar solo las bases de datos
    subprocess.run(["docker-compose", "down", "-v", "--remove-orphans"], cwd=env_path)
    subprocess.run(["docker-compose", "up", "-d", "postgres-db", "mongo-db", "mongo-init"], cwd=env_path)
    print("Esperando 15s a que las DB inicien...")
    time.sleep(15)

    cmd = [
        "docker", "run", "--rm", "-v", f"{env_path}:/app", "--network", network,
        "-e", "USUARIOS_DATABASE_URL=postgresql://postgres:password@postgres-db:5432/usuarios?schema=public",
        "-e", "CATALOGO_DATABASE_URL=mongodb://mongo-db:27017/catalogo?directConnection=true",
        "-e", "RESENAS_DATABASE_URL=postgresql://postgres:password@postgres-db:5432/resenas?schema=public",
        "-e", "ORDENES_DATABASE_URL=postgresql://postgres:password@postgres-db:5432/ordenes?schema=public",
        "node:18-slim", "bash", "-c", "cd /app/seeder && npm install && node seed.js"
    ]
    subprocess.run(cmd, cwd=env_path)
    print(f"Mock Data generada para {env}")
    subprocess.run(["docker-compose", "down"], cwd=env_path)

print("Todas las BD sembradas con exito.")
