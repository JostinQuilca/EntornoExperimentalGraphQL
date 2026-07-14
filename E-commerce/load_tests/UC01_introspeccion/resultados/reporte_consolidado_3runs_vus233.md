# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=233)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 20:12:51

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 13980 | 9.914 ms | 0.18% |
| Run 2 | 13980 | 11.126 ms | 0.00% |
| Run 3 | 0 | 0.000 ms | 0.00% |
| **PROMEDIO** | **9320.0** | **7.013 ms** | **0.06%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |62.20% | 67.00% | 57.11% | **62.10%** |
| **exp-vulnerable-mongo-db-1** |61.78% | 61.71% | 59.82% | **61.10%** |
| **exp-vulnerable-ms-catalogo-1** |3.62% | 3.35% | 2.75% | **3.24%** |
| **exp-vulnerable-ms-ordenes-1** |3.11% | 3.66% | 2.71% | **3.16%** |
| **exp-vulnerable-ms-resenas-1** |3.20% | 3.80% | 2.77% | **3.26%** |
| **exp-vulnerable-ms-usuarios-1** |3.26% | 3.34% | 3.31% | **3.30%** |
| **exp-vulnerable-postgres-db-1** |4.32% | 4.28% | 3.92% | **4.17%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |122.9MiB (122.90 MiB)  | 183.9MiB (183.90 MiB)  | 130.1MiB (130.10 MiB)  |
| **exp-vulnerable-mongo-db-1** |332.4MiB (332.40 MiB)  | 345MiB (345.00 MiB)  | 347.5MiB (347.50 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.43MiB (45.43 MiB)  | 47.29MiB (47.29 MiB)  | 45.82MiB (45.82 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.54MiB (46.54 MiB)  | 45.48MiB (45.48 MiB)  | 48.04MiB (48.04 MiB)  |
| **exp-vulnerable-ms-resenas-1** |45.12MiB (45.12 MiB)  | 47.45MiB (47.45 MiB)  | 49.16MiB (49.16 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.4MiB (45.40 MiB)  | 45.61MiB (45.61 MiB)  | 47.27MiB (47.27 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.46MiB (27.46 MiB)  | 27.74MiB (27.74 MiB)  | 27.41MiB (27.41 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |33.74% | 36.42% | 36.98% | **35.71%** |
| **exp-vulnerable-mongo-db-1** |17.16% | 15.17% | 17.63% | **16.65%** |
| **exp-vulnerable-ms-catalogo-1** |0.84% | 0.81% | 0.75% | **0.80%** |
| **exp-vulnerable-ms-ordenes-1** |0.81% | 0.97% | 0.70% | **0.83%** |
| **exp-vulnerable-ms-resenas-1** |0.79% | 0.92% | 0.94% | **0.88%** |
| **exp-vulnerable-ms-usuarios-1** |0.80% | 0.91% | 0.96% | **0.89%** |
| **exp-vulnerable-postgres-db-1** |1.02% | 1.08% | 1.07% | **1.06%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |106.38 MiB | 127.94 MiB | 113.68 MiB | **116.00 MiB** |
| **exp-vulnerable-mongo-db-1** |196.73 MiB | 195.79 MiB | 204.13 MiB | **198.88 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.30 MiB | 47.17 MiB | 45.71 MiB | **46.06 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.42 MiB | 45.35 MiB | 46.52 MiB | **46.10 MiB** |
| **exp-vulnerable-ms-resenas-1** |45.00 MiB | 47.29 MiB | 47.59 MiB | **46.63 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.28 MiB | 45.49 MiB | 45.70 MiB | **45.49 MiB** |
| **exp-vulnerable-postgres-db-1** |27.33 MiB | 27.32 MiB | 27.36 MiB | **27.34 MiB** |