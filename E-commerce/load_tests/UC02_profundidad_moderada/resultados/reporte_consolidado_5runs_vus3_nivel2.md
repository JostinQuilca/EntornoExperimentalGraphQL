# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 14:32:23

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 12 | 14774.871 ms | 0.00% | 0.00% |
| Run 2 | 12 | 14939.357 ms | 0.00% | 0.00% |
| Run 3 | 12 | 14091.955 ms | 0.00% | 0.00% |
| Run 4 | 9 | 18892.432 ms | 0.00% | 0.00% |
| Run 5 | 12 | 17434.050 ms | 0.00% | 0.00% |
| **PROMEDIO** | **11.4** | **16026.533 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |152.97% | 171.67% | 176.54% | 157.04% | 152.26% | **162.10%** |
| **exp-vulnerable-mongo-db-1** |113.71% | 113.96% | 83.01% | 136.46% | 112.25% | **111.88%** |
| **exp-vulnerable-ms-catalogo-1** |4.86% | 5.38% | 4.90% | 7.16% | 5.84% | **5.63%** |
| **exp-vulnerable-ms-ordenes-1** |8.48% | 5.07% | 4.72% | 6.45% | 5.36% | **6.02%** |
| **exp-vulnerable-ms-resenas-1** |234.05% | 255.55% | 153.47% | 305.86% | 277.45% | **245.28%** |
| **exp-vulnerable-ms-usuarios-1** |272.52% | 242.90% | 277.59% | 242.82% | 228.68% | **252.90%** |
| **exp-vulnerable-postgres-db-1** |44.06% | 26.35% | 24.10% | 13.87% | 48.82% | **31.44%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |691.9MiB (691.90 MiB)  | 815.1MiB (815.10 MiB)  | 704.5MiB (704.50 MiB)  | 698.2MiB (698.20 MiB)  | 764.5MiB (764.50 MiB)  |
| **exp-vulnerable-mongo-db-1** |342.1MiB (342.10 MiB)  | 350.5MiB (350.50 MiB)  | 336.3MiB (336.30 MiB)  | 341.3MiB (341.30 MiB)  | 347.6MiB (347.60 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.77MiB (46.77 MiB)  | 47.24MiB (47.24 MiB)  | 48.36MiB (48.36 MiB)  | 45.78MiB (45.78 MiB)  | 46.8MiB (46.80 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |48.46MiB (48.46 MiB)  | 48.54MiB (48.54 MiB)  | 46.39MiB (46.39 MiB)  | 46.11MiB (46.11 MiB)  | 46.5MiB (46.50 MiB)  |
| **exp-vulnerable-ms-resenas-1** |1016MiB (1016.00 MiB)  | 1022MiB (1022.00 MiB)  | 1021MiB (1021.00 MiB)  | 837.2MiB (837.20 MiB)  | 955.8MiB (955.80 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |794.4MiB (794.40 MiB)  | 1.151GiB (1178.62 MiB)  | 1.047GiB (1072.13 MiB)  | 1.031GiB (1055.74 MiB)  | 884.3MiB (884.30 MiB)  |
| **exp-vulnerable-postgres-db-1** |71.88MiB (71.88 MiB)  | 71.97MiB (71.97 MiB)  | 73.32MiB (73.32 MiB)  | 68.96MiB (68.96 MiB)  | 69.62MiB (69.62 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |45.56% | 42.18% | 44.30% | 42.30% | 45.67% | **44.00%** |
| **exp-vulnerable-mongo-db-1** |30.08% | 34.87% | 21.59% | 33.41% | 31.51% | **30.29%** |
| **exp-vulnerable-ms-catalogo-1** |1.21% | 1.09% | 1.29% | 1.71% | 1.37% | **1.33%** |
| **exp-vulnerable-ms-ordenes-1** |1.34% | 1.25% | 1.11% | 1.48% | 1.18% | **1.27%** |
| **exp-vulnerable-ms-resenas-1** |49.42% | 51.14% | 41.49% | 49.44% | 51.80% | **48.66%** |
| **exp-vulnerable-ms-usuarios-1** |34.23% | 37.91% | 41.06% | 36.13% | 35.73% | **37.01%** |
| **exp-vulnerable-postgres-db-1** |5.56% | 5.70% | 3.57% | 3.44% | 5.49% | **4.75%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |464.30 MiB | 457.14 MiB | 450.08 MiB | 457.14 MiB | 433.69 MiB | **452.47 MiB** |
| **exp-vulnerable-mongo-db-1** |202.63 MiB | 229.33 MiB | 203.40 MiB | 232.94 MiB | 206.83 MiB | **215.03 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.38 MiB | 47.10 MiB | 47.10 MiB | 45.62 MiB | 46.64 MiB | **46.57 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.33 MiB | 46.04 MiB | 46.00 MiB | 45.85 MiB | 46.12 MiB | **46.07 MiB** |
| **exp-vulnerable-ms-resenas-1** |732.06 MiB | 753.94 MiB | 708.96 MiB | 647.59 MiB | 687.48 MiB | **706.01 MiB** |
| **exp-vulnerable-ms-usuarios-1** |641.64 MiB | 660.12 MiB | 657.96 MiB | 626.87 MiB | 644.90 MiB | **646.30 MiB** |
| **exp-vulnerable-postgres-db-1** |69.96 MiB | 70.09 MiB | 68.99 MiB | 65.87 MiB | 67.40 MiB | **68.46 MiB** |