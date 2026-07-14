# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 22:27:08

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 120 | 6.479 ms | 0.00% |
| Run 2 | 120 | 6.117 ms | 0.00% |
| Run 3 | 120 | 5.950 ms | 0.00% |
| Run 4 | 120 | 6.213 ms | 0.00% |
| Run 5 | 120 | 5.818 ms | 0.00% |
| **PROMEDIO** | **120.0** | **6.115 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |5.92% | 1.78% | 1.63% | 3.40% | 1.32% | **2.81%** |
| **exp-vulnerable-mongo-db-1** |53.29% | 57.69% | 52.67% | 51.89% | 52.81% | **53.67%** |
| **exp-vulnerable-ms-catalogo-1** |4.32% | 3.76% | 4.51% | 3.52% | 3.99% | **4.02%** |
| **exp-vulnerable-ms-ordenes-1** |3.19% | 4.73% | 4.40% | 3.24% | 3.72% | **3.86%** |
| **exp-vulnerable-ms-resenas-1** |3.61% | 5.00% | 3.75% | 3.06% | 4.33% | **3.95%** |
| **exp-vulnerable-ms-usuarios-1** |3.30% | 4.86% | 3.50% | 3.43% | 4.43% | **3.90%** |
| **exp-vulnerable-postgres-db-1** |4.94% | 5.20% | 4.02% | 4.34% | 4.71% | **4.64%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.79MiB (65.79 MiB)  | 65.79MiB (65.79 MiB)  | 65.27MiB (65.27 MiB)  | 65.15MiB (65.15 MiB)  | 64.45MiB (64.45 MiB)  |
| **exp-vulnerable-mongo-db-1** |340.9MiB (340.90 MiB)  | 345.5MiB (345.50 MiB)  | 338.4MiB (338.40 MiB)  | 333.8MiB (333.80 MiB)  | 336.7MiB (336.70 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.12MiB (46.12 MiB)  | 46MiB (46.00 MiB)  | 45.88MiB (45.88 MiB)  | 45.55MiB (45.55 MiB)  | 46.32MiB (46.32 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.51MiB (45.51 MiB)  | 45.84MiB (45.84 MiB)  | 47.38MiB (47.38 MiB)  | 47.07MiB (47.07 MiB)  | 45.33MiB (45.33 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.14MiB (46.14 MiB)  | 46.25MiB (46.25 MiB)  | 46.18MiB (46.18 MiB)  | 46.59MiB (46.59 MiB)  | 45.66MiB (45.66 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.37MiB (45.37 MiB)  | 45.78MiB (45.78 MiB)  | 46.71MiB (46.71 MiB)  | 45.55MiB (45.55 MiB)  | 47.22MiB (47.22 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.42MiB (27.42 MiB)  | 27.41MiB (27.41 MiB)  | 27.5MiB (27.50 MiB)  | 29.41MiB (29.41 MiB)  | 29.21MiB (29.21 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.90% | 0.75% | 0.77% | 0.79% | 0.65% | **0.77%** |
| **exp-vulnerable-mongo-db-1** |14.69% | 14.03% | 15.13% | 16.23% | 15.57% | **15.13%** |
| **exp-vulnerable-ms-catalogo-1** |1.00% | 0.92% | 0.87% | 0.80% | 0.90% | **0.90%** |
| **exp-vulnerable-ms-ordenes-1** |0.80% | 0.94% | 0.90% | 0.89% | 1.04% | **0.91%** |
| **exp-vulnerable-ms-resenas-1** |0.83% | 1.12% | 0.86% | 0.84% | 1.06% | **0.94%** |
| **exp-vulnerable-ms-usuarios-1** |0.76% | 1.02% | 0.91% | 0.85% | 1.06% | **0.92%** |
| **exp-vulnerable-postgres-db-1** |1.15% | 1.15% | 1.29% | 1.21% | 1.23% | **1.21%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.03 MiB | 64.54 MiB | 64.66 MiB | 64.57 MiB | 63.99 MiB | **64.56 MiB** |
| **exp-vulnerable-mongo-db-1** |195.40 MiB | 201.89 MiB | 199.34 MiB | 196.87 MiB | 197.03 MiB | **198.11 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.99 MiB | 45.87 MiB | 45.76 MiB | 45.42 MiB | 46.06 MiB | **45.82 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.38 MiB | 45.73 MiB | 47.20 MiB | 46.95 MiB | 45.21 MiB | **46.09 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.02 MiB | 46.14 MiB | 46.04 MiB | 46.47 MiB | 45.55 MiB | **46.04 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.24 MiB | 45.64 MiB | 46.39 MiB | 45.43 MiB | 47.10 MiB | **45.96 MiB** |
| **exp-vulnerable-postgres-db-1** |27.36 MiB | 27.37 MiB | 27.30 MiB | 27.40 MiB | 27.38 MiB | **27.36 MiB** |