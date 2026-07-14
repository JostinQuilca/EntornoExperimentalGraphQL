# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 14:05:22

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 12 | 10138.830 ms | 0.00% | 0.00% |
| Run 2 | 12 | 9987.103 ms | 0.00% | 0.00% |
| Run 3 | 12 | 9547.938 ms | 0.00% | 0.00% |
| Run 4 | 12 | 8902.155 ms | 0.00% | 0.00% |
| Run 5 | 14 | 8939.516 ms | 0.00% | 0.00% |
| **PROMEDIO** | **12.4** | **9503.108 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |152.78% | 143.74% | 156.74% | 146.16% | 151.01% | **150.09%** |
| **exp-vulnerable-mongo-db-1** |106.91% | 114.18% | 105.86% | 88.48% | 98.45% | **102.78%** |
| **exp-vulnerable-ms-catalogo-1** |4.85% | 4.60% | 5.21% | 4.44% | 4.84% | **4.79%** |
| **exp-vulnerable-ms-ordenes-1** |5.36% | 5.80% | 5.85% | 4.55% | 6.11% | **5.53%** |
| **exp-vulnerable-ms-resenas-1** |196.00% | 201.29% | 189.12% | 176.03% | 177.23% | **187.93%** |
| **exp-vulnerable-ms-usuarios-1** |261.95% | 229.02% | 236.62% | 258.66% | 232.30% | **243.71%** |
| **exp-vulnerable-postgres-db-1** |29.14% | 11.56% | 36.87% | 14.53% | 28.96% | **24.21%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |665.1MiB (665.10 MiB)  | 671MiB (671.00 MiB)  | 676.8MiB (676.80 MiB)  | 674.1MiB (674.10 MiB)  | 714.2MiB (714.20 MiB)  |
| **exp-vulnerable-mongo-db-1** |348MiB (348.00 MiB)  | 328.5MiB (328.50 MiB)  | 351.1MiB (351.10 MiB)  | 352MiB (352.00 MiB)  | 343.1MiB (343.10 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |50.62MiB (50.62 MiB)  | 54.63MiB (54.63 MiB)  | 67.83MiB (67.83 MiB)  | 59.67MiB (59.67 MiB)  | 46.81MiB (46.81 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |53.22MiB (53.22 MiB)  | 54.07MiB (54.07 MiB)  | 59.77MiB (59.77 MiB)  | 61.1MiB (61.10 MiB)  | 46.11MiB (46.11 MiB)  |
| **exp-vulnerable-ms-resenas-1** |939.1MiB (939.10 MiB)  | 860.6MiB (860.60 MiB)  | 971.3MiB (971.30 MiB)  | 995.2MiB (995.20 MiB)  | 1024MiB (1024.00 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |1.151GiB (1178.62 MiB)  | 1.253GiB (1283.07 MiB)  | 1.253GiB (1283.07 MiB)  | 987.7MiB (987.70 MiB)  | 1.245GiB (1274.88 MiB)  |
| **exp-vulnerable-postgres-db-1** |68.32MiB (68.32 MiB)  | 74.42MiB (74.42 MiB)  | 75.62MiB (75.62 MiB)  | 72.64MiB (72.64 MiB)  | 68.67MiB (68.67 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |40.16% | 41.01% | 46.43% | 41.23% | 45.04% | **42.77%** |
| **exp-vulnerable-mongo-db-1** |23.52% | 29.65% | 34.85% | 22.33% | 24.43% | **26.96%** |
| **exp-vulnerable-ms-catalogo-1** |1.26% | 1.22% | 1.22% | 1.11% | 1.16% | **1.19%** |
| **exp-vulnerable-ms-ordenes-1** |1.38% | 1.55% | 1.35% | 1.34% | 1.40% | **1.40%** |
| **exp-vulnerable-ms-resenas-1** |47.66% | 44.88% | 47.44% | 40.43% | 46.57% | **45.40%** |
| **exp-vulnerable-ms-usuarios-1** |33.53% | 32.64% | 36.43% | 40.51% | 36.45% | **35.91%** |
| **exp-vulnerable-postgres-db-1** |3.94% | 2.41% | 5.96% | 2.44% | 4.65% | **3.88%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |356.17 MiB | 417.95 MiB | 379.73 MiB | 400.94 MiB | 394.43 MiB | **389.84 MiB** |
| **exp-vulnerable-mongo-db-1** |207.04 MiB | 198.12 MiB | 201.82 MiB | 206.04 MiB | 214.71 MiB | **205.55 MiB** |
| **exp-vulnerable-ms-catalogo-1** |48.65 MiB | 53.68 MiB | 65.30 MiB | 59.55 MiB | 46.66 MiB | **54.77 MiB** |
| **exp-vulnerable-ms-ordenes-1** |49.60 MiB | 53.06 MiB | 59.26 MiB | 60.91 MiB | 46.00 MiB | **53.77 MiB** |
| **exp-vulnerable-ms-resenas-1** |670.55 MiB | 717.90 MiB | 725.00 MiB | 670.97 MiB | 778.59 MiB | **712.60 MiB** |
| **exp-vulnerable-ms-usuarios-1** |610.19 MiB | 637.94 MiB | 746.99 MiB | 656.56 MiB | 738.28 MiB | **677.99 MiB** |
| **exp-vulnerable-postgres-db-1** |66.83 MiB | 70.72 MiB | 74.59 MiB | 70.19 MiB | 66.19 MiB | **69.70 MiB** |