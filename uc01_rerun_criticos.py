# -*- coding: utf-8 -*-
"""
Re-corrida focalizada UC-01 con n=5 replicas para los niveles criticos
(VUs=144, 233, 377) donde el sistema mostro estres real.

Motivacion: con n=3 el Mann-Whitney U bilateral tiene p-valor minimo de 0.10,
lo que impide rechazar H0 al alfa=0.05. Con n=5 en cada grupo el p minimo cae
a ~0.008, habilitando la inferencia estadistica declarada en la seccion 2.4.3.

Los niveles 1-89 permanecen intactos con n=3 (fase exploratoria). Solo los
niveles criticos se validan con n=5.

Uso:
  python uc01_rerun_criticos.py
"""
import os, sys
import uc01_runner as ur

# Sobrescribimos parametros del runner ANTES de ejecutar
ur.RUNS = 5                        # 5 replicas por escenario en los niveles criticos
ur.FIBONACCI_VUS = [144, 233, 377] # solo los niveles donde aparecio estres real

# Nota: la lógica de reuso en run_uc01() busca
# reporte_consolidado_{RUNS}runs_vus{N}.md. Como RUNS=5 y los reportes previos
# son de 3runs, se ejecutaran de cero (no habra falsos SKIP).

if __name__ == "__main__":
    print("=" * 70)
    print("  UC-01 RE-CORRIDA CRITICA: n=5 en VUs 144/233/377")
    print("=" * 70)
    ur.run_uc01()
