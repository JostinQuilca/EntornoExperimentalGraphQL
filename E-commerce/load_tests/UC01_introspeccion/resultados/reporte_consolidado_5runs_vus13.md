# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=13)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 18:08:05

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 0 | 0.000 ms | 0.00% |
| Run 2 | 780 | 7.221 ms | 0.00% |
| Run 3 | 780 | 6.610 ms | 0.00% |
| Run 4 | 780 | 6.214 ms | 0.00% |
| Run 5 | 780 | 7.091 ms | 0.00% |
| **PROMEDIO** | **624.0** | **5.427 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |13.51% | 17.97% | 9.52% | 8.64% | 12.53% | **12.43%** |
| **exp-vulnerable-mongo-db-1** |79.09% | 66.62% | 62.26% | 59.51% | 60.50% | **65.60%** |
| **exp-vulnerable-ms-catalogo-1** |3.17% | 6.72% | 6.28% | 4.01% | 4.53% | **4.94%** |
| **exp-vulnerable-ms-ordenes-1** |4.25% | 4.66% | 3.51% | 5.47% | 6.48% | **4.87%** |
| **exp-vulnerable-ms-resenas-1** |6.38% | 4.19% | 3.29% | 6.19% | 5.80% | **5.17%** |
| **exp-vulnerable-ms-usuarios-1** |4.35% | 4.99% | 3.14% | 5.32% | 6.62% | **4.88%** |
| **exp-vulnerable-postgres-db-1** |4.79% | 5.99% | 5.70% | 4.91% | 6.41% | **5.56%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |74.87MiB (74.87 MiB)  | 93.68MiB (93.68 MiB)  | 91.72MiB (91.72 MiB)  | 93.79MiB (93.79 MiB)  | 94.12MiB (94.12 MiB)  |
| **exp-vulnerable-mongo-db-1** |342.1MiB (342.10 MiB)  | 352.2MiB (352.20 MiB)  | 334.3MiB (334.30 MiB)  | 341.5MiB (341.50 MiB)  | 333.4MiB (333.40 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.62MiB (45.62 MiB)  | 47.62MiB (47.62 MiB)  | 46.93MiB (46.93 MiB)  | 45.51MiB (45.51 MiB)  | 46.29MiB (46.29 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.76MiB (45.76 MiB)  | 47.24MiB (47.24 MiB)  | 45.93MiB (45.93 MiB)  | 45.86MiB (45.86 MiB)  | 46.55MiB (46.55 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.18MiB (46.18 MiB)  | 47.2MiB (47.20 MiB)  | 46.57MiB (46.57 MiB)  | 46.01MiB (46.01 MiB)  | 46.88MiB (46.88 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.34MiB (45.34 MiB)  | 46.9MiB (46.90 MiB)  | 47.1MiB (47.10 MiB)  | 49.23MiB (49.23 MiB)  | 45.88MiB (45.88 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.37MiB (27.37 MiB)  | 27.4MiB (27.40 MiB)  | 27.46MiB (27.46 MiB)  | 27.41MiB (27.41 MiB)  | 27.45MiB (27.45 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |6.33% | 5.55% | 4.68% | 4.39% | 5.18% | **5.23%** |
| **exp-vulnerable-mongo-db-1** |23.41% | 17.83% | 20.63% | 16.50% | 17.51% | **19.18%** |
| **exp-vulnerable-ms-catalogo-1** |0.67% | 1.32% | 1.26% | 1.10% | 1.06% | **1.08%** |
| **exp-vulnerable-ms-ordenes-1** |0.94% | 1.07% | 0.96% | 0.98% | 1.07% | **1.00%** |
| **exp-vulnerable-ms-resenas-1** |1.64% | 1.15% | 0.92% | 0.93% | 1.01% | **1.13%** |
| **exp-vulnerable-ms-usuarios-1** |1.37% | 1.12% | 0.88% | 1.09% | 1.06% | **1.10%** |
| **exp-vulnerable-postgres-db-1** |1.35% | 1.61% | 1.31% | 1.22% | 1.41% | **1.38%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |70.49 MiB | 79.31 MiB | 78.38 MiB | 80.28 MiB | 79.72 MiB | **77.64 MiB** |
| **exp-vulnerable-mongo-db-1** |225.27 MiB | 209.41 MiB | 197.12 MiB | 204.61 MiB | 200.52 MiB | **207.39 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.57 MiB | 47.50 MiB | 46.80 MiB | 45.39 MiB | 46.16 MiB | **46.28 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.72 MiB | 47.00 MiB | 45.81 MiB | 45.74 MiB | 46.42 MiB | **46.14 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.13 MiB | 47.07 MiB | 46.44 MiB | 45.90 MiB | 46.75 MiB | **46.46 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.31 MiB | 46.78 MiB | 46.98 MiB | 47.00 MiB | 45.76 MiB | **46.37 MiB** |
| **exp-vulnerable-postgres-db-1** |27.23 MiB | 27.36 MiB | 27.35 MiB | 27.31 MiB | 27.34 MiB | **27.32 MiB** |