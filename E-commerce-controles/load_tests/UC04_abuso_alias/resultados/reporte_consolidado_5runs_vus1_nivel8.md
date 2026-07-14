# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 00:12:40

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 572.654 ms | 0.00% | 0.00% |
| Run 2 | 39 | 574.478 ms | 0.00% | 0.00% |
| Run 3 | 39 | 572.069 ms | 0.00% | 0.00% |
| Run 4 | 39 | 569.394 ms | 0.00% | 0.00% |
| Run 5 | 39 | 571.552 ms | 0.00% | 0.00% |
| **PROMEDIO** | **39.0** | **572.029 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |3.54% | 1.05% | 3.46% | 1.01% | 6.57% | **3.13%** |
| **exp-protegido-mongo-db-1** |102.51% | 74.40% | 83.37% | 77.26% | 106.24% | **88.76%** |
| **exp-protegido-ms-catalogo-1** |4.94% | 6.05% | 4.04% | 4.67% | 5.40% | **5.02%** |
| **exp-protegido-ms-ordenes-1** |6.49% | 10.09% | 4.87% | 6.33% | 6.50% | **6.86%** |
| **exp-protegido-ms-resenas-1** |5.37% | 4.71% | 4.28% | 4.61% | 5.54% | **4.90%** |
| **exp-protegido-ms-usuarios-1** |5.88% | 4.60% | 4.35% | 5.26% | 6.83% | **5.38%** |
| **exp-protegido-postgres-db-1** |8.81% | 8.87% | 8.47% | 5.58% | 7.86% | **7.92%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.51MiB (67.51 MiB)  | 66MiB (66.00 MiB)  | 65.9MiB (65.90 MiB)  | 66.14MiB (66.14 MiB)  | 65.79MiB (65.79 MiB)  |
| **exp-protegido-mongo-db-1** |343.5MiB (343.50 MiB)  | 343.5MiB (343.50 MiB)  | 350.5MiB (350.50 MiB)  | 337.2MiB (337.20 MiB)  | 347.1MiB (347.10 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.63MiB (46.63 MiB)  | 46.39MiB (46.39 MiB)  | 46.41MiB (46.41 MiB)  | 46.87MiB (46.87 MiB)  | 45.96MiB (45.96 MiB)  |
| **exp-protegido-ms-ordenes-1** |51.12MiB (51.12 MiB)  | 50.61MiB (50.61 MiB)  | 50.57MiB (50.57 MiB)  | 49.24MiB (49.24 MiB)  | 49.62MiB (49.62 MiB)  |
| **exp-protegido-ms-resenas-1** |46.23MiB (46.23 MiB)  | 48MiB (48.00 MiB)  | 47.43MiB (47.43 MiB)  | 47.48MiB (47.48 MiB)  | 47.11MiB (47.11 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.91MiB (45.91 MiB)  | 48.21MiB (48.21 MiB)  | 46.04MiB (46.04 MiB)  | 45.64MiB (45.64 MiB)  | 55.57MiB (55.57 MiB)  |
| **exp-protegido-postgres-db-1** |37.8MiB (37.80 MiB)  | 39.2MiB (39.20 MiB)  | 37.68MiB (37.68 MiB)  | 37.98MiB (37.98 MiB)  | 38.16MiB (38.16 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.66% | 0.54% | 0.62% | 0.47% | 0.74% | **0.61%** |
| **exp-protegido-mongo-db-1** |24.36% | 20.95% | 23.63% | 20.40% | 24.27% | **22.72%** |
| **exp-protegido-ms-catalogo-1** |1.18% | 1.22% | 1.14% | 1.26% | 1.17% | **1.19%** |
| **exp-protegido-ms-ordenes-1** |2.10% | 2.36% | 1.75% | 1.72% | 1.94% | **1.97%** |
| **exp-protegido-ms-resenas-1** |1.35% | 1.25% | 1.08% | 1.08% | 1.22% | **1.20%** |
| **exp-protegido-ms-usuarios-1** |1.33% | 1.31% | 0.96% | 1.08% | 1.22% | **1.18%** |
| **exp-protegido-postgres-db-1** |2.53% | 2.56% | 2.05% | 2.08% | 2.41% | **2.33%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |66.55 MiB | 65.14 MiB | 64.85 MiB | 65.33 MiB | 64.90 MiB | **65.35 MiB** |
| **exp-protegido-mongo-db-1** |210.05 MiB | 207.13 MiB | 210.42 MiB | 202.16 MiB | 216.35 MiB | **209.22 MiB** |
| **exp-protegido-ms-catalogo-1** |46.24 MiB | 46.30 MiB | 46.30 MiB | 46.77 MiB | 45.84 MiB | **46.29 MiB** |
| **exp-protegido-ms-ordenes-1** |50.07 MiB | 49.31 MiB | 49.25 MiB | 48.49 MiB | 48.80 MiB | **49.18 MiB** |
| **exp-protegido-ms-resenas-1** |46.11 MiB | 46.36 MiB | 45.58 MiB | 46.52 MiB | 45.64 MiB | **46.04 MiB** |
| **exp-protegido-ms-usuarios-1** |45.78 MiB | 46.34 MiB | 45.66 MiB | 45.53 MiB | 54.81 MiB | **47.62 MiB** |
| **exp-protegido-postgres-db-1** |37.27 MiB | 37.32 MiB | 37.31 MiB | 37.38 MiB | 37.32 MiB | **37.32 MiB** |