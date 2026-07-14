# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=1)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 17:32:23

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 60 | 6.275 ms | 0.00% |
| Run 2 | 60 | 6.032 ms | 0.00% |
| Run 3 | 60 | 8.860 ms | 0.00% |
| **PROMEDIO** | **60.0** | **7.056 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.72% | 1.75% | 7.68% | **3.38%** |
| **exp-vulnerable-mongo-db-1** |68.13% | 85.57% | 70.20% | **74.63%** |
| **exp-vulnerable-ms-catalogo-1** |4.45% | 5.36% | 4.56% | **4.79%** |
| **exp-vulnerable-ms-ordenes-1** |5.50% | 4.68% | 4.90% | **5.03%** |
| **exp-vulnerable-ms-resenas-1** |5.18% | 5.01% | 5.00% | **5.06%** |
| **exp-vulnerable-ms-usuarios-1** |5.65% | 4.89% | 19.94% | **10.16%** |
| **exp-vulnerable-postgres-db-1** |6.96% | 4.78% | 11.16% | **7.63%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |64.81MiB (64.81 MiB)  | 97.67MiB (97.67 MiB)  | 64.89MiB (64.89 MiB)  |
| **exp-vulnerable-mongo-db-1** |332.1MiB (332.10 MiB)  | 334.4MiB (334.40 MiB)  | 338.5MiB (338.50 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.75MiB (45.75 MiB)  | 46.12MiB (46.12 MiB)  | 47.68MiB (47.68 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.35MiB (46.35 MiB)  | 46.39MiB (46.39 MiB)  | 46.77MiB (46.77 MiB)  |
| **exp-vulnerable-ms-resenas-1** |45.9MiB (45.90 MiB)  | 47.36MiB (47.36 MiB)  | 45.88MiB (45.88 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |48.14MiB (48.14 MiB)  | 47.65MiB (47.65 MiB)  | 48.17MiB (48.17 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.41MiB (27.41 MiB)  | 27.39MiB (27.39 MiB)  | 27.45MiB (27.45 MiB)  |