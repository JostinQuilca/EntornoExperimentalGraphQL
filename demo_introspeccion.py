# -*- coding: utf-8 -*-
"""
Evidencia del control de introspeccion (UC-01) — Opcion A.

Levanta cada entorno por separado, envia la MISMA query de introspeccion y
captura la respuesta, para demostrar el contraste:
  - VULNERABLE  -> HTTP 200 + esquema completo expuesto (ataque exitoso).
  - PROTEGIDO   -> HTTP 400/403 + "introspection not allowed" (ataque bloqueado,
                   esquema OCULTO).

Guarda la evidencia en pruebas/UC01_evidencia_bloqueo_introspeccion.md.

NO ejecutar mientras corre uc01_runner.py (ambos usan el puerto 4000).
"""
import os, subprocess, time, json, urllib.request, urllib.error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GW = "http://localhost:4000/graphql"
QUERY = {"query": "query AtaqueIntrospeccion { __schema { queryType { name } types { name } } }"}

ENVS = [
    ("VULNERABLE", "E-commerce"),
    ("PROTEGIDO",  "E-commerce-controles"),
]


def wait_gateway(timeout_s=200):
    """Espera hasta que el gateway responda (cualquier status = arriba)."""
    for _ in range(timeout_s // 2):
        time.sleep(2)
        try:
            req = urllib.request.Request(GW, data=b'{"query":"{ __typename }"}',
                                         headers={"Content-Type": "application/json"}, method="POST")
            urllib.request.urlopen(req, timeout=5)
            return True
        except urllib.error.HTTPError:
            return True  # respondio con error HTTP => esta arriba
        except Exception:
            pass
    return False


def query_introspection():
    data = json.dumps(QUERY).encode()
    req = urllib.request.Request(GW, data=data,
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        r = urllib.request.urlopen(req, timeout=15)
        return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, f"(sin respuesta: {e})"


def main():
    results = []
    for label, folder in ENVS:
        path = os.path.join(BASE_DIR, folder)
        print(f"\n{'='*60}\n  {label}  ({folder})\n{'='*60}")
        subprocess.run(["docker-compose", "up", "-d", "--wait", "--wait-timeout", "240"], cwd=path)
        print("  Esperando al gateway...")
        wait_gateway()
        time.sleep(3)
        status, body = query_introspection()
        expuesto = (status == 200 and "__schema" in body and '"errors"' not in body)
        n_tipos = body.count('"name"') if expuesto else 0
        veredicto = ("ESQUEMA EXPUESTO (ataque exitoso)" if expuesto
                     else "BLOQUEADO — esquema OCULTO (control efectivo)")
        print(f"  HTTP {status} | {veredicto}")
        print(f"  Respuesta (primeros 350 chars):\n  {body[:350]}")
        results.append({"label": label, "status": status, "expuesto": expuesto,
                        "n_tipos": n_tipos, "body": body[:600]})
        subprocess.run(["docker-compose", "down"], cwd=path)

    # Guardar evidencia en Markdown
    out_dir = os.path.join(BASE_DIR, "pruebas")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "UC01_evidencia_bloqueo_introspeccion.md")
    lines = ["# UC-01 — Evidencia del control de introspeccion\n",
             "Misma query de introspeccion enviada a ambos entornos:\n",
             "```graphql\n" + QUERY["query"] + "\n```\n",
             "| Entorno | HTTP | Esquema expuesto | Veredicto |",
             "| :--- | :---: | :---: | :--- |"]
    for r in results:
        v = "SI" if r["expuesto"] else "NO"
        ver = "Ataque exitoso" if r["expuesto"] else "Ataque bloqueado (control efectivo)"
        lines.append(f"| {r['label']} | {r['status']} | {v} | {ver} |")
    lines.append("\n## Respuestas capturadas\n")
    for r in results:
        lines.append(f"### {r['label']} (HTTP {r['status']})\n```json\n{r['body']}\n```\n")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\n[OK] Evidencia guardada en: {out}")


if __name__ == "__main__":
    main()
