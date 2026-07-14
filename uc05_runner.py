# -*- coding: utf-8 -*-
"""
UC-05 Bomba de Fragmentos
Variable independiente: profundidad de fragmentos con expansion 5^N (Fibonacci: 1..8)
Concurrencia fija: VUs=1
Replicas: 5 por escenario
Total: 5 niveles x 2 entornos x 5 replicas = 50 corridas de hasta 60 s
Nota: nivel 8 = 5^8 = 390,625 resoluciones -> timeout garantizado (dato de colapso total)
"""
import uc_base as ub

LEVELS = [1, 2, 3, 5, 8]  # Fibonacci corto
VUS_FIXED = 1
RUNS = 5
SCRIPT_REL = "UC05_bomba_fragmentos/uc05_fragmentos_nivel.js"

if __name__ == "__main__":
    ub.run_uc_generic(
        uc_id="UC-05",
        uc_folder="UC05_bomba_fragmentos",
        script_rel=SCRIPT_REL,
        var_env_name="LEVEL",
        var_label="Profundidad de fragmentos",
        levels=LEVELS,
        vus_fixed=VUS_FIXED,
        runs=RUNS,
        out_subdir="UC05_BombaFragmentos",
    )
