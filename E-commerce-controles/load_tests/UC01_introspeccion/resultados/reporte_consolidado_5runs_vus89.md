# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=89)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 20:31:32

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 5340 | 10.705 ms | 0.00% |
| Run 2 | 5340 | 9.459 ms | 0.00% |
| Run 3 | 5340 | 11.169 ms | 0.00% |
| Run 4 | 5340 | 9.330 ms | 0.00% |
| Run 5 | 5340 | 9.165 ms | 0.00% |
| **PROMEDIO** | **5340.0** | **9.965 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |35.18% | 35.33% | 46.94% | 34.30% | 38.42% | **38.03%** |
| **exp-protegido-mongo-db-1** |58.45% | 57.74% | 67.39% | 64.98% | 56.94% | **61.10%** |
| **exp-protegido-ms-catalogo-1** |3.30% | 3.42% | 4.67% | 3.04% | 3.18% | **3.52%** |
| **exp-protegido-ms-ordenes-1** |3.40% | 3.31% | 3.42% | 3.80% | 3.10% | **3.41%** |
| **exp-protegido-ms-resenas-1** |3.74% | 3.45% | 3.21% | 3.61% | 3.00% | **3.40%** |
| **exp-protegido-ms-usuarios-1** |10.34% | 3.19% | 3.35% | 3.53% | 2.99% | **4.68%** |
| **exp-protegido-postgres-db-1** |3.86% | 4.53% | 3.89% | 4.29% | 4.47% | **4.21%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |106.4MiB (106.40 MiB)  | 103.5MiB (103.50 MiB)  | 103.7MiB (103.70 MiB)  | 105MiB (105.00 MiB)  | 104.9MiB (104.90 MiB)  |
| **exp-protegido-mongo-db-1** |332.1MiB (332.10 MiB)  | 328.9MiB (328.90 MiB)  | 349.2MiB (349.20 MiB)  | 347.5MiB (347.50 MiB)  | 348.5MiB (348.50 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.82MiB (45.82 MiB)  | 47.57MiB (47.57 MiB)  | 45.68MiB (45.68 MiB)  | 47.63MiB (47.63 MiB)  | 46.14MiB (46.14 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.53MiB (45.53 MiB)  | 45.89MiB (45.89 MiB)  | 46.09MiB (46.09 MiB)  | 46.04MiB (46.04 MiB)  | 46.59MiB (46.59 MiB)  |
| **exp-protegido-ms-resenas-1** |47.18MiB (47.18 MiB)  | 46.54MiB (46.54 MiB)  | 47.96MiB (47.96 MiB)  | 46.43MiB (46.43 MiB)  | 46.08MiB (46.08 MiB)  |
| **exp-protegido-ms-usuarios-1** |55.05MiB (55.05 MiB)  | 46.16MiB (46.16 MiB)  | 45.97MiB (45.97 MiB)  | 46.88MiB (46.88 MiB)  | 45.71MiB (45.71 MiB)  |
| **exp-protegido-postgres-db-1** |27.38MiB (27.38 MiB)  | 28.49MiB (28.49 MiB)  | 27.41MiB (27.41 MiB)  | 27.38MiB (27.38 MiB)  | 27.46MiB (27.46 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |24.69% | 23.23% | 25.09% | 21.64% | 22.28% | **23.39%** |
| **exp-protegido-mongo-db-1** |17.47% | 16.70% | 18.01% | 15.76% | 16.04% | **16.80%** |
| **exp-protegido-ms-catalogo-1** |0.81% | 0.98% | 0.90% | 0.92% | 0.89% | **0.90%** |
| **exp-protegido-ms-ordenes-1** |0.95% | 0.87% | 0.86% | 0.89% | 0.78% | **0.87%** |
| **exp-protegido-ms-resenas-1** |0.97% | 0.87% | 0.79% | 0.96% | 0.70% | **0.86%** |
| **exp-protegido-ms-usuarios-1** |1.23% | 0.74% | 0.84% | 0.97% | 0.74% | **0.90%** |
| **exp-protegido-postgres-db-1** |1.10% | 1.03% | 0.99% | 1.01% | 1.14% | **1.05%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |104.90 MiB | 98.51 MiB | 98.11 MiB | 99.57 MiB | 99.71 MiB | **100.16 MiB** |
| **exp-protegido-mongo-db-1** |195.88 MiB | 191.18 MiB | 202.48 MiB | 202.66 MiB | 200.21 MiB | **198.48 MiB** |
| **exp-protegido-ms-catalogo-1** |45.69 MiB | 47.22 MiB | 45.52 MiB | 45.16 MiB | 46.00 MiB | **45.92 MiB** |
| **exp-protegido-ms-ordenes-1** |45.42 MiB | 45.78 MiB | 45.99 MiB | 45.94 MiB | 46.49 MiB | **45.92 MiB** |
| **exp-protegido-ms-resenas-1** |47.06 MiB | 46.43 MiB | 46.37 MiB | 46.33 MiB | 45.98 MiB | **46.43 MiB** |
| **exp-protegido-ms-usuarios-1** |48.81 MiB | 46.07 MiB | 45.87 MiB | 46.78 MiB | 45.61 MiB | **46.63 MiB** |
| **exp-protegido-postgres-db-1** |27.31 MiB | 27.46 MiB | 27.35 MiB | 27.38 MiB | 27.42 MiB | **27.38 MiB** |