# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 16:04:08

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 72 | 7300.173 ms | 0.00% | 0.00% |
| Run 2 | 64 | 6537.642 ms | 0.00% | 0.00% |
| Run 3 | 64 | 7293.969 ms | 0.00% | 0.00% |
| Run 4 | 80 | 6156.938 ms | 0.00% | 0.00% |
| Run 5 | 56 | 7592.695 ms | 0.00% | 0.00% |
| **PROMEDIO** | **67.2** | **6976.283 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |14.59% | 5.68% | 4.56% | 6.59% | 4.85% | **7.25%** |
| **exp-protegido-mongo-db-1** |101.42% | 94.77% | 83.03% | 71.22% | 101.57% | **90.40%** |
| **exp-protegido-ms-catalogo-1** |5.63% | 4.51% | 5.02% | 4.48% | 4.61% | **4.85%** |
| **exp-protegido-ms-ordenes-1** |5.94% | 5.45% | 4.97% | 4.36% | 3.56% | **4.86%** |
| **exp-protegido-ms-resenas-1** |395.39% | 356.68% | 340.55% | 376.85% | 349.46% | **363.79%** |
| **exp-protegido-ms-usuarios-1** |16.58% | 7.10% | 3.99% | 4.84% | 3.26% | **7.15%** |
| **exp-protegido-postgres-db-1** |52.39% | 48.59% | 50.85% | 44.60% | 40.03% | **47.29%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |68.09MiB (68.09 MiB)  | 67.89MiB (67.89 MiB)  | 68.2MiB (68.20 MiB)  | 68.58MiB (68.58 MiB)  | 68.16MiB (68.16 MiB)  |
| **exp-protegido-mongo-db-1** |340.9MiB (340.90 MiB)  | 346MiB (346.00 MiB)  | 338.4MiB (338.40 MiB)  | 330.9MiB (330.90 MiB)  | 349.6MiB (349.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.74MiB (45.74 MiB)  | 46.34MiB (46.34 MiB)  | 46.52MiB (46.52 MiB)  | 48.92MiB (48.92 MiB)  | 46.58MiB (46.58 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.25MiB (46.25 MiB)  | 46MiB (46.00 MiB)  | 46.84MiB (46.84 MiB)  | 47.97MiB (47.97 MiB)  | 46.49MiB (46.49 MiB)  |
| **exp-protegido-ms-resenas-1** |1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  |
| **exp-protegido-ms-usuarios-1** |55.99MiB (55.99 MiB)  | 47.34MiB (47.34 MiB)  | 45.57MiB (45.57 MiB)  | 48.23MiB (48.23 MiB)  | 47.53MiB (47.53 MiB)  |
| **exp-protegido-postgres-db-1** |74.49MiB (74.49 MiB)  | 70.78MiB (70.78 MiB)  | 72.02MiB (72.02 MiB)  | 70.69MiB (70.69 MiB)  | 72.78MiB (72.78 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.00% | 0.64% | 0.33% | 0.69% | 0.36% | **0.60%** |
| **exp-protegido-mongo-db-1** |33.51% | 32.72% | 26.24% | 20.84% | 36.10% | **29.88%** |
| **exp-protegido-ms-catalogo-1** |1.18% | 0.82% | 1.17% | 1.09% | 0.98% | **1.05%** |
| **exp-protegido-ms-ordenes-1** |1.06% | 0.97% | 0.99% | 1.19% | 0.84% | **1.01%** |
| **exp-protegido-ms-resenas-1** |151.52% | 161.43% | 161.73% | 196.61% | 166.07% | **167.47%** |
| **exp-protegido-ms-usuarios-1** |1.60% | 1.21% | 1.01% | 1.17% | 0.79% | **1.16%** |
| **exp-protegido-postgres-db-1** |6.96% | 8.02% | 6.47% | 8.04% | 4.74% | **6.85%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.18 MiB | 66.42 MiB | 66.81 MiB | 66.53 MiB | 66.38 MiB | **66.66 MiB** |
| **exp-protegido-mongo-db-1** |209.27 MiB | 197.15 MiB | 202.49 MiB | 200.10 MiB | 214.34 MiB | **204.67 MiB** |
| **exp-protegido-ms-catalogo-1** |45.60 MiB | 46.24 MiB | 45.15 MiB | 47.45 MiB | 46.49 MiB | **46.19 MiB** |
| **exp-protegido-ms-ordenes-1** |45.89 MiB | 45.61 MiB | 46.41 MiB | 46.19 MiB | 45.72 MiB | **45.96 MiB** |
| **exp-protegido-ms-resenas-1** |821.88 MiB | 789.68 MiB | 861.02 MiB | 772.22 MiB | 850.66 MiB | **819.09 MiB** |
| **exp-protegido-ms-usuarios-1** |53.31 MiB | 46.90 MiB | 45.46 MiB | 46.56 MiB | 46.13 MiB | **47.67 MiB** |
| **exp-protegido-postgres-db-1** |64.31 MiB | 62.78 MiB | 64.73 MiB | 63.98 MiB | 64.67 MiB | **64.09 MiB** |