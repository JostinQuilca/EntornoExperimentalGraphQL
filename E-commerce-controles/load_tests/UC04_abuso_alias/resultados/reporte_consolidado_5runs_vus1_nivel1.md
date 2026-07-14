# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-10 22:46:01

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 572.076 ms | 0.00% | 0.00% |
| Run 2 | 39 | 571.682 ms | 0.00% | 0.00% |
| Run 3 | 39 | 571.019 ms | 0.00% | 0.00% |
| Run 4 | 39 | 571.147 ms | 0.00% | 0.00% |
| Run 5 | 39 | 566.453 ms | 0.00% | 0.00% |
| **PROMEDIO** | **39.0** | **570.475 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |12.64% | 2.84% | 0.85% | 3.35% | 4.10% | **4.76%** |
| **exp-protegido-mongo-db-1** |117.27% | 101.22% | 128.99% | 131.96% | 92.48% | **114.38%** |
| **exp-protegido-ms-catalogo-1** |14.94% | 4.05% | 7.65% | 5.44% | 4.65% | **7.35%** |
| **exp-protegido-ms-ordenes-1** |6.99% | 4.52% | 7.88% | 5.28% | 5.10% | **5.95%** |
| **exp-protegido-ms-resenas-1** |5.14% | 5.86% | 9.05% | 26.77% | 4.73% | **10.31%** |
| **exp-protegido-ms-usuarios-1** |5.55% | 4.64% | 7.13% | 18.32% | 5.94% | **8.32%** |
| **exp-protegido-postgres-db-1** |11.82% | 5.86% | 6.71% | 8.88% | 6.22% | **7.90%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |96.52MiB (96.52 MiB)  | 66.19MiB (66.19 MiB)  | 65.38MiB (65.38 MiB)  | 65.13MiB (65.13 MiB)  | 66.03MiB (66.03 MiB)  |
| **exp-protegido-mongo-db-1** |348.9MiB (348.90 MiB)  | 335.3MiB (335.30 MiB)  | 336.4MiB (336.40 MiB)  | 347.7MiB (347.70 MiB)  | 348.5MiB (348.50 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.11MiB (46.11 MiB)  | 47.21MiB (47.21 MiB)  | 46.86MiB (46.86 MiB)  | 45.86MiB (45.86 MiB)  | 45.88MiB (45.88 MiB)  |
| **exp-protegido-ms-ordenes-1** |50.22MiB (50.22 MiB)  | 49.87MiB (49.87 MiB)  | 48.68MiB (48.68 MiB)  | 48.4MiB (48.40 MiB)  | 50.3MiB (50.30 MiB)  |
| **exp-protegido-ms-resenas-1** |46.24MiB (46.24 MiB)  | 47.25MiB (47.25 MiB)  | 46.43MiB (46.43 MiB)  | 46.6MiB (46.60 MiB)  | 48.96MiB (48.96 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.91MiB (45.91 MiB)  | 46.23MiB (46.23 MiB)  | 46.57MiB (46.57 MiB)  | 47.66MiB (47.66 MiB)  | 45.93MiB (45.93 MiB)  |
| **exp-protegido-postgres-db-1** |30.96MiB (30.96 MiB)  | 30.93MiB (30.93 MiB)  | 31.3MiB (31.30 MiB)  | 30.9MiB (30.90 MiB)  | 31.98MiB (31.98 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.12% | 0.59% | 0.46% | 0.62% | 0.64% | **0.69%** |
| **exp-protegido-mongo-db-1** |25.57% | 24.63% | 23.97% | 40.24% | 23.39% | **27.56%** |
| **exp-protegido-ms-catalogo-1** |2.30% | 1.14% | 1.53% | 1.32% | 1.20% | **1.50%** |
| **exp-protegido-ms-ordenes-1** |1.86% | 1.71% | 2.02% | 1.64% | 1.70% | **1.79%** |
| **exp-protegido-ms-resenas-1** |1.29% | 1.31% | 1.75% | 2.20% | 1.11% | **1.53%** |
| **exp-protegido-ms-usuarios-1** |1.23% | 1.16% | 1.63% | 1.89% | 1.27% | **1.44%** |
| **exp-protegido-postgres-db-1** |2.42% | 1.77% | 1.84% | 2.26% | 1.64% | **1.99%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |66.80 MiB | 65.30 MiB | 64.50 MiB | 64.32 MiB | 65.02 MiB | **65.19 MiB** |
| **exp-protegido-mongo-db-1** |238.72 MiB | 203.74 MiB | 209.63 MiB | 229.64 MiB | 203.76 MiB | **217.10 MiB** |
| **exp-protegido-ms-catalogo-1** |45.98 MiB | 45.71 MiB | 46.75 MiB | 45.75 MiB | 45.78 MiB | **45.99 MiB** |
| **exp-protegido-ms-ordenes-1** |49.52 MiB | 48.08 MiB | 47.96 MiB | 47.71 MiB | 48.35 MiB | **48.32 MiB** |
| **exp-protegido-ms-resenas-1** |46.11 MiB | 46.41 MiB | 46.32 MiB | 45.85 MiB | 47.90 MiB | **46.52 MiB** |
| **exp-protegido-ms-usuarios-1** |45.78 MiB | 46.13 MiB | 46.46 MiB | 47.34 MiB | 45.84 MiB | **46.31 MiB** |
| **exp-protegido-postgres-db-1** |30.78 MiB | 30.77 MiB | 30.82 MiB | 30.76 MiB | 30.89 MiB | **30.80 MiB** |