# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 15:04:27

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 10 | 29963.828 ms | 50.00% | 0.00% |
| Run 2 | 14 | 28027.840 ms | 35.71% | 0.00% |
| Run 3 | 9 | 29391.060 ms | 44.44% | 0.00% |
| Run 4 | 10 | 29500.346 ms | 40.00% | 0.00% |
| Run 5 | 10 | 28419.287 ms | 50.00% | 0.00% |
| **PROMEDIO** | **10.6** | **29060.472 ms** | **44.03%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |186.25% | 145.93% | 170.39% | 148.54% | 164.88% | **163.20%** |
| **exp-protegido-mongo-db-1** |84.19% | 82.41% | 104.63% | 79.49% | 105.12% | **91.17%** |
| **exp-protegido-ms-catalogo-1** |4.05% | 4.21% | 3.76% | 3.43% | 3.99% | **3.89%** |
| **exp-protegido-ms-ordenes-1** |4.32% | 4.51% | 4.85% | 5.52% | 4.44% | **4.73%** |
| **exp-protegido-ms-resenas-1** |162.94% | 167.69% | 146.13% | 351.00% | 242.51% | **214.05%** |
| **exp-protegido-ms-usuarios-1** |171.84% | 220.50% | 245.36% | 196.94% | 188.13% | **204.55%** |
| **exp-protegido-postgres-db-1** |32.35% | 32.97% | 32.79% | 51.06% | 38.34% | **37.50%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  |
| **exp-protegido-mongo-db-1** |340.3MiB (340.30 MiB)  | 348.6MiB (348.60 MiB)  | 345.9MiB (345.90 MiB)  | 334.4MiB (334.40 MiB)  | 318.4MiB (318.40 MiB)  |
| **exp-protegido-ms-catalogo-1** |47.48MiB (47.48 MiB)  | 48.66MiB (48.66 MiB)  | 46.2MiB (46.20 MiB)  | 47.07MiB (47.07 MiB)  | 46.26MiB (46.26 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.88MiB (46.88 MiB)  | 46.4MiB (46.40 MiB)  | 47.34MiB (47.34 MiB)  | 46.24MiB (46.24 MiB)  | 45.98MiB (45.98 MiB)  |
| **exp-protegido-ms-resenas-1** |819.4MiB (819.40 MiB)  | 912.5MiB (912.50 MiB)  | 970.1MiB (970.10 MiB)  | 955MiB (955.00 MiB)  | 1023MiB (1023.00 MiB)  |
| **exp-protegido-ms-usuarios-1** |512MiB (512.00 MiB)  | 512MiB (512.00 MiB)  | 512MiB (512.00 MiB)  | 511.8MiB (511.80 MiB)  | 512MiB (512.00 MiB)  |
| **exp-protegido-postgres-db-1** |76.93MiB (76.93 MiB)  | 79.9MiB (79.90 MiB)  | 79.8MiB (79.80 MiB)  | 79.7MiB (79.70 MiB)  | 79.72MiB (79.72 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |71.64% | 60.65% | 49.27% | 59.99% | 56.52% | **59.61%** |
| **exp-protegido-mongo-db-1** |22.02% | 24.66% | 22.56% | 19.30% | 19.90% | **21.69%** |
| **exp-protegido-ms-catalogo-1** |0.87% | 1.10% | 0.91% | 0.81% | 0.83% | **0.90%** |
| **exp-protegido-ms-ordenes-1** |1.02% | 0.83% | 1.05% | 1.05% | 0.99% | **0.99%** |
| **exp-protegido-ms-resenas-1** |16.55% | 24.05% | 19.67% | 27.04% | 25.86% | **22.63%** |
| **exp-protegido-ms-usuarios-1** |25.53% | 33.83% | 42.53% | 32.86% | 34.01% | **33.75%** |
| **exp-protegido-postgres-db-1** |2.34% | 2.74% | 3.33% | 4.00% | 2.52% | **2.99%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |647.17 MiB | 585.61 MiB | 635.47 MiB | 623.66 MiB | 603.56 MiB | **619.09 MiB** |
| **exp-protegido-mongo-db-1** |205.26 MiB | 213.43 MiB | 208.42 MiB | 200.65 MiB | 196.04 MiB | **204.76 MiB** |
| **exp-protegido-ms-catalogo-1** |47.34 MiB | 47.04 MiB | 46.06 MiB | 46.78 MiB | 46.10 MiB | **46.66 MiB** |
| **exp-protegido-ms-ordenes-1** |46.72 MiB | 45.82 MiB | 45.60 MiB | 45.80 MiB | 45.53 MiB | **45.89 MiB** |
| **exp-protegido-ms-resenas-1** |537.28 MiB | 600.73 MiB | 649.46 MiB | 597.97 MiB | 598.13 MiB | **596.71 MiB** |
| **exp-protegido-ms-usuarios-1** |189.92 MiB | 225.15 MiB | 237.10 MiB | 174.48 MiB | 248.45 MiB | **215.02 MiB** |
| **exp-protegido-postgres-db-1** |67.62 MiB | 67.37 MiB | 69.76 MiB | 67.42 MiB | 66.31 MiB | **67.70 MiB** |