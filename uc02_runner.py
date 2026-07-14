# -*- coding: utf-8 -*-
"""
UC-02 Ataque por Profundidad Moderada — Diseño factorial (Matriz)
Variables independientes:
  - Profundidad de anidamiento: 1, 2, 3, 4, 5, 6, 7 (escala lineal)
  - Concurrencia (VUs): 1, 2, 3, 5, 8 (Fibonacci corto)
Réplicas: 5 por celda de la matriz
Ventana: 60 s por réplica

Total escenarios: 7 × 5 × 2 entornos × 5 réplicas = 350 corridas de 60 s
"""
import uc_base as ub

LEVELS = [1, 2, 3, 4, 5, 6, 7]        # Profundidad de anidamiento
VUS_LIST = [1, 2, 3, 5, 8]             # Fibonacci corto
RUNS = 5
SCRIPT_REL = "UC02_profundidad_moderada/uc02_profundidad_nivel.js"

if __name__ == "__main__":
    ub.run_uc_matrix(
        uc_id="UC-02",
        uc_folder="UC02_profundidad_moderada",
        script_rel=SCRIPT_REL,
        var_env_name="LEVEL",
        var_label="Profundidad de anidamiento",
        levels=LEVELS,
        vus_list=VUS_LIST,
        runs=RUNS,
        out_subdir="UC02_ProfundidadModerada",
    )
