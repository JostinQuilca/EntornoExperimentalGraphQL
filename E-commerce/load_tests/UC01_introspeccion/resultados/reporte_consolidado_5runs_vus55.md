# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=55)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 20:00:40

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 3300 | 6.952 ms | 0.00% |
| Run 2 | 165 | 45.179 ms | 0.00% |
| Run 3 | 3300 | 7.476 ms | 0.00% |
| Run 4 | 3300 | 7.679 ms | 0.00% |
| Run 5 | 3300 | 7.182 ms | 0.00% |
| **PROMEDIO** | **2673.0** | **14.893 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |21.43% | 24.90% | 25.68% | 31.31% | 33.92% | **27.45%** |
| **exp-vulnerable-mongo-db-1** |50.16% | 51.48% | 52.05% | 58.13% | 54.88% | **53.34%** |
| **exp-vulnerable-ms-catalogo-1** |3.31% | 0.00% | 3.67% | 3.72% | 3.43% | **2.83%** |
| **exp-vulnerable-ms-ordenes-1** |3.48% | 2.81% | 3.31% | 2.98% | 3.50% | **3.22%** |
| **exp-vulnerable-ms-resenas-1** |3.57% | 3.10% | 3.30% | 3.53% | 3.94% | **3.49%** |
| **exp-vulnerable-ms-usuarios-1** |3.21% | 2.28% | 3.40% | 3.69% | 2.98% | **3.11%** |
| **exp-vulnerable-postgres-db-1** |5.16% | 2.76% | 4.19% | 4.21% | 3.81% | **4.03%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |101.9MiB (101.90 MiB)  | 74.09MiB (74.09 MiB)  | 102.5MiB (102.50 MiB)  | 102.4MiB (102.40 MiB)  | 100.2MiB (100.20 MiB)  |
| **exp-vulnerable-mongo-db-1** |349.7MiB (349.70 MiB)  | 188.1MiB (188.10 MiB)  | 334.8MiB (334.80 MiB)  | 348.4MiB (348.40 MiB)  | 346.1MiB (346.10 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.78MiB (46.78 MiB)  | 46.13MiB (46.13 MiB)  | 46.1MiB (46.10 MiB)  | 45.44MiB (45.44 MiB)  | 45.98MiB (45.98 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |54.67MiB (54.67 MiB)  | 45.95MiB (45.95 MiB)  | 46.2MiB (46.20 MiB)  | 46.19MiB (46.19 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.32MiB (46.32 MiB)  | 45.82MiB (45.82 MiB)  | 45.37MiB (45.37 MiB)  | 47.82MiB (47.82 MiB)  | 46.53MiB (46.53 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.55MiB (45.55 MiB)  | 46.58MiB (46.58 MiB)  | 45.68MiB (45.68 MiB)  | 48.18MiB (48.18 MiB)  | 46.27MiB (46.27 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.37MiB (27.37 MiB)  | 27.2MiB (27.20 MiB)  | 27.4MiB (27.40 MiB)  | 28.44MiB (28.44 MiB)  | 28.09MiB (28.09 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |11.14% | 8.30% | 11.65% | 12.59% | 12.52% | **11.24%** |
| **exp-vulnerable-mongo-db-1** |14.57% | 17.64% | 14.26% | 15.57% | 14.64% | **15.34%** |
| **exp-vulnerable-ms-catalogo-1** |0.83% | 0.00% | 0.87% | 0.87% | 0.87% | **0.69%** |
| **exp-vulnerable-ms-ordenes-1** |0.90% | 1.67% | 0.86% | 0.90% | 0.93% | **1.05%** |
| **exp-vulnerable-ms-resenas-1** |0.90% | 2.02% | 0.85% | 0.98% | 0.96% | **1.14%** |
| **exp-vulnerable-ms-usuarios-1** |0.91% | 0.76% | 0.88% | 0.98% | 0.79% | **0.86%** |
| **exp-vulnerable-postgres-db-1** |1.12% | 0.94% | 1.14% | 1.11% | 1.05% | **1.07%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |95.93 MiB | 70.36 MiB | 96.71 MiB | 96.85 MiB | 94.46 MiB | **90.86 MiB** |
| **exp-vulnerable-mongo-db-1** |199.16 MiB | 188.10 MiB | 200.49 MiB | 201.67 MiB | 202.67 MiB | **198.42 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.65 MiB | 46.11 MiB | 45.98 MiB | 45.30 MiB | 45.86 MiB | **45.98 MiB** |
| **exp-vulnerable-ms-ordenes-1** |54.61 MiB | 45.92 MiB | 45.81 MiB | 46.04 MiB | 45.96 MiB | **47.67 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.20 MiB | 45.77 MiB | 45.25 MiB | 47.68 MiB | 46.42 MiB | **46.26 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.42 MiB | 46.57 MiB | 45.56 MiB | 46.19 MiB | 46.15 MiB | **45.98 MiB** |
| **exp-vulnerable-postgres-db-1** |27.31 MiB | 27.20 MiB | 27.35 MiB | 27.35 MiB | 27.36 MiB | **27.31 MiB** |