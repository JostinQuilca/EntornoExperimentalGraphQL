# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 13:52:51

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 9 | 6131.708 ms | 0.00% | 0.00% |
| Run 2 | 10 | 5181.948 ms | 0.00% | 0.00% |
| Run 3 | 10 | 5449.547 ms | 0.00% | 0.00% |
| Run 4 | 10 | 5522.852 ms | 0.00% | 0.00% |
| Run 5 | 10 | 4926.665 ms | 0.00% | 0.00% |
| **PROMEDIO** | **9.8** | **5442.544 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |121.95% | 134.69% | 111.75% | 110.49% | 73.50% | **110.48%** |
| **exp-protegido-mongo-db-1** |88.95% | 85.81% | 81.59% | 112.55% | 102.04% | **94.19%** |
| **exp-protegido-ms-catalogo-1** |9.72% | 4.92% | 3.47% | 4.51% | 4.42% | **5.41%** |
| **exp-protegido-ms-ordenes-1** |5.46% | 4.84% | 3.62% | 4.11% | 4.13% | **4.43%** |
| **exp-protegido-ms-resenas-1** |135.05% | 131.85% | 122.57% | 131.32% | 135.12% | **131.18%** |
| **exp-protegido-ms-usuarios-1** |140.95% | 173.98% | 140.67% | 141.29% | 154.33% | **150.24%** |
| **exp-protegido-postgres-db-1** |11.94% | 13.84% | 10.26% | 10.40% | 11.57% | **11.60%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |461MiB (461.00 MiB)  | 438.2MiB (438.20 MiB)  | 459.1MiB (459.10 MiB)  | 444.7MiB (444.70 MiB)  | 443MiB (443.00 MiB)  |
| **exp-protegido-mongo-db-1** |336.4MiB (336.40 MiB)  | 342.5MiB (342.50 MiB)  | 351.6MiB (351.60 MiB)  | 348.7MiB (348.70 MiB)  | 343.7MiB (343.70 MiB)  |
| **exp-protegido-ms-catalogo-1** |59.18MiB (59.18 MiB)  | 47.13MiB (47.13 MiB)  | 45.77MiB (45.77 MiB)  | 46.69MiB (46.69 MiB)  | 46.27MiB (46.27 MiB)  |
| **exp-protegido-ms-ordenes-1** |52.99MiB (52.99 MiB)  | 48.61MiB (48.61 MiB)  | 47.81MiB (47.81 MiB)  | 46.44MiB (46.44 MiB)  | 45.87MiB (45.87 MiB)  |
| **exp-protegido-ms-resenas-1** |1023MiB (1023.00 MiB)  | 765.9MiB (765.90 MiB)  | 1024MiB (1024.00 MiB)  | 849.5MiB (849.50 MiB)  | 828.2MiB (828.20 MiB)  |
| **exp-protegido-ms-usuarios-1** |507MiB (507.00 MiB)  | 511.6MiB (511.60 MiB)  | 511.7MiB (511.70 MiB)  | 511.8MiB (511.80 MiB)  | 511.3MiB (511.30 MiB)  |
| **exp-protegido-postgres-db-1** |72.5MiB (72.50 MiB)  | 65.65MiB (65.65 MiB)  | 65.43MiB (65.43 MiB)  | 62.54MiB (62.54 MiB)  | 62.58MiB (62.58 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |48.14% | 36.43% | 31.32% | 34.80% | 19.66% | **34.07%** |
| **exp-protegido-mongo-db-1** |21.10% | 19.29% | 19.97% | 23.28% | 22.66% | **21.26%** |
| **exp-protegido-ms-catalogo-1** |1.10% | 0.98% | 0.82% | 1.03% | 0.99% | **0.98%** |
| **exp-protegido-ms-ordenes-1** |1.09% | 0.99% | 0.92% | 1.02% | 1.05% | **1.01%** |
| **exp-protegido-ms-resenas-1** |33.56% | 34.75% | 33.42% | 31.75% | 36.63% | **34.02%** |
| **exp-protegido-ms-usuarios-1** |14.33% | 25.94% | 29.92% | 26.84% | 31.33% | **25.67%** |
| **exp-protegido-postgres-db-1** |2.55% | 2.76% | 2.65% | 2.39% | 2.17% | **2.50%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |321.82 MiB | 240.04 MiB | 324.66 MiB | 273.96 MiB | 335.58 MiB | **299.21 MiB** |
| **exp-protegido-mongo-db-1** |202.02 MiB | 204.09 MiB | 204.91 MiB | 194.96 MiB | 200.20 MiB | **201.24 MiB** |
| **exp-protegido-ms-catalogo-1** |54.38 MiB | 47.02 MiB | 45.66 MiB | 46.57 MiB | 45.90 MiB | **47.91 MiB** |
| **exp-protegido-ms-ordenes-1** |51.44 MiB | 48.08 MiB | 47.70 MiB | 46.31 MiB | 45.76 MiB | **47.86 MiB** |
| **exp-protegido-ms-resenas-1** |669.14 MiB | 595.83 MiB | 650.67 MiB | 616.43 MiB | 565.57 MiB | **619.53 MiB** |
| **exp-protegido-ms-usuarios-1** |354.53 MiB | 306.24 MiB | 318.15 MiB | 382.61 MiB | 367.16 MiB | **345.74 MiB** |
| **exp-protegido-postgres-db-1** |69.83 MiB | 64.67 MiB | 61.65 MiB | 60.44 MiB | 60.45 MiB | **63.41 MiB** |