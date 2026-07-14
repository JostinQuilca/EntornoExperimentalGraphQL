# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 03:33:30

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 44 | 371.001 ms | 0.00% | 0.00% |
| Run 2 | 46 | 305.012 ms | 0.00% | 0.00% |
| Run 3 | 47 | 286.838 ms | 0.00% | 0.00% |
| Run 4 | 46 | 324.836 ms | 0.00% | 0.00% |
| Run 5 | 45 | 327.944 ms | 0.00% | 0.00% |
| **PROMEDIO** | **45.6** | **323.126 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |38.77% | 27.72% | 25.37% | 27.39% | 26.58% | **29.17%** |
| **exp-protegido-mongo-db-1** |94.77% | 96.45% | 91.06% | 99.05% | 100.47% | **96.36%** |
| **exp-protegido-ms-catalogo-1** |5.43% | 5.41% | 4.24% | 4.10% | 5.60% | **4.96%** |
| **exp-protegido-ms-ordenes-1** |6.16% | 4.43% | 4.88% | 5.41% | 4.27% | **5.03%** |
| **exp-protegido-ms-resenas-1** |5.53% | 4.61% | 4.71% | 4.88% | 4.99% | **4.94%** |
| **exp-protegido-ms-usuarios-1** |46.99% | 33.26% | 49.62% | 37.34% | 48.27% | **43.10%** |
| **exp-protegido-postgres-db-1** |9.21% | 6.13% | 5.64% | 5.44% | 7.57% | **6.80%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |176.6MiB (176.60 MiB)  | 110.1MiB (110.10 MiB)  | 106.9MiB (106.90 MiB)  | 107.5MiB (107.50 MiB)  | 106.6MiB (106.60 MiB)  |
| **exp-protegido-mongo-db-1** |342.5MiB (342.50 MiB)  | 348.1MiB (348.10 MiB)  | 335.1MiB (335.10 MiB)  | 350.5MiB (350.50 MiB)  | 348.9MiB (348.90 MiB)  |
| **exp-protegido-ms-catalogo-1** |47.26MiB (47.26 MiB)  | 45.61MiB (45.61 MiB)  | 46.94MiB (46.94 MiB)  | 47.39MiB (47.39 MiB)  | 46.64MiB (46.64 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.22MiB (46.22 MiB)  | 46.29MiB (46.29 MiB)  | 47.38MiB (47.38 MiB)  | 47.2MiB (47.20 MiB)  | 45.27MiB (45.27 MiB)  |
| **exp-protegido-ms-resenas-1** |46.51MiB (46.51 MiB)  | 46.24MiB (46.24 MiB)  | 55.1MiB (55.10 MiB)  | 45.93MiB (45.93 MiB)  | 47.02MiB (47.02 MiB)  |
| **exp-protegido-ms-usuarios-1** |125.9MiB (125.90 MiB)  | 126.8MiB (126.80 MiB)  | 132.7MiB (132.70 MiB)  | 128.7MiB (128.70 MiB)  | 136MiB (136.00 MiB)  |
| **exp-protegido-postgres-db-1** |30.27MiB (30.27 MiB)  | 30.3MiB (30.30 MiB)  | 30.73MiB (30.73 MiB)  | 30.78MiB (30.78 MiB)  | 30.21MiB (30.21 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |12.16% | 13.50% | 12.72% | 12.88% | 13.38% | **12.93%** |
| **exp-protegido-mongo-db-1** |37.42% | 26.33% | 20.56% | 25.49% | 24.79% | **26.92%** |
| **exp-protegido-ms-catalogo-1** |1.48% | 1.28% | 1.17% | 1.23% | 1.21% | **1.27%** |
| **exp-protegido-ms-ordenes-1** |1.51% | 1.30% | 1.34% | 1.17% | 1.19% | **1.30%** |
| **exp-protegido-ms-resenas-1** |1.37% | 1.38% | 1.32% | 1.27% | 1.27% | **1.32%** |
| **exp-protegido-ms-usuarios-1** |20.17% | 18.38% | 17.76% | 20.75% | 20.87% | **19.59%** |
| **exp-protegido-postgres-db-1** |2.42% | 2.06% | 1.73% | 2.09% | 2.27% | **2.11%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |124.66 MiB | 101.49 MiB | 99.96 MiB | 100.98 MiB | 101.76 MiB | **105.77 MiB** |
| **exp-protegido-mongo-db-1** |195.05 MiB | 216.03 MiB | 202.12 MiB | 212.53 MiB | 207.63 MiB | **206.67 MiB** |
| **exp-protegido-ms-catalogo-1** |47.14 MiB | 45.51 MiB | 46.84 MiB | 47.30 MiB | 46.55 MiB | **46.67 MiB** |
| **exp-protegido-ms-ordenes-1** |46.10 MiB | 46.19 MiB | 45.88 MiB | 46.30 MiB | 45.17 MiB | **45.93 MiB** |
| **exp-protegido-ms-resenas-1** |46.39 MiB | 46.14 MiB | 53.24 MiB | 45.84 MiB | 46.35 MiB | **47.59 MiB** |
| **exp-protegido-ms-usuarios-1** |116.34 MiB | 117.16 MiB | 119.65 MiB | 119.31 MiB | 120.55 MiB | **118.60 MiB** |
| **exp-protegido-postgres-db-1** |30.18 MiB | 30.28 MiB | 30.15 MiB | 30.09 MiB | 30.20 MiB | **30.18 MiB** |