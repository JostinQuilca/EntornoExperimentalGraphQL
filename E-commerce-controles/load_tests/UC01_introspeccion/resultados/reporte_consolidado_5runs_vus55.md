# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=55)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 20:11:27

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 3300 | 7.434 ms | 0.00% |
| Run 2 | 3300 | 7.960 ms | 0.00% |
| Run 3 | 3300 | 7.493 ms | 0.00% |
| Run 4 | 3300 | 8.267 ms | 0.00% |
| Run 5 | 3297 | 11.311 ms | 0.00% |
| **PROMEDIO** | **3299.4** | **8.493 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |24.68% | 25.87% | 20.11% | 29.66% | 48.16% | **29.70%** |
| **exp-protegido-mongo-db-1** |56.84% | 51.31% | 50.60% | 58.82% | 93.12% | **62.14%** |
| **exp-protegido-ms-catalogo-1** |3.37% | 3.63% | 3.72% | 3.57% | 3.91% | **3.64%** |
| **exp-protegido-ms-ordenes-1** |3.91% | 3.39% | 3.57% | 3.08% | 3.25% | **3.44%** |
| **exp-protegido-ms-resenas-1** |4.34% | 3.43% | 3.32% | 2.96% | 4.61% | **3.73%** |
| **exp-protegido-ms-usuarios-1** |4.86% | 4.06% | 3.37% | 2.78% | 3.78% | **3.77%** |
| **exp-protegido-postgres-db-1** |3.74% | 3.96% | 4.37% | 4.46% | 9.07% | **5.12%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |102.1MiB (102.10 MiB)  | 103.8MiB (103.80 MiB)  | 101.8MiB (101.80 MiB)  | 104.8MiB (104.80 MiB)  | 100.1MiB (100.10 MiB)  |
| **exp-protegido-mongo-db-1** |329.2MiB (329.20 MiB)  | 341.7MiB (341.70 MiB)  | 340.1MiB (340.10 MiB)  | 349.6MiB (349.60 MiB)  | 340.9MiB (340.90 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.93MiB (45.93 MiB)  | 46MiB (46.00 MiB)  | 46.16MiB (46.16 MiB)  | 46.37MiB (46.37 MiB)  | 45.5MiB (45.50 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.16MiB (46.16 MiB)  | 46.1MiB (46.10 MiB)  | 45.97MiB (45.97 MiB)  | 46.26MiB (46.26 MiB)  | 45.12MiB (45.12 MiB)  |
| **exp-protegido-ms-resenas-1** |46.41MiB (46.41 MiB)  | 47.14MiB (47.14 MiB)  | 47.15MiB (47.15 MiB)  | 47.11MiB (47.11 MiB)  | 45.34MiB (45.34 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.34MiB (45.34 MiB)  | 47.8MiB (47.80 MiB)  | 45.84MiB (45.84 MiB)  | 46.04MiB (46.04 MiB)  | 46.5MiB (46.50 MiB)  |
| **exp-protegido-postgres-db-1** |28.23MiB (28.23 MiB)  | 27.38MiB (27.38 MiB)  | 27.41MiB (27.41 MiB)  | 27.37MiB (27.37 MiB)  | 29.07MiB (29.07 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |13.92% | 13.99% | 12.78% | 14.32% | 20.42% | **15.09%** |
| **exp-protegido-mongo-db-1** |14.09% | 13.50% | 14.76% | 15.41% | 18.66% | **15.28%** |
| **exp-protegido-ms-catalogo-1** |0.83% | 0.97% | 0.94% | 0.89% | 1.04% | **0.93%** |
| **exp-protegido-ms-ordenes-1** |0.88% | 0.85% | 0.80% | 0.76% | 0.83% | **0.82%** |
| **exp-protegido-ms-resenas-1** |1.04% | 0.93% | 0.79% | 0.77% | 0.91% | **0.89%** |
| **exp-protegido-ms-usuarios-1** |0.93% | 0.89% | 0.78% | 0.71% | 0.90% | **0.84%** |
| **exp-protegido-postgres-db-1** |1.07% | 1.16% | 1.03% | 1.27% | 1.35% | **1.18%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |96.41 MiB | 95.75 MiB | 95.40 MiB | 96.96 MiB | 93.88 MiB | **95.68 MiB** |
| **exp-protegido-mongo-db-1** |195.99 MiB | 199.80 MiB | 196.08 MiB | 201.38 MiB | 201.91 MiB | **199.03 MiB** |
| **exp-protegido-ms-catalogo-1** |45.80 MiB | 45.90 MiB | 46.05 MiB | 46.22 MiB | 45.40 MiB | **45.87 MiB** |
| **exp-protegido-ms-ordenes-1** |46.04 MiB | 46.00 MiB | 45.87 MiB | 45.91 MiB | 45.03 MiB | **45.77 MiB** |
| **exp-protegido-ms-resenas-1** |46.29 MiB | 47.04 MiB | 47.05 MiB | 46.75 MiB | 45.24 MiB | **46.47 MiB** |
| **exp-protegido-ms-usuarios-1** |45.22 MiB | 47.69 MiB | 45.75 MiB | 45.56 MiB | 46.40 MiB | **46.12 MiB** |
| **exp-protegido-postgres-db-1** |27.34 MiB | 27.37 MiB | 27.32 MiB | 27.37 MiB | 27.44 MiB | **27.37 MiB** |