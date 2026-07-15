#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  GENERADOR MAESTRO DE GRÁFICOS - TESIS                                     ║
║  Genera TODOS los gráficos comparativos (Vulnerable vs Protegido)          ║
║  para los 5 Casos de Uso (UC01-UC05)                                       ║
║  + Gráficos de Resumen Ejecutivo Transversal                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
import os, re, warnings, sys
# La consola de Windows (cp1252) no puede imprimir caracteres como ═ o á y hace
# crashear el script antes de generar nada. Forzamos UTF-8 en la salida.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

warnings.filterwarnings('ignore')

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════════════════════
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAFICOS_DIR = os.path.join(BASE_DIR, "graficos")
VUS_LIST = [10, 20, 50, 100, 250]
VUS_LABELS = ['10', '20', '50', '100', '250']
CONTAINERS = ['api-gateway', 'mongo-db', 'ms-catalogo', 'ms-ordenes', 'ms-resenas', 'ms-usuarios', 'postgres-db']

UC_CONFIG = {
    'UC01_introspeccion': {
        'titulo': 'UC-01: Exposición de Introspección',
        'subtitulo': 'Query __schema sin restricciones',
        'servicio_impactado': 'api-gateway',
        'carpeta': 'UC01_introspeccion'
    },
    'UC02_profundidad_moderada': {
        'titulo': 'UC-02: Ataque de Profundidad Moderada',
        'subtitulo': 'Query anidada de 8+ niveles',
        'servicio_impactado': 'ms-resenas',
        'carpeta': 'UC02_profundidad_moderada'
    },
    'UC03_recursividad_circular': {
        'titulo': 'UC-03: Ataque Recursivo Circular',
        'subtitulo': 'Ciclo reseña ↔ autor infinito',
        'servicio_impactado': 'ms-resenas',
        'carpeta': 'UC03_recursividad_circular'
    },
    'UC04_abuso_alias': {
        'titulo': 'UC-04: Abuso de Alias',
        'subtitulo': '50 aliases por petición',
        'servicio_impactado': 'ms-ordenes',
        'carpeta': 'UC04_abuso_alias'
    },
    'UC05_bomba_fragmentos': {
        'titulo': 'UC-05: Bomba de Fragmentos',
        'subtitulo': 'Expansión exponencial 5^4 = 625 resoluciones',
        'servicio_impactado': 'ms-usuarios',
        'carpeta': 'UC05_bomba_fragmentos'
    }
}

COLOR_VULN = '#E74C3C'; COLOR_PROT = '#2ECC71'
COLOR_VULN2 = '#C0392B'; COLOR_PROT2 = '#27AE60'
COLOR_VULN_LIGHT = '#FADBD8'; COLOR_PROT_LIGHT = '#D5F5E3'

# Paleta para contenedores
CONTAINER_COLORS = {
    'api-gateway': '#3498DB',
    'mongo-db': '#E67E22',
    'ms-catalogo': '#9B59B6',
    'ms-ordenes': '#1ABC9C',
    'ms-resenas': '#E74C3C',
    'ms-usuarios': '#2ECC71',
    'postgres-db': '#F39C12'
}

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 11, 'axes.titlesize': 13,
    'axes.labelsize': 12, 'legend.fontsize': 9, 'figure.facecolor': 'white',
    'axes.facecolor': '#fafafa', 'axes.grid': True, 'grid.alpha': 0.3,
    'grid.linestyle': '--', 'figure.dpi': 200
})

# ═══════════════════════════════════════════════════════════════════════════════
# EXTRACCIÓN DE DATOS
# ═══════════════════════════════════════════════════════════════════════════════
def parse_ram_value(text):
    """Convierte '1.032GiB (1056.77 MiB)' o '523.3MiB (523.30 MiB)' a float MiB"""
    m = re.search(r'\(([\d\.]+)\s*MiB\)', text)
    if m:
        return float(m.group(1))
    m = re.search(r'([\d\.]+)GiB', text)
    if m:
        return float(m.group(1)) * 1024
    m = re.search(r'([\d\.]+)MiB', text)
    if m:
        return float(m.group(1))
    return 0.0

def extract_all_metrics(env_dir, uc_name):
    """Extrae TODAS las métricas de un UC en un entorno dado."""
    data = {
        'peticiones': [], 'latencia': [], 'fallos': [],
        'cpu': {c: [] for c in CONTAINERS},
        'ram': {c: [] for c in CONTAINERS}
    }

    for vus in VUS_LIST:
        filepath = os.path.join(BASE_DIR, env_dir, "load_tests", uc_name, "resultados",
                                f"reporte_consolidado_3runs_vus{vus}.md")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"  [WARN] No encontrado: {filepath}")
            data['peticiones'].append(0); data['latencia'].append(0); data['fallos'].append(0)
            for c in CONTAINERS:
                data['cpu'][c].append(0); data['ram'][c].append(0)
            continue

        # K6 metrics
        m = re.search(r'\|\s*\*\*PROMEDIO\*\*\s*\|\s*\*\*([\d\.]+)\*\*\s*\|\s*\*\*([\d\.]+)\s*ms\*\*\s*\|\s*\*\*([\d\.]+)%\*\*\s*\|', content)
        if m:
            data['peticiones'].append(float(m.group(1)))
            data['latencia'].append(float(m.group(2)))
            data['fallos'].append(float(m.group(3)))
        else:
            data['peticiones'].append(0); data['latencia'].append(0); data['fallos'].append(0)

        # CPU por contenedor (Promedio Pico - última columna de la tabla CPU)
        for container in CONTAINERS:
            m = re.search(
                r'\|\s*\*\*' + re.escape(container) + r'\*\*\s*\|.*?\|\s*\*\*([\d\.]+)%\*\*\s*\|',
                content
            )
            data['cpu'][container].append(float(m.group(1)) if m else 0)

        # RAM por contenedor (último Run - última columna de la tabla RAM)
        lines = content.split('\n')
        in_ram_section = False
        for line in lines:
            if '## 3. PICOS DE MEMORIA' in line:
                in_ram_section = True
                continue
            if in_ram_section:
                for container in CONTAINERS:
                    if f'**{container}**' in line:
                        # Tomar el último valor (Run 3)
                        parts = line.split('|')
                        if len(parts) >= 4:
                            last_val = parts[-2].strip()  # penúltimo (antes del | final)
                            data['ram'][container].append(parse_ram_value(last_val))
                        else:
                            data['ram'][container].append(0)

    return data

# Extraer datos para todos los UCs
print("═" * 70)
print("  EXTRAYENDO DATOS DE TODOS LOS CASOS DE USO")
print("═" * 70)
all_data = {}
for uc_name in UC_CONFIG:
    print(f"\n📊 {uc_name}:")
    all_data[uc_name] = {
        'vuln': extract_all_metrics("E-commerce", uc_name),
        'prot': extract_all_metrics("E-commerce-controles", uc_name)
    }
    print(f"  ✓ Vulnerable: {len(all_data[uc_name]['vuln']['peticiones'])} niveles de VUs")
    print(f"  ✓ Protegido:  {len(all_data[uc_name]['prot']['peticiones'])} niveles de VUs")

# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES HELPER PARA GRÁFICOS
# ═══════════════════════════════════════════════════════════════════════════════
x = np.arange(len(VUS_LABELS))
width = 0.35
count = 0

def save_fig(fig, uc_folder, name):
    global count
    out_dir = os.path.join(GRAFICOS_DIR, uc_folder)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, name)
    fig.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    count += 1
    print(f"  [{count:02d}] {uc_folder}/{name}")

def add_bar_labels(ax, bars, color, offset=30, fmt='{:.0f}', fontsize=7):
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2., h + offset,
                    fmt.format(h), ha='center', va='bottom',
                    fontsize=fontsize, fontweight='bold', color=color)

# ═══════════════════════════════════════════════════════════════════════════════
# GENERACIÓN DE GRÁFICOS POR CASO DE USO
# ═══════════════════════════════════════════════════════════════════════════════
print("\n" + "═" * 70)
print("  GENERANDO GRÁFICOS POR CASO DE USO")
print("═" * 70)

for uc_name, config in UC_CONFIG.items():
    vuln = all_data[uc_name]['vuln']
    prot = all_data[uc_name]['prot']
    folder = config['carpeta']
    titulo = config['titulo']
    sub = config['subtitulo']
    svc = config['servicio_impactado']

    print(f"\n{'─' * 50}")
    print(f"  {titulo}")
    print(f"{'─' * 50}")

    # ──────────────────────────────────────────────────────────────────────
    # 1. THROUGHPUT (Peticiones Totales)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    b1 = ax.bar(x - width/2, vuln['peticiones'], width, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
    b2 = ax.bar(x + width/2, prot['peticiones'], width, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
    ax.set_xlabel('Usuarios Virtuales Concurrentes (VUs)')
    ax.set_ylabel('Peticiones Totales (Promedio 3 Runs)')
    ax.set_title(f'{titulo}\nThroughput: Peticiones Procesadas en 60s')
    ax.set_xticks(x); ax.set_xticklabels(VUS_LABELS); ax.legend(loc='best')
    add_bar_labels(ax, b1, COLOR_VULN2)
    add_bar_labels(ax, b2, COLOR_PROT2)
    save_fig(fig, folder, f'{folder.lower()}_01_throughput.png')

    # ──────────────────────────────────────────────────────────────────────
    # 2. LATENCIA MEDIA (líneas)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    lat_v = [l/1000 for l in vuln['latencia']]
    lat_p = [l/1000 for l in prot['latencia']]
    ax.plot(VUS_LIST, lat_v, 'o-', color=COLOR_VULN, linewidth=2.5, markersize=9, label='Vulnerable', zorder=3)
    ax.plot(VUS_LIST, lat_p, 's--', color=COLOR_PROT, linewidth=2.5, markersize=9, label='Protegido', zorder=3)
    ax.fill_between(VUS_LIST, lat_v, alpha=0.1, color=COLOR_VULN)
    ax.fill_between(VUS_LIST, lat_p, alpha=0.1, color=COLOR_PROT)
    ax.set_xlabel('VUs'); ax.set_ylabel('Latencia Media (segundos)')
    ax.set_title(f'{titulo}\nLatencia Media de Respuesta')
    ax.legend(); ax.set_xticks(VUS_LIST)
    for i in range(len(VUS_LIST)):
        ax.annotate(f'{lat_v[i]:.1f}s', (VUS_LIST[i], lat_v[i]), textcoords="offset points",
                    xytext=(0, 12), ha='center', fontsize=8, color=COLOR_VULN2, fontweight='bold')
        ax.annotate(f'{lat_p[i]:.1f}s', (VUS_LIST[i], lat_p[i]), textcoords="offset points",
                    xytext=(0, -15), ha='center', fontsize=8, color=COLOR_PROT2, fontweight='bold')
    save_fig(fig, folder, f'{folder.lower()}_02_latencia.png')

    # ──────────────────────────────────────────────────────────────────────
    # 3. TASA DE FALLOS (barras)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    b1 = ax.bar(x - width/2, vuln['fallos'], width, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
    b2 = ax.bar(x + width/2, prot['fallos'], width, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
    ax.set_xlabel('VUs'); ax.set_ylabel('Tasa de Fallos (%)')
    ax.set_title(f'{titulo}\nTasa de Fallos por Nivel de Carga')
    ax.set_xticks(x); ax.set_xticklabels(VUS_LABELS)
    ax.set_ylim(0, 110); ax.legend()
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 1, f'{h:.0f}%', ha='center', va='bottom', fontsize=8, fontweight='bold', color=COLOR_VULN2)
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 1, f'{h:.0f}%', ha='center', va='bottom', fontsize=8, fontweight='bold', color=COLOR_PROT2)
    save_fig(fig, folder, f'{folder.lower()}_03_tasa_fallos.png')

    # ──────────────────────────────────────────────────────────────────────
    # 4. CPU DEL SERVICIO IMPACTADO (líneas con área sombreada)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    cpu_v = vuln['cpu'][svc]
    cpu_p = prot['cpu'][svc]
    ax.plot(VUS_LIST, cpu_v, 'o-', color=COLOR_VULN, linewidth=2.5, markersize=9, label='Vulnerable', zorder=3)
    ax.plot(VUS_LIST, cpu_p, 's--', color=COLOR_PROT, linewidth=2.5, markersize=9, label='Protegido', zorder=3)
    ax.fill_between(VUS_LIST, cpu_v, alpha=0.15, color=COLOR_VULN)
    ax.fill_between(VUS_LIST, cpu_p, alpha=0.15, color=COLOR_PROT)
    ax.axhline(y=100, color='gray', linestyle=':', alpha=0.7, label='Límite 1 CPU core')
    ax.set_xlabel('VUs'); ax.set_ylabel('Pico de CPU (%)')
    ax.set_title(f'{titulo}\nPico de CPU en {svc}')
    ax.legend(); ax.set_xticks(VUS_LIST)
    for i in range(len(VUS_LIST)):
        ax.annotate(f'{cpu_v[i]:.0f}%', (VUS_LIST[i], cpu_v[i]), textcoords="offset points",
                    xytext=(0, 10), ha='center', fontsize=8, color=COLOR_VULN2, fontweight='bold')
        ax.annotate(f'{cpu_p[i]:.0f}%', (VUS_LIST[i], cpu_p[i]), textcoords="offset points",
                    xytext=(0, -14), ha='center', fontsize=8, color=COLOR_PROT2, fontweight='bold')
    save_fig(fig, folder, f'{folder.lower()}_04_cpu_{svc.replace("-","_")}.png')

    # ──────────────────────────────────────────────────────────────────────
    # 5. RAM DEL SERVICIO IMPACTADO (barras)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    ram_v = vuln['ram'][svc]
    ram_p = prot['ram'][svc]
    b1 = ax.bar(x - width/2, ram_v, width, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
    b2 = ax.bar(x + width/2, ram_p, width, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
    ax.set_xlabel('VUs'); ax.set_ylabel('Pico de RAM (MiB)')
    ax.set_title(f'{titulo}\nConsumo de RAM en {svc}')
    ax.set_xticks(x); ax.set_xticklabels(VUS_LABELS); ax.legend(loc='upper left')
    add_bar_labels(ax, b1, COLOR_VULN2, offset=5)
    add_bar_labels(ax, b2, COLOR_PROT2, offset=5)
    save_fig(fig, folder, f'{folder.lower()}_05_ram_{svc.replace("-","_")}.png')

    # ──────────────────────────────────────────────────────────────────────
    # 6. CPU DEL API-GATEWAY (líneas)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    cpu_gw_v = vuln['cpu']['api-gateway']
    cpu_gw_p = prot['cpu']['api-gateway']
    ax.plot(VUS_LIST, cpu_gw_v, 'o-', color=COLOR_VULN, linewidth=2.5, markersize=9, label='Vulnerable', zorder=3)
    ax.plot(VUS_LIST, cpu_gw_p, 's--', color=COLOR_PROT, linewidth=2.5, markersize=9, label='Protegido', zorder=3)
    ax.fill_between(VUS_LIST, cpu_gw_v, alpha=0.15, color=COLOR_VULN)
    ax.fill_between(VUS_LIST, cpu_gw_p, alpha=0.15, color=COLOR_PROT)
    ax.axhline(y=100, color='gray', linestyle=':', alpha=0.7)
    ax.set_xlabel('VUs'); ax.set_ylabel('Pico de CPU (%)')
    ax.set_title(f'{titulo}\nPico de CPU en api-gateway')
    ax.legend(); ax.set_xticks(VUS_LIST)
    save_fig(fig, folder, f'{folder.lower()}_06_cpu_api_gateway.png')

    # ──────────────────────────────────────────────────────────────────────
    # 7. RAM DEL API-GATEWAY (barras)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    ram_gw_v = vuln['ram']['api-gateway']
    ram_gw_p = prot['ram']['api-gateway']
    b1 = ax.bar(x - width/2, ram_gw_v, width, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
    b2 = ax.bar(x + width/2, ram_gw_p, width, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
    ax.set_xlabel('VUs'); ax.set_ylabel('Pico de RAM (MiB)')
    ax.set_title(f'{titulo}\nConsumo de RAM en api-gateway')
    ax.set_xticks(x); ax.set_xticklabels(VUS_LABELS); ax.legend(loc='upper left')
    add_bar_labels(ax, b1, COLOR_VULN2, offset=2)
    add_bar_labels(ax, b2, COLOR_PROT2, offset=2)
    save_fig(fig, folder, f'{folder.lower()}_07_ram_api_gateway.png')

    # ──────────────────────────────────────────────────────────────────────
    # 8. CPU TODOS LOS CONTENEDORES - VULNERABLE (barras agrupadas)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 7))
    n_cont = len(CONTAINERS)
    bar_w = 0.12
    for i, c in enumerate(CONTAINERS):
        offset = (i - n_cont/2) * bar_w + bar_w/2
        vals = vuln['cpu'][c]
        bars = ax.bar(x + offset, vals, bar_w, label=c, color=CONTAINER_COLORS[c], edgecolor='white', zorder=3)
    ax.set_xlabel('VUs'); ax.set_ylabel('Pico de CPU (%)')
    ax.set_title(f'{titulo}\nPicos de CPU por Contenedor - Entorno VULNERABLE')
    ax.set_xticks(x); ax.set_xticklabels(VUS_LABELS)
    ax.axhline(y=100, color='gray', linestyle=':', alpha=0.7)
    ax.legend(loc='upper left', ncol=2, fontsize=8)
    save_fig(fig, folder, f'{folder.lower()}_08_cpu_todos_vulnerable.png')

    # ──────────────────────────────────────────────────────────────────────
    # 9. CPU TODOS LOS CONTENEDORES - PROTEGIDO (barras agrupadas)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 7))
    for i, c in enumerate(CONTAINERS):
        offset = (i - n_cont/2) * bar_w + bar_w/2
        vals = prot['cpu'][c]
        bars = ax.bar(x + offset, vals, bar_w, label=c, color=CONTAINER_COLORS[c], edgecolor='white', zorder=3)
    ax.set_xlabel('VUs'); ax.set_ylabel('Pico de CPU (%)')
    ax.set_title(f'{titulo}\nPicos de CPU por Contenedor - Entorno PROTEGIDO')
    ax.set_xticks(x); ax.set_xticklabels(VUS_LABELS)
    ax.axhline(y=100, color='gray', linestyle=':', alpha=0.7)
    ax.legend(loc='upper left', ncol=2, fontsize=8)
    save_fig(fig, folder, f'{folder.lower()}_09_cpu_todos_protegido.png')

    # ──────────────────────────────────────────────────────────────────────
    # 10. RAM TODOS LOS CONTENEDORES - VULNERABLE (barras agrupadas)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 7))
    for i, c in enumerate(CONTAINERS):
        offset = (i - n_cont/2) * bar_w + bar_w/2
        vals = vuln['ram'][c]
        bars = ax.bar(x + offset, vals, bar_w, label=c, color=CONTAINER_COLORS[c], edgecolor='white', zorder=3)
    ax.set_xlabel('VUs'); ax.set_ylabel('Pico de RAM (MiB)')
    ax.set_title(f'{titulo}\nPicos de RAM por Contenedor - Entorno VULNERABLE')
    ax.set_xticks(x); ax.set_xticklabels(VUS_LABELS)
    ax.legend(loc='upper left', ncol=2, fontsize=8)
    save_fig(fig, folder, f'{folder.lower()}_10_ram_todos_vulnerable.png')

    # ──────────────────────────────────────────────────────────────────────
    # 11. RAM TODOS LOS CONTENEDORES - PROTEGIDO (barras agrupadas)
    # ──────────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 7))
    for i, c in enumerate(CONTAINERS):
        offset = (i - n_cont/2) * bar_w + bar_w/2
        vals = prot['ram'][c]
        bars = ax.bar(x + offset, vals, bar_w, label=c, color=CONTAINER_COLORS[c], edgecolor='white', zorder=3)
    ax.set_xlabel('VUs'); ax.set_ylabel('Pico de RAM (MiB)')
    ax.set_title(f'{titulo}\nPicos de RAM por Contenedor - Entorno PROTEGIDO')
    ax.set_xticks(x); ax.set_xticklabels(VUS_LABELS)
    ax.legend(loc='upper left', ncol=2, fontsize=8)
    save_fig(fig, folder, f'{folder.lower()}_11_ram_todos_protegido.png')

    # ──────────────────────────────────────────────────────────────────────
    # 12. DUAL CPU: Servicio impactado + api-gateway lado a lado
    # ──────────────────────────────────────────────────────────────────────
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    ax1.plot(VUS_LIST, vuln['cpu'][svc], 'o-', color=COLOR_VULN, lw=2.5, ms=9, label='Vulnerable', zorder=3)
    ax1.plot(VUS_LIST, prot['cpu'][svc], 's--', color=COLOR_PROT, lw=2.5, ms=9, label='Protegido', zorder=3)
    ax1.set_xlabel('VUs'); ax1.set_ylabel('CPU (%)'); ax1.set_title(f'CPU: {svc}', fontweight='bold')
    ax1.legend(); ax1.set_xticks(VUS_LIST); ax1.axhline(y=100, color='gray', ls=':', alpha=0.5)

    ax2.plot(VUS_LIST, vuln['cpu']['api-gateway'], 'o-', color=COLOR_VULN, lw=2.5, ms=9, label='Vulnerable', zorder=3)
    ax2.plot(VUS_LIST, prot['cpu']['api-gateway'], 's--', color=COLOR_PROT, lw=2.5, ms=9, label='Protegido', zorder=3)
    ax2.set_xlabel('VUs'); ax2.set_ylabel('CPU (%)'); ax2.set_title('CPU: api-gateway', fontweight='bold')
    ax2.legend(); ax2.set_xticks(VUS_LIST); ax2.axhline(y=100, color='gray', ls=':', alpha=0.5)
    fig.suptitle(f'{titulo} — Comparativa de CPU', fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout()
    save_fig(fig, folder, f'{folder.lower()}_12_cpu_dual.png')

    # ──────────────────────────────────────────────────────────────────────
    # 13. DUAL RAM: Servicio impactado + api-gateway lado a lado
    # ──────────────────────────────────────────────────────────────────────
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    b1 = ax1.bar(x - width/2, vuln['ram'][svc], width, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
    b2 = ax1.bar(x + width/2, prot['ram'][svc], width, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
    ax1.set_xlabel('VUs'); ax1.set_ylabel('RAM (MiB)'); ax1.set_title(f'RAM: {svc}', fontweight='bold')
    ax1.set_xticks(x); ax1.set_xticklabels(VUS_LABELS); ax1.legend()

    b3 = ax2.bar(x - width/2, vuln['ram']['api-gateway'], width, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
    b4 = ax2.bar(x + width/2, prot['ram']['api-gateway'], width, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
    ax2.set_xlabel('VUs'); ax2.set_ylabel('RAM (MiB)'); ax2.set_title('RAM: api-gateway', fontweight='bold')
    ax2.set_xticks(x); ax2.set_xticklabels(VUS_LABELS); ax2.legend()
    fig.suptitle(f'{titulo} — Comparativa de RAM', fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout()
    save_fig(fig, folder, f'{folder.lower()}_13_ram_dual.png')

    # ──────────────────────────────────────────────────────────────────────
    # 14. HEATMAP CPU VULNERABLE vs PROTEGIDO (250 VUs)
    # ──────────────────────────────────────────────────────────────────────
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    cpu_matrix_v = np.array([vuln['cpu'][c] for c in CONTAINERS])
    cpu_matrix_p = np.array([prot['cpu'][c] for c in CONTAINERS])
    vmax = max(cpu_matrix_v.max(), cpu_matrix_p.max())

    im1 = ax1.imshow(cpu_matrix_v, cmap='YlOrRd', aspect='auto', vmin=0, vmax=vmax)
    ax1.set_xticks(range(len(VUS_LABELS))); ax1.set_xticklabels(VUS_LABELS)
    ax1.set_yticks(range(len(CONTAINERS))); ax1.set_yticklabels(CONTAINERS, fontsize=9)
    ax1.set_xlabel('VUs'); ax1.set_title('CPU (%) — Vulnerable', fontweight='bold')
    for i in range(len(CONTAINERS)):
        for j in range(len(VUS_LABELS)):
            v = cpu_matrix_v[i, j]
            color = 'white' if v > vmax*0.6 else 'black'
            ax1.text(j, i, f'{v:.0f}', ha='center', va='center', fontsize=7, color=color, fontweight='bold')

    im2 = ax2.imshow(cpu_matrix_p, cmap='YlGn', aspect='auto', vmin=0, vmax=vmax)
    ax2.set_xticks(range(len(VUS_LABELS))); ax2.set_xticklabels(VUS_LABELS)
    ax2.set_yticks(range(len(CONTAINERS))); ax2.set_yticklabels(CONTAINERS, fontsize=9)
    ax2.set_xlabel('VUs'); ax2.set_title('CPU (%) — Protegido', fontweight='bold')
    for i in range(len(CONTAINERS)):
        for j in range(len(VUS_LABELS)):
            v = cpu_matrix_p[i, j]
            color = 'white' if v > vmax*0.6 else 'black'
            ax2.text(j, i, f'{v:.0f}', ha='center', va='center', fontsize=7, color=color, fontweight='bold')

    fig.suptitle(f'{titulo} — Mapa de Calor de CPU', fontsize=13, fontweight='bold')
    fig.tight_layout()
    save_fig(fig, folder, f'{folder.lower()}_14_heatmap_cpu.png')

    # ──────────────────────────────────────────────────────────────────────
    # 15. HEATMAP RAM VULNERABLE vs PROTEGIDO
    # ──────────────────────────────────────────────────────────────────────
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    ram_matrix_v = np.array([vuln['ram'][c] for c in CONTAINERS])
    ram_matrix_p = np.array([prot['ram'][c] for c in CONTAINERS])
    vmax_ram = max(ram_matrix_v.max(), ram_matrix_p.max())

    im1 = ax1.imshow(ram_matrix_v, cmap='YlOrRd', aspect='auto', vmin=0, vmax=vmax_ram)
    ax1.set_xticks(range(len(VUS_LABELS))); ax1.set_xticklabels(VUS_LABELS)
    ax1.set_yticks(range(len(CONTAINERS))); ax1.set_yticklabels(CONTAINERS, fontsize=9)
    ax1.set_xlabel('VUs'); ax1.set_title('RAM (MiB) — Vulnerable', fontweight='bold')
    for i in range(len(CONTAINERS)):
        for j in range(len(VUS_LABELS)):
            v = ram_matrix_v[i, j]
            color = 'white' if v > vmax_ram*0.6 else 'black'
            ax1.text(j, i, f'{v:.0f}', ha='center', va='center', fontsize=7, color=color, fontweight='bold')

    im2 = ax2.imshow(ram_matrix_p, cmap='YlGn', aspect='auto', vmin=0, vmax=vmax_ram)
    ax2.set_xticks(range(len(VUS_LABELS))); ax2.set_xticklabels(VUS_LABELS)
    ax2.set_yticks(range(len(CONTAINERS))); ax2.set_yticklabels(CONTAINERS, fontsize=9)
    ax2.set_xlabel('VUs'); ax2.set_title('RAM (MiB) — Protegido', fontweight='bold')
    for i in range(len(CONTAINERS)):
        for j in range(len(VUS_LABELS)):
            v = ram_matrix_p[i, j]
            color = 'white' if v > vmax_ram*0.6 else 'black'
            ax2.text(j, i, f'{v:.0f}', ha='center', va='center', fontsize=7, color=color, fontweight='bold')

    fig.suptitle(f'{titulo} — Mapa de Calor de RAM', fontsize=13, fontweight='bold')
    fig.tight_layout()
    save_fig(fig, folder, f'{folder.lower()}_15_heatmap_ram.png')

# ═══════════════════════════════════════════════════════════════════════════════
# GRÁFICOS TRANSVERSALES (RESUMEN EJECUTIVO)
# ═══════════════════════════════════════════════════════════════════════════════
print(f"\n{'═' * 70}")
print("  GENERANDO GRÁFICOS TRANSVERSALES (RESUMEN EJECUTIVO)")
print(f"{'═' * 70}")

resumen_dir = "Resumen_Ejecutivo"
uc_short = ['UC-01', 'UC-02', 'UC-03', 'UC-04', 'UC-05']
uc_keys = list(UC_CONFIG.keys())

# ──────────────────────────────────────────────────────────────────────
# T1. LATENCIA COMPARATIVA A 250 VUs (barras horizontales)
# ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6))
lat_v_250 = [all_data[k]['vuln']['latencia'][4]/1000 for k in uc_keys]
lat_p_250 = [all_data[k]['prot']['latencia'][4]/1000 for k in uc_keys]
y_pos = np.arange(len(uc_short))
bars1 = ax.barh(y_pos + 0.2, lat_v_250, 0.35, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
bars2 = ax.barh(y_pos - 0.2, lat_p_250, 0.35, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
ax.set_yticks(y_pos); ax.set_yticklabels(uc_short)
ax.set_xlabel('Latencia Media (segundos)'); ax.set_title('Latencia Media a 250 VUs — Todos los Casos de Uso', fontweight='bold')
ax.legend()
for i, bar in enumerate(bars1):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, f'{lat_v_250[i]:.1f}s',
            va='center', fontsize=9, fontweight='bold', color=COLOR_VULN2)
for i, bar in enumerate(bars2):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, f'{lat_p_250[i]:.1f}s',
            va='center', fontsize=9, fontweight='bold', color=COLOR_PROT2)
save_fig(fig, resumen_dir, 'resumen_01_latencia_250vus.png')

# ──────────────────────────────────────────────────────────────────────
# T2. THROUGHPUT COMPARATIVO A 250 VUs
# ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6))
thr_v_250 = [all_data[k]['vuln']['peticiones'][4] for k in uc_keys]
thr_p_250 = [all_data[k]['prot']['peticiones'][4] for k in uc_keys]
b1 = ax.bar(y_pos - 0.2, thr_v_250, 0.35, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
b2 = ax.bar(y_pos + 0.2, thr_p_250, 0.35, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
ax.set_xticks(y_pos); ax.set_xticklabels(uc_short)
ax.set_ylabel('Peticiones Totales (60s)'); ax.set_title('Throughput a 250 VUs — Todos los Casos de Uso', fontweight='bold')
ax.legend()
add_bar_labels(ax, b1, COLOR_VULN2, offset=50)
add_bar_labels(ax, b2, COLOR_PROT2, offset=50)
save_fig(fig, resumen_dir, 'resumen_02_throughput_250vus.png')

# ──────────────────────────────────────────────────────────────────────
# T3. CPU PICO DEL SERVICIO IMPACTADO A 250 VUs
# ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6))
svcs = [UC_CONFIG[k]['servicio_impactado'] for k in uc_keys]
cpu_v_250 = [all_data[k]['vuln']['cpu'][UC_CONFIG[k]['servicio_impactado']][4] for k in uc_keys]
cpu_p_250 = [all_data[k]['prot']['cpu'][UC_CONFIG[k]['servicio_impactado']][4] for k in uc_keys]
b1 = ax.bar(y_pos - 0.2, cpu_v_250, 0.35, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
b2 = ax.bar(y_pos + 0.2, cpu_p_250, 0.35, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
ax.set_xticks(y_pos)
ax.set_xticklabels([f'{uc_short[i]}\n({svcs[i]})' for i in range(len(uc_short))], fontsize=9)
ax.set_ylabel('Pico de CPU (%)'); ax.set_title('CPU Pico del Servicio Impactado a 250 VUs', fontweight='bold')
ax.axhline(y=100, color='gray', linestyle=':', alpha=0.7)
ax.legend()
add_bar_labels(ax, b1, COLOR_VULN2, offset=10, fmt='{:.0f}%')
add_bar_labels(ax, b2, COLOR_PROT2, offset=10, fmt='{:.0f}%')
save_fig(fig, resumen_dir, 'resumen_03_cpu_impactado_250vus.png')

# ──────────────────────────────────────────────────────────────────────
# T4. RAM PICO DEL SERVICIO IMPACTADO A 250 VUs
# ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6))
ram_v_250 = [all_data[k]['vuln']['ram'][UC_CONFIG[k]['servicio_impactado']][4] for k in uc_keys]
ram_p_250 = [all_data[k]['prot']['ram'][UC_CONFIG[k]['servicio_impactado']][4] for k in uc_keys]
b1 = ax.bar(y_pos - 0.2, ram_v_250, 0.35, label='Vulnerable', color=COLOR_VULN, edgecolor='white', zorder=3)
b2 = ax.bar(y_pos + 0.2, ram_p_250, 0.35, label='Protegido', color=COLOR_PROT, edgecolor='white', zorder=3)
ax.set_xticks(y_pos)
ax.set_xticklabels([f'{uc_short[i]}\n({svcs[i]})' for i in range(len(uc_short))], fontsize=9)
ax.set_ylabel('Pico de RAM (MiB)'); ax.set_title('RAM Pico del Servicio Impactado a 250 VUs', fontweight='bold')
ax.legend()
add_bar_labels(ax, b1, COLOR_VULN2, offset=5)
add_bar_labels(ax, b2, COLOR_PROT2, offset=5)
save_fig(fig, resumen_dir, 'resumen_04_ram_impactado_250vus.png')

# ──────────────────────────────────────────────────────────────────────
# T5. EVOLUCIÓN DE LATENCIA POR UC (un subplot por UC)
# ──────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 5, figsize=(22, 5), sharey=False)
for i, (k, ax) in enumerate(zip(uc_keys, axes)):
    lat_v = [l/1000 for l in all_data[k]['vuln']['latencia']]
    lat_p = [l/1000 for l in all_data[k]['prot']['latencia']]
    ax.plot(VUS_LIST, lat_v, 'o-', color=COLOR_VULN, lw=2, ms=6, label='Vulnerable')
    ax.plot(VUS_LIST, lat_p, 's--', color=COLOR_PROT, lw=2, ms=6, label='Protegido')
    ax.fill_between(VUS_LIST, lat_v, alpha=0.1, color=COLOR_VULN)
    ax.set_title(uc_short[i], fontweight='bold', fontsize=11)
    ax.set_xlabel('VUs'); ax.set_xticks(VUS_LIST)
    ax.tick_params(axis='x', labelsize=7)
    if i == 0: ax.set_ylabel('Latencia (s)')
    if i == 4: ax.legend(fontsize=7)
fig.suptitle('Evolución de Latencia por Caso de Uso', fontsize=14, fontweight='bold', y=1.03)
fig.tight_layout()
save_fig(fig, resumen_dir, 'resumen_05_latencia_evolucion.png')

# ──────────────────────────────────────────────────────────────────────
# T6. EVOLUCIÓN DE THROUGHPUT POR UC (un subplot por UC)
# ──────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 5, figsize=(22, 5), sharey=False)
for i, (k, ax) in enumerate(zip(uc_keys, axes)):
    ax.plot(VUS_LIST, all_data[k]['vuln']['peticiones'], 'o-', color=COLOR_VULN, lw=2, ms=6, label='Vulnerable')
    ax.plot(VUS_LIST, all_data[k]['prot']['peticiones'], 's--', color=COLOR_PROT, lw=2, ms=6, label='Protegido')
    ax.fill_between(VUS_LIST, all_data[k]['vuln']['peticiones'], alpha=0.1, color=COLOR_VULN)
    ax.fill_between(VUS_LIST, all_data[k]['prot']['peticiones'], alpha=0.1, color=COLOR_PROT)
    ax.set_title(uc_short[i], fontweight='bold', fontsize=11)
    ax.set_xlabel('VUs'); ax.set_xticks(VUS_LIST)
    ax.tick_params(axis='x', labelsize=7)
    if i == 0: ax.set_ylabel('Peticiones')
    if i == 4: ax.legend(fontsize=7)
fig.suptitle('Evolución de Throughput por Caso de Uso', fontsize=14, fontweight='bold', y=1.03)
fig.tight_layout()
save_fig(fig, resumen_dir, 'resumen_06_throughput_evolucion.png')

# ──────────────────────────────────────────────────────────────────────
# T7. REDUCCIÓN PORCENTUAL DE LATENCIA (protegido vs vulnerable)
# ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
reduccion = []
for k in uc_keys:
    lv = all_data[k]['vuln']['latencia'][4]
    lp = all_data[k]['prot']['latencia'][4]
    if lv > 0:
        reduccion.append(((lv - lp) / lv) * 100)
    else:
        reduccion.append(0)
colors_bar = ['#3498DB', '#9B59B6', '#E67E22', '#1ABC9C', '#E74C3C']
bars = ax.bar(uc_short, reduccion, color=colors_bar, edgecolor='white', zorder=3)
ax.set_ylabel('Reducción de Latencia (%)')
ax.set_title('Mejora en Latencia del Entorno Protegido vs Vulnerable\n(a 250 VUs)', fontweight='bold')
ax.set_ylim(0, 110)
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 1, f'{h:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
save_fig(fig, resumen_dir, 'resumen_07_reduccion_latencia.png')

# ──────────────────────────────────────────────────────────────────────
# T8. FACTOR DE MEJORA EN THROUGHPUT
# ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
factor = []
for k in uc_keys:
    tv = all_data[k]['vuln']['peticiones'][4]
    tp = all_data[k]['prot']['peticiones'][4]
    if tv > 0:
        factor.append(tp / tv)
    else:
        factor.append(0)
bars = ax.bar(uc_short, factor, color=colors_bar, edgecolor='white', zorder=3)
ax.set_ylabel('Factor de Mejora (x)')
ax.set_title('Factor de Mejora en Throughput\n(Protegido / Vulnerable a 250 VUs)', fontweight='bold')
ax.axhline(y=1, color='gray', linestyle=':', alpha=0.7, label='Sin cambio (1x)')
ax.legend()
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 0.1, f'{h:.1f}x', ha='center', va='bottom', fontsize=11, fontweight='bold')
save_fig(fig, resumen_dir, 'resumen_08_factor_throughput.png')

# ──────────────────────────────────────────────────────────────────────
# T9. REDUCCIÓN DE CPU DEL SERVICIO IMPACTADO
# ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
reduccion_cpu = []
for k in uc_keys:
    svc = UC_CONFIG[k]['servicio_impactado']
    cv = all_data[k]['vuln']['cpu'][svc][4]
    cp = all_data[k]['prot']['cpu'][svc][4]
    if cv > 0:
        reduccion_cpu.append(((cv - cp) / cv) * 100)
    else:
        reduccion_cpu.append(0)
bars = ax.bar(uc_short, reduccion_cpu, color=colors_bar, edgecolor='white', zorder=3)
ax.set_ylabel('Reducción de CPU (%)')
ax.set_title('Reducción de CPU del Servicio Impactado\n(Protegido vs Vulnerable a 250 VUs)', fontweight='bold')
ax.set_ylim(0, 110)
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 1, f'{h:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
save_fig(fig, resumen_dir, 'resumen_09_reduccion_cpu.png')

# ──────────────────────────────────────────────────────────────────────
# T10. REDUCCIÓN DE RAM DEL SERVICIO IMPACTADO
# ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
reduccion_ram = []
for k in uc_keys:
    svc = UC_CONFIG[k]['servicio_impactado']
    rv = all_data[k]['vuln']['ram'][svc][4]
    rp = all_data[k]['prot']['ram'][svc][4]
    if rv > 0:
        reduccion_ram.append(((rv - rp) / rv) * 100)
    else:
        reduccion_ram.append(0)
bars = ax.bar(uc_short, reduccion_ram, color=colors_bar, edgecolor='white', zorder=3)
ax.set_ylabel('Reducción de RAM (%)')
ax.set_title('Reducción de RAM del Servicio Impactado\n(Protegido vs Vulnerable a 250 VUs)', fontweight='bold')
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 1, f'{h:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
save_fig(fig, resumen_dir, 'resumen_10_reduccion_ram.png')

# ──────────────────────────────────────────────────────────────────────
# T11. TABLA RESUMEN VISUAL (RADAR CHART)
# ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
categories = ['Latencia\n(reducción %)', 'Throughput\n(factor x)', 'CPU\n(reducción %)', 'RAM\n(reducción %)']
N = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# Normalizar: latencia reducción, throughput factor (escalar a 0-100), cpu reducción, ram reducción
for i, k in enumerate(uc_keys):
    values = [reduccion[i], min(factor[i]*10, 100), reduccion_cpu[i], reduccion_ram[i]]
    values += values[:1]
    ax.plot(angles, values, 'o-', linewidth=2, label=uc_short[i], color=colors_bar[i])
    ax.fill(angles, values, alpha=0.1, color=colors_bar[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=9)
ax.set_title('Radar de Efectividad de Controles\n(a 250 VUs)', fontsize=13, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9)
save_fig(fig, resumen_dir, 'resumen_11_radar_efectividad.png')

# ──────────────────────────────────────────────────────────────────────
# T12. HEATMAP CONSOLIDADO - LATENCIA POR UC Y VUs
# ──────────────────────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

lat_matrix_v = np.array([[(all_data[k]['vuln']['latencia'][j])/1000 for j in range(5)] for k in uc_keys])
lat_matrix_p = np.array([[(all_data[k]['prot']['latencia'][j])/1000 for j in range(5)] for k in uc_keys])
vmax_lat = max(lat_matrix_v.max(), lat_matrix_p.max())

im1 = ax1.imshow(lat_matrix_v, cmap='YlOrRd', aspect='auto', vmin=0, vmax=vmax_lat)
ax1.set_xticks(range(5)); ax1.set_xticklabels(VUS_LABELS)
ax1.set_yticks(range(5)); ax1.set_yticklabels(uc_short)
ax1.set_xlabel('VUs'); ax1.set_title('Latencia (s) — Vulnerable', fontweight='bold')
for i in range(5):
    for j in range(5):
        v = lat_matrix_v[i, j]
        color = 'white' if v > vmax_lat*0.5 else 'black'
        ax1.text(j, i, f'{v:.1f}', ha='center', va='center', fontsize=8, color=color, fontweight='bold')

im2 = ax2.imshow(lat_matrix_p, cmap='YlGn', aspect='auto', vmin=0, vmax=vmax_lat)
ax2.set_xticks(range(5)); ax2.set_xticklabels(VUS_LABELS)
ax2.set_yticks(range(5)); ax2.set_yticklabels(uc_short)
ax2.set_xlabel('VUs'); ax2.set_title('Latencia (s) — Protegido', fontweight='bold')
for i in range(5):
    for j in range(5):
        v = lat_matrix_p[i, j]
        color = 'white' if v > vmax_lat*0.5 else 'black'
        ax2.text(j, i, f'{v:.1f}', ha='center', va='center', fontsize=8, color=color, fontweight='bold')

fig.suptitle('Mapa de Calor de Latencia — Todos los Casos de Uso', fontsize=13, fontweight='bold')
fig.tight_layout()
save_fig(fig, resumen_dir, 'resumen_12_heatmap_latencia.png')

# ═══════════════════════════════════════════════════════════════════════════════
# RESUMEN FINAL
# ═══════════════════════════════════════════════════════════════════════════════
print(f"\n{'═' * 70}")
print(f"  ✅ TOTAL DE GRÁFICOS GENERADOS: {count}")
print(f"  📁 Directorio: {GRAFICOS_DIR}")
print(f"{'═' * 70}")

# Listar estructura final
for folder in sorted(os.listdir(GRAFICOS_DIR)):
    folder_path = os.path.join(GRAFICOS_DIR, folder)
    if os.path.isdir(folder_path):
        files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])
        print(f"\n  📂 {folder}/ ({len(files)} gráficos)")
        for f in files:
            print(f"     └─ {f}")
