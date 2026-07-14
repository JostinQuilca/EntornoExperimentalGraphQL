# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=377)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 21:58:02

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 21609 | 57.822 ms | 0.61% |
| Run 2 | 21940 | 39.055 ms | 0.71% |
| Run 3 | 22284 | 21.276 ms | 0.72% |
| Run 4 | 22090 | 31.927 ms | 0.71% |
| Run 5 | 22356 | 18.197 ms | 0.71% |
| **PROMEDIO** | **22055.8** | **33.655 ms** | **0.69%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |121.70% | 123.71% | 100.20% | 106.26% | 99.42% | **110.26%** |
| **exp-protegido-mongo-db-1** |125.19% | 121.15% | 63.17% | 114.94% | 75.97% | **100.08%** |
| **exp-protegido-ms-catalogo-1** |6.56% | 5.09% | 3.14% | 3.31% | 2.99% | **4.22%** |
| **exp-protegido-ms-ordenes-1** |6.02% | 5.68% | 4.84% | 5.90% | 3.22% | **5.13%** |
| **exp-protegido-ms-resenas-1** |7.18% | 6.04% | 4.40% | 6.25% | 3.75% | **5.52%** |
| **exp-protegido-ms-usuarios-1** |6.31% | 6.09% | 5.71% | 5.34% | 2.84% | **5.26%** |
| **exp-protegido-postgres-db-1** |6.25% | 6.70% | 4.03% | 4.69% | 4.79% | **5.29%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |200.5MiB (200.50 MiB)  | 164.6MiB (164.60 MiB)  | 154.9MiB (154.90 MiB)  | 151.8MiB (151.80 MiB)  | 178.5MiB (178.50 MiB)  |
| **exp-protegido-mongo-db-1** |348.6MiB (348.60 MiB)  | 349.8MiB (349.80 MiB)  | 349.6MiB (349.60 MiB)  | 349.8MiB (349.80 MiB)  | 341MiB (341.00 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.9MiB (45.90 MiB)  | 46.57MiB (46.57 MiB)  | 46.13MiB (46.13 MiB)  | 46.57MiB (46.57 MiB)  | 45.82MiB (45.82 MiB)  |
| **exp-protegido-ms-ordenes-1** |47.04MiB (47.04 MiB)  | 45.48MiB (45.48 MiB)  | 46.06MiB (46.06 MiB)  | 46.4MiB (46.40 MiB)  | 45.51MiB (45.51 MiB)  |
| **exp-protegido-ms-resenas-1** |46.71MiB (46.71 MiB)  | 46.07MiB (46.07 MiB)  | 47.66MiB (47.66 MiB)  | 47.85MiB (47.85 MiB)  | 45.9MiB (45.90 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.31MiB (45.31 MiB)  | 46MiB (46.00 MiB)  | 46.45MiB (46.45 MiB)  | 46.4MiB (46.40 MiB)  | 46.2MiB (46.20 MiB)  |
| **exp-protegido-postgres-db-1** |27.95MiB (27.95 MiB)  | 29.46MiB (29.46 MiB)  | 27.92MiB (27.92 MiB)  | 27.95MiB (27.95 MiB)  | 27.99MiB (27.99 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |86.29% | 77.22% | 68.72% | 74.64% | 65.71% | **74.52%** |
| **exp-protegido-mongo-db-1** |36.31% | 31.96% | 17.68% | 23.97% | 17.10% | **25.40%** |
| **exp-protegido-ms-catalogo-1** |1.45% | 0.89% | 0.85% | 0.84% | 0.75% | **0.96%** |
| **exp-protegido-ms-ordenes-1** |1.30% | 1.20% | 1.04% | 1.31% | 0.84% | **1.14%** |
| **exp-protegido-ms-resenas-1** |1.33% | 1.25% | 1.02% | 1.27% | 0.82% | **1.14%** |
| **exp-protegido-ms-usuarios-1** |1.28% | 1.25% | 1.02% | 1.29% | 0.73% | **1.11%** |
| **exp-protegido-postgres-db-1** |1.33% | 1.29% | 1.03% | 0.99% | 1.24% | **1.18%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |148.60 MiB | 128.88 MiB | 125.62 MiB | 125.02 MiB | 132.81 MiB | **132.19 MiB** |
| **exp-protegido-mongo-db-1** |200.00 MiB | 215.23 MiB | 203.40 MiB | 210.63 MiB | 198.46 MiB | **205.54 MiB** |
| **exp-protegido-ms-catalogo-1** |45.77 MiB | 46.46 MiB | 46.03 MiB | 46.46 MiB | 45.71 MiB | **46.09 MiB** |
| **exp-protegido-ms-ordenes-1** |46.53 MiB | 45.38 MiB | 45.81 MiB | 45.68 MiB | 45.41 MiB | **45.76 MiB** |
| **exp-protegido-ms-resenas-1** |45.83 MiB | 45.97 MiB | 46.18 MiB | 46.36 MiB | 45.80 MiB | **46.03 MiB** |
| **exp-protegido-ms-usuarios-1** |44.97 MiB | 45.90 MiB | 45.54 MiB | 46.30 MiB | 46.10 MiB | **45.76 MiB** |
| **exp-protegido-postgres-db-1** |27.81 MiB | 28.02 MiB | 27.92 MiB | 27.94 MiB | 27.98 MiB | **27.93 MiB** |