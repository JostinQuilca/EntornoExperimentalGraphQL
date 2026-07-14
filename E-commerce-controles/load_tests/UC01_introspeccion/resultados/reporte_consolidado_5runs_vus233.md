# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=233)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 21:38:12

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 13906 | 13.833 ms | 0.10% |
| Run 2 | 13915 | 12.660 ms | 0.13% |
| Run 3 | 13916 | 12.419 ms | 0.06% |
| Run 4 | 0 | 0.000 ms | 0.00% |
| Run 5 | 13895 | 13.748 ms | 0.19% |
| **PROMEDIO** | **11126.4** | **10.532 ms** | **0.10%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |96.36% | 77.46% | 87.39% | 102.59% | 79.04% | **88.57%** |
| **exp-protegido-mongo-db-1** |89.77% | 81.07% | 63.72% | 103.78% | 57.28% | **79.12%** |
| **exp-protegido-ms-catalogo-1** |3.98% | 2.89% | 3.30% | 3.72% | 3.06% | **3.39%** |
| **exp-protegido-ms-ordenes-1** |4.55% | 5.04% | 3.04% | 5.22% | 3.37% | **4.24%** |
| **exp-protegido-ms-resenas-1** |4.48% | 4.58% | 3.42% | 4.99% | 3.29% | **4.15%** |
| **exp-protegido-ms-usuarios-1** |5.50% | 5.10% | 3.47% | 4.65% | 3.55% | **4.45%** |
| **exp-protegido-postgres-db-1** |4.29% | 4.22% | 3.81% | 2.71% | 3.98% | **3.80%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |144.1MiB (144.10 MiB)  | 129MiB (129.00 MiB)  | 119.7MiB (119.70 MiB)  | 108.7MiB (108.70 MiB)  | 131.1MiB (131.10 MiB)  |
| **exp-protegido-mongo-db-1** |343.5MiB (343.50 MiB)  | 342.9MiB (342.90 MiB)  | 338.7MiB (338.70 MiB)  | 341.6MiB (341.60 MiB)  | 341MiB (341.00 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.87MiB (46.87 MiB)  | 47.14MiB (47.14 MiB)  | 47.23MiB (47.23 MiB)  | 45.83MiB (45.83 MiB)  | 46.13MiB (46.13 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.27MiB (45.27 MiB)  | 45.95MiB (45.95 MiB)  | 54.68MiB (54.68 MiB)  | 45.2MiB (45.20 MiB)  | 46.23MiB (46.23 MiB)  |
| **exp-protegido-ms-resenas-1** |44.87MiB (44.87 MiB)  | 47.21MiB (47.21 MiB)  | 46.23MiB (46.23 MiB)  | 45.16MiB (45.16 MiB)  | 48.04MiB (48.04 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.49MiB (45.49 MiB)  | 45.9MiB (45.90 MiB)  | 45.63MiB (45.63 MiB)  | 46.6MiB (46.60 MiB)  | 49.69MiB (49.69 MiB)  |
| **exp-protegido-postgres-db-1** |28MiB (28.00 MiB)  | 27.96MiB (27.96 MiB)  | 28MiB (28.00 MiB)  | 27.98MiB (27.98 MiB)  | 27.97MiB (27.97 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |49.71% | 48.48% | 49.92% | 54.43% | 46.51% | **49.81%** |
| **exp-protegido-mongo-db-1** |22.89% | 18.42% | 18.55% | 25.23% | 16.56% | **20.33%** |
| **exp-protegido-ms-catalogo-1** |0.96% | 0.76% | 0.85% | 1.72% | 0.85% | **1.03%** |
| **exp-protegido-ms-ordenes-1** |1.12% | 0.88% | 0.89% | 1.28% | 0.93% | **1.02%** |
| **exp-protegido-ms-resenas-1** |1.01% | 0.90% | 0.93% | 1.24% | 0.84% | **0.98%** |
| **exp-protegido-ms-usuarios-1** |1.12% | 0.81% | 0.94% | 1.17% | 0.97% | **1.00%** |
| **exp-protegido-postgres-db-1** |1.24% | 1.25% | 1.13% | 0.48% | 1.19% | **1.06%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |120.71 MiB | 110.83 MiB | 108.16 MiB | 97.38 MiB | 112.04 MiB | **109.82 MiB** |
| **exp-protegido-mongo-db-1** |202.44 MiB | 204.23 MiB | 198.86 MiB | 237.43 MiB | 198.18 MiB | **208.23 MiB** |
| **exp-protegido-ms-catalogo-1** |45.55 MiB | 47.04 MiB | 47.12 MiB | 45.79 MiB | 46.02 MiB | **46.30 MiB** |
| **exp-protegido-ms-ordenes-1** |45.14 MiB | 45.85 MiB | 50.72 MiB | 45.17 MiB | 45.98 MiB | **46.57 MiB** |
| **exp-protegido-ms-resenas-1** |44.73 MiB | 47.11 MiB | 46.13 MiB | 45.13 MiB | 45.93 MiB | **45.81 MiB** |
| **exp-protegido-ms-usuarios-1** |45.36 MiB | 45.80 MiB | 45.53 MiB | 46.57 MiB | 47.82 MiB | **46.22 MiB** |
| **exp-protegido-postgres-db-1** |27.83 MiB | 27.96 MiB | 27.99 MiB | 27.97 MiB | 27.96 MiB | **27.94 MiB** |