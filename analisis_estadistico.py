# -*- coding: utf-8 -*-
"""
Analisis estadistico inferencial de los resultados UC-01 (seccion 2.4.3 tesis).

Implementa el protocolo declarado en 2.4.3:
  1) Prueba de Shapiro-Wilk sobre cada muestra (3 replicas por nivel/entorno)
     para evaluar normalidad.
  2) Prueba no parametrica de Mann-Whitney U entre Vulnerable y Protegido
     por nivel de VUs y por cada metrica, con nivel de confianza 95% (alpha=0.05).

Genera:
  - pruebas/UC01_Introspeccion/UC01_analisis_estadistico.md  (reporte lectura)
  - pruebas/UC01_Introspeccion/UC01_analisis_estadistico.xlsx (matriz p-valores)

Uso:
  python analisis_estadistico.py
"""
import os, re
from datetime import datetime
try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    HAS_XLSX = True
except ImportError:
    HAS_XLSX = False

try:
    from scipy import stats
except ImportError:
    print("ERROR: falta 'scipy'. Instala con:  pip install scipy")
    raise

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "pruebas", "UC01_Introspeccion")
os.makedirs(OUT_DIR, exist_ok=True)

ENVS = {
    "Vulnerable": os.path.join(BASE_DIR, "E-commerce",
                               "load_tests", "UC01_introspeccion", "resultados"),
    "Protegido":  os.path.join(BASE_DIR, "E-commerce-controles",
                               "load_tests", "UC01_introspeccion", "resultados"),
}
ALPHA = 0.05
# El script busca automaticamente reportes con la mayor N replicas disponible.
# Los niveles criticos re-corridos con n=5 tienen prioridad; los demas usan n=3.
RUNS_CANDIDATES = [5, 3]


def parse_replicas(md_path):
    """Devuelve lista de dicts con las 3 replicas: peticiones, latencia, fallos."""
    with open(md_path, "r", encoding="utf-8", errors="replace") as f:
        txt = f.read()
    replicas = []
    for m in re.finditer(r"\|\s*Run\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*ms\s*\|\s*([\d.]+)%", txt):
        replicas.append({
            "idx": int(m.group(1)),
            "peticiones": float(m.group(2)),
            "latencia": float(m.group(3)),
            "fallos": float(m.group(4)),
        })
    return replicas


def load_data():
    """Estructura: data[vus][env][metric] = [n valores] con n en RUNS_CANDIDATES."""
    data = {}
    n_map = {}  # n_map[vus] = n usado (5 tiene prioridad sobre 3)
    for env_name, res_dir in ENVS.items():
        if not os.path.isdir(res_dir):
            continue
        for fname in os.listdir(res_dir):
            m = re.match(r"reporte_consolidado_(\d+)runs_vus(\d+)\.md$", fname)
            if not m: continue
            n_runs = int(m.group(1))
            vus = int(m.group(2))
            if n_runs not in RUNS_CANDIDATES:
                continue
            # Prioridad: mayor n_runs primero (n=5 antes que n=3)
            if vus in n_map and n_map[vus] > n_runs:
                continue
            replicas = parse_replicas(os.path.join(res_dir, fname))
            # Filtrar replicas invalidas (peticiones=0 = k6 colgado)
            replicas = [r for r in replicas if r["peticiones"] > 0]
            if len(replicas) < 3:
                continue
            n_map[vus] = n_runs
            data.setdefault(vus, {}).setdefault(env_name, {})
            data[vus][env_name] = {
                "peticiones": [r["peticiones"] for r in replicas],
                "latencia":   [r["latencia"]   for r in replicas],
                "fallos":     [r["fallos"]     for r in replicas],
                "_n": len(replicas),
            }
    return data


def shapiro(sample):
    """Devuelve (p_valor, es_normal). n=3 es el minimo aceptado por scipy."""
    if len(set(sample)) < 2:
        return (1.0, True)  # muestras constantes: no rechaza normalidad
    try:
        _, p = stats.shapiro(sample)
        return (float(p), p >= ALPHA)
    except Exception:
        return (float("nan"), False)


def mann_whitney(a, b):
    """Mann-Whitney U bilateral. Devuelve (U, p)."""
    if len(set(a + b)) < 2:
        return (0.0, 1.0)
    try:
        U, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        return (float(U), float(p))
    except Exception:
        return (float("nan"), float("nan"))


def main():
    data = load_data()
    if not data:
        print("No se encontraron reportes .md para analizar.")
        return

    vus_sorted = sorted(data.keys())
    metrics = [
        ("latencia",   "Latencia (ms)"),
        ("peticiones", "Throughput (peticiones/60s)"),
        ("fallos",     "Tasa de Fallos (%)"),
    ]

    # ---------------- Reporte Markdown ----------------
    md = []
    md.append("# UC-01 - Analisis estadistico inferencial")
    md.append(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
    md.append(f"Alfa (nivel de significancia) = **{ALPHA}**, confianza = **{int((1-ALPHA)*100)}%**  ")
    md.append(f"N replicas por escenario: **variable segun disponibilidad** (n=5 en niveles criticos re-corridos, n=3 en exploratorios; se filtran replicas invalidas con k6 colgado)\n")
    md.append("## 1. Prueba de Shapiro-Wilk (normalidad)")
    md.append("H0: la muestra proviene de una poblacion normal. Se rechaza si p < alfa.\n")
    md.append("| VUs | Entorno | Metrica | p (Shapiro) | Normal? |")
    md.append("| :---: | :--- | :--- | :---: | :---: |")
    all_normal = True
    for vus in vus_sorted:
        for env in ("Vulnerable", "Protegido"):
            if env not in data[vus]: continue
            for key, label in metrics:
                sample = data[vus][env][key]
                p, norm = shapiro(sample)
                if not norm: all_normal = False
                md.append(f"| {vus} | {env} | {label} | {p:.4f} | {'Si' if norm else 'No'} |")
    md.append("")
    md.append(f"**Conclusion normalidad:** { 'Todas las muestras cumplen normalidad.' if all_normal else 'Existe evidencia de no normalidad -> se justifica el uso de Mann-Whitney U (no parametrica), acorde a la seccion 2.4.3 de la tesis.' }\n")

    md.append("## 2. Mann-Whitney U: Vulnerable vs Protegido")
    md.append("H0: no existe diferencia significativa entre los rangos de ambos grupos.")
    md.append("H1: existe diferencia significativa (bilateral). Se rechaza H0 si p < alfa.\n")
    md.append("| VUs | Metrica | U | p-valor | Conclusion |")
    md.append("| :---: | :--- | :---: | :---: | :--- |")

    p_matrix = {}  # p_matrix[(vus, metric_key)] = p
    for vus in vus_sorted:
        if "Vulnerable" not in data[vus] or "Protegido" not in data[vus]:
            continue
        for key, label in metrics:
            a = data[vus]["Vulnerable"][key]
            b = data[vus]["Protegido"][key]
            U, p = mann_whitney(a, b)
            p_matrix[(vus, key)] = p
            veredicto = ("Rechaza H0 (diferencia SIGNIFICATIVA)" if p < ALPHA
                         else "No rechaza H0 (sin diferencia significativa)")
            md.append(f"| {vus} | {label} | {U:.2f} | {p:.4f} | {veredicto} |")

    md.append("\n## 3. Interpretacion frente a las hipotesis de la tesis")
    md.append("- **H_A2** (controles reducen latencia/fallos/consumo): se sustenta cuando p<alfa a favor del Protegido en las metricas de recursos/red bajo estres.")
    md.append("- Si el Vulnerable **no colapsa** en el rango probado, la ausencia de diferencia significativa en latencia y fallos es esperada y no contradice H_A2 -> se requiere ampliar la carga.")

    out_md = os.path.join(OUT_DIR, "UC01_analisis_estadistico.md")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"[OK] Reporte guardado: {out_md}")

    # ---------------- Excel ----------------
    if not HAS_XLSX:
        print("[WARN] openpyxl no instalado; se omite Excel.")
        return

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Analisis Estadistico"
    ws.sheet_view.showGridLines = False
    thin = Side(style="thin", color="000000")
    bdr = Border(top=thin, left=thin, right=thin, bottom=thin)
    center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    hdr = Font(bold=True, color="FFFFFF", size=10)
    fill_hdr = PatternFill("solid", fgColor="2F5597")
    fill_sig = PatternFill("solid", fgColor="C6EFCE")  # verde: significativo
    fill_no  = PatternFill("solid", fgColor="FFE699")  # amarillo: no significativo

    ws.cell(row=1, column=1, value=f"UC-01 - Mann-Whitney U (alfa={ALPHA})").font = Font(bold=True, size=13)
    HEAD = ["VUs", "Metrica", "Vulnerable (n=3)", "Protegido (n=3)", "U", "p-valor", "p<alfa?"]
    for j, h in enumerate(HEAD, 1):
        c = ws.cell(row=3, column=j, value=h)
        c.font = hdr; c.fill = fill_hdr; c.alignment = center; c.border = bdr

    r = 4
    for vus in vus_sorted:
        if "Vulnerable" not in data[vus] or "Protegido" not in data[vus]:
            continue
        for key, label in metrics:
            a = data[vus]["Vulnerable"][key]
            b = data[vus]["Protegido"][key]
            U, p = mann_whitney(a, b)
            sig = p < ALPHA
            row_vals = [vus, label, str(a), str(b), round(U, 2), round(p, 4), "SI" if sig else "no"]
            for j, v in enumerate(row_vals, 1):
                cc = ws.cell(row=r, column=j, value=v)
                cc.alignment = center; cc.border = bdr
                if j == 7: cc.fill = fill_sig if sig else fill_no
            r += 1

    for j, w in enumerate([8, 26, 22, 22, 10, 12, 12], 1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(j)].width = w
    ws.freeze_panes = "A4"

    out_xlsx = os.path.join(OUT_DIR, "UC01_analisis_estadistico.xlsx")
    wb.save(out_xlsx)
    print(f"[OK] Excel guardado: {out_xlsx}")


if __name__ == "__main__":
    main()
