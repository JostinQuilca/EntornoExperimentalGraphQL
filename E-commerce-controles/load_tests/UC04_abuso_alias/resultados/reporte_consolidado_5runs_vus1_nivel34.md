# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 01:12:20

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 38 | 605.378 ms | 0.00% | 0.00% |
| Run 2 | 38 | 594.994 ms | 0.00% | 0.00% |
| Run 3 | 38 | 592.656 ms | 0.00% | 0.00% |
| Run 4 | 38 | 593.119 ms | 0.00% | 0.00% |
| Run 5 | 38 | 591.694 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.0** | **595.568 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |18.55% | 6.14% | 7.57% | 7.96% | 4.23% | **8.89%** |
| **exp-protegido-mongo-db-1** |108.71% | 80.59% | 82.42% | 110.61% | 79.28% | **92.32%** |
| **exp-protegido-ms-catalogo-1** |4.96% | 4.45% | 4.32% | 3.76% | 4.87% | **4.47%** |
| **exp-protegido-ms-ordenes-1** |24.33% | 8.07% | 8.37% | 8.55% | 9.50% | **11.76%** |
| **exp-protegido-ms-resenas-1** |12.52% | 5.13% | 5.25% | 5.23% | 5.11% | **6.65%** |
| **exp-protegido-ms-usuarios-1** |23.84% | 5.04% | 5.39% | 3.60% | 5.22% | **8.62%** |
| **exp-protegido-postgres-db-1** |16.32% | 12.62% | 13.16% | 13.11% | 12.79% | **13.60%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |97.41MiB (97.41 MiB)  | 66.63MiB (66.63 MiB)  | 66.6MiB (66.60 MiB)  | 66.89MiB (66.89 MiB)  | 66.85MiB (66.85 MiB)  |
| **exp-protegido-mongo-db-1** |341.7MiB (341.70 MiB)  | 349.2MiB (349.20 MiB)  | 349.7MiB (349.70 MiB)  | 350.4MiB (350.40 MiB)  | 338.2MiB (338.20 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.4MiB (46.40 MiB)  | 46.66MiB (46.66 MiB)  | 48.5MiB (48.50 MiB)  | 48.83MiB (48.83 MiB)  | 46.32MiB (46.32 MiB)  |
| **exp-protegido-ms-ordenes-1** |54.67MiB (54.67 MiB)  | 54.66MiB (54.66 MiB)  | 53.21MiB (53.21 MiB)  | 55.59MiB (55.59 MiB)  | 54.06MiB (54.06 MiB)  |
| **exp-protegido-ms-resenas-1** |46.32MiB (46.32 MiB)  | 47.09MiB (47.09 MiB)  | 54.96MiB (54.96 MiB)  | 48.59MiB (48.59 MiB)  | 46.46MiB (46.46 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.43MiB (46.43 MiB)  | 45.93MiB (45.93 MiB)  | 47.15MiB (47.15 MiB)  | 46.13MiB (46.13 MiB)  | 46.25MiB (46.25 MiB)  |
| **exp-protegido-postgres-db-1** |38.17MiB (38.17 MiB)  | 37.84MiB (37.84 MiB)  | 37.8MiB (37.80 MiB)  | 37.75MiB (37.75 MiB)  | 39.21MiB (39.21 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.90% | 1.13% | 1.01% | 1.02% | 0.90% | **1.19%** |
| **exp-protegido-mongo-db-1** |30.77% | 22.04% | 20.04% | 21.83% | 19.76% | **22.89%** |
| **exp-protegido-ms-catalogo-1** |1.30% | 1.22% | 1.00% | 1.06% | 1.12% | **1.14%** |
| **exp-protegido-ms-ordenes-1** |4.87% | 3.93% | 3.23% | 3.87% | 2.89% | **3.76%** |
| **exp-protegido-ms-resenas-1** |1.48% | 1.42% | 1.36% | 1.20% | 1.20% | **1.33%** |
| **exp-protegido-ms-usuarios-1** |1.94% | 1.41% | 1.31% | 1.05% | 1.16% | **1.37%** |
| **exp-protegido-postgres-db-1** |7.20% | 5.98% | 5.92% | 6.34% | 5.32% | **6.15%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |68.31 MiB | 65.60 MiB | 65.25 MiB | 65.59 MiB | 65.73 MiB | **66.10 MiB** |
| **exp-protegido-mongo-db-1** |211.57 MiB | 206.91 MiB | 208.66 MiB | 207.46 MiB | 205.62 MiB | **208.04 MiB** |
| **exp-protegido-ms-catalogo-1** |46.27 MiB | 46.57 MiB | 48.03 MiB | 47.19 MiB | 46.22 MiB | **46.86 MiB** |
| **exp-protegido-ms-ordenes-1** |51.24 MiB | 51.81 MiB | 51.35 MiB | 52.38 MiB | 51.65 MiB | **51.69 MiB** |
| **exp-protegido-ms-resenas-1** |46.20 MiB | 47.00 MiB | 53.33 MiB | 46.55 MiB | 46.36 MiB | **47.89 MiB** |
| **exp-protegido-ms-usuarios-1** |46.30 MiB | 45.83 MiB | 46.10 MiB | 46.03 MiB | 46.15 MiB | **46.08 MiB** |
| **exp-protegido-postgres-db-1** |37.18 MiB | 37.30 MiB | 37.40 MiB | 37.36 MiB | 37.41 MiB | **37.33 MiB** |