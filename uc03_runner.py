# -*- coding: utf-8 -*-
"""
UC-03 Ataque por Recursividad Circular
Variable independiente: ciclos de recursion (1-7)
Concurrencia fija: VUs=8
Replicas: 5 por escenario
Total: 7 niveles x 2 entornos x 5 replicas = 70 corridas de 60 s
"""
import uc_base as ub

LEVELS = [1, 2, 3, 4, 5, 6, 7]  # Lineal, mismo rango que UC-02
VUS_FIXED = 8
RUNS = 5
SCRIPT_REL = "UC03_recursividad_circular/uc03_recursividad_nivel.js"

if __name__ == "__main__":
    ub.run_uc_generic(
        uc_id="UC-03",
        uc_folder="UC03_recursividad_circular",
        script_rel=SCRIPT_REL,
        var_env_name="LEVEL",
        var_label="Ciclos de recursion",
        levels=LEVELS,
        vus_fixed=VUS_FIXED,
        runs=RUNS,
        out_subdir="UC03_RecursividadCircular",
    )
