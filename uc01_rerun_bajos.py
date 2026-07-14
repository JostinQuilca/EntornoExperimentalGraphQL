# -*- coding: utf-8 -*-
"""
Fase 2: Re-corrida focalizada UC-01 con n=5 en los niveles bajos y medios.

Complementa uc01_rerun_criticos.py (que ya cubrio VUs=144, 233, 377 con n=5).
Al terminar esta fase, TODOS los niveles Fibonacci de UC-01 tienen n=5 real.

Uso:
  python uc01_rerun_bajos.py
"""
import uc01_runner as ur

ur.RUNS = 5
ur.FIBONACCI_VUS = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

if __name__ == "__main__":
    print("=" * 70)
    print("  UC-01 FASE 2: n=5 en niveles bajos/medios (1-89)")
    print("=" * 70)
    ur.run_uc01()
