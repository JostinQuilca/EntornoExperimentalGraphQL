# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 15:35:57

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 11 | 41741.152 ms | 72.72% | 0.00% |
| Run 2 | 12 | 41612.270 ms | 66.66% | 0.00% |
| Run 3 | 11 | 47438.559 ms | 72.72% | 0.00% |
| Run 4 | 35 | 11342.691 ms | 91.42% | 0.00% |
| Run 5 | 12 | 42782.415 ms | 66.66% | 0.00% |
| **PROMEDIO** | **16.2** | **36983.417 ms** | **74.04%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |190.07% | 164.60% | 191.02% | 188.74% | 199.87% | **186.86%** |
| **exp-protegido-mongo-db-1** |91.33% | 73.98% | 91.48% | 94.72% | 90.33% | **88.37%** |
| **exp-protegido-ms-catalogo-1** |4.83% | 4.46% | 3.97% | 6.68% | 5.23% | **5.03%** |
| **exp-protegido-ms-ordenes-1** |4.95% | 6.19% | 9.10% | 4.68% | 5.63% | **6.11%** |
| **exp-protegido-ms-resenas-1** |312.03% | 338.80% | 304.18% | 362.94% | 314.47% | **326.48%** |
| **exp-protegido-ms-usuarios-1** |166.47% | 252.10% | 134.02% | 206.36% | 236.74% | **199.14%** |
| **exp-protegido-postgres-db-1** |36.68% | 34.56% | 17.85% | 33.01% | 28.59% | **30.14%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  |
| **exp-protegido-mongo-db-1** |352.4MiB (352.40 MiB)  | 350.8MiB (350.80 MiB)  | 350.6MiB (350.60 MiB)  | 348.8MiB (348.80 MiB)  | 343.6MiB (343.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |68.98MiB (68.98 MiB)  | 46.17MiB (46.17 MiB)  | 47.29MiB (47.29 MiB)  | 45.7MiB (45.70 MiB)  | 47.33MiB (47.33 MiB)  |
| **exp-protegido-ms-ordenes-1** |67.09MiB (67.09 MiB)  | 45.4MiB (45.40 MiB)  | 55.87MiB (55.87 MiB)  | 48.19MiB (48.19 MiB)  | 46.51MiB (46.51 MiB)  |
| **exp-protegido-ms-resenas-1** |1015MiB (1015.00 MiB)  | 1003MiB (1003.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1023MiB (1023.00 MiB)  |
| **exp-protegido-ms-usuarios-1** |511.9MiB (511.90 MiB)  | 511.9MiB (511.90 MiB)  | 512MiB (512.00 MiB)  | 511.9MiB (511.90 MiB)  | 511.9MiB (511.90 MiB)  |
| **exp-protegido-postgres-db-1** |72.48MiB (72.48 MiB)  | 75.64MiB (75.64 MiB)  | 66.62MiB (66.62 MiB)  | 77.71MiB (77.71 MiB)  | 79.68MiB (79.68 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |78.01% | 73.77% | 72.95% | 62.45% | 74.49% | **72.33%** |
| **exp-protegido-mongo-db-1** |19.66% | 20.60% | 21.52% | 23.64% | 24.12% | **21.91%** |
| **exp-protegido-ms-catalogo-1** |1.01% | 1.01% | 0.86% | 1.13% | 0.92% | **0.99%** |
| **exp-protegido-ms-ordenes-1** |1.14% | 1.19% | 1.08% | 1.02% | 1.09% | **1.10%** |
| **exp-protegido-ms-resenas-1** |33.85% | 33.50% | 32.47% | 45.66% | 34.23% | **35.94%** |
| **exp-protegido-ms-usuarios-1** |13.80% | 15.34% | 10.69% | 28.70% | 27.62% | **19.23%** |
| **exp-protegido-postgres-db-1** |2.17% | 3.33% | 1.98% | 2.60% | 2.97% | **2.61%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |718.34 MiB | 727.00 MiB | 789.63 MiB | 652.85 MiB | 696.84 MiB | **716.93 MiB** |
| **exp-protegido-mongo-db-1** |201.32 MiB | 209.84 MiB | 203.18 MiB | 197.85 MiB | 204.94 MiB | **203.43 MiB** |
| **exp-protegido-ms-catalogo-1** |68.76 MiB | 46.02 MiB | 47.13 MiB | 45.47 MiB | 45.46 MiB | **50.57 MiB** |
| **exp-protegido-ms-ordenes-1** |66.80 MiB | 44.95 MiB | 52.07 MiB | 45.83 MiB | 45.47 MiB | **51.02 MiB** |
| **exp-protegido-ms-resenas-1** |585.03 MiB | 581.92 MiB | 566.05 MiB | 704.85 MiB | 604.49 MiB | **608.47 MiB** |
| **exp-protegido-ms-usuarios-1** |76.91 MiB | 70.62 MiB | 89.51 MiB | 110.68 MiB | 102.06 MiB | **89.96 MiB** |
| **exp-protegido-postgres-db-1** |64.27 MiB | 65.13 MiB | 63.96 MiB | 65.25 MiB | 65.79 MiB | **64.88 MiB** |