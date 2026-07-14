# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 13:38:53

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 8 | 6647.228 ms | 0.00% | 0.00% |
| Run 2 | 9 | 5808.959 ms | 0.00% | 0.00% |
| Run 3 | 11 | 4746.198 ms | 0.00% | 0.00% |
| Run 4 | 10 | 5426.532 ms | 0.00% | 0.00% |
| Run 5 | 10 | 5124.361 ms | 0.00% | 0.00% |
| **PROMEDIO** | **9.6** | **5550.656 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |137.94% | 124.22% | 100.23% | 133.84% | 119.08% | **123.06%** |
| **exp-vulnerable-mongo-db-1** |112.09% | 98.78% | 76.07% | 97.67% | 89.51% | **94.82%** |
| **exp-vulnerable-ms-catalogo-1** |4.80% | 4.46% | 3.40% | 4.05% | 5.11% | **4.36%** |
| **exp-vulnerable-ms-ordenes-1** |5.48% | 4.44% | 5.16% | 4.33% | 3.97% | **4.68%** |
| **exp-vulnerable-ms-resenas-1** |142.47% | 132.73% | 124.48% | 127.16% | 127.64% | **130.90%** |
| **exp-vulnerable-ms-usuarios-1** |156.94% | 158.12% | 169.54% | 158.74% | 153.94% | **159.46%** |
| **exp-vulnerable-postgres-db-1** |11.20% | 15.71% | 10.60% | 15.43% | 10.25% | **12.64%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |460.7MiB (460.70 MiB)  | 439.6MiB (439.60 MiB)  | 441.4MiB (441.40 MiB)  | 447.5MiB (447.50 MiB)  | 462MiB (462.00 MiB)  |
| **exp-vulnerable-mongo-db-1** |315.9MiB (315.90 MiB)  | 344.8MiB (344.80 MiB)  | 351.3MiB (351.30 MiB)  | 348.2MiB (348.20 MiB)  | 342.6MiB (342.60 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |48.23MiB (48.23 MiB)  | 51.91MiB (51.91 MiB)  | 50.04MiB (50.04 MiB)  | 46.41MiB (46.41 MiB)  | 46.5MiB (46.50 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |48.18MiB (48.18 MiB)  | 52.11MiB (52.11 MiB)  | 51.45MiB (51.45 MiB)  | 46.64MiB (46.64 MiB)  | 47.71MiB (47.71 MiB)  |
| **exp-vulnerable-ms-resenas-1** |811.1MiB (811.10 MiB)  | 934.2MiB (934.20 MiB)  | 837.6MiB (837.60 MiB)  | 895.9MiB (895.90 MiB)  | 755.6MiB (755.60 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |708.1MiB (708.10 MiB)  | 708MiB (708.00 MiB)  | 705.2MiB (705.20 MiB)  | 746.3MiB (746.30 MiB)  | 660.9MiB (660.90 MiB)  |
| **exp-vulnerable-postgres-db-1** |63.72MiB (63.72 MiB)  | 69.43MiB (69.43 MiB)  | 64.89MiB (64.89 MiB)  | 62.88MiB (62.88 MiB)  | 63.24MiB (63.24 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |54.69% | 50.81% | 31.95% | 54.76% | 37.76% | **45.99%** |
| **exp-vulnerable-mongo-db-1** |33.24% | 25.59% | 22.73% | 23.58% | 23.41% | **25.71%** |
| **exp-vulnerable-ms-catalogo-1** |1.14% | 1.10% | 0.83% | 0.99% | 0.90% | **0.99%** |
| **exp-vulnerable-ms-ordenes-1** |1.28% | 0.94% | 1.17% | 1.06% | 0.97% | **1.08%** |
| **exp-vulnerable-ms-resenas-1** |31.23% | 34.59% | 34.38% | 28.01% | 34.06% | **32.45%** |
| **exp-vulnerable-ms-usuarios-1** |16.15% | 18.34% | 33.64% | 20.28% | 26.77% | **23.04%** |
| **exp-vulnerable-postgres-db-1** |3.05% | 2.99% | 2.95% | 3.40% | 3.04% | **3.09%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |361.64 MiB | 299.88 MiB | 324.56 MiB | 319.19 MiB | 327.93 MiB | **326.64 MiB** |
| **exp-vulnerable-mongo-db-1** |193.33 MiB | 213.86 MiB | 207.08 MiB | 210.15 MiB | 208.90 MiB | **206.66 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.99 MiB | 51.83 MiB | 49.90 MiB | 46.26 MiB | 46.37 MiB | **48.27 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.98 MiB | 51.81 MiB | 51.25 MiB | 45.93 MiB | 47.59 MiB | **48.71 MiB** |
| **exp-vulnerable-ms-resenas-1** |553.08 MiB | 624.54 MiB | 596.70 MiB | 609.32 MiB | 576.73 MiB | **592.07 MiB** |
| **exp-vulnerable-ms-usuarios-1** |377.70 MiB | 454.12 MiB | 434.00 MiB | 452.44 MiB | 393.54 MiB | **422.36 MiB** |
| **exp-vulnerable-postgres-db-1** |61.54 MiB | 66.12 MiB | 63.90 MiB | 61.50 MiB | 61.99 MiB | **63.01 MiB** |