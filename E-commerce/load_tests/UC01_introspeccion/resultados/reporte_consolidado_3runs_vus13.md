# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=13)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 18:52:35

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 780 | 5.413 ms | 0.00% |
| Run 2 | 780 | 6.079 ms | 0.00% |
| Run 3 | 780 | 5.670 ms | 0.00% |
| **PROMEDIO** | **780.0** | **5.721 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |14.34% | 18.71% | 12.08% | **15.04%** |
| **exp-vulnerable-mongo-db-1** |62.36% | 54.78% | 53.28% | **56.81%** |
| **exp-vulnerable-ms-catalogo-1** |3.41% | 4.08% | 2.75% | **3.41%** |
| **exp-vulnerable-ms-ordenes-1** |2.99% | 3.19% | 3.22% | **3.13%** |
| **exp-vulnerable-ms-resenas-1** |2.64% | 3.23% | 3.42% | **3.10%** |
| **exp-vulnerable-ms-usuarios-1** |4.32% | 3.35% | 2.90% | **3.52%** |
| **exp-vulnerable-postgres-db-1** |5.07% | 4.55% | 4.17% | **4.60%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |94.43MiB (94.43 MiB)  | 94MiB (94.00 MiB)  | 95.02MiB (95.02 MiB)  |
| **exp-vulnerable-mongo-db-1** |338.7MiB (338.70 MiB)  | 329.9MiB (329.90 MiB)  | 338.6MiB (338.60 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.3MiB (46.30 MiB)  | 45.56MiB (45.56 MiB)  | 47.43MiB (47.43 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.93MiB (45.93 MiB)  | 48.57MiB (48.57 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47.2MiB (47.20 MiB)  | 45.56MiB (45.56 MiB)  | 45.74MiB (45.74 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.64MiB (45.64 MiB)  | 46.05MiB (46.05 MiB)  | 46.99MiB (46.99 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.38MiB (27.38 MiB)  | 30.09MiB (30.09 MiB)  | 27.52MiB (27.52 MiB)  |