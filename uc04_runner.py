# -*- coding: utf-8 -*-
"""
UC-04 Ataque por Abuso de Alias
Variable independiente: numero de alias por peticion (escala Fibonacci: 1..377)
Concurrencia fija: VUs=1
Replicas: 5 por escenario
Total: 13 niveles x 2 entornos x 5 replicas = 130 corridas de 60 s
Nota: el control queryComplexity cuenta 3 campos por alias (max 1000). El bloqueo
se activa en 377 alias (1131 campos > 1000); 233 alias (699 campos) aun pasa.
"""
import uc_base as ub

LEVELS = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]  # Fibonacci hasta cruzar el umbral de complejidad (1000)
VUS_FIXED = 1
RUNS = 5
SCRIPT_REL = "UC04_abuso_alias/uc04_alias_nivel.js"

if __name__ == "__main__":
    ub.run_uc_generic(
        uc_id="UC-04",
        uc_folder="UC04_abuso_alias",
        script_rel=SCRIPT_REL,
        var_env_name="ALIAS_COUNT",
        var_label="Numero de alias",
        levels=LEVELS,
        vus_fixed=VUS_FIXED,
        runs=RUNS,
        out_subdir="UC04_AbusoAlias",
    )
