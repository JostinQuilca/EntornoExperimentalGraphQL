# -*- coding: utf-8 -*-
"""
Restaura reportes que un --reiniciar mando a carpetas _respaldo_.

Para cada escenario de la rejilla cuyo reporte NO este en la carpeta activa,
lo busca en los _respaldo_ (del mas reciente al mas viejo) y lo devuelve. No
sobrescribe nada que ya este en activo: si un escenario ya tiene su reporte
bueno, se respeta.

Uso:
    python restaurar_respaldo.py            # restaura lo que falte
    python restaurar_respaldo.py --simular  # solo muestra que restauraria
"""
import argparse
import glob
import os
import shutil
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

from experimento_completo import DISENO, REPLICAS, ruta_reporte


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true", help="muestra que haria, sin mover nada")
    ap.add_argument("--excluir", default=None, metavar="UC-0N",
                    help="no restaurar esta UC (util cuando ya se esta rehaciendo)")
    ap.add_argument("--replicas", type=int, default=REPLICAS)
    args = ap.parse_args()

    restaurados = 0
    faltan = 0
    por_uc = {}

    for env_name in ("Vulnerable", "Protegido"):
        for uc_id, uc in DISENO.items():
            if args.excluir and uc_id == args.excluir:
                continue
            por_uc.setdefault(uc_id, 0)
            for vus, nivel in uc["escenarios"]:
                destino = ruta_reporte(env_name, uc, vus, nivel, args.replicas)
                if os.path.isfile(destino):
                    continue  # ya esta en activo: no se toca

                carpeta = os.path.dirname(destino)
                nombre = os.path.basename(destino)
                # _respaldo_YYYYMMDD_HHMMSS -> ordenados del mas nuevo al mas viejo
                respaldos = sorted(glob.glob(os.path.join(carpeta, "_respaldo_*")), reverse=True)
                encontrado = None
                for rb in respaldos:
                    cand = os.path.join(rb, nombre)
                    if os.path.isfile(cand):
                        encontrado = cand
                        break

                if encontrado:
                    if args.simular:
                        print(f"  [restauraria] {uc_id} {env_name} vus{vus} niv{nivel}")
                    else:
                        shutil.move(encontrado, destino)
                    restaurados += 1
                    por_uc[uc_id] += 1
                else:
                    faltan += 1

    print()
    if args.simular:
        print(f"[SIMULACION] Restauraria {restaurados} reportes. No se movio nada.")
    else:
        print(f"[OK] Restaurados {restaurados} reportes desde _respaldo_ a la carpeta activa.")
    for uc_id, n in por_uc.items():
        if n:
            print(f"    {uc_id}: {n} restaurados")
    if faltan:
        print(f"  {faltan} escenarios sin reporte en activo ni en respaldo (hay que correrlos).")


if __name__ == "__main__":
    main()
