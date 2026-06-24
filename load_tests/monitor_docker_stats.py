"""
Monitor de Docker Stats - Captura picos de CPU y Memoria.
=========================================================
Se ejecuta en bucle hasta que detecta el archivo 'stop_monitor.tmp'.
Al finalizar, genera un reporte markdown con los picos observados.

Uso (invocado automáticamente por run_multiple_experiments.py):
    python monitor_docker_stats.py --output-dir <ruta_carpeta_resultados>
"""

import subprocess
import time
import re
import sys
import os
import argparse
from collections import defaultdict
from typing import Any


def parse_memory(mem_str: str) -> float:
    """
    Parses memory usage string from docker stats (e.g. '12.5MiB / 15.54GiB')
    Returns value in MiB.
    """
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
    """
    Parses CPU percentage string (e.g. '1.25%')
    Returns value as a float.
    """
    try:
        val_str = cpu_str.replace('%', '').strip()
        return float(val_str)
    except (ValueError, AttributeError):
        return 0.0


def main() -> None:
    """Punto de entrada del monitor de Docker."""
    parser = argparse.ArgumentParser(description="Monitor de picos Docker Stats")
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Carpeta donde guardar el reporte de picos (default: directorio actual)"
    )
    args = parser.parse_args()

    output_dir: str = args.output_dir if args.output_dir else os.getcwd()
    os.makedirs(output_dir, exist_ok=True)

    print("Iniciando monitoreo de docker stats...")

    # Almacenamiento de picos (máximos)
    peaks: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"cpu_peak": 0.0, "mem_peak_mib": 0.0, "mem_raw_peak": "", "mem_perc_peak": 0.0}
    )

    stop_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stop_monitor.tmp")
    if os.path.exists(stop_file):
        try:
            os.remove(stop_file)
        except OSError:
            pass

    try:
        while not os.path.exists(stop_file):
            # Ejecutar docker stats (una sola captura)
            result = subprocess.run(
                ["docker", "stats", "--no-stream", "--format",
                 "{{.Name}},{{.CPUPerc}},{{.MemUsage}},{{.MemPerc}}"],
                capture_output=True,
                text=True,
                shell=True,
                check=False
            )

            if result.returncode != 0:
                print(f"Error al ejecutar docker stats: {result.stderr}", file=sys.stderr)
                time.sleep(1)
                continue

            lines = result.stdout.strip().split('\n')
            for line in lines:
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) < 4:
                    continue

                name = parts[0].strip()
                cpu_val = parse_cpu(parts[1])
                mem_raw = parts[2].strip()
                mem_val = parse_memory(mem_raw)
                mem_perc_val = parse_cpu(parts[3])

                # Actualizar picos
                if cpu_val > peaks[name]["cpu_peak"]:
                    peaks[name]["cpu_peak"] = cpu_val

                if mem_val > peaks[name]["mem_peak_mib"]:
                    peaks[name]["mem_peak_mib"] = mem_val
                    peaks[name]["mem_raw_peak"] = mem_raw.split('/')[0].strip()
                    peaks[name]["mem_perc_peak"] = mem_perc_val

            # Espera discreta antes del siguiente ciclo
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nMonitoreo finalizado via Ctrl+C. Generando reporte de picos...")

    # Limpiar archivo de parada
    if os.path.exists(stop_file):
        try:
            os.remove(stop_file)
        except OSError:
            pass

    # Formatear reporte de picos
    report_lines: list[str] = []
    report_lines.append("# REPORTES DE PICOS DE CONSUMO DOCKER STATS")
    report_lines.append(f"Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    report_lines.append("| Contenedor | CPU Pico (%) | Memoria Pico (MiB) | Memoria Pico (%) |")
    report_lines.append("| :--- | :---: | :---: | :---: |")

    for name, stats in sorted(peaks.items()):
        report_lines.append(
            f"| **{name}** | {stats['cpu_peak']:.2f}% "
            f"| {stats['mem_raw_peak']} ({stats['mem_peak_mib']:.2f} MiB) "
            f"| {stats['mem_perc_peak']:.2f}% |"
        )

    report = "\n".join(report_lines)

    # Guardar reporte en la carpeta de salida indicada
    report_filename = os.path.join(output_dir, f"reporte_picos_docker_{int(time.time())}.md")
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n" + "=" * 50)
    print(report)
    print("=" * 50)
    print(f"\nReporte guardado en: {report_filename}")


if __name__ == "__main__":
    main()
