#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Panel de Control - Entorno Experimental GraphQL
"""
from datetime import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import subprocess, threading, os, sys, re, time, io, unicodedata, glob
import scipy.stats as stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

try:
    import openpyxl
    from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    HAS_EXCEL = True
except ImportError:
    HAS_EXCEL = False

# ───────────────────────────────────────────────────────────────────────
# UTILIDADES
# ───────────────────────────────────────────────────────────────────────
def strip_accents(s):
    s = unicodedata.normalize("NFKD", str(s))
    return "".join(c for c in s if not unicodedata.combining(c))

def sa(s):          # strip accents + ascii safe
    return strip_accents(s).encode("ascii","replace").decode("ascii").replace("?","")

# ───────────────────────────────────────────────────────────────────────
# DATOS
# ───────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ENVS = {
    "Vulnerable": {
        "path":  os.path.join(BASE_DIR, "E-commerce"),
        "color": "#f85149", "label": "Sin controles de seguridad",
    },
    "Protegido": {
        "path":  os.path.join(BASE_DIR, "E-commerce-controles"),
        "color": "#3fb950", "label": "Con depth-limit + complexity + introspection block",
    },
}

ATTACKS = {
    "UC-01: Introspeccion del Schema": {
        "script": os.path.join("UC01_introspeccion","uc01_stress_introspeccion.js"),
        "script_nivel": None,  # UC-01 no usa script parametrizado (misma query, varían VUs)
        "desc":   "Expone el schema completo (tipos, campos, relaciones).\nControl: introspectionControlPlugin\nEje: Usuarios Virtuales (Fibonacci)",
        "query":  "query IntrospectionExposure {\n  __schema {\n    types { name fields { name type { name kind } } }\n    queryType { name }\n  }\n}",
        "nivel_queries": None,  # Siempre la misma query
    },
    "UC-02: Profundidad Moderada": {
        "script": os.path.join("UC02_profundidad_moderada","uc02_profundidad_moderada.js"),
        "script_nivel": os.path.join("UC02_profundidad_moderada","uc02_profundidad_nivel.js"),
        "desc":   "Escala progresiva de profundidad (1-7 niveles).\nControl: graphql-depth-limit (max: 5)\nEje: Niveles de anidamiento",
        "query":  "",
        "nivel_queries": {
            1: "# Nivel 1 — Consulta Plana (1 nivel)\nquery ProfundidadNivel1 {\n  listarResenas {\n    id\n    comentario\n  }\n}",
            2: "# Nivel 2 — Normal (2 niveles)\nquery ProfundidadNivel2 {\n  listarResenas {\n    id\n    comentario\n    autor {\n      id\n      nombre\n      email\n    }\n  }\n}",
            3: "# Nivel 3 — Normal (3 niveles)\nquery ProfundidadNivel3 {\n  listarResenas {\n    id\n    autor {\n      id\n      resenas {\n        id\n        comentario\n      }\n    }\n  }\n}",
            4: "# Nivel 4 — Limite OWASP (4 niveles)\nquery ProfundidadNivel4 {\n  listarResenas {\n    id\n    autor {\n      id\n      resenas {\n        id\n        producto {\n          id\n          nombre\n          precio\n        }\n      }\n    }\n  }\n}",
            5: "# Nivel 5 — Depth Limit (5 niveles)\nquery ProfundidadNivel5 {\n  listarResenas {\n    id\n    autor {\n      resenas {\n        producto {\n          resenas {\n            id\n            comentario\n          }\n        }\n      }\n    }\n  }\n}",
            6: "# Nivel 6 — ATAQUE (6 niveles)\nquery ProfundidadNivel6 {\n  listarResenas {\n    autor {\n      resenas {\n        producto {\n          resenas {\n            autor {\n              id\n              nombre\n            }\n          }\n        }\n      }\n    }\n  }\n}",
            7: "# Nivel 7 — ATAQUE SEVERO (7 niveles)\nquery ProfundidadNivel7 {\n  listarResenas {\n    autor {\n      resenas {\n        producto {\n          resenas {\n            autor {\n              resenas {\n                id\n                comentario\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}",
        },
    },
    "UC-03: Recursividad Circular": {
        "script": os.path.join("UC03_recursividad_circular","uc03_recursividad_circular.js"),
        "script_nivel": os.path.join("UC03_recursividad_circular","uc03_recursividad_nivel.js"),
        "desc":   "Escala progresiva de ciclos recursivos (1-5).\nControl: graphql-depth-limit (rechaza nivel > 5)\nEje: Ciclos de recursion circular",
        "query":  "",
        "nivel_queries": {
            1: "# Nivel 1 — Normal (resena -> autor)\nquery RecursividadNivel1 {\n  listarResenas {\n    id\n    autor {\n      id\n      nombre\n    }\n  }\n}",
            2: "# Nivel 2 — Normal (1 ciclo)\nquery RecursividadNivel2 {\n  listarResenas {\n    id\n    autor {\n      resenas {\n        id\n        comentario\n      }\n    }\n  }\n}",
            3: "# Nivel 3 — Moderado (2 ciclos)\nquery RecursividadNivel3 {\n  listarResenas {\n    autor {\n      resenas {\n        autor {\n          resenas {\n            id\n          }\n        }\n      }\n    }\n  }\n}",
            4: "# Nivel 4 — ATAQUE (3 ciclos)\nquery RecursividadNivel4 {\n  listarResenas {\n    autor {\n      resenas {\n        autor {\n          resenas {\n            autor {\n              resenas {\n                id\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}",
            5: "# Nivel 5 — ATAQUE SEVERO (4 ciclos)\nquery RecursividadNivel5 {\n  listarResenas {\n    autor {\n      resenas {\n        autor {\n          resenas {\n            autor {\n              resenas {\n                autor {\n                  resenas {\n                    id\n                  }\n                }\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}",
        },
    },
    "UC-04: Abuso de Alias": {
        "script": os.path.join("UC04_abuso_alias","uc04_abuso_alias.js"),
        "script_nivel": os.path.join("UC04_abuso_alias","uc04_alias_nivel.js"),
        "desc":   "Escala Fibonacci de aliases (1-55).\nControl: queryComplexityPlugin (max: 1000 puntos)\nEje: Numero de aliases",
        "query":  "",
        "nivel_queries": {
            1: "# Nivel 1 — Normal (1 alias)\nquery AliasNivel1 {\n  reporte1: obtenerReporteGeneral {\n    id totalVentas\n  }\n}",
            2: "# Nivel 2 — Normal (2 aliases)\nquery AliasNivel2 {\n  reporte1: obtenerReporteGeneral { id totalVentas }\n  reporte2: obtenerReporteGeneral { id totalVentas }\n}",
            3: "# Nivel 3 — Normal (3 aliases)\nquery AliasNivel3 {\n  reporte1: obtenerReporteGeneral { id totalVentas }\n  reporte2: obtenerReporteGeneral { id totalVentas }\n  reporte3: obtenerReporteGeneral { id totalVentas }\n}",
            4: "# Nivel 4 — Moderado (5 aliases)\nquery AliasNivel4 {\n  reporte1: obtenerReporteGeneral { id totalVentas }\n  # ... (5 aliases en total)\n  reporte5: obtenerReporteGeneral { id totalVentas }\n}",
            5: "# Nivel 5 — Estres (8 aliases)\nquery AliasNivel5 {\n  # 8 aliases x 500ms = 4s por peticion\n  reporte1: obtenerReporteGeneral { id totalVentas }\n  # ...\n  reporte8: obtenerReporteGeneral { id totalVentas }\n}",
            6: "# Nivel 6 — ATAQUE (13 aliases)\nquery AliasNivel6 {\n  # 13 aliases x 500ms = 6.5s por peticion\n  reporte1: obtenerReporteGeneral { id totalVentas }\n  # ...\n  reporte13: obtenerReporteGeneral { id totalVentas }\n}",
            7: "# Nivel 7 — ATAQUE MODERADO (21 aliases)\nquery AliasNivel7 {\n  # 21 aliases x 500ms = 10.5s por peticion\n  reporte1: obtenerReporteGeneral { id totalVentas }\n  # ...\n  reporte21: obtenerReporteGeneral { id totalVentas }\n}",
            8: "# Nivel 8 — ATAQUE SEVERO (34 aliases)\nquery AliasNivel8 {\n  # 34 aliases x 500ms = 17s por peticion\n  reporte1: obtenerReporteGeneral { id totalVentas }\n  # ...\n  reporte34: obtenerReporteGeneral { id totalVentas }\n}",
            9: "# Nivel 9 — ATAQUE CRITICO (55 aliases)\nquery AliasNivel9 {\n  # 55 aliases x 500ms = 27.5s por peticion\n  reporte1: obtenerReporteGeneral { id totalVentas }\n  # ...\n  reporte55: obtenerReporteGeneral { id totalVentas }\n}",
        },
    },
    "UC-05: Bomba de Fragmentos": {
        "script": os.path.join("UC05_bomba_fragmentos","uc05_bomba_fragmentos.js"),
        "script_nivel": os.path.join("UC05_bomba_fragmentos","uc05_fragmentos_nivel.js"),
        "desc":   "Escala progresiva de expansion exponencial (1-625 resoluciones).\nControl: queryComplexityPlugin (complejidad > 1000)\nEje: Factor de multiplicacion",
        "query":  "",
        "nivel_queries": {
            1: "# Nivel 1 — Normal (1 resolucion)\nquery FragmentosNivel1 {\n  listarUsuarios {\n    id\n    nombre\n    email\n  }\n}",
            2: "# Nivel 2 — Normal (4 resoluciones: 2x2)\nquery FragmentosNivel2 {\n  listarUsuarios {\n    ...F1\n    ...F1\n  }\n}\nfragment F1 on Usuario {\n  ...F2\n  ...F2\n}\nfragment F2 on Usuario {\n  id nombre email\n}",
            3: "# Nivel 3 — Moderado (27 resoluciones: 3x3x3)\nquery FragmentosNivel3 {\n  listarUsuarios {\n    ...F1 ...F1 ...F1\n  }\n}\nfragment F1 on Usuario { ...F2 ...F2 ...F2 }\nfragment F2 on Usuario { ...F3 ...F3 ...F3 }\nfragment F3 on Usuario { id nombre email }",
            4: "# Nivel 4 — ATAQUE (125 resoluciones: 5x5x5)\nquery FragmentosNivel4 {\n  listarUsuarios {\n    ...F1 ...F1 ...F1 ...F1 ...F1\n  }\n}\nfragment F1 on Usuario { ...F2 ...F2 ...F2 ...F2 ...F2 }\nfragment F2 on Usuario { ...F3 ...F3 ...F3 ...F3 ...F3 }\nfragment F3 on Usuario { id nombre email }",
            5: "# Nivel 5 — ATAQUE SEVERO (625 resoluciones: 5^4)\nquery FragmentosNivel5 {\n  listarUsuarios {\n    ...F1 ...F1 ...F1 ...F1 ...F1\n  }\n}\nfragment F1 on Usuario { ...F2 x5 }\nfragment F2 on Usuario { ...F3 x5 }\nfragment F3 on Usuario { ...F4 x5 }\nfragment F4 on Usuario { id nombre email }",
        },
    },
}

ALL_VUS    = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
RUNS_OPTS  = ["1","2","3","5"]
ATK_NAMES  = list(ATTACKS.keys())

# Niveles por UC para escalamiento progresivo
UC_LEVELS = {
    "UC-01": {"max": 13, "label": "VUs (Fibonacci Extendido)", "scale": [1,2,3,5,8,13,21,34,55,89,144,233,377]},
    "UC-02": {"max": 7, "label": "Profundidad (1-7)", "scale": list(range(1,8))},
    "UC-03": {"max": 7, "label": "Ciclos (1-7)",      "scale": list(range(1,8))},
    "UC-04": {"max": 8, "label": "Aliases (Fibonacci)","scale": [1,2,3,5,8,13,21,34]},
    "UC-05": {"max": 5, "label": "Factor (Fibonacci)",  "scale": [1,2,3,5,8]},
}

# Columna del nivel en el Excel: es la variable independiente real de cada UC.
NIVEL_LABEL = {
    "UC-01": "Nivel",
    "UC-02": "Profundidad",
    "UC-03": "Ciclos recursivos",
    "UC-04": "Numero de alias",
    "UC-05": "Factor de expansion",
}
def nivel_col(uc_short, level):
    """(etiqueta, valor) de la columna de nivel. Traduce el indice al valor real de
    la escala (p.ej. UC-04 nivel 8 -> 34 alias; UC-02 nivel 6 -> profundidad 6)."""
    lab = NIVEL_LABEL.get(uc_short, "Nivel")
    val = level if level else ""
    try:
        sc = UC_LEVELS[uc_short]["scale"]
        if level and 1 <= int(level) <= len(sc):
            val = sc[int(level) - 1]
    except Exception:
        pass
    return lab, val

METRICS_DEF = [
    ("Peticiones Totales",         "peticiones",      "req"),
    ("Latencia Media (ms)",        "latencia",        "ms"),
    ("Tasa de Fallos (%)",         "fallos",          "%"),
    ("CPU api-gateway (%)",        "cpu_gw",          "%"),
    ("CPU ms-usuarios (%)",        "cpu_ms_usuarios", "%"),
    ("CPU ms-catalogo (%)",        "cpu_ms_catalogo", "%"),
    ("CPU ms-resenas (%)",         "cpu_ms_resenas",  "%"),
    ("CPU ms-ordenes (%)",         "cpu_ms_ordenes",  "%"),
    ("CPU Mongo (%)",              "cpu_mongo",       "%"),
    ("CPU Postgres (%)",           "cpu_pg",          "%"),
]
CHART_TYPES = [
    "Barras Comparativas",
    "Lineas de Tendencia",
    "Barras Horizontales",
    "Area con Sombra",
]

# ───────────────────────────────────────────────────────────────────────
# PALETA
# ───────────────────────────────────────────────────────────────────────
BG    = "#0d1117"
BG2   = "#161b22"
BG3   = "#21262d"
BORD  = "#30363d"
FG    = "#c9d1d9"
MUTED = "#8b949e"
ACC   = "#6e40c9"
GREEN = "#3fb950"
RED   = "#f85149"
ORG   = "#d29922"
CYAN  = "#56d364"
YEL   = "#e3b341"
BLUE  = "#58a6ff"

MONO    = ("Cascadia Code", 9)
MONO_SM = ("Cascadia Code", 8)
UI      = ("Segoe UI", 9)
UI_B    = ("Segoe UI", 9, "bold")
UI_SM   = ("Segoe UI", 8)
UI_SM_B = ("Segoe UI", 8, "bold")

# ───────────────────────────────────────────────────────────────────────
# PARSE DE RESULTADOS
# ───────────────────────────────────────────────────────────────────────
def _pct(text):
    """Extrae primer porcentaje flotante de un string."""
    m = re.search(r'([\d.]+)%', text)
    return float(m.group(1)) if m else 0.0

def _mib(text):
    """Extrae primer valor MiB flotante de un string."""
    m = re.search(r'([\d.]+)\s*MiB', text)
    return float(m.group(1)) if m else 0.0

def parse_md_full(md_text):
    """
    Devuelve dict con:
      fecha, hora  — del encabezado del reporte
      runs         — lista de dicts, uno por run
      avg          — dict con promedios
    """
    txt = strip_accents(md_text)

    # --- Fecha y hora del reporte ---
    fecha = datetime.now().strftime("%d/%m/%Y")
    hora  = datetime.now().strftime("%H:%M")
    m_dt = re.search(r'Fecha de Consolidacion[:\s]*(\d{4})-(\d{2})-(\d{2})\s*(\d{2}):(\d{2})', txt)
    if m_dt:
        y,mo,d,h,mi = m_dt.groups()
        fecha = f"{d}/{mo}/{y}"
        hora  = f"{h}:{mi}"

    # --- Datos por run de metricas K6 (soporta 4 o 5 columnas: la 5ta = bloqueo) ---
    run_metrics = {}
    for line in txt.splitlines():
        m = re.match(
            r'\|\s*Run\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*ms\s*\|\s*([\d.]+)%(?:\s*\|\s*([\d.]+)%)?',
            line
        )
        if m:
            n = int(m.group(1))
            run_metrics[n] = {
                "peticiones": float(m.group(2)),
                "latencia":   float(m.group(3)),
                "fallos":     float(m.group(4)),
                "bloqueo_control": float(m.group(5)) if m.group(5) else 0.0,
            }

    # Aislar secciones por marcadores para separar picos de promedios
    def _section(text, start, end=None):
        i = text.find(start)
        if i < 0: return ""
        if end:
            j = text.find(end, i + len(start))
            return text[i:j] if j > 0 else text[i:]
        return text[i:]

    sec_cpu_pico = _section(txt, "PICOS DE CPU", "PICOS DE MEMORIA")
    sec_ram_pico = _section(txt, "PICOS DE MEMORIA", "PROMEDIO DE CPU")
    sec_cpu_mean = _section(txt, "PROMEDIO DE CPU", "PROMEDIO DE MEMORIA")
    sec_ram_mean = _section(txt, "PROMEDIO DE MEMORIA")

    containers = ["api-gateway","mongo-db","postgres-db",
                  "ms-usuarios","ms-resenas","ms-ordenes","ms-catalogo"]

    def _pick_pct_runs(section, cont):
        """Retorna diccionario {run: %} descartando el 'Promedio Pico' final."""
        for line in section.splitlines():
            if cont in line and "|" in line:
                vals = re.findall(r'([\d.]+)%', line)
                if vals:
                    # el ultimo valor es el promedio pico (en negritas)
                    n_runs = max(len(vals) - 1, 1)
                    return {i+1: float(vals[i]) for i in range(n_runs)}
        return {}

    def _pick_mib_runs(section, cont):
        for line in section.splitlines():
            if cont in line and "MiB" in line:
                vals = re.findall(r'([\d.]+)\s*MiB', line)
                if vals:
                    # Si el ultimo es promedio (aparece en negritas): descartarlo
                    line_no_avg = re.sub(r'\*\*[\d.]+\s*MiB\*\*.*$', '', line)
                    vals2 = re.findall(r'([\d.]+)\s*MiB', line_no_avg)
                    v = vals2 if vals2 else vals
                    return {i+1: float(v[i]) for i in range(len(v))}
        return {}

    cpu       = {c: _pick_pct_runs(sec_cpu_pico, c) for c in containers}
    cpu_mean  = {c: _pick_pct_runs(sec_cpu_mean, c) for c in containers}
    ram       = {c: _pick_mib_runs(sec_ram_pico, c) for c in containers}
    ram_mean  = {c: _pick_mib_runs(sec_ram_mean, c) for c in containers}

    # Promedios generales
    avg = {"peticiones":0.0,"latencia":0.0,"fallos":0.0,"cpu_gw":0.0,"cpu_top":0.0,
           "bloqueo_control":0.0, "cpu_gw_mean":0.0,
           "throughput_rps":0.0, "disponibilidad":1}
    txt_clean = txt.replace('*', '')
    m_avg = re.search(r'PROMEDIO[^|]*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*ms\s*\|\s*([\d.]+)%(?:\s*\|\s*([\d.]+)%)?', txt_clean)
    if m_avg:
        avg["peticiones"] = float(m_avg.group(1))
        avg["latencia"]   = float(m_avg.group(2))
        avg["fallos"]     = float(m_avg.group(3))
        if m_avg.group(4): avg["bloqueo_control"] = float(m_avg.group(4))
    gw_vals = list(cpu.get("api-gateway",{}).values())
    avg["cpu_gw"] = sum(gw_vals)/len(gw_vals) if gw_vals else 0.0
    gw_mean_vals = list(cpu_mean.get("api-gateway",{}).values())
    avg["cpu_gw_mean"] = sum(gw_mean_vals)/len(gw_mean_vals) if gw_mean_vals else 0.0
    max_cpu = 0.0
    for svc in ["ms-usuarios","ms-resenas","ms-ordenes","ms-catalogo","mongo-db","postgres-db"]:
        vals = list(cpu.get(svc,{}).values())
        if vals: max_cpu = max(max_cpu, max(vals))
    avg["cpu_top"] = max_cpu
    avg["throughput_rps"] = round(avg["peticiones"] / 60.0, 3)
    avg["disponibilidad"] = 0 if (avg["peticiones"] == 0 or avg["fallos"] >= 50.0) else 1

    # Combinar en lista de runs
    runs = []
    for n in sorted(run_metrics.keys()):
        rm = run_metrics[n]
        tp = rm["peticiones"] / 60.0
        disp = 0 if (rm["peticiones"] == 0 or rm["fallos"] >= 50.0) else 1
        runs.append({
            "idx":       n,
            "peticiones":rm["peticiones"],
            "latencia":  rm["latencia"],
            "fallos":    rm["fallos"],
            "bloqueo_control": rm.get("bloqueo_control", 0.0),
            "throughput_rps":  round(tp, 3),
            "disponibilidad":  disp,
            "fecha":     fecha,
            "hora":      hora,
            "cpu_gw":           cpu.get("api-gateway",{}).get(n, 0.0),
            "cpu_gw_mean":      cpu_mean.get("api-gateway",{}).get(n, 0.0),
            "cpu_ms_usuarios":  cpu.get("ms-usuarios",{}).get(n, 0.0),
            "cpu_ms_catalogo":  cpu.get("ms-catalogo",{}).get(n, 0.0),
            "cpu_ms_resenas":   cpu.get("ms-resenas",{}).get(n, 0.0),
            "cpu_ms_ordenes":   cpu.get("ms-ordenes",{}).get(n, 0.0),
            "cpu_mongo":        cpu.get("mongo-db",{}).get(n, 0.0),
            "cpu_pg":           cpu.get("postgres-db",{}).get(n, 0.0),
            "ram_gw":           ram.get("api-gateway",{}).get(n, 0.0),
            "ram_gw_mean":      ram_mean.get("api-gateway",{}).get(n, 0.0),
            "ram_ms_usuarios":  ram.get("ms-usuarios",{}).get(n, 0.0),
            "ram_ms_catalogo":  ram.get("ms-catalogo",{}).get(n, 0.0),
            "ram_ms_resenas":   ram.get("ms-resenas",{}).get(n, 0.0),
            "ram_ms_ordenes":   ram.get("ms-ordenes",{}).get(n, 0.0),
            "ram_mongo":        ram.get("mongo-db",{}).get(n, 0.0),
            "ram_pg":           ram.get("postgres-db",{}).get(n, 0.0),
        })

    return {"fecha": fecha, "hora": hora, "runs": runs, "avg": avg}

def parse_md(md_text):
    """Compatibilidad: retorna solo los promedios."""
    return parse_md_full(md_text)["avg"]

def read_results(env_path, script, vus_list):
    """Lee solo los VUs de la lista. Retorna {vus: metrics_dict}"""
    uc_dir = os.path.dirname(script)
    out = {}
    for vus in vus_list:
        rdir = os.path.join(env_path, "load_tests", uc_dir, "resultados")
        files = (glob.glob(os.path.join(rdir, f"reporte_consolidado_*_vus{vus}.md"))
                 + glob.glob(os.path.join(rdir, f"reporte_consolidado_*_vus{vus}_nivel*.md")))
        # Tomar SIEMPRE el mas reciente. Si no, se lee un reporte viejo (de corridas
        # anteriores que siguen en la carpeta) y salen datos rancios y otro nro de replicas.
        files.sort(key=os.path.getmtime, reverse=True)
        if files:
            # Si hay varios, tomamos el mas reciente o el primero
            with open(files[0], encoding="utf-8", errors="replace") as f:
                out[vus] = parse_md(f.read())
    return out

def read_results_full(env_path, script, vus_list):
    """Lee datos completos por run. Retorna {vus: parse_md_full_result}"""
    uc_dir = os.path.dirname(script)
    out = {}
    for vus in vus_list:
        rdir = os.path.join(env_path, "load_tests", uc_dir, "resultados")
        files = (glob.glob(os.path.join(rdir, f"reporte_consolidado_*_vus{vus}.md"))
                 + glob.glob(os.path.join(rdir, f"reporte_consolidado_*_vus{vus}_nivel*.md")))
        # Tomar SIEMPRE el mas reciente. Si no, se lee un reporte viejo (de corridas
        # anteriores que siguen en la carpeta) y salen datos rancios y otro nro de replicas.
        files.sort(key=os.path.getmtime, reverse=True)
        if files:
            with open(files[0], encoding="utf-8", errors="replace") as f:
                out[vus] = parse_md_full(f.read())
    return out


# EXCEL EXPORT — TABLA PLANA UNIFICADA
# ───────────────────────────────────────────────────────────────────────
TRATAMIENTO = {
    "Vulnerable": "Linea Base Vulnerable",
    "Protegido":  "Hardening ISO 27001",
}
ENV_TAB_COLOR = {"Vulnerable": "f85149", "Protegido": "3fb950"}

def _safe_shapiro(data):
    # Requiere al menos 3 datos; si todos son iguales (var=0), el p-value es irrelevante
    if len(data) < 3 or max(data) == min(data):
        return None, None
    try:
        return stats.shapiro(data)
    except:
        return None, None

def _safe_mannwhitneyu(data1, data2):
    # Si ambos grupos son identicos en sus valores, no hay diff
    if max(data1) == min(data1) and max(data2) == min(data2) and data1[0] == data2[0]:
        return None, None
    try:
        return stats.mannwhitneyu(data1, data2, alternative='two-sided')
    except:
        return None, None

def _add_statistics_sheet(wb, full_data, vus_list):
    """
    Agrega una hoja de "Estadistica" al workbook, comparando Vulnerable vs Protegido.
    full_data: {"Vulnerable": {vus: parse_md_full_result}, "Protegido": ...}
    """
    if "Vulnerable" not in full_data or "Protegido" not in full_data:
        return # Solo aplica si tenemos ambos
    
    ws = wb.create_sheet(title="Estadística")
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = "C6E0B4"
    
    # Estilos
    hdr_font  = Font(bold=True, color="FFFFFF", name="Calibri", size=10)
    data_font = Font(color="000000", name="Calibri", size=10)
    center    = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin = Border(left=Side(style="thin",color="BFBFBF"), right=Side(style="thin",color="BFBFBF"),
                  top=Side(style="thin",color="BFBFBF"), bottom=Side(style="thin",color="BFBFBF"))
    fill_hdr = PatternFill("solid", fgColor="3B3838")
    
    headers = [
        "Métrica", "Carga (VUs)", "Runs",
        "W Shapiro (Vuln)", "p-value Norm (Vuln)", 
        "W Shapiro (Prot)", "p-value Norm (Prot)",
        "U Mann-Whitney", "p-value (M-W)", "Conclusión (Sig. 0.05)"
    ]
    
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.font = hdr_font; cell.alignment = center; cell.fill = fill_hdr; cell.border = thin

    metrics_to_test = [
        ("Throughput (req/s)", "peticiones"),
        ("Latencia (ms)", "latencia"),
        ("Fallos (%)", "fallos"),
        ("GW CPU (%)", "cpu_gw"),
        ("ms-usuarios CPU (%)", "cpu_ms_usuarios"),
        ("ms-catalogo CPU (%)", "cpu_ms_catalogo"),
        ("ms-resenas CPU (%)", "cpu_ms_resenas"),
        ("ms-ordenes CPU (%)", "cpu_ms_ordenes"),
        ("Mongo CPU (%)", "cpu_mongo"),
        ("Postgres CPU (%)", "cpu_pg"),
        ("GW RAM (MiB)", "ram_gw"),
        ("ms-usuarios RAM (MiB)", "ram_ms_usuarios"),
        ("ms-catalogo RAM (MiB)", "ram_ms_catalogo"),
        ("ms-resenas RAM (MiB)", "ram_ms_resenas"),
        ("ms-ordenes RAM (MiB)", "ram_ms_ordenes"),
        ("Mongo RAM (MiB)", "ram_mongo"),
        ("Postgres RAM (MiB)", "ram_pg")
    ]
    
    r = 2
    for vus in vus_list:
        vuln_res = full_data["Vulnerable"].get(vus, {})
        prot_res = full_data["Protegido"].get(vus, {})
        
        runs_v = vuln_res.get("runs", [])
        runs_p = prot_res.get("runs", [])
        n_runs = min(len(runs_v), len(runs_p))
        
        if n_runs < 3:
            # Muy pocos datos para analisis
            ws.cell(row=r, column=1, value=f"VUs: {vus} (Datos Insuficientes: N={n_runs})").font = data_font
            r += 1
            continue
            
        for met_name, met_key in metrics_to_test:
            arr_v = [run.get(met_key, 0.0) for run in runs_v]
            arr_p = [run.get(met_key, 0.0) for run in runs_p]
            
            # Shapiro-Wilk
            w_v, p_v = _safe_shapiro(arr_v)
            w_p, p_p = _safe_shapiro(arr_p)
            
            # Mann-Whitney U
            u_mw, p_mw = _safe_mannwhitneyu(arr_v, arr_p)
            
            conclusion = "No Aplica (Datos ctes)"
            if p_mw is not None:
                if p_mw < 0.05:
                    conclusion = "Diferencia Significativa"
                else:
                    conclusion = "No Significativa"
            
            row_data = [
                met_name, vus, n_runs,
                f"{w_v:.4f}" if w_v else "-", f"{p_v:.4f}" if p_v else "-",
                f"{w_p:.4f}" if w_p else "-", f"{p_p:.4f}" if p_p else "-",
                f"{u_mw:.2f}" if u_mw is not None else "-", 
                f"{p_mw:.4f}" if p_mw is not None else "-", 
                conclusion
            ]
            for c, val in enumerate(row_data, 1):
                cell = ws.cell(row=r, column=c, value=val)
                cell.font = data_font; cell.alignment = center; cell.border = thin
                if c == len(row_data): # conclusion color
                    if conclusion == "Diferencia Significativa":
                        cell.fill = PatternFill("solid", fgColor="C6E0B4") # green
                    elif conclusion == "No Significativa":
                        cell.fill = PatternFill("solid", fgColor="F8CBAD") # orange
                    else:
                        cell.fill = PatternFill("solid", fgColor="D9D9D9") # gray
            r += 1

    # Auto-ajuste de columnas
    for c in range(1, len(headers)+1):
        ws.column_dimensions[get_column_letter(c)].width = 20



def export_excel(results_by_env, atk_name, vus_list, script_path="", level=None):
    """
    Genera un unico Excel con tabla plana donde cada fila = 1 run.
    Ambos entornos aparecen en el mismo sheet, agrupados por VUs.
    results_by_env: {env_name: {vus: metrics_dict_promedio}}
    Para exportar con datos por run, usa export_excel_full().
    """
    if not HAS_EXCEL:
        messagebox.showerror("Error","Instala openpyxl: pip install openpyxl"); return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{atk_name.split(':')[0].strip().replace(' ','_')}_resultados_{timestamp}.xlsx")
    
    if not path: return

    # Intentar leer datos completos por run desde disco
    # si no hay, usar promedios
    full_data = {}   # {env_name: {vus: parse_md_full_result}}
    for env_name in results_by_env:
        env_path = ENVS[env_name]["path"]
        if script_path and os.path.isdir(env_path):
            full_data[env_name] = read_results_full(env_path, script_path, vus_list)
        else:
            full_data[env_name] = {}

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Resultados"
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = "2b579a"

    # ---------- Estilos ----------
    ttl_font  = Font(bold=True, color="000000", name="Calibri", size=13)
    hdr_font  = Font(bold=True, color="FFFFFF", name="Calibri", size=9)
    data_font = Font(color="000000", name="Calibri", size=9)
    center    = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin = Border(
        left=Side(style="thin",color="BFBFBF"), right=Side(style="thin",color="BFBFBF"),
        top=Side(style="thin",color="BFBFBF"),   bottom=Side(style="thin",color="BFBFBF"),
    )
    fill_title  = PatternFill("solid", fgColor="FFFFFF")
    fill_hdr    = PatternFill("solid", fgColor="2F5597") # Azul oscuro para encabezados
    # Vulnerable: Tonos amarillos claros
    fill_vuln_a = PatternFill("solid", fgColor="FFF2CC")
    fill_vuln_b = PatternFill("solid", fgColor="FFE699")
    # Protegido: Tonos azules claros
    fill_prot_a = PatternFill("solid", fgColor="D9E1F2")
    fill_prot_b = PatternFill("solid", fgColor="B4C6E7")
    
    fill_avg    = PatternFill("solid", fgColor="E2EFDA") # Verde muy clarito para promedios
    col_vuln    = Font(bold=False, color="000000", name="Calibri", size=9)
    col_prot    = Font(bold=False, color="000000", name="Calibri", size=9)
    col_avg     = Font(bold=True,  color="000000", name="Calibri", size=9)

    # ---------- Fila de titulo ----------
    NCOLS = 28
    now_str = datetime.now().strftime("%d/%m/%Y %H:%M")
    ws.merge_cells(f"A1:{get_column_letter(NCOLS)}1")
    c = ws["A1"]
    c.value     = f"{atk_name}  —  Exportado: {now_str}"
    c.font      = ttl_font
    c.fill      = fill_title
    c.alignment = center
    ws.row_dimensions[1].height = 30

    # Fila separadora
    ws.merge_cells(f"A2:{get_column_letter(NCOLS)}2")
    ws["A2"].fill = fill_title
    ws.row_dimensions[2].height = 6

    # ---------- Cabeceras ----------
    _nivel_lab, _ = nivel_col(atk_name.split(":")[0].strip(), level)
    HEADERS = [
        "Caso de Uso",
        "Entorno",
        "Tratamiento",
        "Carga (VUs)",
        _nivel_lab,
        "Replica",
        "Fecha",
        "Hora",
        "Peticiones Totales",
        "Throughput (req/s)",
        "Latencia (ms)",
        "Fallos (%)",
        "Bloqueo Control (%)",
        "Disponibilidad (D)",
        "GW CPU (%)",
        "ms-usuarios CPU (%)",
        "ms-catalogo CPU (%)",
        "ms-resenas CPU (%)",
        "ms-ordenes CPU (%)",
        "Mongo CPU (%)",
        "Postgres CPU (%)",
        "GW RAM (MiB)",
        "ms-usuarios RAM (MiB)",
        "ms-catalogo RAM (MiB)",
        "ms-resenas RAM (MiB)",
        "ms-ordenes RAM (MiB)",
        "Mongo RAM (MiB)",
        "Postgres RAM (MiB)",
        "Tipo",
    ]
    for ci, h in enumerate(HEADERS, 1):
        cell = ws.cell(row=3, column=ci, value=h)
        cell.font      = hdr_font
        cell.fill      = fill_hdr
        cell.alignment = center
        cell.border    = thin
    ws.row_dimensions[3].height = 32

    # ---------- Datos ----------
    uc_short = atk_name.split(":")[0].strip()   # e.g. "UC-01"
    row_idx  = 4
    env_order = [e for e in ["Vulnerable","Protegido"] if e in results_by_env]

    for vus in sorted(vus_list):
        for env_name in env_order:
            is_vuln = (env_name == "Vulnerable")
            fill_a  = fill_vuln_a if is_vuln else fill_prot_a
            fill_b  = fill_vuln_b if is_vuln else fill_prot_b
            dfont   = col_vuln if is_vuln else col_prot
            tratam  = TRATAMIENTO.get(env_name, env_name)

            # Datos completos del run
            fd_env = full_data.get(env_name, {})
            fd_vus = fd_env.get(vus)
            avg_m  = results_by_env[env_name].get(vus, {})

            # Determinar runs a escribir
            if fd_vus and fd_vus.get("runs"):
                run_rows = fd_vus["runs"]
                fecha_base = fd_vus["fecha"]
                hora_base  = fd_vus["hora"]
            else:
                # Fallback: una fila con promedio
                fecha_base = datetime.now().strftime("%d/%m/%Y")
                hora_base  = datetime.now().strftime("%H:%M")
                run_rows = [{
                    "idx":1, "peticiones":avg_m.get("peticiones",0),
                    "latencia":avg_m.get("latencia",0), "fallos":avg_m.get("fallos",0),
                    "fecha":fecha_base, "hora":hora_base,
                    "cpu_gw":avg_m.get("cpu_gw",0),
                    "cpu_ms_usuarios":0, "cpu_ms_catalogo":0,
                    "cpu_ms_resenas":0, "cpu_ms_ordenes":0,
                    "cpu_mongo":0, "cpu_pg":0,
                    "ram_gw":0,
                    "ram_ms_usuarios":0, "ram_ms_catalogo":0,
                    "ram_ms_resenas":0, "ram_ms_ordenes":0,
                    "ram_mongo":0, "ram_pg":0,
                }]

            for run in run_rows:
                i   = run["idx"]
                fll = fill_a if i%2==1 else fill_b
                tp_rps = round(run.get("throughput_rps", run["peticiones"] / 60.0), 3)
                disp = run.get("disponibilidad",
                               0 if (run["peticiones"] == 0 or run["fallos"] >= 50.0) else 1)
                _, _nivel_val = nivel_col(uc_short, level)
                row_vals = [
                    uc_short,
                    env_name,
                    tratam,
                    vus,
                    _nivel_val,
                    f"R{i}",
                    run["fecha"],
                    run["hora"],
                    round(run["peticiones"], 2),
                    tp_rps,
                    round(run["latencia"],   2),
                    round(run["fallos"],     2),
                    round(run.get("bloqueo_control", 0.0), 2),
                    disp,
                    round(run["cpu_gw"],     2),
                    round(run.get("cpu_ms_usuarios", 0.0), 2),
                    round(run.get("cpu_ms_catalogo", 0.0), 2),
                    round(run.get("cpu_ms_resenas",  0.0), 2),
                    round(run.get("cpu_ms_ordenes",  0.0), 2),
                    round(run["cpu_mongo"],  2),
                    round(run["cpu_pg"],     2),
                    round(run["ram_gw"],     2),
                    round(run.get("ram_ms_usuarios", 0.0), 2),
                    round(run.get("ram_ms_catalogo", 0.0), 2),
                    round(run.get("ram_ms_resenas",  0.0), 2),
                    round(run.get("ram_ms_ordenes",  0.0), 2),
                    round(run["ram_mongo"],  2),
                    round(run["ram_pg"],     2),
                    "Replica",
                ]
                for ci, val in enumerate(row_vals, 1):
                    cell = ws.cell(row=row_idx, column=ci, value=val)
                    cell.font      = dfont
                    cell.fill      = fll
                    cell.alignment = center
                    cell.border    = thin
                ws.row_dimensions[row_idx].height = 18
                row_idx += 1

        # Fila separadora entre grupos de VUs
        for ci in range(1, NCOLS+1):
            cell = ws.cell(row=row_idx, column=ci, value="")
            cell.fill = fill_title; cell.border = thin
        ws.row_dimensions[row_idx].height = 4
        row_idx += 1

    # ---------- Anchos de columna ----------
    col_widths = [10, 14, 22, 10, 8, 12, 8, 18, 14, 10,
                  12, 16, 16, 15, 15, 13, 15,
                  13, 18, 18, 17, 17, 15, 15, 9]
    for ci, w in enumerate(col_widths, 1):
        if ci <= NCOLS:
            ws.column_dimensions[get_column_letter(ci)].width = w

    # ---------- Freeze header ----------
    ws.freeze_panes = "A4"

    # ---------- Agregar pestaña de Estadistica ----------
    if len(full_data.keys()) >= 2:
        _add_statistics_sheet(wb, full_data, vus_list)

    wb.save(path)
    messagebox.showinfo("Guardado", f"Excel guardado:\n{path}")

# ───────────────────────────────────────────────────────────────────────
# VENTANA DE GRAFICAS
# ───────────────────────────────────────────────────────────────────────
class ChartWindow(tk.Toplevel):
    def __init__(self, parent, results, atk_name):
        """results = {env_name: {vus_int: metrics_dict}} — solo VUs ejecutados"""
        super().__init__(parent)
        self.title(f"Graficas — {atk_name}")
        self.geometry("940x640")
        self.configure(bg=BG)
        self.resizable(True, True)
        self.results  = results
        self.atk_name = atk_name
        self.fig      = None
        self._build()
        self.after(250, self._generate)

    def _build(self):
        bar = tk.Frame(self, bg=BG2, pady=10)
        bar.pack(fill=tk.X)
        inner = tk.Frame(bar, bg=BG2)
        inner.pack(padx=16)

        tk.Label(inner,text="Tipo:",bg=BG2,fg=FG,font=UI).grid(row=0,column=0,padx=(0,4))
        self.ctype = tk.StringVar(value=CHART_TYPES[0])
        ttk.Combobox(inner,textvariable=self.ctype,values=CHART_TYPES,
                     width=22,state="readonly").grid(row=0,column=1,padx=(0,16))

        tk.Label(inner,text="Metrica:",bg=BG2,fg=FG,font=UI).grid(row=0,column=2,padx=(0,4))
        self.metric = tk.StringVar(value=METRICS_DEF[0][0])
        ttk.Combobox(inner,textvariable=self.metric,
                     values=[m[0] for m in METRICS_DEF],
                     width=28,state="readonly").grid(row=0,column=3,padx=(0,16))

        _btn(inner,"Generar",ACC,"#fff",self._generate).grid(row=0,column=4,padx=(0,6))
        _btn(inner,"Exportar PNG / PDF","#1f6feb","#fff",self._export).grid(row=0,column=5)

        tk.Frame(self,bg=BORD,height=1).pack(fill=tk.X)
        self.cf = tk.Frame(self,bg=BG3)
        self.cf.pack(fill=tk.BOTH,expand=True)
        tk.Label(self.cf,text="Generando...",bg=BG3,fg=MUTED,font=("Segoe UI",11)).pack(expand=True)

    def _generate(self):
        metric_lbl = self.metric.get()
        ctype      = self.ctype.get()
        key        = next((k for l,k,_ in METRICS_DEF if l==metric_lbl),"peticiones")
        ylabel     = next((u for l,k,u in METRICS_DEF if l==metric_lbl),"")

        # Reunir series SOLO con VUs presentes en los resultados
        series = {}   # {env_name: (vus_list, vals)}
        for env_name, vus_dict in self.results.items():
            if not vus_dict: continue
            vus_sorted = sorted(vus_dict.keys())
            vals = [vus_dict[v].get(key, 0) for v in vus_sorted]
            series[env_name] = (vus_sorted, vals)

        if not series:
            messagebox.showwarning("Sin datos","No hay datos para graficar."); return

        all_vus  = sorted(set(v for vl,_ in series.values() for v in vl))
        env_list = list(series.keys())
        env_col  = {"Vulnerable":"#f85149","Protegido":"#3fb950"}
        env_mk   = {"Vulnerable":"o","Protegido":"s"}

        plt.rcParams.update({
            "font.family":"DejaVu Sans","font.size":9,
            "axes.titlesize":12,"axes.labelsize":9,
            "figure.facecolor":BG2,"axes.facecolor":BG,
            "axes.edgecolor":BORD,"axes.labelcolor":FG,
            "xtick.color":MUTED,"ytick.color":MUTED,
            "grid.color":BORD,"grid.alpha":0.45,"axes.grid":True,
            "grid.linestyle":"--","legend.facecolor":BG3,
            "legend.edgecolor":BORD,"legend.labelcolor":FG,"text.color":FG,
        })

        fig, ax = plt.subplots(figsize=(10,5.6))
        fig.patch.set_facecolor(BG2)
        atk_short = self.atk_name.split(":")[0].strip()

        def aligned(env_name):
            vl,vals = series[env_name]
            return [vals[vl.index(v)] if v in vl else 0 for v in all_vus]

        if ctype == "Barras Comparativas":
            n = len(env_list); w = 0.68/n; x = np.arange(len(all_vus))
            for i, en in enumerate(env_list):
                a = aligned(en); offset = (i-(n-1)/2)*w
                bars = ax.bar(x+offset, a, w, label=en,
                              color=env_col.get(en,ACC), alpha=0.88, edgecolor="none", zorder=3)
                for b in bars:
                    h=b.get_height()
                    if h>0:
                        ax.text(b.get_x()+b.get_width()/2, h*1.015, f"{h:.1f}",
                                ha="center",va="bottom",fontsize=7.5,
                                color=env_col.get(en,FG))
            ax.set_xticks(np.arange(len(all_vus)))
            ax.set_xticklabels([str(v) for v in all_vus])
            ax.set_xlabel("Usuarios Virtuales (VUs)")

        elif ctype == "Lineas de Tendencia":
            for en in env_list:
                vl,vals = series[en]
                ax.plot(vl, vals, linestyle="-" if en=="Vulnerable" else "--",
                        marker=env_mk.get(en,"o"), color=env_col.get(en,ACC),
                        lw=2.2, ms=8, label=en, zorder=3)
                for v,val in zip(vl,vals):
                    off = 9 if en=="Vulnerable" else -13
                    ax.annotate(f"{val:.1f}",(v,val),
                                textcoords="offset points",xytext=(0,off),
                                ha="center",fontsize=7.5,color=env_col.get(en,FG))
            ax.set_xticks(all_vus)
            ax.set_xlabel("Usuarios Virtuales (VUs)")

        elif ctype == "Barras Horizontales":
            n=len(env_list); h_b=0.66/n; y=np.arange(len(all_vus))
            for i,en in enumerate(env_list):
                a = aligned(en); off = (i-(n-1)/2)*h_b
                ax.barh(y+off, a, h_b, label=en,
                        color=env_col.get(en,ACC), alpha=0.88, zorder=3)
            ax.set_yticks(y); ax.set_yticklabels([f"VUs={v}" for v in all_vus])
            ax.set_xlabel(f"{metric_lbl}")

        elif ctype == "Area con Sombra":
            for en in env_list:
                vl,vals = series[en]; c = env_col.get(en,ACC)
                ax.fill_between(vl,vals,alpha=0.15,color=c)
                ax.plot(vl,vals, linestyle="-" if en=="Vulnerable" else "--",
                        marker=env_mk.get(en,"o"), color=c, lw=2.2,ms=8,label=en,zorder=3)
            ax.set_xticks(all_vus)
            ax.set_xlabel("Usuarios Virtuales (VUs)")

        ax.set_title(f"{atk_short}  —  {metric_lbl}",fontsize=12,pad=12,
                     color=FG,fontweight="bold")
        ax.set_ylabel(ylabel)
        if len(env_list)>0: ax.legend(loc="best",framealpha=0.85)
        fig.tight_layout(pad=2.2)
        self.fig = fig

        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        for w in self.cf.winfo_children(): w.destroy()
        canvas = FigureCanvasTkAgg(fig, master=self.cf)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)

    def _export(self):
        if not self.fig: messagebox.showinfo("Exportar","Genera primero."); return
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG","*.png"),("PDF","*.pdf"),("SVG","*.svg")],
            initialfile=f"{self.atk_name.replace(':','').replace(' ','_')}.png",
            title="Guardar grafica")
        if path:
            self.fig.savefig(path,dpi=200,bbox_inches="tight",
                             facecolor=self.fig.get_facecolor())
            messagebox.showinfo("Guardado",f"Grafica guardada:\n{path}")

# ───────────────────────────────────────────────────────────────────────
# HELPERS UI COMUNES
# ───────────────────────────────────────────────────────────────────────
def _btn(parent,text,bg,fg,cmd,size=9,pady=7):
    return tk.Button(parent,text=text,bg=bg,fg=fg,font=("Segoe UI",size,"bold"),
                     relief=tk.FLAT,bd=0,cursor="hand2",
                     activebackground=bg,activeforeground=fg,
                     pady=pady,padx=10,command=cmd)

def _sec(parent,text):
    tk.Label(parent,text=text.upper(),bg=BG2,fg=MUTED,font=UI_SM_B
             ).pack(anchor=tk.W,padx=14,pady=(12,3))

def _div(parent):
    tk.Frame(parent,bg=BORD,height=1).pack(fill=tk.X,padx=14,pady=4)

def _card(parent,**kw):
    return tk.Frame(parent,bg=BG2,highlightthickness=1,highlightbackground=BORD,**kw)

def style_ttk():
    s=ttk.Style(); s.theme_use("clam")
    s.configure("TCombobox",fieldbackground=BG3,background=BG3,foreground=FG,
                selectbackground=BG3,selectforeground=FG,arrowcolor=MUTED,
                bordercolor=BORD,lightcolor=BORD,darkcolor=BORD)
    s.map("TCombobox",fieldbackground=[("readonly",BG3)],background=[("readonly",BG3)])

# ───────────────────────────────────────────────────────────────────────
# WIDGET: VUs CHECKBOXES
# ───────────────────────────────────────────────────────────────────────
class VUsSelector(tk.Frame):
    """Fila de checkboxes para seleccionar VUs + boton 'Todos'."""
    def __init__(self, parent, **kw):
        super().__init__(parent, bg=BG2, **kw)
        self._vars = {}
        # Checkboxes individuales
        for vus in ALL_VUS:
            var = tk.BooleanVar(value=False)
            self._vars[vus] = var
            cb = tk.Checkbutton(
                self, text=str(vus), variable=var,
                bg=BG2, fg=FG, selectcolor=BG3,
                activebackground=BG2, activeforeground=FG,
                font=UI_SM, bd=0, padx=2,
                command=self._on_change
            )
            cb.pack(side=tk.LEFT, padx=(0,4))
        # Boton todos / ninguno
        self._all = False
        self._btn_all = tk.Button(self,text="Todos",bg=BG3,fg=MUTED,
                                  font=UI_SM,relief=tk.FLAT,bd=0,
                                  padx=6,pady=2,cursor="hand2",
                                  command=self._toggle_all)
        self._btn_all.pack(side=tk.LEFT,padx=(6,0))

    def _toggle_all(self):
        self._all = not self._all
        for var in self._vars.values():
            var.set(self._all)
        self._btn_all.config(text="Ninguno" if self._all else "Todos")
        self._on_change()

    def _on_change(self):
        selected = self.get()
        self._all = len(selected)==len(ALL_VUS)
        self._btn_all.config(text="Ninguno" if self._all else "Todos")

    def get(self):
        """Retorna lista de VUs seleccionados ordenada."""
        return sorted([v for v,var in self._vars.items() if var.get()])

    def select_default(self):
        first = ALL_VUS[0] if ALL_VUS else 1
        if first in self._vars:
            self._vars[first].set(True)
        self._on_change()

# ───────────────────────────────────────────────────────────────────────
# PANEL DE BOTONES POST-EJECUCION (Grafica + Excel)
# ───────────────────────────────────────────────────────────────────────
class ResultPanel(tk.Frame):
    """Barra con botones de grafica y exportar. Se activa tras ejecucion."""
    def __init__(self, parent, on_chart, on_excel_all, mode="simple"):
        super().__init__(parent, bg=BG)
        self.mode = mode

        self.btn_chart = _btn(self,"Ver Graficas",ACC,"#fff",on_chart)
        self.btn_chart.pack(side=tk.LEFT,padx=(0,6))

        self.btn_excel = _btn(self,"Exportar Excel","#1f6feb","#fff",on_excel_all)
        self.btn_excel.pack(side=tk.LEFT,padx=(0,6))

        self.disable_all()

    def enable_all(self):
        for w in self.winfo_children():
            try:
                w.config(state=tk.NORMAL)  # type: ignore
                # Restaurar colores
                if w == self.btn_chart:
                    w.config(bg=ACC, fg="#fff")  # type: ignore
                elif w == self.btn_excel:
                    w.config(bg="#1f6feb", fg="#fff")  # type: ignore
                else:
                    w.config(bg=BG3, fg=FG)  # type: ignore
            except tk.TclError:
                pass

    def disable_all(self):
        for w in self.winfo_children():
            try:
                w.config(state=tk.DISABLED, bg=BG3, fg=MUTED)  # type: ignore
            except tk.TclError:
                pass

# ───────────────────────────────────────────────────────────────────────
# CONSOLA HELPERS
# ───────────────────────────────────────────────────────────────────────
TAGS = {
    "hdr":  {"foreground":ACC,  "font":MONO},
    "ok":   {"foreground":CYAN},
    "err":  {"foreground":RED},
    "warn": {"foreground":ORG},
    "info": {"foreground":BLUE},
    "num":  {"foreground":YEL},
    "data": {"foreground":FG},
    "dim":  {"foreground":MUTED},
    "sep":  {"foreground":BG3},
    "val":  {"foreground":GREEN, "font":MONO},
}

def setup_tags(widget):
    for tag,opts in TAGS.items():
        widget.tag_config(tag,**opts)

def tag_for(line):
    low = line.lower()
    if not line.strip(): return "dim"
    if any(k in low for k in ["error","failed","exception","traceback"]): return "err"
    if any(k in low for k in ["exitoso","completad","ok","success"]): return "ok"
    if any(k in low for k in ["warn","reinici","restart","esperando"]): return "warn"
    if any(k in line for k in ["===","────","----"]): return "sep"
    if any(k in line for k in ["RUN ","ORQUESTADOR","EJECUTANDO","REPORTE","RESUMEN"]): return "hdr"
    if any(k in low for k in ["peticion","latencia","promedio","cpu","ram","vus","ms","fallos"]): return "num"
    if any(k in low for k in ["iniciando","ejecutando","procesando","corriendo","copiando"]): return "info"
    return "data"

# ───────────────────────────────────────────────────────────────────────
# APP PRINCIPAL
# ───────────────────────────────────────────────────────────────────────
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Panel de Control — Entorno Experimental GraphQL")
        self.geometry("1380x900")
        self.minsize(1100,720)
        self.configure(bg=BG)
        style_ttk()

        self.running = False
        self.process = None

        # Resultados de ultima ejecucion
        # {env_name: {vus_int: metrics_dict}}
        self.s_results  = {}    # simple
        self.c_results  = {"Vulnerable":{},"Protegido":{}}  # comparative
        self.last_atk   = ATK_NAMES[0]
        self.last_script= ATTACKS[ATK_NAMES[0]]["script"]
        self.last_vus   = []    # VUs realmente ejecutados
        self.last_level = None  # nivel usado (profundidad/ciclos/alias/factor)

        self._build()

    # ─────────────────────────────────────────────────────────
    # BUILD
    # ─────────────────────────────────────────────────────────
    def _build(self):
        # Topbar
        top = tk.Frame(self,bg=BG2,height=50)
        top.pack(fill=tk.X); top.pack_propagate(False)
        tk.Label(top,text=" ⬡ ",bg=ACC,fg="#fff",
                 font=("Segoe UI",13,"bold"),padx=4).pack(side=tk.LEFT)
        tk.Label(top,text=" Panel de Control  —  Entorno Experimental GraphQL",
                 bg=BG2,fg=FG,font=("Segoe UI",12,"bold")).pack(side=tk.LEFT,padx=6)
        self.lbl_status = tk.Label(top,text="● Inactivo",bg=BG2,fg=MUTED,font=UI)
        self.lbl_status.pack(side=tk.RIGHT,padx=20)
        tk.Frame(self,bg=BORD,height=1).pack(fill=tk.X)

        # Tabs
        tbar = tk.Frame(self,bg=BG,height=38)
        tbar.pack(fill=tk.X); tbar.pack_propagate(False)
        self._tbns=[]; self._pages=[]
        for i,lbl in enumerate(["  Ejecucion Simple  ","  Ejecucion Comparativa  "]):
            b=tk.Button(tbar,text=lbl,font=UI,relief=tk.FLAT,bd=0,cursor="hand2",
                        command=lambda idx=i:self._switch(idx))
            b.pack(side=tk.LEFT)
            self._tbns.append(b)
        tk.Frame(self,bg=ACC,height=2).pack(fill=tk.X)
        self._cnt=tk.Frame(self,bg=BG); self._cnt.pack(fill=tk.BOTH,expand=True)
        self._build_simple()
        self._build_comparative()
        self._switch(0)

    def _switch(self,idx):
        for i,(b,p) in enumerate(zip(self._tbns,self._pages)):
            if i==idx:
                b.config(bg=BG3,fg=FG,font=UI_B); p.pack(fill=tk.BOTH,expand=True)
            else:
                b.config(bg=BG,fg=MUTED,font=UI); p.pack_forget()

    # ─────────────────────────────────────────────────────────
    # PANEL IZQUIERDO (COMPARTIDO - misma estructura)
    # ─────────────────────────────────────────────────────────
    def _make_left_panel(self, parent, atk_var, runs_var, vus_widget_holder, env_radios=False):
        """Construye el panel izquierdo uniforme."""
        card = _card(parent, width=380)
        card.pack(side=tk.LEFT,fill=tk.Y,padx=(12,6),pady=12)
        card.pack_propagate(False)

        # Ataque
        _sec(card,"Ataque")
        atk_cb = ttk.Combobox(card,textvariable=atk_var,values=ATK_NAMES,
                               state="readonly",font=UI)
        atk_cb.pack(fill=tk.X,padx=12,pady=(0,4))

        lbl_desc = tk.Label(card,text="",bg=BG2,fg=MUTED,font=("Segoe UI",8),
                             justify=tk.LEFT,wraplength=346,anchor=tk.NW)
        lbl_desc.pack(fill=tk.X,padx=14,pady=(2,6))

        _div(card)

        if env_radios:
            _sec(card,"Entorno")
            env_var = tk.StringVar(value="Vulnerable")
            for en,ev in ENVS.items():
                row=tk.Frame(card,bg=BG2); row.pack(fill=tk.X,padx=12,pady=2)
                tk.Radiobutton(row,text=f"  {en}",variable=env_var,value=en,
                               bg=BG2,fg=ev["color"],selectcolor=BG3,
                               activebackground=BG2,activeforeground=ev["color"],
                               font=("Segoe UI",10,"bold")).pack(side=tk.LEFT)
                tk.Label(row,text=ev["label"],bg=BG2,fg=MUTED,
                         font=("Segoe UI",7)).pack(side=tk.LEFT,padx=(4,0))
            _div(card)
        else:
            env_var = None

        # VUs
        _sec(card,"Usuarios Virtuales (VUs)")
        vus_sel = VUsSelector(card)
        vus_sel.pack(padx=12,pady=(0,4),anchor=tk.W)
        vus_sel.select_default()
        vus_widget_holder.append(vus_sel)

        _div(card)

        # Runs
        _sec(card,"Parametros")
        pf=tk.Frame(card,bg=BG2); pf.pack(fill=tk.X,padx=14,pady=(0,6))
        tk.Label(pf,text="Num. Ejecuciones:",bg=BG2,fg=FG,font=UI,
                 width=20,anchor=tk.W).grid(row=0,column=0,pady=4,sticky=tk.W)
        runs_cb=ttk.Combobox(pf,textvariable=runs_var,values=RUNS_OPTS,
                              width=6,state="readonly")
        runs_cb.grid(row=0,column=1,padx=(8,0),pady=4)

        # Nivel de Intensidad (para UC-02/03/04/05)
        _sec(card,"Nivel de Intensidad")
        level_f=tk.Frame(card,bg=BG2); level_f.pack(fill=tk.X,padx=14,pady=(0,4))
        level_var = tk.IntVar(value=1)
        level_lbl = tk.Label(level_f,text="Nivel:",bg=BG2,fg=FG,font=UI,
                             width=8,anchor=tk.W)
        level_lbl.grid(row=0,column=0,pady=4,sticky=tk.W)
        level_spin = tk.Spinbox(level_f,from_=1,to=9,textvariable=level_var,
                                 width=4,font=UI,state="readonly",
                                 bg=BG3,fg=FG,buttonbackground=BG3,
                                 readonlybackground=BG3)
        level_spin.grid(row=0,column=1,padx=(8,0),pady=4)
        level_desc_lbl = tk.Label(level_f,text="",bg=BG2,fg=MUTED,font=("Segoe UI",7),
                                   anchor=tk.W)
        level_desc_lbl.grid(row=0,column=2,padx=(8,0),pady=4,sticky=tk.W)

        _div(card)
        return card, lbl_desc, env_var, level_var, level_spin, level_desc_lbl

    # ─────────────────────────────────────────────────────────
    # TAB 1: EJECUCION SIMPLE
    # ─────────────────────────────────────────────────────────
    def _build_simple(self):
        page=tk.Frame(self._cnt,bg=BG); self._pages.append(page)

        self.s_atk  = tk.StringVar(value=ATK_NAMES[0])
        self.s_runs = tk.StringVar(value="1")
        self.s_env  = tk.StringVar(value="Vulnerable")
        self._s_vus_holder = []

        card, lbl_desc, env_var, s_level_var, s_level_spin, s_level_desc = self._make_left_panel(
            page, self.s_atk, self.s_runs, self._s_vus_holder, env_radios=True
        )
        self.s_env = env_var
        self.s_level_var = s_level_var
        self._s_level_spin = s_level_spin
        self._s_level_desc = s_level_desc

        def _update_level_range(*_):
            name = self.s_atk.get()
            uc_key = name[:5] if name else ""
            info = UC_LEVELS.get(uc_key)
            if info and uc_key != "UC-01":
                self._s_level_spin.config(state="normal")
                self._s_level_spin.config(to=info["max"])
                self._s_level_spin.config(state="readonly")
                self._s_level_desc.config(text=info["label"])
                if self.s_level_var.get() > info["max"]:
                    self.s_level_var.set(1)
            else:
                self._s_level_spin.config(state="normal")
                self.s_level_var.set(1)
                self._s_level_spin.config(state="disabled")
                self._s_level_desc.config(text="No aplica para este UC")

        def on_atk(*_):
            name = self.s_atk.get()
            if name in ATTACKS:
                atk = ATTACKS[name]
                lbl_desc.config(text=atk["desc"])
                _update_level_range()
                # Mostrar query del nivel actual
                level = self.s_level_var.get()
                if atk.get("nivel_queries"):
                    q = atk["nivel_queries"].get(level, "")
                    self._set_query(q, self.s_query_txt)
                else:
                    self._set_query(atk["query"], self.s_query_txt)

        def on_level(*_):
            on_atk()

        self._s_level_spin.config(command=on_level)
        self.s_atk.trace_add("write", on_atk)
        self.s_level_var.trace_add("write", on_level)

        # Botones
        bf=tk.Frame(card,bg=BG2)
        bf.pack(fill=tk.X,padx=12,pady=(0,12))

        self.s_btn_run = _btn(bf,"EJECUTAR ATAQUE",ACC,"#fff",self._run_simple,size=10)
        self.s_btn_run.pack(fill=tk.X,pady=(0,5))

        self.s_btn_stop = _btn(bf,"Detener","#2d2d2d",MUTED,self._stop)
        self.s_btn_stop.pack(fill=tk.X,pady=(0,8))
        self.s_btn_stop.config(state=tk.DISABLED)

        tk.Frame(bf,bg=BORD,height=1).pack(fill=tk.X,pady=(0,8))

        self.s_rp = ResultPanel(bf,
            on_chart=self._chart_simple,
            on_excel_all=self._excel_simple,
            mode="simple")
        self.s_rp.pack(fill=tk.X)

        # Panel derecho
        right=tk.Frame(page,bg=BG)
        right.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=(0,12),pady=12)

        tk.Label(right,text="QUERY GraphQL",bg=BG,fg=MUTED,font=UI_SM_B).pack(anchor=tk.W,pady=(0,3))
        self.s_query_txt = scrolledtext.ScrolledText(
            right,bg="#161b22",fg=FG,font=MONO_SM,height=9,bd=0,wrap=tk.NONE,
            padx=12,pady=8,insertbackground=FG,
            highlightthickness=1,highlightcolor=BORD,highlightbackground=BORD)
        self.s_query_txt.pack(fill=tk.X,pady=(0,8))
        self.s_query_txt.config(state=tk.DISABLED)

        ch=tk.Frame(right,bg=BG); ch.pack(fill=tk.X,pady=(0,3))
        tk.Label(ch,text="SALIDA EN TIEMPO REAL",bg=BG,fg=MUTED,font=UI_SM_B).pack(side=tk.LEFT)
        tk.Button(ch,text="Limpiar",bg=BG3,fg=MUTED,font=UI_SM,
                  relief=tk.FLAT,bd=0,padx=6,cursor="hand2",
                  command=lambda:self._clr(self.s_console)).pack(side=tk.RIGHT)

        self.s_console=scrolledtext.ScrolledText(
            right,bg="#0a0f14",fg=MUTED,font=MONO_SM,bd=0,wrap=tk.WORD,
            padx=12,pady=8,highlightthickness=1,
            highlightcolor=BORD,highlightbackground=BORD)
        self.s_console.pack(fill=tk.BOTH,expand=True)
        setup_tags(self.s_console)

        # Iniciar con el primer ataque
        self.s_atk.set(ATK_NAMES[0])
        on_atk()

    # ─────────────────────────────────────────────────────────
    # TAB 2: EJECUCION COMPARATIVA
    # ─────────────────────────────────────────────────────────
    def _build_comparative(self):
        page=tk.Frame(self._cnt,bg=BG); self._pages.append(page)

        self.c_atk  = tk.StringVar(value=ATK_NAMES[0])
        self.c_runs = tk.StringVar(value="1")
        self._c_vus_holder = []

        card, lbl_desc, _, c_level_var, c_level_spin, c_level_desc = self._make_left_panel(
            page, self.c_atk, self.c_runs, self._c_vus_holder, env_radios=False
        )
        self.c_level_var = c_level_var
        self._c_level_spin = c_level_spin
        self._c_level_desc = c_level_desc

        def _update_level_range_c(*_):
            name = self.c_atk.get()
            uc_key = name[:5] if name else ""
            info = UC_LEVELS.get(uc_key)
            if info and uc_key != "UC-01":
                self._c_level_spin.config(state="normal")
                self._c_level_spin.config(to=info["max"])
                self._c_level_spin.config(state="readonly")
                self._c_level_desc.config(text=info["label"])
                if self.c_level_var.get() > info["max"]:
                    self.c_level_var.set(1)
            else:
                self._c_level_spin.config(state="normal")
                self.c_level_var.set(1)
                self._c_level_spin.config(state="disabled")
                self._c_level_desc.config(text="No aplica para este UC")

        def on_atk(*_):
            name = self.c_atk.get()
            if name in ATTACKS:
                atk = ATTACKS[name]
                lbl_desc.config(text=atk["desc"])
                _update_level_range_c()
                level = self.c_level_var.get()
                if atk.get("nivel_queries"):
                    q = atk["nivel_queries"].get(level, "")
                    self._set_query(q, self.c_query_txt)
                else:
                    self._set_query(atk["query"], self.c_query_txt)

        def on_level_c(*_):
            on_atk()

        self._c_level_spin.config(command=on_level_c)
        self.c_atk.trace_add("write", on_atk)
        self.c_level_var.trace_add("write", on_level_c)

        # Botones
        bf=tk.Frame(card,bg=BG2)
        bf.pack(fill=tk.X,padx=12,pady=(0,12))

        info = tk.Label(bf,
            text="Ejecuta Vulnerable, luego Protegido\nautomaticamente en secuencia.",
            bg=BG2,fg=MUTED,font=("Segoe UI",8),justify=tk.LEFT)
        info.pack(anchor=tk.W,pady=(0,6))

        self.c_btn_run = _btn(bf,"EJECUTAR AMBOS ENTORNOS",ACC,"#fff",
                              self._run_comparative,size=10)
        self.c_btn_run.pack(fill=tk.X,pady=(0,5))

        self.c_btn_stop = _btn(bf,"Detener","#2d2d2d",MUTED,self._stop)
        self.c_btn_stop.pack(fill=tk.X,pady=(0,8))
        self.c_btn_stop.config(state=tk.DISABLED)

        tk.Frame(bf,bg=BORD,height=1).pack(fill=tk.X,pady=(0,8))

        self.c_rp = ResultPanel(bf,
            on_chart=self._chart_comparative,
            on_excel_all=self._excel_comparative,
            mode="comparative")
        self.c_rp.pack(fill=tk.X)

        # Panel derecho
        right=tk.Frame(page,bg=BG)
        right.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=(0,12),pady=12)

        tk.Label(right,text="QUERY GraphQL",bg=BG,fg=MUTED,font=UI_SM_B).pack(anchor=tk.W,pady=(0,3))
        self.c_query_txt=scrolledtext.ScrolledText(
            right,bg="#161b22",fg=FG,font=MONO_SM,height=7,bd=0,wrap=tk.NONE,
            padx=12,pady=8,insertbackground=FG,
            highlightthickness=1,highlightcolor=BORD,highlightbackground=BORD)
        self.c_query_txt.pack(fill=tk.X,pady=(0,8))
        self.c_query_txt.config(state=tk.DISABLED)

        # Consolas lado a lado
        cons=tk.Frame(right,bg=BG); cons.pack(fill=tk.BOTH,expand=True,pady=(0,6))
        for en,ev in ENVS.items():
            col=tk.Frame(cons,bg=BG)
            col.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,
                     padx=(0,4) if en=="Vulnerable" else (4,0))
            hdr=tk.Frame(col,bg=BG); hdr.pack(fill=tk.X,pady=(0,3))
            tk.Label(hdr,text=f"● {en.upper()}",bg=BG,fg=ev["color"],
                     font=UI_SM_B).pack(side=tk.LEFT)
            slbl=tk.Label(hdr,text="",bg=BG,fg=MUTED,font=UI_SM); slbl.pack(side=tk.RIGHT)
            c=scrolledtext.ScrolledText(col,bg="#0a0f14",fg=MUTED,font=MONO_SM,
                                        bd=0,wrap=tk.WORD,padx=10,pady=6,
                                        highlightthickness=1,
                                        highlightcolor=ev["color"],
                                        highlightbackground=BORD)
            c.pack(fill=tk.BOTH,expand=True); c.config(state=tk.DISABLED)
            setup_tags(c)
            if en=="Vulnerable":
                self.v_console=c; self.v_status=slbl
            else:
                self.p_console=c; self.p_status=slbl

        # Iniciar
        self.c_atk.set(ATK_NAMES[0]); on_atk()

    # ─────────────────────────────────────────────────────────
    # HELPERS
    # ─────────────────────────────────────────────────────────
    def _set_query(self,text,widget):
        widget.config(state=tk.NORMAL)
        widget.delete("1.0",tk.END)
        widget.insert("1.0",text)
        # Highlight
        widget.tag_config("kw",foreground="#ff79c6")
        widget.tag_config("str",foreground="#f1fa8c")
        widget.tag_config("cmt",foreground="#6272a4")
        widget.tag_config("spr",foreground="#ffb86c")
        for kw in ["query","mutation","fragment","on","subscription"]:
            start="1.0"
            while True:
                pos=widget.search(r"\b"+kw+r"\b",start,tk.END,regexp=True)
                if not pos: break
                end=f"{pos}+{len(kw)}c"
                widget.tag_add("kw",pos,end); start=end
        for m in re.finditer(r'"[^"]*"',text):
            ls=text[:m.start()].count("\n")+1
            cs=m.start()-(text[:m.start()].rfind("\n")+1)
            le=text[:m.end()].count("\n")+1
            ce=m.end()-(text[:m.end()].rfind("\n")+1)
            widget.tag_add("str",f"{ls}.{cs}",f"{le}.{ce}")
        for m in re.finditer(r"#.*$",text,re.MULTILINE):
            ls=text[:m.start()].count("\n")+1
            cs=m.start()-(text[:m.start()].rfind("\n")+1)
            widget.tag_add("cmt",f"{ls}.{cs}",f"{ls}.end")
        for m in re.finditer(r"\.\.\.",text):
            ls=text[:m.start()].count("\n")+1
            cs=m.start()-(text[:m.start()].rfind("\n")+1)
            widget.tag_add("spr",f"{ls}.{cs}",f"{ls}.{cs+3}")
        widget.config(state=tk.DISABLED)

    def _log(self,text,tag="data",w=None):
        if w is None: w=self.s_console
        def _do():
            w.config(state=tk.NORMAL)
            w.insert(tk.END,text+"\n",tag)
            w.see(tk.END)
            w.config(state=tk.DISABLED)
        self.after(0,_do)

    def _log_sep(self,w=None):
        self._log("  "+"─"*46,"sep",w)

    def _log_kv(self,label,value,w=None):
        ww=w if w else self.s_console
        def _do():
            ww.config(state=tk.NORMAL)
            ww.insert(tk.END,f"  {label:<28}","dim")
            ww.insert(tk.END,f"{value}\n","val")
            ww.see(tk.END)
            ww.config(state=tk.DISABLED)
        self.after(0,_do)

    def _clr(self,w):
        w.config(state=tk.NORMAL); w.delete("1.0",tk.END); w.config(state=tk.DISABLED)

    def _setstatus(self,text,color=MUTED):
        self.after(0,lambda:self.lbl_status.config(text=text,fg=color))

    # ─────────────────────────────────────────────────────────
    # DOCKER AUTOMATICO
    # ─────────────────────────────────────────────────────────
    def _ensure_env(self,env_name,w):
        env_path=ENVS[env_name]["path"]
        if not os.path.isdir(env_path):
            self._log(f"  ERROR: directorio no encontrado:\n  {env_path}","err",w); return False
        self._log(f"  Preparando entorno {env_name}...","info",w)
        # Bajar TODOS los entornos primero y esperar a que terminen
        for e in ENVS.values():
            if os.path.isdir(e["path"]):
                subprocess.run(["docker-compose","down","--remove-orphans"],cwd=e["path"],
                               capture_output=True,timeout=60,shell=True)
        time.sleep(3)  # Dar tiempo a Docker para liberar recursos
        # Levantar el entorno deseado
        r=subprocess.run(["docker-compose","up","-d","--wait"],cwd=env_path,
                         capture_output=True,text=True,timeout=300,shell=True)
        # Docker Compose v2 escribe TODO el progreso en stderr (Creating, Started, etc.)
        # Solo es error real si returncode!=0 Y stderr contiene palabras de fallo genuino
        if r.returncode!=0:
            stderr_text = r.stderr.strip() if r.stderr else ""
            fail_keywords = ["error response from daemon","unable to","failed to",
                             "no such","permission denied","bind:","port is already"]
            has_real_error = any(kw in stderr_text.lower() for kw in fail_keywords)
            if has_real_error:
                self._log(f"  ERROR docker:\n{stderr_text[:300]}","err",w); return False
        self._log(f"  Entorno listo. Estabilizando 15s...","ok",w)
        time.sleep(15); return True

    def _stop(self):
        if self.process:
            self._log("  Deteniendo...","warn")
            try: self.process.terminate(); self.process.wait(timeout=8)
            except:
                try: self.process.kill()
                except: pass
        self._finish_both()

    # ─────────────────────────────────────────────────────────
    # CORE EXEC
    # ─────────────────────────────────────────────────────────
    def _wait_gateway(self, timeout=80):
        """Espera hasta que el gateway federado responda (cualquier respuesta = vivo).
        Evita las filas en 0 por arrancar k6 antes de que el supergrafo este listo."""
        import urllib.request, urllib.error, json
        payload = json.dumps({"query": "{ __typename }"}).encode()
        start = time.time()
        while time.time() - start < timeout:
            if not self.running:
                return False
            try:
                req = urllib.request.Request("http://localhost:4000/graphql",
                    data=payload, headers={"Content-Type": "application/json"})
                urllib.request.urlopen(req, timeout=5)
                return True
            except urllib.error.HTTPError:
                return True   # respondio (aunque sea 4xx) = gateway vivo
            except Exception:
                time.sleep(2)  # aun no responde; reintenta
        return False

    def _exec_vus(self,env_path,script,vus_list,runs,w,on_done,level=None):
        """Ejecuta prueba para cada VUs seleccionado secuencialmente."""
        self.last_level = level   # para que el Excel muestre la columna del nivel
        run_script=os.path.join(env_path,"load_tests","run_multiple_experiments.py")
        if not os.path.isfile(run_script):
            self._log(f"  No encontrado: {run_script}","err",w)
            on_done(False,{}); return

        all_results={}
        for vus in vus_list:
            if not self.running: break
            self._log_sep(w)
            level_info = f" | Nivel={level}" if level else ""
            self._log(f"  Ejecutando VUs={vus} | Runs={runs}{level_info}","hdr",w)
            self._log_sep(w)

            # Restart rapido entre VUs
            subprocess.run(["docker-compose","restart"],cwd=env_path,
                           capture_output=True,timeout=60,shell=True)
            # Esperar a que el gateway RESPONDA antes de lanzar k6.
            # (Si arranca antes de que recomponga el supergrafo, k6 recibe 0 y da filas en 0.)
            self._log("  Esperando a que el gateway responda...","info",w)
            if not self._wait_gateway():
                self._log("  [!] El gateway tardo en responder; el resultado podria salir en 0.","warn",w)

            cmd=[sys.executable,run_script,
                 "--test-script",script,"--vus",str(vus),"--runs",str(runs)]
            # Pasar LEVEL como variable de entorno al script K6
            env = os.environ.copy()
            if level is not None:
                env["LEVEL"] = str(level)
            self.process=subprocess.Popen(
                cmd,cwd=env_path,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                text=True,encoding="utf-8",errors="replace",bufsize=1,env=env)

            in_metrics=False; in_resources=False
            for line in self.process.stdout:
                line=sa(line.rstrip())
                if not line: continue
                if "RESUMEN DE M" in line or "METRICAS K6" in line:
                    in_metrics=True; in_resources=False
                    self._log("  METRICAS K6","hdr",w); continue
                if "PICOS DE CPU" in line:
                    in_resources=True; in_metrics=False
                    self._log("  RECURSOS — CPU","hdr",w); continue
                if "PICOS DE MEMORIA" in line:
                    in_resources=True; in_metrics=False
                    self._log("  RECURSOS — MEMORIA","hdr",w); continue
                if "PROMEDIO" in line and "|" in line and in_metrics:
                    parts=[p.strip().strip("*") for p in line.split("|") if p.strip()]
                    if len(parts)>=4:
                        self._log_kv("  Peticiones prom.",parts[1],w)
                        self._log_kv("  Latencia media",  parts[2],w)
                        self._log_kv("  Tasa de fallos",  parts[3],w)
                    continue
                if "|" in line and in_resources and "---" not in line and "Run" not in line:
                    parts=[p.strip().strip("*") for p in line.split("|") if p.strip()]
                    if len(parts)>=2 and parts[0] not in ("Contenedor","Servicio"):
                        self._log_kv(f"    {parts[0]}"," | ".join(parts[1:]),w)
                    continue
                if "|" in line and in_metrics and "---" not in line and "Run" not in line:
                    parts=[p.strip().strip("*") for p in line.split("|") if p.strip()]
                    if len(parts)>=4 and parts[0] not in ("Ejecucion","Run","Ejec"):
                        self._log_kv(f"  Run {parts[0]}",
                                     f"{parts[1]} req  |  {parts[2]}  |  {parts[3]} fallos",w)
                    continue
                self._log(f"  {line}",tag_for(line),w)

            self.process.wait()

            # Leer resultado del disco para este VUs (el archivo incluye _nivelN cuando hay nivel)
            uc_dir=os.path.dirname(script)
            level_str=f"_nivel{level}" if level else ""
            md_path=os.path.join(env_path,"load_tests",uc_dir,"resultados",
                                 f"reporte_consolidado_{runs}runs_vus{vus}{level_str}.md")
            if os.path.isfile(md_path):
                with open(md_path,encoding="utf-8",errors="replace") as f:
                    all_results[vus]=parse_md(f.read())
                self._log(f"  Resultado VUs={vus} registrado.","ok",w)
                
                fallos = all_results[vus].get("fallos", 0.0)
                if fallos >= 50.0:
                    self._log(f"  [ABORT] Servidor colapsado ({fallos}% fallos).","warn",w)
                    self._log("  Abortando la ejecución de los VUs restantes.","warn",w)
                    break
            else:
                self._log(f"  Reporte VUs={vus} no encontrado en disco.","warn",w)

        on_done(True,all_results)

    # ─────────────────────────────────────────────────────────
    # EJECUCION SIMPLE
    # ─────────────────────────────────────────────────────────
    def _run_simple(self):
        if self.running: messagebox.showwarning("En ejecucion","Ya hay una prueba activa."); return
        atk_name=self.s_atk.get()
        if atk_name not in ATTACKS: messagebox.showwarning("Seleccion","Selecciona un ataque."); return
        vus_list=self._s_vus_holder[0].get()
        if not vus_list: messagebox.showwarning("VUs","Selecciona al menos un valor de VUs."); return

        atk=ATTACKS[atk_name]; env_name=self.s_env.get()
        runs=self.s_runs.get(); env_path=ENVS[env_name]["path"]
        level = self.s_level_var.get()
        # Usar script parametrizado si existe, sino el original
        script = atk.get("script_nivel") or atk["script"]
        self.last_atk=atk_name; self.last_script=script; self.last_vus=vus_list
        self.s_results={}

        self.running=True
        self.after(0,lambda:self.s_btn_run.config(state=tk.DISABLED,bg="#444"))
        self.after(0,lambda:self.s_btn_stop.config(state=tk.NORMAL,bg=RED))
        self.s_rp.disable_all()
        self._setstatus(f"● {env_name} — {atk_name} Nivel {level}...",ORG)
        self._clr(self.s_console)
        self._log_sep()
        self._log(f"  {atk_name}  |  Nivel {level}","hdr")
        self._log(f"  Entorno: {env_name}  |  VUs: {vus_list}  |  Runs: {runs}","info")
        self._log_sep()

        def thread():
            ok=self._ensure_env(env_name,self.s_console)
            if not ok: self._finish_simple(env_name,False); return
            def on_done(success,results):
                self.s_results={env_name:results}
                self._finish_simple(env_name,success)
            self._exec_vus(env_path,script,vus_list,runs,self.s_console,on_done,level=level)
        threading.Thread(target=thread,daemon=True).start()

    def _finish_simple(self,env_name,success):
        self.running=False; self.process=None
        self.after(0,lambda:self.s_btn_run.config(state=tk.NORMAL,bg=ACC))
        self.after(0,lambda:self.s_btn_stop.config(state=tk.DISABLED,bg="#2d2d2d"))
        if self.s_results.get(env_name):
            self.after(0,self.s_rp.enable_all)
        c=ENVS[env_name]["color"] if success else ORG
        self._setstatus(f"● {env_name} — {'Completado' if success else 'Error'}",c)

    # ─────────────────────────────────────────────────────────
    # EJECUCION COMPARATIVA
    # ─────────────────────────────────────────────────────────
    def _run_comparative(self):
        if self.running: messagebox.showwarning("En ejecucion","Ya hay una prueba activa."); return
        atk_name=self.c_atk.get()
        if atk_name not in ATTACKS: messagebox.showwarning("Seleccion","Selecciona un ataque."); return
        vus_list=self._c_vus_holder[0].get()
        if not vus_list: messagebox.showwarning("VUs","Selecciona al menos un valor de VUs."); return

        atk=ATTACKS[atk_name]; runs=self.c_runs.get()
        level = self.c_level_var.get()
        script = atk.get("script_nivel") or atk["script"]
        self.last_atk=atk_name; self.last_script=script; self.last_vus=vus_list
        self.c_results={"Vulnerable":{},"Protegido":{}}

        self.running=True
        self.after(0,lambda:self.c_btn_run.config(state=tk.DISABLED,bg="#444"))
        self.after(0,lambda:self.c_btn_stop.config(state=tk.NORMAL,bg=RED))
        self.c_rp.disable_all()
        self._setstatus(f"● Comparativo — {atk_name} Nivel {level}",ORG)
        self._clr(self.v_console); self._clr(self.p_console)
        self.after(0,lambda:self.v_status.config(text="Preparando...",fg=ORG))
        self.after(0,lambda:self.p_status.config(text="En espera...",fg=MUTED))

        def thread():
            # Vulnerable
            self._log_sep(self.v_console)
            self._log(f"  {atk_name} — VULNERABLE  |  Nivel {level}","hdr",self.v_console)
            self._log(f"  VUs: {vus_list}  |  Runs: {runs}","info",self.v_console)
            self._log_sep(self.v_console)
            ok_v=self._ensure_env("Vulnerable",self.v_console)
            self.after(0,lambda:self.v_status.config(text="Ejecutando...",fg=ORG))
            if ok_v:
                ev={}
                def on_v(success,results):
                    ev["r"]=results; ev["ok"]=success
                self._exec_vus(ENVS["Vulnerable"]["path"],script,
                               vus_list,runs,self.v_console,on_v,level=level)
                self.c_results["Vulnerable"]=ev.get("r",{})
                self.after(0,lambda ok=ev.get("ok",False):self.v_status.config(
                    text="Completado" if ok else "Error",fg=GREEN if ok else RED))
            else:
                self.after(0,lambda:self.v_status.config(text="Error",fg=RED))

            # Protegido
            self._log_sep(self.p_console)
            self._log(f"  {atk_name} — PROTEGIDO  |  Nivel {level}","hdr",self.p_console)
            self._log(f"  VUs: {vus_list}  |  Runs: {runs}","info",self.p_console)
            self._log_sep(self.p_console)
            self.after(0,lambda:self.p_status.config(text="Ejecutando...",fg=ORG))
            ok_p=self._ensure_env("Protegido",self.p_console)
            if ok_p:
                ep={}
                def on_p(success,results):
                    ep["r"]=results; ep["ok"]=success
                self._exec_vus(ENVS["Protegido"]["path"],script,
                               vus_list,runs,self.p_console,on_p,level=level)
                self.c_results["Protegido"]=ep.get("r",{})
                self.after(0,lambda ok=ep.get("ok",False):self.p_status.config(
                    text="Completado" if ok else "Error",fg=GREEN if ok else RED))
                self._finish_comparative(ep.get("ok",False))
            else:
                self.after(0,lambda:self.p_status.config(text="Error",fg=RED))
                self._finish_comparative(False)

        threading.Thread(target=thread,daemon=True).start()

    def _finish_comparative(self,success):
        self.running=False; self.process=None
        self.after(0,lambda:self.c_btn_run.config(state=tk.NORMAL,bg=ACC))
        self.after(0,lambda:self.c_btn_stop.config(state=tk.DISABLED,bg="#2d2d2d"))
        has=any(self.c_results[e] for e in self.c_results)
        if has: self.after(0,self.c_rp.enable_all)
        self._setstatus("● Comparativo completado",GREEN if success else ORG)

    def _finish_both(self):
        self.running=False; self.process=None
        for btn in (self.s_btn_run,self.c_btn_run):
            self.after(0,lambda b=btn:b.config(state=tk.NORMAL,bg=ACC))
        for btn in (self.s_btn_stop,self.c_btn_stop):
            self.after(0,lambda b=btn:b.config(state=tk.DISABLED,bg="#2d2d2d"))
        self._setstatus("● Detenido",MUTED)

    # ─────────────────────────────────────────────────────────
    # GRAFICAS Y EXCEL
    # ─────────────────────────────────────────────────────────
    def _chart_simple(self):
        if not self.s_results: messagebox.showinfo("Sin datos","Ejecuta la prueba primero."); return
        ChartWindow(self, self.s_results, self.last_atk)

    def _chart_comparative(self):
        data={k:v for k,v in self.c_results.items() if v}
        if not data: messagebox.showinfo("Sin datos","Ejecuta el comparativo primero."); return
        ChartWindow(self, data, self.last_atk)

    def _excel_simple(self):
        if not self.s_results: messagebox.showinfo("Sin datos","Ejecuta primero."); return
        export_excel(self.s_results, self.last_atk, self.last_vus, script_path=self.last_script, level=self.last_level)

    def _excel_comparative(self):
        data={k:v for k,v in self.c_results.items() if v}
        if not data: messagebox.showinfo("Sin datos","Ejecuta el comparativo primero."); return
        export_excel(data, self.last_atk, self.last_vus, script_path=self.last_script, level=self.last_level)

    def _excel_single(self,env_name):
        d=self.c_results.get(env_name,{})
        if not d: messagebox.showinfo("Sin datos",f"No hay datos para {env_name}."); return
        export_excel({env_name:d}, self.last_atk, self.last_vus, script_path=self.last_script, level=self.last_level)

# ───────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if sys.platform=="win32":
        sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
        sys.stderr=io.TextIOWrapper(sys.stderr.buffer,encoding="utf-8",errors="replace")
    App().mainloop()
