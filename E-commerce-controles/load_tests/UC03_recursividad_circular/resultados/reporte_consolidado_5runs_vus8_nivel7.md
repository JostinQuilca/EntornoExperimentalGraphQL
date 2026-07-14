# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 22:25:31

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 481 | 8.161 ms | 0.00% | 100.00% |
| Run 2 | 481 | 8.517 ms | 0.00% | 100.00% |
| Run 3 | 481 | 7.054 ms | 0.00% | 100.00% |
| Run 4 | 481 | 7.886 ms | 0.00% | 100.00% |
| Run 5 | 481 | 9.759 ms | 0.00% | 100.00% |
| **PROMEDIO** | **481.0** | **8.275 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |36.37% | 30.23% | 11.76% | 27.38% | 27.81% | **26.71%** |
| **exp-protegido-mongo-db-1** |104.82% | 130.31% | 84.44% | 93.51% | 138.51% | **110.32%** |
| **exp-protegido-ms-catalogo-1** |6.96% | 5.79% | 4.76% | 4.46% | 5.53% | **5.50%** |
| **exp-protegido-ms-ordenes-1** |5.60% | 5.83% | 5.08% | 5.19% | 5.59% | **5.46%** |
| **exp-protegido-ms-resenas-1** |8.70% | 7.14% | 3.96% | 4.86% | 5.18% | **5.97%** |
| **exp-protegido-ms-usuarios-1** |5.42% | 36.12% | 37.00% | 40.95% | 29.19% | **29.74%** |
| **exp-protegido-postgres-db-1** |6.89% | 5.79% | 5.72% | 5.62% | 5.28% | **5.86%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |103.7MiB (103.70 MiB)  | 82.59MiB (82.59 MiB)  | 83.85MiB (83.85 MiB)  | 83.21MiB (83.21 MiB)  | 84.3MiB (84.30 MiB)  |
| **exp-protegido-mongo-db-1** |342.2MiB (342.20 MiB)  | 340.9MiB (340.90 MiB)  | 349.4MiB (349.40 MiB)  | 351.8MiB (351.80 MiB)  | 350.4MiB (350.40 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.66MiB (45.66 MiB)  | 50.45MiB (50.45 MiB)  | 47.7MiB (47.70 MiB)  | 47.05MiB (47.05 MiB)  | 45.97MiB (45.97 MiB)  |
| **exp-protegido-ms-ordenes-1** |48.82MiB (48.82 MiB)  | 48.42MiB (48.42 MiB)  | 48.87MiB (48.87 MiB)  | 46MiB (46.00 MiB)  | 47.45MiB (47.45 MiB)  |
| **exp-protegido-ms-resenas-1** |45.96MiB (45.96 MiB)  | 48.2MiB (48.20 MiB)  | 46.74MiB (46.74 MiB)  | 46.05MiB (46.05 MiB)  | 46.62MiB (46.62 MiB)  |
| **exp-protegido-ms-usuarios-1** |73.67MiB (73.67 MiB)  | 69.46MiB (69.46 MiB)  | 71.62MiB (71.62 MiB)  | 67MiB (67.00 MiB)  | 66.07MiB (66.07 MiB)  |
| **exp-protegido-postgres-db-1** |30.2MiB (30.20 MiB)  | 31.52MiB (31.52 MiB)  | 30.23MiB (30.23 MiB)  | 30.2MiB (30.20 MiB)  | 30.24MiB (30.24 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |5.58% | 5.30% | 3.68% | 4.85% | 5.52% | **4.99%** |
| **exp-protegido-mongo-db-1** |23.46% | 30.74% | 20.73% | 23.82% | 28.49% | **25.45%** |
| **exp-protegido-ms-catalogo-1** |1.62% | 1.36% | 1.14% | 1.12% | 1.30% | **1.31%** |
| **exp-protegido-ms-ordenes-1** |1.39% | 1.46% | 1.11% | 1.23% | 1.40% | **1.32%** |
| **exp-protegido-ms-resenas-1** |1.53% | 1.44% | 1.09% | 1.23% | 1.54% | **1.37%** |
| **exp-protegido-ms-usuarios-1** |1.47% | 3.03% | 2.33% | 2.37% | 2.38% | **2.32%** |
| **exp-protegido-postgres-db-1** |1.76% | 1.75% | 1.49% | 1.50% | 1.84% | **1.67%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |79.77 MiB | 78.26 MiB | 78.63 MiB | 77.60 MiB | 77.86 MiB | **78.42 MiB** |
| **exp-protegido-mongo-db-1** |220.64 MiB | 213.83 MiB | 202.66 MiB | 219.01 MiB | 234.43 MiB | **218.11 MiB** |
| **exp-protegido-ms-catalogo-1** |45.54 MiB | 47.93 MiB | 46.11 MiB | 46.23 MiB | 45.87 MiB | **46.34 MiB** |
| **exp-protegido-ms-ordenes-1** |47.04 MiB | 46.56 MiB | 47.00 MiB | 45.89 MiB | 47.35 MiB | **46.77 MiB** |
| **exp-protegido-ms-resenas-1** |45.83 MiB | 45.83 MiB | 46.64 MiB | 45.96 MiB | 46.53 MiB | **46.16 MiB** |
| **exp-protegido-ms-usuarios-1** |71.33 MiB | 62.92 MiB | 70.21 MiB | 66.77 MiB | 66.04 MiB | **67.45 MiB** |
| **exp-protegido-postgres-db-1** |30.08 MiB | 30.25 MiB | 30.22 MiB | 30.07 MiB | 30.21 MiB | **30.17 MiB** |