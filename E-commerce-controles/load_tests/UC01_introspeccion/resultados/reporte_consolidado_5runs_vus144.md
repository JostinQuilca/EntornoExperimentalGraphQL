# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=144)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 20:59:21

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 8608 | 12.949 ms | 0.00% |
| Run 2 | 8640 | 10.759 ms | 0.00% |
| Run 3 | 8628 | 11.492 ms | 0.00% |
| Run 4 | 8640 | 11.109 ms | 0.00% |
| Run 5 | 8625 | 11.700 ms | 0.00% |
| **PROMEDIO** | **8628.2** | **11.602 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |78.52% | 59.54% | 57.96% | 60.41% | 51.70% | **61.63%** |
| **exp-protegido-mongo-db-1** |64.18% | 61.72% | 66.74% | 68.57% | 67.98% | **65.84%** |
| **exp-protegido-ms-catalogo-1** |3.13% | 3.86% | 2.82% | 3.23% | 4.74% | **3.56%** |
| **exp-protegido-ms-ordenes-1** |3.51% | 3.83% | 3.17% | 3.05% | 3.23% | **3.36%** |
| **exp-protegido-ms-resenas-1** |4.82% | 4.10% | 3.63% | 5.01% | 3.36% | **4.18%** |
| **exp-protegido-ms-usuarios-1** |4.61% | 3.58% | 3.21% | 3.10% | 3.08% | **3.52%** |
| **exp-protegido-postgres-db-1** |7.04% | 4.73% | 4.44% | 3.95% | 4.50% | **4.93%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |116.5MiB (116.50 MiB)  | 111.9MiB (111.90 MiB)  | 107MiB (107.00 MiB)  | 106.3MiB (106.30 MiB)  | 111MiB (111.00 MiB)  |
| **exp-protegido-mongo-db-1** |344.2MiB (344.20 MiB)  | 344MiB (344.00 MiB)  | 333MiB (333.00 MiB)  | 334MiB (334.00 MiB)  | 333.2MiB (333.20 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.23MiB (46.23 MiB)  | 45.7MiB (45.70 MiB)  | 48.8MiB (48.80 MiB)  | 46.4MiB (46.40 MiB)  | 49.73MiB (49.73 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.83MiB (45.83 MiB)  | 45.18MiB (45.18 MiB)  | 45.54MiB (45.54 MiB)  | 47.48MiB (47.48 MiB)  | 45.72MiB (45.72 MiB)  |
| **exp-protegido-ms-resenas-1** |47.17MiB (47.17 MiB)  | 46.57MiB (46.57 MiB)  | 47.58MiB (47.58 MiB)  | 53.85MiB (53.85 MiB)  | 46.76MiB (46.76 MiB)  |
| **exp-protegido-ms-usuarios-1** |47.44MiB (47.44 MiB)  | 45.21MiB (45.21 MiB)  | 45.99MiB (45.99 MiB)  | 46.72MiB (46.72 MiB)  | 45.58MiB (45.58 MiB)  |
| **exp-protegido-postgres-db-1** |27.99MiB (27.99 MiB)  | 28.8MiB (28.80 MiB)  | 28.07MiB (28.07 MiB)  | 27.98MiB (27.98 MiB)  | 28.13MiB (28.13 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |40.36% | 34.17% | 34.91% | 34.41% | 35.08% | **35.79%** |
| **exp-protegido-mongo-db-1** |19.95% | 18.34% | 17.24% | 16.20% | 19.23% | **18.19%** |
| **exp-protegido-ms-catalogo-1** |0.81% | 0.91% | 0.78% | 0.90% | 0.92% | **0.86%** |
| **exp-protegido-ms-ordenes-1** |0.89% | 0.87% | 0.84% | 0.80% | 0.79% | **0.84%** |
| **exp-protegido-ms-resenas-1** |0.97% | 0.91% | 0.85% | 0.93% | 0.78% | **0.89%** |
| **exp-protegido-ms-usuarios-1** |0.96% | 0.81% | 0.77% | 0.77% | 0.84% | **0.83%** |
| **exp-protegido-postgres-db-1** |1.50% | 1.31% | 1.26% | 1.28% | 1.16% | **1.30%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |107.85 MiB | 104.14 MiB | 102.78 MiB | 101.49 MiB | 103.42 MiB | **103.94 MiB** |
| **exp-protegido-mongo-db-1** |199.38 MiB | 200.00 MiB | 199.75 MiB | 200.39 MiB | 197.21 MiB | **199.35 MiB** |
| **exp-protegido-ms-catalogo-1** |46.09 MiB | 45.59 MiB | 46.89 MiB | 46.29 MiB | 47.30 MiB | **46.43 MiB** |
| **exp-protegido-ms-ordenes-1** |45.70 MiB | 45.08 MiB | 45.44 MiB | 47.38 MiB | 45.62 MiB | **45.84 MiB** |
| **exp-protegido-ms-resenas-1** |46.88 MiB | 46.47 MiB | 47.28 MiB | 53.35 MiB | 46.66 MiB | **48.13 MiB** |
| **exp-protegido-ms-usuarios-1** |45.68 MiB | 45.11 MiB | 45.90 MiB | 46.62 MiB | 45.48 MiB | **45.76 MiB** |
| **exp-protegido-postgres-db-1** |27.81 MiB | 27.99 MiB | 27.92 MiB | 27.97 MiB | 27.99 MiB | **27.94 MiB** |