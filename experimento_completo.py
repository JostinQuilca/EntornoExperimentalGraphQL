# -*- coding: utf-8 -*-
"""
Corrida completa del experimento (UC-01 a UC-05, entornos vulnerable y protegido).

A diferencia de night_runner.py, la rejilla de escenarios de aqui es la del
diseno documentado en la Guia_Variables: cada caso de uso tiene su propia
variable independiente y no un producto cartesiano de niveles por VUs.

La corrida es reanudable: un escenario cuyo reporte ya esta en disco se salta.
Cortarla con Ctrl+C y relanzarla mas tarde continua donde se quedo, que es
imprescindible en una tanda que dura casi veinte horas.

Uso:
    python experimento_completo.py --simular          # plan y estimacion, sin ejecutar
    python experimento_completo.py                    # corrida completa
    python experimento_completo.py --solo UC-02       # un solo caso de uso
    python experimento_completo.py --entorno Protegido
"""
import argparse
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import uc_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPLICAS = 3          # R1-R3
CARGAS = [1, 2, 3, 5, 8]   # escala comun a la mayoria de casos de uso
# UC-04 necesita llegar mas alto: el control de complejidad bloquea a partir de
# 334 alias (complejidad 3xN > 1000) y el primer Fibonacci que lo cruza es 377.
# Con la escala corta el bloqueo nunca aparece; con esta si.
FIBONACCI = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

# Duracion mediana de una replica medida sobre 606 intervalos de corridas
# anteriores en esta misma maquina. Solo se usa para estimar, se recalcula
# con los tiempos reales en cuanto hay escenarios completados.
SEG_POR_REPLICA = 124


# ─────────────────────────────────────────────────────────────
# DISENO EXPERIMENTAL  (unica fuente de verdad de la rejilla)
#
# escenarios: lista de (vus, nivel). Cada caso de uso mueve UNA variable
# independiente y deja fija la otra, tal como esta descrito en Guia_Variables.
# ─────────────────────────────────────────────────────────────
DISENO = {
    "UC-01": {
        "nombre":  "UC-01: Introspección Pasiva",
        "dir":     "UC01_introspeccion",
        "script":  "uc01_stress_introspeccion.js",
        "iso":     "A.8.12",
        "amenaza": "Reconocimiento",
        # La carga es el numero de VUs; el nivel queda fijo en 1.
        "escenarios": [(v, 1) for v in CARGAS],
        "carga":   lambda vus, niv: str(vus),
    },
    "UC-02": {
        "nombre":  "UC-02: Profundidad Jerárquica Moderada",
        "dir":     "UC02_profundidad_moderada",
        "script":  "uc02_profundidad_nivel.js",
        "iso":     "A.8.28",
        "amenaza": "DoS / Agotamiento",
        # graphql-depth-limit corta en 5, asi que la rejilla cruza el umbral:
        # 1 y 3 dentro del rango permitido, 5 justo en el limite, 6 y 7 fuera.
        # Se omiten 2 y 4 porque se comportan igual que 1 y 3 y solo anaden horas.
        "escenarios": [(v, n) for n in [1, 3, 5, 6, 7] for v in CARGAS],
        "carga":   lambda vus, niv: f"N{niv}·V{vus}",
    },
    "UC-03": {
        "nombre":  "UC-03: Complejidad Recursiva Circular",
        "dir":     "UC03_recursividad_circular",
        "script":  "uc03_recursividad_nivel.js",
        "iso":     "A.8.28",
        "amenaza": "DoS / Bloqueo",
        # La carga son los ciclos de recursion, con VUs fijo en 8.
        "escenarios": [(8, n) for n in CARGAS],
        "carga":   lambda vus, niv: str(niv),
    },
    "UC-04": {
        "nombre":  "UC-04: Abuso Horizontal de Alias",
        "dir":     "UC04_abuso_alias",
        "script":  "uc04_alias_nivel.js",
        "iso":     "A.8.6",
        "amenaza": "DoS / Saturación",
        # La carga es el numero de alias en una sola peticion, con VUs fijo en 1.
        # Escala Fibonacci hasta 377 para cruzar el umbral del control (334 alias).
        "escenarios": [(1, n) for n in FIBONACCI],
        "carga":   lambda vus, niv: str(niv),
    },
    "UC-05": {
        "nombre":  "UC-05: Bomba de Fragmentos (AST)",
        "dir":     "UC05_bomba_fragmentos",
        "script":  "uc05_fragmentos_nivel.js",
        "iso":     "A.8.28",
        "amenaza": "DoS / Desbordamiento",
        # La carga es el factor de expansion del AST, con VUs fijo en 1.
        "escenarios": [(1, n) for n in CARGAS],
        "carga":   lambda vus, niv: str(niv),
    },
}

TRATAMIENTO = {
    "Vulnerable": "Línea Base Vulnerable",
    "Protegido":  "Hardening ISO 27001",
}


def ruta_reporte(env_name, uc, vus, nivel, replicas=REPLICAS):
    """Ruta del reporte consolidado de un escenario (existe = ya ejecutado)."""
    return os.path.join(uc_base.ENVS[env_name], "load_tests", uc["dir"], "resultados",
                        f"reporte_consolidado_{replicas}runs_vus{vus}_nivel{nivel}.md")


def plan(entornos, solo, replicas, rehacer=False):
    """Lista de escenarios a ejecutar, separando los que ya estan en disco."""
    pendientes, hechos = [], []
    for env_name in entornos:
        for uc_id, uc in DISENO.items():
            if solo and uc_id != solo:
                continue
            for vus, nivel in uc["escenarios"]:
                item = (env_name, uc_id, uc, vus, nivel)
                ya_esta = os.path.isfile(ruta_reporte(env_name, uc, vus, nivel, replicas))
                if ya_esta and not rehacer:
                    hechos.append(item)
                else:
                    pendientes.append(item)
    return pendientes, hechos


def fmt_dur(seg):
    return str(timedelta(seconds=int(seg)))


def ejecutar_escenario(env_name, uc, vus, nivel, replicas):
    """Lanza run_multiple_experiments.py para un escenario. Devuelve True si genero el reporte."""
    env_path = uc_base.ENVS[env_name]
    runner = os.path.join(env_path, "load_tests", "run_multiple_experiments.py")
    script_rel = os.path.join(uc["dir"], uc["script"])

    variables = os.environ.copy()
    # Cada script k6 lee su variable: UC-02, UC-03 y UC-05 usan LEVEL, pero
    # UC-04 usa ALIAS_COUNT. Pasando solo LEVEL, UC-04 se quedaba con su valor
    # por defecto (10 alias) en los 13 niveles, asi que nunca variaba la carga
    # ni llegaba al umbral del control. Se pasan ambas con el mismo valor y cada
    # script toma la que le corresponde.
    variables["LEVEL"] = str(nivel)
    variables["ALIAS_COUNT"] = str(nivel)

    cmd = [sys.executable, runner, "--test-script", script_rel,
           "--vus", str(vus), "--runs", str(replicas)]

    proc = subprocess.Popen(cmd, cwd=env_path, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True,
                            encoding="utf-8", errors="replace",
                            bufsize=1, env=variables)
    for linea in proc.stdout:
        print("    " + linea.rstrip())
    proc.wait()
    return os.path.isfile(ruta_reporte(env_name, uc, vus, nivel, replicas))


def main():
    ap = argparse.ArgumentParser(description="Corrida completa del experimento GraphQL + ISO 27001")
    ap.add_argument("--simular", action="store_true",
                    help="muestra el plan y la estimacion sin ejecutar nada")
    ap.add_argument("--solo", default=None, metavar="UC-0N",
                    help="ejecuta un unico caso de uso (UC-01 ... UC-05)")
    ap.add_argument("--entorno", default="ambos", choices=["Vulnerable", "Protegido", "ambos"])
    ap.add_argument("--replicas", type=int, default=REPLICAS,
                    help=f"replicas por escenario (por defecto {REPLICAS})")
    ap.add_argument("--rehacer", action="store_true",
                    help="vuelve a medir todo, ignorando los reportes que ya esten en disco")
    args = ap.parse_args()

    if args.solo and args.solo not in DISENO:
        sys.exit(f"[ERROR] --solo debe ser uno de: {', '.join(DISENO)}")

    entornos = ["Vulnerable", "Protegido"] if args.entorno == "ambos" else [args.entorno]
    pendientes, hechos = plan(entornos, args.solo, args.replicas, args.rehacer)
    total = len(pendientes) + len(hechos)

    print("=" * 70)
    print("  CORRIDA COMPLETA DEL EXPERIMENTO")
    print(f"  Entornos : {', '.join(entornos)}")
    print(f"  Replicas : {args.replicas} por escenario")
    if args.rehacer:
        print(f"  Escenarios: {total}  (se vuelven a medir todos: --rehacer)")
    else:
        print(f"  Escenarios: {total}  ({len(hechos)} ya en disco, {len(pendientes)} por ejecutar)")
    est = len(pendientes) * args.replicas * SEG_POR_REPLICA
    print(f"  Estimado : {fmt_dur(est)}  (~{est/3600:.1f} h)")
    print("=" * 70)

    for uc_id, uc in DISENO.items():
        if args.solo and uc_id != args.solo:
            continue
        n_uc = len(uc["escenarios"]) * len(entornos)
        falta = sum(1 for p in pendientes if p[1] == uc_id)
        print(f"  {uc_id}: {n_uc:3d} escenarios ({falta} por ejecutar) | "
              f"ISO {uc['iso']} | {uc['amenaza']}")

    if args.simular:
        print("\n[SIMULACION] No se ejecuto nada. Quita --simular para lanzar la corrida.")
        return

    if not pendientes:
        print("\n[OK] No hay nada pendiente: todos los escenarios ya estan en disco.")
        return

    inicio = time.time()
    duraciones = []
    completados, fallidos = 0, []

    # Se agrupa por entorno para levantar Docker una sola vez por entorno en
    # lugar de alternar entre los dos, que es la parte lenta del ciclo.
    try:
        for env_name in entornos:
            del_entorno = [p for p in pendientes if p[0] == env_name]
            if not del_entorno:
                continue

            print(f"\n{'=' * 70}")
            print(f"  ENTORNO {env_name.upper()}  ({len(del_entorno)} escenarios)")
            print(f"{'=' * 70}")
            uc_base.restart_env_full(uc_base.ENVS[env_name])

            for env_n, uc_id, uc, vus, nivel in del_entorno:
                completados += 1
                t0 = time.time()
                if duraciones:
                    medio = sum(duraciones) / len(duraciones)
                    restantes = len(pendientes) - completados + 1
                    eta = datetime.now() + timedelta(seconds=medio * restantes)
                    txt_eta = f" | ETA {eta.strftime('%d/%m %H:%M')}"
                else:
                    txt_eta = ""

                print(f"\n{'-' * 70}")
                print(f"  [{completados}/{len(pendientes)}] {env_name} | {uc_id} | "
                      f"VUs={vus} Nivel={nivel} | carga={uc['carga'](vus, nivel)}{txt_eta}")
                print(f"{'-' * 70}")

                ok = ejecutar_escenario(env_name, uc, vus, nivel, args.replicas)
                dur = time.time() - t0
                duraciones.append(dur)

                if ok:
                    print(f"  [OK] Escenario completado en {fmt_dur(dur)}")
                else:
                    fallidos.append((env_name, uc_id, vus, nivel))
                    print(f"  [FALLO] No se genero el reporte. Se continua con el siguiente.")

    except KeyboardInterrupt:
        print("\n\n[INTERRUMPIDO] Corrida detenida a mano.")
        print("Los escenarios ya terminados quedan en disco; relanza el script para continuar.")

    total_seg = time.time() - inicio
    print(f"\n{'=' * 70}")
    print(f"  Escenarios ejecutados: {completados - len(fallidos)} de {len(pendientes)}")
    print(f"  Tiempo total         : {fmt_dur(total_seg)}")
    if fallidos:
        print(f"  Fallidos ({len(fallidos)}):")
        for env_n, uc_id, vus, nivel in fallidos:
            print(f"    - {env_n} | {uc_id} | VUs={vus} Nivel={nivel}")
        print("  Relanza el script para reintentar solo esos.")
    print(f"{'=' * 70}")
    print("\nPara construir el Excel:  python generar_registro_datos.py")


if __name__ == "__main__":
    main()
