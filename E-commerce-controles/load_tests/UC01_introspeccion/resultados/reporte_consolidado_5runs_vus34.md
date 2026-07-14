# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=34)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 19:51:31

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 2040 | 7.423 ms | 0.00% |
| Run 2 | 2040 | 7.235 ms | 0.00% |
| Run 3 | 2040 | 7.844 ms | 0.00% |
| Run 4 | 2040 | 7.228 ms | 0.00% |
| Run 5 | 2040 | 7.969 ms | 0.00% |
| **PROMEDIO** | **2040.0** | **7.540 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |16.08% | 16.34% | 17.58% | 20.51% | 23.96% | **18.89%** |
| **exp-protegido-mongo-db-1** |56.78% | 47.73% | 57.20% | 51.19% | 59.96% | **54.57%** |
| **exp-protegido-ms-catalogo-1** |3.08% | 2.94% | 3.62% | 3.31% | 3.81% | **3.35%** |
| **exp-protegido-ms-ordenes-1** |4.27% | 3.31% | 3.81% | 2.96% | 2.97% | **3.46%** |
| **exp-protegido-ms-resenas-1** |5.09% | 3.25% | 3.19% | 3.53% | 3.18% | **3.65%** |
| **exp-protegido-ms-usuarios-1** |4.93% | 2.95% | 3.54% | 3.13% | 3.38% | **3.59%** |
| **exp-protegido-postgres-db-1** |3.97% | 5.58% | 3.89% | 4.24% | 4.44% | **4.42%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |101.4MiB (101.40 MiB)  | 100.6MiB (100.60 MiB)  | 99.86MiB (99.86 MiB)  | 100.9MiB (100.90 MiB)  | 101.5MiB (101.50 MiB)  |
| **exp-protegido-mongo-db-1** |347.3MiB (347.30 MiB)  | 346.6MiB (346.60 MiB)  | 340MiB (340.00 MiB)  | 333.7MiB (333.70 MiB)  | 340MiB (340.00 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.83MiB (46.83 MiB)  | 45.95MiB (45.95 MiB)  | 46.15MiB (46.15 MiB)  | 45.82MiB (45.82 MiB)  | 45.55MiB (45.55 MiB)  |
| **exp-protegido-ms-ordenes-1** |48.49MiB (48.49 MiB)  | 45.21MiB (45.21 MiB)  | 45.73MiB (45.73 MiB)  | 46.62MiB (46.62 MiB)  | 46.66MiB (46.66 MiB)  |
| **exp-protegido-ms-resenas-1** |47.57MiB (47.57 MiB)  | 46.66MiB (46.66 MiB)  | 45.63MiB (45.63 MiB)  | 46.56MiB (46.56 MiB)  | 46.16MiB (46.16 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.96MiB (45.96 MiB)  | 45.88MiB (45.88 MiB)  | 45.82MiB (45.82 MiB)  | 46.59MiB (46.59 MiB)  | 45.98MiB (45.98 MiB)  |
| **exp-protegido-postgres-db-1** |27.39MiB (27.39 MiB)  | 27.78MiB (27.78 MiB)  | 28MiB (28.00 MiB)  | 27.38MiB (27.38 MiB)  | 28.86MiB (28.86 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |9.12% | 8.81% | 9.00% | 9.71% | 9.27% | **9.18%** |
| **exp-protegido-mongo-db-1** |16.24% | 14.22% | 15.61% | 14.97% | 15.34% | **15.28%** |
| **exp-protegido-ms-catalogo-1** |0.94% | 0.85% | 0.92% | 0.97% | 0.93% | **0.92%** |
| **exp-protegido-ms-ordenes-1** |0.85% | 0.79% | 0.86% | 0.84% | 0.86% | **0.84%** |
| **exp-protegido-ms-resenas-1** |0.90% | 0.80% | 0.83% | 0.75% | 0.90% | **0.84%** |
| **exp-protegido-ms-usuarios-1** |0.87% | 0.81% | 0.86% | 0.80% | 0.89% | **0.85%** |
| **exp-protegido-postgres-db-1** |1.07% | 1.14% | 1.04% | 1.26% | 1.11% | **1.12%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |92.45 MiB | 90.19 MiB | 89.83 MiB | 89.93 MiB | 90.45 MiB | **90.57 MiB** |
| **exp-protegido-mongo-db-1** |200.05 MiB | 201.35 MiB | 196.44 MiB | 196.45 MiB | 200.31 MiB | **198.92 MiB** |
| **exp-protegido-ms-catalogo-1** |46.69 MiB | 45.85 MiB | 45.96 MiB | 45.69 MiB | 45.41 MiB | **45.92 MiB** |
| **exp-protegido-ms-ordenes-1** |47.38 MiB | 45.11 MiB | 45.64 MiB | 46.12 MiB | 46.36 MiB | **46.12 MiB** |
| **exp-protegido-ms-resenas-1** |46.35 MiB | 46.56 MiB | 45.53 MiB | 46.25 MiB | 46.07 MiB | **46.15 MiB** |
| **exp-protegido-ms-usuarios-1** |45.08 MiB | 45.78 MiB | 45.72 MiB | 46.06 MiB | 45.89 MiB | **45.71 MiB** |
| **exp-protegido-postgres-db-1** |27.32 MiB | 27.40 MiB | 27.36 MiB | 27.37 MiB | 27.42 MiB | **27.37 MiB** |