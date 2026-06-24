"""
Orquestador de Pruebas de Carga - Metodología Wohlin et al.
===========================================================
Ejecuta un script K6 N veces consecutivas, captura picos de Docker
y genera un reporte consolidado en Markdown.

Uso:
    python run_multiple_experiments.py --test-script UC01_introspeccion/uc01_stress_introspeccion.js --vus 10 --runs 3
"""

import subprocess
import time
import sys
import os
import re
import argparse
from typing import Any


def parse_memory(mem_str: str) -> float:
    """Convierte cadenas de memoria como '459.6MiB / 1.5GiB' a un valor en MiB."""
    try:
        parts = mem_str.split('/')
        usage_part = parts[0].strip()
        match = re.match(r"([0-9.]+)\s*([a-zA-Z]*)", usage_part)
        if not match:
            return 0.0
        val = float(match.group(1))
        unit = match.group(2).lower()
        if 'g' in unit:
            return val * 1024.0
        elif 'k' in unit:
            return val / 1024.0
        elif 'b' in unit and 'm' not in unit:
            return val / (1024.0 * 1024.0)
        return val
    except (ValueError, IndexError):
        return 0.0


def parse_cpu(cpu_str: str) -> float:
    """Convierte cadenas de CPU como '12.5%' a float."""
    try:
        val_str = cpu_str.replace('%', '').strip()
        return float(val_str)
    except (ValueError, AttributeError):
        return 0.0


def run_single_experiment(
    run_number: int,
    test_script: str,
    vus: int,
    base_dir: str
) -> dict[str, Any]:
    """Ejecuta una sola iteración del experimento (monitor Docker + K6)."""
    print(f"\n{'=' * 50}")
    print(f"  EJECUCIÓN {run_number} | VUS={vus} | Script: {os.path.basename(test_script)}")
    print(f"{'=' * 50}")

    log_file_path = os.path.join(base_dir, f"temp_run_{run_number}.log")
    stop_file_path = os.path.join(base_dir, "stop_monitor.tmp")

    if os.path.exists(stop_file_path):
        try:
            os.remove(stop_file_path)
        except OSError:
            pass

    # 1. Iniciar monitor de Docker (redirigir stdout a archivo para evitar deadlock)
    monitor_script = os.path.join(base_dir, "monitor_docker_stats.py")
    # Calcular carpeta de resultados para que el monitor guarde ahí sus reportes
    test_results_dir = os.path.join(
        os.path.dirname(os.path.join(base_dir, test_script)), "resultados"
    )
    os.makedirs(test_results_dir, exist_ok=True)
    monitor_cmd = [sys.executable, monitor_script, "--output-dir", test_results_dir]

    log_file = open(log_file_path, "w", encoding="utf-8")  # noqa: SIM115
    try:
        monitor_proc = subprocess.Popen(
            monitor_cmd,
            cwd=base_dir,
            stdout=log_file,
            stderr=log_file,
            text=True,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
        )

        # Esperar inicialización del monitor
        time.sleep(2)

        # 2. Ejecutar K6
        k6_cmd = ["k6", "run", "-e", f"VUS={vus}", test_script]
        k6_result = subprocess.run(
            k6_cmd,
            cwd=base_dir,
            capture_output=True,
            text=True,
            check=False
        )

        # 3. Detener monitor mediante archivo señal
        with open(stop_file_path, "w", encoding="utf-8") as stop_f:
            stop_f.write("stop")

        monitor_proc.wait(timeout=15)
    finally:
        log_file.close()

    # Leer salida del monitor
    with open(log_file_path, "r", encoding="utf-8") as result_f:
        stdout_mon = result_f.read()

    # Limpiar archivo temporal
    try:
        os.remove(log_file_path)
    except OSError:
        pass

    # Parsear picos de CPU y Memoria del monitor
    cpu_peaks: dict[str, float] = {}
    mem_peaks: dict[str, str] = {}

    pattern = r"\|\s*\*\*([a-zA-Z0-9_-]+)\*\*\s*\|\s*([0-9.]+)%\s*\|\s*([0-9.a-zA-Z\s()]+)\s*\|\s*([0-9.]+)%"
    found_matches = re.findall(pattern, stdout_mon)
    for entry in found_matches:
        container_name = entry[0]
        cpu_val = float(entry[1])
        mem_raw = entry[2]
        cpu_peaks[container_name] = cpu_val
        mem_peaks[container_name] = mem_raw

    # Parsear métricas de K6
    k6_reqs: int = 0
    k6_avg_lat: float = 0.0
    k6_fail_rate: float = 0.0

    k6_stdout = k6_result.stdout

    reqs_match = re.search(r"http_reqs\.+:\s*(\d+)", k6_stdout)
    if reqs_match:
        k6_reqs = int(reqs_match.group(1))

    lat_match = re.search(r"iso_latencia_media\.+:\s*avg=([0-9.]+)", k6_stdout)
    if lat_match:
        k6_avg_lat = float(lat_match.group(1))

    fail_match = re.search(r"iso_tasa_fallos_red\.+:\s*([0-9.]+)%", k6_stdout)
    if fail_match:
        k6_fail_rate = float(fail_match.group(1))

    print(f"  [OK] Ejecución {run_number} completada.")
    print(f"    Peticiones: {k6_reqs} | Latencia: {k6_avg_lat:.2f} ms | Fallos: {k6_fail_rate:.2f}%")

    return {
        "run": run_number,
        "reqs": k6_reqs,
        "avg_lat": k6_avg_lat,
        "fail_rate": k6_fail_rate,
        "cpu_peaks": cpu_peaks,
        "mem_peaks": mem_peaks,
    }


def generate_report(
    results: list[dict[str, Any]],
    vus: int,
    test_name: str,
    output_path: str
) -> str:
    """Genera el reporte consolidado en Markdown."""
    num_runs = len(results)
    lines: list[str] = []
    lines.append(f"# INFORME CONSOLIDADO DE {num_runs} EJECUCIONES (VUS={vus})")
    lines.append(f"**Prueba:** {test_name}")
    lines.append(f"**Fecha de Consolidación:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Sección 1: Métricas K6
    lines.append("## 1. RESUMEN DE MÉTRICAS K6")
    lines.append("| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |")
    lines.append("| :---: | :---: | :---: | :---: |")
    for r in results:
        lines.append(f"| Run {r['run']} | {r['reqs']} | {r['avg_lat']:.3f} ms | {r['fail_rate']:.2f}% |")

    avg_reqs = sum(r['reqs'] for r in results) / num_runs
    avg_lat = sum(r['avg_lat'] for r in results) / num_runs
    avg_fail = sum(r['fail_rate'] for r in results) / num_runs
    lines.append(f"| **PROMEDIO** | **{avg_reqs:.1f}** | **{avg_lat:.3f} ms** | **{avg_fail:.2f}%** |")
    lines.append("")

    # Sección 2: Picos de CPU
    lines.append("## 2. PICOS DE CPU (%) EN CONTENEDORES")

    all_containers: set[str] = set()
    for r in results:
        all_containers.update(r["cpu_peaks"].keys())
    sorted_containers = sorted(all_containers)

    header = "| Contenedor |" + " | ".join(f"Run {r['run']}" for r in results) + " | Promedio Pico |"
    lines.append(header)
    separator = "| :--- |" + " | ".join(":---:" for _ in results) + " | :---: |"
    lines.append(separator)
    for c in sorted_containers:
        vals = [r["cpu_peaks"].get(c, 0.0) for r in results]
        avg_c = sum(vals) / num_runs
        row = f"| **{c}** |" + " | ".join(f"{v:.2f}%" for v in vals) + f" | **{avg_c:.2f}%** |"
        lines.append(row)

    lines.append("")

    # Sección 3: Picos de Memoria
    lines.append("## 3. PICOS DE MEMORIA EN CONTENEDORES")
    header_mem = "| Contenedor |" + " | ".join(f"Run {r['run']}" for r in results) + " |"
    lines.append(header_mem)
    separator_mem = "| :--- |" + " | ".join(":---:" for _ in results) + " |"
    lines.append(separator_mem)
    for c in sorted_containers:
        mems = [r["mem_peaks"].get(c, "N/A") for r in results]
        row_mem = f"| **{c}** |" + " | ".join(str(m) for m in mems) + " |"
        lines.append(row_mem)

    report = "\n".join(lines)

    with open(output_path, "w", encoding="utf-8") as out_f:
        out_f.write(report)

    return report


def main() -> None:
    """Punto de entrada principal del orquestador."""
    parser = argparse.ArgumentParser(
        description="Orquestador de Pruebas de Carga - Metodología Wohlin et al."
    )
    parser.add_argument(
        "--test-script",
        required=True,
        help="Ruta relativa al script K6 (ej: UC01_introspeccion/uc01_stress_introspeccion.js)"
    )
    parser.add_argument(
        "--vus",
        type=int,
        default=10,
        help="Número de usuarios virtuales concurrentes (default: 10)"
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=3,
        help="Número de ejecuciones consecutivas (default: 3)"
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Ruta del reporte de salida (default: auto-generado junto al script de test)"
    )

    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_script: str = args.test_script
    test_name = os.path.splitext(os.path.basename(test_script))[0]

    # Determinar ruta de salida del reporte
    if args.output:
        output_path: str = args.output
    else:
        test_dir = os.path.dirname(os.path.join(base_dir, test_script))
        results_dir = os.path.join(test_dir, "resultados")
        os.makedirs(results_dir, exist_ok=True)
        output_path = os.path.join(results_dir, f"reporte_consolidado_{args.runs}runs_vus{args.vus}.md")

    print(f"\n{'#' * 60}")
    print("  ORQUESTADOR DE PRUEBAS DE CARGA")
    print(f"  Script: {test_script}")
    print(f"  VUS: {args.vus} | Ejecuciones: {args.runs}")
    print(f"  Reporte: {output_path}")
    print(f"{'#' * 60}")

    results: list[dict[str, Any]] = []
    for i in range(1, args.runs + 1):
        res = run_single_experiment(i, test_script, args.vus, base_dir)
        results.append(res)
        if i < args.runs:
            print("\n  [WAIT] Esperando 5 segundos para estabilizar el sistema...")
            time.sleep(5)

    report = generate_report(results, args.vus, test_name, output_path)

    print(f"\n{'=' * 60}")
    print("  REPORTE CONSOLIDADO GENERADO")
    print(f"{'=' * 60}")
    print(report)
    print(f"\n[FILE] Archivo guardado en: {output_path}")


if __name__ == "__main__":
    main()
