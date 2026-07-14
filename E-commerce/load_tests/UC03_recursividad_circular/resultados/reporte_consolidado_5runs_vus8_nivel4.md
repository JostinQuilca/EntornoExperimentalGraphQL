# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 21:08:16

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 321 | 511.997 ms | 0.00% | 0.00% |
| Run 2 | 317 | 529.959 ms | 0.00% | 0.00% |
| Run 3 | 322 | 507.529 ms | 0.00% | 0.00% |
| Run 4 | 323 | 502.676 ms | 0.00% | 0.00% |
| Run 5 | 306 | 586.911 ms | 0.00% | 0.00% |
| **PROMEDIO** | **317.8** | **527.814 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |104.02% | 109.46% | 112.28% | 103.24% | 101.23% | **106.05%** |
| **exp-vulnerable-mongo-db-1** |99.61% | 110.80% | 110.73% | 107.74% | 117.33% | **109.24%** |
| **exp-vulnerable-ms-catalogo-1** |7.37% | 5.37% | 5.96% | 5.08% | 8.01% | **6.36%** |
| **exp-vulnerable-ms-ordenes-1** |4.91% | 5.24% | 5.86% | 7.80% | 6.15% | **5.99%** |
| **exp-vulnerable-ms-resenas-1** |163.38% | 133.43% | 131.49% | 184.83% | 155.81% | **153.79%** |
| **exp-vulnerable-ms-usuarios-1** |8.71% | 8.98% | 37.54% | 9.87% | 9.80% | **14.98%** |
| **exp-vulnerable-postgres-db-1** |49.44% | 22.18% | 27.70% | 22.13% | 36.51% | **31.59%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |203.1MiB (203.10 MiB)  | 200.1MiB (200.10 MiB)  | 190.5MiB (190.50 MiB)  | 194.8MiB (194.80 MiB)  | 194.5MiB (194.50 MiB)  |
| **exp-vulnerable-mongo-db-1** |335.9MiB (335.90 MiB)  | 344.4MiB (344.40 MiB)  | 355.2MiB (355.20 MiB)  | 345.6MiB (345.60 MiB)  | 351MiB (351.00 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |48.76MiB (48.76 MiB)  | 45.9MiB (45.90 MiB)  | 46.53MiB (46.53 MiB)  | 45.97MiB (45.97 MiB)  | 46.05MiB (46.05 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |47.14MiB (47.14 MiB)  | 46.77MiB (46.77 MiB)  | 46.64MiB (46.64 MiB)  | 45.59MiB (45.59 MiB)  | 45.56MiB (45.56 MiB)  |
| **exp-vulnerable-ms-resenas-1** |145.2MiB (145.20 MiB)  | 164.1MiB (164.10 MiB)  | 143.5MiB (143.50 MiB)  | 140.7MiB (140.70 MiB)  | 154MiB (154.00 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |73.71MiB (73.71 MiB)  | 72.27MiB (72.27 MiB)  | 72.54MiB (72.54 MiB)  | 67.64MiB (67.64 MiB)  | 69.31MiB (69.31 MiB)  |
| **exp-vulnerable-postgres-db-1** |68.73MiB (68.73 MiB)  | 70.11MiB (70.11 MiB)  | 68.45MiB (68.45 MiB)  | 68.72MiB (68.72 MiB)  | 69.11MiB (69.11 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |72.92% | 75.72% | 73.40% | 67.29% | 70.53% | **71.97%** |
| **exp-vulnerable-mongo-db-1** |32.88% | 28.22% | 43.95% | 40.82% | 35.46% | **36.27%** |
| **exp-vulnerable-ms-catalogo-1** |1.61% | 1.21% | 1.63% | 1.55% | 1.58% | **1.52%** |
| **exp-vulnerable-ms-ordenes-1** |1.58% | 1.29% | 1.58% | 1.57% | 1.37% | **1.48%** |
| **exp-vulnerable-ms-resenas-1** |100.98% | 98.80% | 92.10% | 97.04% | 99.77% | **97.74%** |
| **exp-vulnerable-ms-usuarios-1** |4.41% | 4.79% | 6.02% | 4.66% | 4.73% | **4.92%** |
| **exp-vulnerable-postgres-db-1** |15.16% | 12.83% | 13.34% | 13.04% | 14.54% | **13.78%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |149.54 MiB | 144.20 MiB | 147.32 MiB | 144.55 MiB | 146.18 MiB | **146.36 MiB** |
| **exp-vulnerable-mongo-db-1** |193.90 MiB | 230.25 MiB | 243.29 MiB | 207.22 MiB | 212.14 MiB | **217.36 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.47 MiB | 45.77 MiB | 46.41 MiB | 45.84 MiB | 45.93 MiB | **46.08 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.84 MiB | 46.66 MiB | 46.53 MiB | 45.47 MiB | 45.05 MiB | **45.91 MiB** |
| **exp-vulnerable-ms-resenas-1** |119.47 MiB | 124.76 MiB | 123.88 MiB | 124.23 MiB | 122.65 MiB | **123.00 MiB** |
| **exp-vulnerable-ms-usuarios-1** |66.37 MiB | 65.12 MiB | 68.96 MiB | 60.21 MiB | 62.17 MiB | **64.57 MiB** |
| **exp-vulnerable-postgres-db-1** |66.80 MiB | 68.51 MiB | 66.26 MiB | 67.03 MiB | 67.02 MiB | **67.12 MiB** |