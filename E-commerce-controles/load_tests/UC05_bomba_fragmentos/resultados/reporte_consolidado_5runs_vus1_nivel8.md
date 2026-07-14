# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 04:33:28

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 46 | 301.559 ms | 0.00% | 0.00% |
| Run 2 | 46 | 300.695 ms | 0.00% | 0.00% |
| Run 3 | 47 | 296.550 ms | 0.00% | 0.00% |
| Run 4 | 46 | 300.322 ms | 0.00% | 0.00% |
| Run 5 | 46 | 315.589 ms | 0.00% | 0.00% |
| **PROMEDIO** | **46.2** | **302.943 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |28.82% | 25.94% | 25.53% | 25.90% | 37.31% | **28.70%** |
| **exp-protegido-mongo-db-1** |76.91% | 74.84% | 71.70% | 114.32% | 75.14% | **82.58%** |
| **exp-protegido-ms-catalogo-1** |3.62% | 3.47% | 4.01% | 3.46% | 4.05% | **3.72%** |
| **exp-protegido-ms-ordenes-1** |4.57% | 4.74% | 4.79% | 4.25% | 4.82% | **4.63%** |
| **exp-protegido-ms-resenas-1** |4.46% | 4.77% | 4.82% | 4.46% | 4.32% | **4.57%** |
| **exp-protegido-ms-usuarios-1** |35.12% | 35.42% | 32.23% | 42.95% | 44.72% | **38.09%** |
| **exp-protegido-postgres-db-1** |5.74% | 6.90% | 5.82% | 6.58% | 6.38% | **6.28%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |108.8MiB (108.80 MiB)  | 106.9MiB (106.90 MiB)  | 107MiB (107.00 MiB)  | 107.5MiB (107.50 MiB)  | 110.4MiB (110.40 MiB)  |
| **exp-protegido-mongo-db-1** |349.3MiB (349.30 MiB)  | 348.6MiB (348.60 MiB)  | 343.1MiB (343.10 MiB)  | 340.9MiB (340.90 MiB)  | 340.6MiB (340.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.96MiB (46.96 MiB)  | 45.12MiB (45.12 MiB)  | 46.65MiB (46.65 MiB)  | 45.42MiB (45.42 MiB)  | 45.91MiB (45.91 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.84MiB (46.84 MiB)  | 45.8MiB (45.80 MiB)  | 46MiB (46.00 MiB)  | 45.29MiB (45.29 MiB)  | 45.93MiB (45.93 MiB)  |
| **exp-protegido-ms-resenas-1** |45.16MiB (45.16 MiB)  | 45.99MiB (45.99 MiB)  | 46.8MiB (46.80 MiB)  | 45.78MiB (45.78 MiB)  | 45.68MiB (45.68 MiB)  |
| **exp-protegido-ms-usuarios-1** |133.1MiB (133.10 MiB)  | 129.4MiB (129.40 MiB)  | 126.5MiB (126.50 MiB)  | 131.2MiB (131.20 MiB)  | 135.1MiB (135.10 MiB)  |
| **exp-protegido-postgres-db-1** |32.23MiB (32.23 MiB)  | 30.16MiB (30.16 MiB)  | 30.34MiB (30.34 MiB)  | 30.76MiB (30.76 MiB)  | 31.07MiB (31.07 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |12.72% | 13.14% | 12.72% | 13.10% | 15.24% | **13.38%** |
| **exp-protegido-mongo-db-1** |20.13% | 21.70% | 18.03% | 26.21% | 20.26% | **21.27%** |
| **exp-protegido-ms-catalogo-1** |1.18% | 0.95% | 1.16% | 1.00% | 1.02% | **1.06%** |
| **exp-protegido-ms-ordenes-1** |1.14% | 1.13% | 1.15% | 1.10% | 1.10% | **1.12%** |
| **exp-protegido-ms-resenas-1** |1.14% | 1.16% | 1.05% | 1.12% | 1.03% | **1.10%** |
| **exp-protegido-ms-usuarios-1** |17.57% | 17.44% | 16.65% | 17.92% | 18.66% | **17.65%** |
| **exp-protegido-postgres-db-1** |1.97% | 1.81% | 1.80% | 1.87% | 1.87% | **1.86%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |101.19 MiB | 101.89 MiB | 101.97 MiB | 101.58 MiB | 102.26 MiB | **101.78 MiB** |
| **exp-protegido-mongo-db-1** |207.59 MiB | 199.87 MiB | 208.56 MiB | 201.33 MiB | 205.28 MiB | **204.53 MiB** |
| **exp-protegido-ms-catalogo-1** |45.27 MiB | 45.03 MiB | 46.56 MiB | 45.32 MiB | 45.81 MiB | **45.60 MiB** |
| **exp-protegido-ms-ordenes-1** |46.72 MiB | 45.71 MiB | 45.91 MiB | 45.19 MiB | 45.85 MiB | **45.88 MiB** |
| **exp-protegido-ms-resenas-1** |45.02 MiB | 45.90 MiB | 46.68 MiB | 45.68 MiB | 45.54 MiB | **45.76 MiB** |
| **exp-protegido-ms-usuarios-1** |117.07 MiB | 117.00 MiB | 116.27 MiB | 118.30 MiB | 126.18 MiB | **118.96 MiB** |
| **exp-protegido-postgres-db-1** |30.18 MiB | 30.03 MiB | 30.08 MiB | 30.16 MiB | 30.24 MiB | **30.14 MiB** |