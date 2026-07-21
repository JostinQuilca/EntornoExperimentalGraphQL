# -*- coding: utf-8 -*-
"""
Avance de la corrida en marcha, para consultarlo desde otra ventana.

Solo lee archivos, asi que no interfiere con la corrida.

Cuenta unicamente los escenarios de la rejilla vigente y escritos en las ultimas
horas. Un glob suelto sobre "3runs" no sirve: en resultados quedan reportes de
tandas anteriores con ese mismo nombre y el avance saldria inflado.

Uso:
    python progreso.py
    python progreso.py --horas 24
"""
import argparse
import os
import sys
import time
from datetime import datetime, timedelta

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

from experimento_completo import DISENO, REPLICAS, ruta_reporte


def main():
    ap = argparse.ArgumentParser(description="Avance de la corrida en marcha")
    ap.add_argument("--horas", type=float, default=12,
                    help="antiguedad maxima para considerar que un reporte es de esta tanda")
    ap.add_argument("--replicas", type=int, default=REPLICAS)
    args = ap.parse_args()

    limite = time.time() - args.horas * 3600
    candidatos, total, por_uc = [], 0, {}

    for uc_id, uc in DISENO.items():
        n_uc = 0
        for env_name in ("Vulnerable", "Protegido"):
            for vus, nivel in uc["escenarios"]:
                total += 1
                n_uc += 1
                md = ruta_reporte(env_name, uc, vus, nivel, args.replicas)
                if os.path.isfile(md) and os.path.getmtime(md) > limite:
                    candidatos.append((os.path.getmtime(md), uc_id))
        por_uc[uc_id] = [0, n_uc]

    # Quedarse con la tanda en curso. En resultados sobreviven reportes de sesiones
    # anteriores del mismo dia, y contarlos falsea tanto el avance como el ritmo:
    # un hueco grande entre dos marcas consecutivas separa una sesion de la otra.
    candidatos.sort()
    corte = 1800  # media hora sin escribir nada ya no es la misma tanda
    inicio = 0
    for i in range(len(candidatos) - 1, 0, -1):
        if candidatos[i][0] - candidatos[i - 1][0] > corte:
            inicio = i
            break
    candidatos = candidatos[inicio:]

    marcas = [m for m, _ in candidatos]
    for _, uc_id in candidatos:
        por_uc[uc_id][0] += 1
    n = len(candidatos)
    barra = "█" * int(30 * n / total) + "░" * (30 - int(30 * n / total))
    print(f"\n  [{barra}]  {n} de {total}  ({100*n/total:.0f}%)\n")

    for uc_id, (h, t) in por_uc.items():
        estado = "completo" if h == t else f"{h}/{t}"
        print(f"    {uc_id}: {estado}")

    if len(marcas) >= 2:
        marcas.sort()
        ritmo = (marcas[-1] - marcas[0]) / (len(marcas) - 1)
        faltan = total - n
        fin = datetime.now() + timedelta(seconds=ritmo * faltan)
        print(f"\n    Ritmo    : {ritmo/60:.1f} min por escenario")
        print(f"    Ultimo   : {datetime.fromtimestamp(marcas[-1]).strftime('%H:%M')}"
              f"  (hace {int((time.time()-marcas[-1])/60)} min)")
        print(f"    Faltan   : {faltan} escenarios")
        print(f"    Fin aprox: {fin.strftime('%d/%m %H:%M')}")
        # Si el ultimo reporte es muy viejo comparado con el ritmo, algo se atasco.
        if time.time() - marcas[-1] > max(900, ritmo * 3):
            print("\n    [AVISO] Hace demasiado que no se escribe un reporte.")
            print("            Revisa la ventana donde corre por si se quedo parada.")
    elif n:
        print(f"\n    Primer escenario listo a las "
              f"{datetime.fromtimestamp(marcas[0]).strftime('%H:%M')}."
              " Vuelve a consultar en unos minutos para ver el ritmo.")
    else:
        print("\n    Todavia no hay reportes de esta tanda.")
        print("    El primero tarda unos minutos (levantar Docker + 3 replicas).")
    print()


if __name__ == "__main__":
    main()
