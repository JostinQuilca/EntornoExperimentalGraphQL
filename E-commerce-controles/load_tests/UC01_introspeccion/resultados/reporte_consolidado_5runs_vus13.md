# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=13)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 19:07:53

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 780 | 6.959 ms | 0.00% |
| Run 2 | 117 | 12.012 ms | 0.00% |
| Run 3 | 780 | 8.554 ms | 0.00% |
| Run 4 | 780 | 7.067 ms | 0.00% |
| Run 5 | 780 | 6.116 ms | 0.00% |
| **PROMEDIO** | **647.4** | **8.142 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |12.02% | 7.94% | 28.12% | 12.88% | 9.83% | **14.16%** |
| **exp-protegido-mongo-db-1** |66.24% | 87.94% | 136.90% | 78.46% | 65.27% | **86.96%** |
| **exp-protegido-ms-catalogo-1** |4.16% | 2.50% | 6.37% | 3.73% | 3.50% | **4.05%** |
| **exp-protegido-ms-ordenes-1** |5.34% | 3.05% | 5.90% | 3.85% | 3.69% | **4.37%** |
| **exp-protegido-ms-resenas-1** |4.97% | 2.90% | 4.97% | 3.33% | 3.22% | **3.88%** |
| **exp-protegido-ms-usuarios-1** |5.35% | 3.67% | 5.38% | 5.64% | 3.55% | **4.72%** |
| **exp-protegido-postgres-db-1** |3.99% | 4.17% | 5.89% | 4.69% | 5.35% | **4.82%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |85.31MiB (85.31 MiB)  | 69.36MiB (69.36 MiB)  | 82.02MiB (82.02 MiB)  | 83.57MiB (83.57 MiB)  | 83.08MiB (83.08 MiB)  |
| **exp-protegido-mongo-db-1** |338MiB (338.00 MiB)  | 272.1MiB (272.10 MiB)  | 340.9MiB (340.90 MiB)  | 347.5MiB (347.50 MiB)  | 336.9MiB (336.90 MiB)  |
| **exp-protegido-ms-catalogo-1** |48.13MiB (48.13 MiB)  | 45.4MiB (45.40 MiB)  | 45.84MiB (45.84 MiB)  | 48.21MiB (48.21 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.76MiB (45.76 MiB)  | 45.77MiB (45.77 MiB)  | 45.64MiB (45.64 MiB)  | 46.79MiB (46.79 MiB)  | 47.46MiB (47.46 MiB)  |
| **exp-protegido-ms-resenas-1** |46.73MiB (46.73 MiB)  | 46.52MiB (46.52 MiB)  | 45.85MiB (45.85 MiB)  | 46.22MiB (46.22 MiB)  | 45.89MiB (45.89 MiB)  |
| **exp-protegido-ms-usuarios-1** |47.04MiB (47.04 MiB)  | 45.57MiB (45.57 MiB)  | 45.14MiB (45.14 MiB)  | 46.27MiB (46.27 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-protegido-postgres-db-1** |27.36MiB (27.36 MiB)  | 27.39MiB (27.39 MiB)  | 28MiB (28.00 MiB)  | 28.85MiB (28.85 MiB)  | 29.14MiB (29.14 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |4.23% | 4.10% | 6.25% | 4.66% | 4.23% | **4.69%** |
| **exp-protegido-mongo-db-1** |17.45% | 38.30% | 21.17% | 21.23% | 17.67% | **23.16%** |
| **exp-protegido-ms-catalogo-1** |1.07% | 0.79% | 1.38% | 0.98% | 1.00% | **1.04%** |
| **exp-protegido-ms-ordenes-1** |1.04% | 0.51% | 1.14% | 0.95% | 0.90% | **0.91%** |
| **exp-protegido-ms-resenas-1** |1.06% | 0.95% | 1.11% | 0.94% | 0.84% | **0.98%** |
| **exp-protegido-ms-usuarios-1** |1.04% | 1.12% | 1.09% | 1.10% | 0.85% | **1.04%** |
| **exp-protegido-postgres-db-1** |1.14% | 0.80% | 1.46% | 1.22% | 1.27% | **1.18%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |77.01 MiB | 67.03 MiB | 74.88 MiB | 75.60 MiB | 75.91 MiB | **74.09 MiB** |
| **exp-protegido-mongo-db-1** |198.68 MiB | 200.55 MiB | 207.40 MiB | 200.83 MiB | 195.13 MiB | **200.52 MiB** |
| **exp-protegido-ms-catalogo-1** |47.03 MiB | 45.36 MiB | 45.75 MiB | 46.19 MiB | 45.98 MiB | **46.06 MiB** |
| **exp-protegido-ms-ordenes-1** |45.62 MiB | 45.74 MiB | 45.53 MiB | 45.12 MiB | 47.35 MiB | **45.87 MiB** |
| **exp-protegido-ms-resenas-1** |46.58 MiB | 46.50 MiB | 45.74 MiB | 45.99 MiB | 45.79 MiB | **46.12 MiB** |
| **exp-protegido-ms-usuarios-1** |46.89 MiB | 45.55 MiB | 45.05 MiB | 46.17 MiB | 45.97 MiB | **45.93 MiB** |
| **exp-protegido-postgres-db-1** |27.30 MiB | 27.38 MiB | 27.36 MiB | 27.46 MiB | 27.48 MiB | **27.40 MiB** |