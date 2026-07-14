# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 23:17:27

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 300 | 7.300 ms | 0.00% |
| Run 2 | 300 | 7.321 ms | 0.00% |
| Run 3 | 300 | 6.555 ms | 0.00% |
| Run 4 | 300 | 6.394 ms | 0.00% |
| Run 5 | 300 | 6.120 ms | 0.00% |
| **PROMEDIO** | **300.0** | **6.738 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |5.18% | 12.79% | 7.74% | 10.70% | 6.76% | **8.63%** |
| **exp-protegido-mongo-db-1** |57.15% | 59.88% | 47.15% | 56.06% | 52.24% | **54.50%** |
| **exp-protegido-ms-catalogo-1** |4.19% | 3.67% | 3.59% | 3.80% | 3.34% | **3.72%** |
| **exp-protegido-ms-ordenes-1** |3.84% | 3.83% | 3.93% | 2.98% | 3.88% | **3.69%** |
| **exp-protegido-ms-resenas-1** |3.42% | 3.67% | 3.21% | 3.25% | 3.70% | **3.45%** |
| **exp-protegido-ms-usuarios-1** |2.86% | 3.45% | 3.01% | 3.00% | 5.99% | **3.66%** |
| **exp-protegido-postgres-db-1** |5.82% | 4.68% | 5.28% | 4.03% | 5.67% | **5.10%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |74.82MiB (74.82 MiB)  | 75.23MiB (75.23 MiB)  | 75.55MiB (75.55 MiB)  | 74.43MiB (74.43 MiB)  | 75.23MiB (75.23 MiB)  |
| **exp-protegido-mongo-db-1** |327MiB (327.00 MiB)  | 338.9MiB (338.90 MiB)  | 330.4MiB (330.40 MiB)  | 333.4MiB (333.40 MiB)  | 330.2MiB (330.20 MiB)  |
| **exp-protegido-ms-catalogo-1** |47.92MiB (47.92 MiB)  | 47.64MiB (47.64 MiB)  | 46.16MiB (46.16 MiB)  | 45.68MiB (45.68 MiB)  | 45.9MiB (45.90 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.52MiB (45.52 MiB)  | 46.91MiB (46.91 MiB)  | 46.59MiB (46.59 MiB)  | 47.23MiB (47.23 MiB)  | 45.54MiB (45.54 MiB)  |
| **exp-protegido-ms-resenas-1** |46.75MiB (46.75 MiB)  | 48.34MiB (48.34 MiB)  | 46.33MiB (46.33 MiB)  | 46.46MiB (46.46 MiB)  | 46.22MiB (46.22 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.69MiB (45.69 MiB)  | 46.09MiB (46.09 MiB)  | 45.76MiB (45.76 MiB)  | 47.1MiB (47.10 MiB)  | 54.13MiB (54.13 MiB)  |
| **exp-protegido-postgres-db-1** |28.02MiB (28.02 MiB)  | 27.98MiB (27.98 MiB)  | 27.97MiB (27.97 MiB)  | 27.98MiB (27.98 MiB)  | 27.93MiB (27.93 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.34% | 2.77% | 2.32% | 2.28% | 2.10% | **2.36%** |
| **exp-protegido-mongo-db-1** |15.89% | 16.85% | 13.79% | 15.78% | 15.45% | **15.55%** |
| **exp-protegido-ms-catalogo-1** |0.86% | 1.06% | 0.88% | 0.93% | 0.89% | **0.92%** |
| **exp-protegido-ms-ordenes-1** |0.93% | 0.96% | 0.98% | 0.73% | 0.87% | **0.89%** |
| **exp-protegido-ms-resenas-1** |0.87% | 0.96% | 0.85% | 0.86% | 0.82% | **0.87%** |
| **exp-protegido-ms-usuarios-1** |0.83% | 0.91% | 0.87% | 0.79% | 1.03% | **0.89%** |
| **exp-protegido-postgres-db-1** |1.36% | 1.30% | 1.22% | 1.13% | 1.21% | **1.24%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |70.74 MiB | 69.91 MiB | 70.61 MiB | 69.19 MiB | 70.68 MiB | **70.23 MiB** |
| **exp-protegido-mongo-db-1** |195.34 MiB | 201.25 MiB | 191.31 MiB | 195.89 MiB | 194.62 MiB | **195.68 MiB** |
| **exp-protegido-ms-catalogo-1** |46.10 MiB | 47.54 MiB | 46.06 MiB | 45.57 MiB | 45.78 MiB | **46.21 MiB** |
| **exp-protegido-ms-ordenes-1** |45.39 MiB | 45.50 MiB | 46.23 MiB | 45.47 MiB | 45.44 MiB | **45.61 MiB** |
| **exp-protegido-ms-resenas-1** |46.62 MiB | 46.79 MiB | 46.24 MiB | 46.10 MiB | 46.12 MiB | **46.37 MiB** |
| **exp-protegido-ms-usuarios-1** |45.55 MiB | 44.96 MiB | 45.67 MiB | 46.15 MiB | 46.93 MiB | **45.85 MiB** |
| **exp-protegido-postgres-db-1** |27.89 MiB | 27.97 MiB | 27.96 MiB | 27.97 MiB | 27.92 MiB | **27.94 MiB** |