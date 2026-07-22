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

    # El AVANCE cuenta TODO lo que hay en disco de esta rejilla, sin importar en
    # cuantas sesiones se hizo. (Antes solo contaba la ultima tanda tras un hueco,
    # y con varios cuelgues seguidos mostraba de menos: decia "1 de 106" cuando ya
    # habia decenas hechos en tandas anteriores.)
    hechos, total, por_uc = [], 0, {}
    por_env = {"Vulnerable": [0, 0], "Protegido": [0, 0]}

    for uc_id, uc in DISENO.items():
        n_uc = hechos_uc = 0
        for env_name in ("Vulnerable", "Protegido"):
            for vus, nivel in uc["escenarios"]:
                total += 1
                n_uc += 1
                por_env[env_name][1] += 1
                md = ruta_reporte(env_name, uc, vus, nivel, args.replicas)
                if os.path.isfile(md):
                    hechos.append(os.path.getmtime(md))
                    hechos_uc += 1
                    por_env[env_name][0] += 1
        por_uc[uc_id] = [hechos_uc, n_uc]

    n = len(hechos)

    # El RITMO si usa solo la tanda reciente: se toma el ultimo tramo de marcas sin
    # huecos mayores a media hora, para que un cuelgue viejo no falsee el promedio.
    hechos.sort()
    corte = 1800
    inicio = 0
    for i in range(len(hechos) - 1, 0, -1):
        if hechos[i] - hechos[i - 1] > corte:
            inicio = i
            break
    marcas = hechos[inicio:]
    barra = "█" * int(30 * n / total) + "░" * (30 - int(30 * n / total))
    print(f"\n  [{barra}]  {n} de {total}  ({100*n/total:.0f}%)\n")

    # Los entornos van uno detras de otro: primero Vulnerable entero y luego
    # Protegido, para levantar Docker una sola vez por entorno.
    for env_name, (h, t) in por_env.items():
        if h == t:
            estado = "completo"
        elif h == 0:
            estado = f"0/{t}  (en espera)"
        else:
            estado = f"{h}/{t}  <- en curso"
        print(f"    {env_name:11s}: {estado}")
    print()

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
