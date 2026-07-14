# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-10 23:52:33

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 571.090 ms | 0.00% | 0.00% |
| Run 2 | 39 | 570.019 ms | 0.00% | 0.00% |
| Run 3 | 38 | 580.115 ms | 0.00% | 0.00% |
| Run 4 | 39 | 575.161 ms | 0.00% | 0.00% |
| Run 5 | 39 | 571.099 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.8** | **573.497 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |3.21% | 4.95% | 6.23% | 3.62% | 5.32% | **4.67%** |
| **exp-protegido-mongo-db-1** |128.78% | 119.14% | 106.70% | 97.42% | 90.55% | **108.52%** |
| **exp-protegido-ms-catalogo-1** |4.57% | 3.56% | 9.62% | 4.67% | 3.55% | **5.19%** |
| **exp-protegido-ms-ordenes-1** |7.55% | 6.17% | 12.32% | 7.78% | 7.19% | **8.20%** |
| **exp-protegido-ms-resenas-1** |5.12% | 6.33% | 9.82% | 4.47% | 6.33% | **6.41%** |
| **exp-protegido-ms-usuarios-1** |12.39% | 4.80% | 9.56% | 6.53% | 14.93% | **9.64%** |
| **exp-protegido-postgres-db-1** |19.01% | 6.86% | 7.25% | 8.52% | 7.10% | **9.75%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.5MiB (65.50 MiB)  | 66.2MiB (66.20 MiB)  | 66.21MiB (66.21 MiB)  | 66.32MiB (66.32 MiB)  | 65.59MiB (65.59 MiB)  |
| **exp-protegido-mongo-db-1** |345.5MiB (345.50 MiB)  | 347.8MiB (347.80 MiB)  | 346.2MiB (346.20 MiB)  | 343.3MiB (343.30 MiB)  | 345.3MiB (345.30 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.95MiB (45.95 MiB)  | 46.77MiB (46.77 MiB)  | 46.3MiB (46.30 MiB)  | 47.15MiB (47.15 MiB)  | 47MiB (47.00 MiB)  |
| **exp-protegido-ms-ordenes-1** |49.33MiB (49.33 MiB)  | 49.85MiB (49.85 MiB)  | 49.85MiB (49.85 MiB)  | 50.9MiB (50.90 MiB)  | 51.88MiB (51.88 MiB)  |
| **exp-protegido-ms-resenas-1** |45.87MiB (45.87 MiB)  | 48.3MiB (48.30 MiB)  | 54.64MiB (54.64 MiB)  | 54.96MiB (54.96 MiB)  | 48.99MiB (48.99 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.85MiB (45.85 MiB)  | 47.47MiB (47.47 MiB)  | 46.39MiB (46.39 MiB)  | 48.64MiB (48.64 MiB)  | 47.51MiB (47.51 MiB)  |
| **exp-protegido-postgres-db-1** |37.7MiB (37.70 MiB)  | 37.64MiB (37.64 MiB)  | 38.55MiB (38.55 MiB)  | 37.65MiB (37.65 MiB)  | 37.7MiB (37.70 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.70% | 0.66% | 0.89% | 0.77% | 0.73% | **0.75%** |
| **exp-protegido-mongo-db-1** |29.74% | 25.34% | 23.25% | 26.56% | 19.60% | **24.90%** |
| **exp-protegido-ms-catalogo-1** |1.17% | 1.16% | 1.36% | 0.98% | 1.04% | **1.14%** |
| **exp-protegido-ms-ordenes-1** |2.13% | 1.83% | 2.29% | 2.08% | 2.06% | **2.08%** |
| **exp-protegido-ms-resenas-1** |1.13% | 1.22% | 1.72% | 1.07% | 1.37% | **1.30%** |
| **exp-protegido-ms-usuarios-1** |1.82% | 1.12% | 2.03% | 1.37% | 1.52% | **1.57%** |
| **exp-protegido-postgres-db-1** |2.61% | 2.04% | 2.19% | 2.16% | 1.87% | **2.17%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |64.78 MiB | 65.32 MiB | 65.27 MiB | 65.38 MiB | 64.65 MiB | **65.08 MiB** |
| **exp-protegido-mongo-db-1** |209.83 MiB | 206.65 MiB | 207.79 MiB | 210.28 MiB | 206.90 MiB | **208.29 MiB** |
| **exp-protegido-ms-catalogo-1** |45.82 MiB | 46.66 MiB | 46.17 MiB | 45.72 MiB | 46.89 MiB | **46.25 MiB** |
| **exp-protegido-ms-ordenes-1** |48.40 MiB | 49.12 MiB | 48.98 MiB | 48.81 MiB | 48.72 MiB | **48.81 MiB** |
| **exp-protegido-ms-resenas-1** |45.75 MiB | 46.85 MiB | 54.29 MiB | 54.66 MiB | 47.35 MiB | **49.78 MiB** |
| **exp-protegido-ms-usuarios-1** |45.71 MiB | 45.95 MiB | 46.28 MiB | 47.26 MiB | 46.10 MiB | **46.26 MiB** |
| **exp-protegido-postgres-db-1** |37.27 MiB | 37.32 MiB | 37.31 MiB | 37.27 MiB | 37.33 MiB | **37.30 MiB** |