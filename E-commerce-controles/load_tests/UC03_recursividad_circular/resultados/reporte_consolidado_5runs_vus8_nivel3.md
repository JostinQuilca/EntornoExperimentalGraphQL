# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 20:58:51

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 481 | 10.748 ms | 0.00% | 100.00% |
| Run 2 | 481 | 7.107 ms | 0.00% | 100.00% |
| Run 3 | 481 | 7.597 ms | 0.00% | 100.00% |
| Run 4 | 481 | 8.054 ms | 0.00% | 100.00% |
| Run 5 | 481 | 6.761 ms | 0.00% | 100.00% |
| **PROMEDIO** | **481.0** | **8.053 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |23.67% | 9.84% | 34.06% | 11.26% | 11.67% | **18.10%** |
| **exp-protegido-mongo-db-1** |122.46% | 93.07% | 112.15% | 96.53% | 89.71% | **102.78%** |
| **exp-protegido-ms-catalogo-1** |3.73% | 4.16% | 4.95% | 4.62% | 4.89% | **4.47%** |
| **exp-protegido-ms-ordenes-1** |5.81% | 4.93% | 4.39% | 11.42% | 5.85% | **6.48%** |
| **exp-protegido-ms-resenas-1** |6.61% | 4.66% | 3.73% | 10.98% | 5.54% | **6.30%** |
| **exp-protegido-ms-usuarios-1** |37.29% | 40.38% | 46.19% | 38.61% | 35.27% | **39.55%** |
| **exp-protegido-postgres-db-1** |14.84% | 6.71% | 5.72% | 13.75% | 5.87% | **9.38%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |101.5MiB (101.50 MiB)  | 81.33MiB (81.33 MiB)  | 82.45MiB (82.45 MiB)  | 81.75MiB (81.75 MiB)  | 82.19MiB (82.19 MiB)  |
| **exp-protegido-mongo-db-1** |345.5MiB (345.50 MiB)  | 348.9MiB (348.90 MiB)  | 349.8MiB (349.80 MiB)  | 349MiB (349.00 MiB)  | 341.6MiB (341.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |47.28MiB (47.28 MiB)  | 46.03MiB (46.03 MiB)  | 47.33MiB (47.33 MiB)  | 46.61MiB (46.61 MiB)  | 47.43MiB (47.43 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.51MiB (46.51 MiB)  | 47.71MiB (47.71 MiB)  | 45.92MiB (45.92 MiB)  | 48.11MiB (48.11 MiB)  | 46.34MiB (46.34 MiB)  |
| **exp-protegido-ms-resenas-1** |48.9MiB (48.90 MiB)  | 45.95MiB (45.95 MiB)  | 47.73MiB (47.73 MiB)  | 55.65MiB (55.65 MiB)  | 45.82MiB (45.82 MiB)  |
| **exp-protegido-ms-usuarios-1** |73.74MiB (73.74 MiB)  | 68.57MiB (68.57 MiB)  | 66.46MiB (66.46 MiB)  | 69.02MiB (69.02 MiB)  | 69.09MiB (69.09 MiB)  |
| **exp-protegido-postgres-db-1** |30.21MiB (30.21 MiB)  | 30.16MiB (30.16 MiB)  | 30.23MiB (30.23 MiB)  | 31.87MiB (31.87 MiB)  | 30.16MiB (30.16 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |5.34% | 3.10% | 4.72% | 3.40% | 3.35% | **3.98%** |
| **exp-protegido-mongo-db-1** |29.61% | 26.04% | 23.90% | 28.31% | 27.62% | **27.10%** |
| **exp-protegido-ms-catalogo-1** |1.06% | 1.03% | 1.18% | 1.20% | 1.13% | **1.12%** |
| **exp-protegido-ms-ordenes-1** |1.09% | 1.29% | 1.03% | 1.48% | 1.32% | **1.24%** |
| **exp-protegido-ms-resenas-1** |1.26% | 1.32% | 1.09% | 1.81% | 1.32% | **1.36%** |
| **exp-protegido-ms-usuarios-1** |2.53% | 2.50% | 2.69% | 2.67% | 2.41% | **2.56%** |
| **exp-protegido-postgres-db-1** |2.05% | 1.79% | 1.56% | 2.05% | 1.42% | **1.77%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |75.38 MiB | 75.73 MiB | 78.48 MiB | 76.20 MiB | 76.56 MiB | **76.47 MiB** |
| **exp-protegido-mongo-db-1** |218.58 MiB | 207.38 MiB | 206.21 MiB | 203.02 MiB | 211.76 MiB | **209.39 MiB** |
| **exp-protegido-ms-catalogo-1** |45.95 MiB | 45.92 MiB | 45.71 MiB | 46.49 MiB | 46.02 MiB | **46.02 MiB** |
| **exp-protegido-ms-ordenes-1** |45.40 MiB | 46.07 MiB | 45.83 MiB | 46.39 MiB | 46.23 MiB | **45.98 MiB** |
| **exp-protegido-ms-resenas-1** |45.95 MiB | 45.85 MiB | 46.39 MiB | 53.62 MiB | 45.73 MiB | **47.51 MiB** |
| **exp-protegido-ms-usuarios-1** |71.47 MiB | 68.55 MiB | 66.44 MiB | 68.43 MiB | 69.07 MiB | **68.79 MiB** |
| **exp-protegido-postgres-db-1** |30.20 MiB | 30.15 MiB | 30.22 MiB | 30.21 MiB | 30.16 MiB | **30.19 MiB** |