# -*- coding: utf-8 -*-
"""
UC-02 (Vista aislada VUs=8) — reutiliza los reportes de la matriz UC-02
para producir un analisis con una sola variable independiente:
profundidad de anidamiento (1..7) con concurrencia fija VUs=8.

No ejecuta k6 ni docker. Solo lee los reportes consolidados ya generados
por uc02_runner.py y produce:
  - pruebas/UC02_VUs8_Aislado/UC02_VUs8_Comparativa.xlsx
  - pruebas/UC02_VUs8_Aislado/UC02_*.png (4 graficas, tema claro)
"""
import os
import sys
import uc_base as ub

LEVELS = [1, 2, 3, 4, 5, 6, 7]
VUS_FIXED = 8
RUNS = 5
UC_FOLDER = "UC02_profundidad_moderada"
OUT_SUBDIR = "UC02_VUs8_Aislado"
UC_ID = "UC-02"
VAR_LABEL = "Profundidad de anidamiento"


def main():
    out_dir = os.path.join(ub.BASE_DIR, "pruebas", OUT_SUBDIR)
    os.makedirs(out_dir, exist_ok=True)

    print("=" * 70)
    print(f"  {UC_ID} — VISTA AISLADA VUs={VUS_FIXED}")
    print(f"  Niveles: {LEVELS}")
    print(f"  Fuente: reportes existentes en load_tests/{UC_FOLDER}/resultados/")
    print("=" * 70)

    full_data = {"Vulnerable": {}, "Protegido": {}}
    avg_data = {"Vulnerable": {}, "Protegido": {}}
    levels_completed = []
    missing = []

    for level in LEVELS:
        for env_name, env_path in ub.ENVS.items():
            md_path = os.path.join(
                env_path, "load_tests", UC_FOLDER, "resultados",
                f"reporte_consolidado_{RUNS}runs_vus{VUS_FIXED}_nivel{level}.md"
            )
            if not os.path.isfile(md_path):
                missing.append((env_name, level, md_path))
                continue
            res = ub.parse_md_report(md_path)
            if res:
                full_data[env_name][level] = res
                avg_data[env_name][level] = res["avg"]
                a = res["avg"]
                print(f"  [OK] {env_name} nivel={level} | Pet: {a['peticiones']:.0f} | "
                      f"Lat: {a['latencia']:.2f} ms | Fal: {a['fallos']:.2f}% | "
                      f"Bloq: {a.get('bloqueo_control', 0.0):.2f}%")
        if level not in levels_completed and (level in full_data["Vulnerable"]
                                              or level in full_data["Protegido"]):
            levels_completed.append(level)

    if missing:
        print("\n[WARN] Reportes ausentes (se omiten en el analisis):")
        for env_name, level, path in missing:
            print(f"  - {env_name} nivel={level}: {path}")

    if not levels_completed:
        print("\n[ERROR] No se encontro ningun reporte para VUs=8. Aborto.")
        sys.exit(1)

    excel_path = os.path.join(out_dir, f"{UC_ID.replace('-','')}_VUs{VUS_FIXED}_Comparativa.xlsx")
    ub.export_excel(UC_ID, VAR_LABEL, full_data, levels_completed, excel_path, VUS_FIXED)

    ub.generate_graphs(UC_ID, VAR_LABEL, avg_data, levels_completed, out_dir)

    print("\n" + "=" * 70)
    print(f"  RESUMEN {UC_ID} — VISTA AISLADA VUs={VUS_FIXED}")
    print(f"  Niveles con datos: {levels_completed}")
    print(f"  Excel:     {excel_path}")
    print(f"  Graficas:  {out_dir}")
    print("=" * 70)


if __name__ == "__main__":
    main()
