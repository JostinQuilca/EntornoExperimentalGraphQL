# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 22:18:12

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 60 | 7.467 ms | 0.00% |
| Run 2 | 60 | 6.824 ms | 0.00% |
| Run 3 | 60 | 6.753 ms | 0.00% |
| Run 4 | 60 | 6.504 ms | 0.00% |
| Run 5 | 60 | 6.658 ms | 0.00% |
| **PROMEDIO** | **60.0** | **6.841 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.94% | 1.18% | 1.19% | 2.61% | 2.18% | **1.82%** |
| **exp-protegido-mongo-db-1** |63.46% | 57.22% | 54.07% | 49.22% | 55.05% | **55.80%** |
| **exp-protegido-ms-catalogo-1** |4.57% | 4.14% | 3.36% | 3.64% | 3.58% | **3.86%** |
| **exp-protegido-ms-ordenes-1** |3.59% | 5.12% | 3.48% | 3.91% | 3.88% | **4.00%** |
| **exp-protegido-ms-resenas-1** |3.91% | 4.36% | 3.52% | 4.00% | 4.49% | **4.06%** |
| **exp-protegido-ms-usuarios-1** |3.98% | 4.05% | 3.36% | 3.93% | 4.10% | **3.88%** |
| **exp-protegido-postgres-db-1** |4.33% | 9.14% | 4.24% | 5.42% | 5.16% | **5.66%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |64.05MiB (64.05 MiB)  | 64.98MiB (64.98 MiB)  | 65.77MiB (65.77 MiB)  | 65.26MiB (65.26 MiB)  | 64.88MiB (64.88 MiB)  |
| **exp-protegido-mongo-db-1** |342MiB (342.00 MiB)  | 343.8MiB (343.80 MiB)  | 332.1MiB (332.10 MiB)  | 332.1MiB (332.10 MiB)  | 338.6MiB (338.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.45MiB (45.45 MiB)  | 47.61MiB (47.61 MiB)  | 46.23MiB (46.23 MiB)  | 47.48MiB (47.48 MiB)  | 45.49MiB (45.49 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.45MiB (45.45 MiB)  | 46.45MiB (46.45 MiB)  | 45.97MiB (45.97 MiB)  | 46.82MiB (46.82 MiB)  | 46.24MiB (46.24 MiB)  |
| **exp-protegido-ms-resenas-1** |46.05MiB (46.05 MiB)  | 46.52MiB (46.52 MiB)  | 45.58MiB (45.58 MiB)  | 46.75MiB (46.75 MiB)  | 46.88MiB (46.88 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.33MiB (46.33 MiB)  | 47MiB (47.00 MiB)  | 45.63MiB (45.63 MiB)  | 45.87MiB (45.87 MiB)  | 47.41MiB (47.41 MiB)  |
| **exp-protegido-postgres-db-1** |28MiB (28.00 MiB)  | 29.71MiB (29.71 MiB)  | 29.71MiB (29.71 MiB)  | 29.48MiB (29.48 MiB)  | 29.94MiB (29.94 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.62% | 0.52% | 0.53% | 0.55% | 0.58% | **0.56%** |
| **exp-protegido-mongo-db-1** |18.25% | 16.77% | 15.34% | 15.25% | 16.45% | **16.41%** |
| **exp-protegido-ms-catalogo-1** |1.10% | 1.01% | 1.00% | 1.06% | 1.08% | **1.05%** |
| **exp-protegido-ms-ordenes-1** |1.00% | 0.96% | 0.96% | 0.93% | 0.95% | **0.96%** |
| **exp-protegido-ms-resenas-1** |0.91% | 0.95% | 0.86% | 0.92% | 0.99% | **0.93%** |
| **exp-protegido-ms-usuarios-1** |1.03% | 0.94% | 0.90% | 0.93% | 0.94% | **0.95%** |
| **exp-protegido-postgres-db-1** |1.18% | 1.34% | 1.12% | 1.26% | 1.24% | **1.23%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |63.22 MiB | 64.17 MiB | 64.86 MiB | 64.22 MiB | 64.10 MiB | **64.11 MiB** |
| **exp-protegido-mongo-db-1** |201.87 MiB | 201.74 MiB | 196.17 MiB | 196.42 MiB | 196.22 MiB | **198.48 MiB** |
| **exp-protegido-ms-catalogo-1** |45.17 MiB | 46.85 MiB | 46.12 MiB | 47.18 MiB | 45.39 MiB | **46.14 MiB** |
| **exp-protegido-ms-ordenes-1** |45.32 MiB | 46.14 MiB | 45.65 MiB | 46.46 MiB | 45.95 MiB | **45.90 MiB** |
| **exp-protegido-ms-resenas-1** |45.93 MiB | 46.05 MiB | 45.23 MiB | 46.39 MiB | 46.06 MiB | **45.93 MiB** |
| **exp-protegido-ms-usuarios-1** |46.20 MiB | 46.68 MiB | 45.52 MiB | 45.47 MiB | 47.31 MiB | **46.24 MiB** |
| **exp-protegido-postgres-db-1** |27.81 MiB | 28.04 MiB | 28.00 MiB | 28.03 MiB | 28.09 MiB | **27.99 MiB** |