# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=144)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 20:48:31

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 8640 | 10.407 ms | 0.00% |
| Run 2 | 8640 | 9.933 ms | 0.00% |
| Run 3 | 8640 | 10.488 ms | 0.00% |
| Run 4 | 8640 | 10.500 ms | 0.00% |
| Run 5 | 8634 | 11.124 ms | 0.00% |
| **PROMEDIO** | **8638.8** | **10.490 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |49.61% | 49.57% | 49.97% | 44.84% | 44.07% | **47.61%** |
| **exp-vulnerable-mongo-db-1** |58.76% | 57.69% | 58.61% | 63.44% | 72.61% | **62.22%** |
| **exp-vulnerable-ms-catalogo-1** |2.93% | 6.38% | 4.28% | 3.81% | 3.84% | **4.25%** |
| **exp-vulnerable-ms-ordenes-1** |3.40% | 3.87% | 4.56% | 3.90% | 4.90% | **4.13%** |
| **exp-vulnerable-ms-resenas-1** |8.11% | 3.80% | 3.88% | 3.22% | 4.58% | **4.72%** |
| **exp-vulnerable-ms-usuarios-1** |3.03% | 4.20% | 4.17% | 3.55% | 3.86% | **3.76%** |
| **exp-vulnerable-postgres-db-1** |4.24% | 4.99% | 5.92% | 3.66% | 4.45% | **4.65%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |107.9MiB (107.90 MiB)  | 107.9MiB (107.90 MiB)  | 105.2MiB (105.20 MiB)  | 104.9MiB (104.90 MiB)  | 110.5MiB (110.50 MiB)  |
| **exp-vulnerable-mongo-db-1** |340.6MiB (340.60 MiB)  | 337.3MiB (337.30 MiB)  | 339.6MiB (339.60 MiB)  | 341.2MiB (341.20 MiB)  | 340.9MiB (340.90 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.85MiB (45.85 MiB)  | 45.75MiB (45.75 MiB)  | 45.69MiB (45.69 MiB)  | 47.2MiB (47.20 MiB)  | 46.05MiB (46.05 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.94MiB (45.94 MiB)  | 47.52MiB (47.52 MiB)  | 46.79MiB (46.79 MiB)  | 46.74MiB (46.74 MiB)  | 45.57MiB (45.57 MiB)  |
| **exp-vulnerable-ms-resenas-1** |54.73MiB (54.73 MiB)  | 47.95MiB (47.95 MiB)  | 54.3MiB (54.30 MiB)  | 47.55MiB (47.55 MiB)  | 46.71MiB (46.71 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |46.08MiB (46.08 MiB)  | 46.54MiB (46.54 MiB)  | 47.16MiB (47.16 MiB)  | 46.88MiB (46.88 MiB)  | 45.21MiB (45.21 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.45MiB (27.45 MiB)  | 27.35MiB (27.35 MiB)  | 28.67MiB (28.67 MiB)  | 27.4MiB (27.40 MiB)  | 27.39MiB (27.39 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |28.32% | 28.91% | 27.25% | 25.65% | 27.70% | **27.57%** |
| **exp-vulnerable-mongo-db-1** |13.31% | 18.54% | 16.17% | 16.28% | 17.73% | **16.41%** |
| **exp-vulnerable-ms-catalogo-1** |0.82% | 0.88% | 0.88% | 0.86% | 0.83% | **0.85%** |
| **exp-vulnerable-ms-ordenes-1** |1.07% | 0.89% | 0.98% | 0.87% | 0.99% | **0.96%** |
| **exp-vulnerable-ms-resenas-1** |1.28% | 0.98% | 0.96% | 0.93% | 0.94% | **1.02%** |
| **exp-vulnerable-ms-usuarios-1** |1.03% | 1.04% | 0.96% | 0.84% | 0.92% | **0.96%** |
| **exp-vulnerable-postgres-db-1** |1.07% | 1.29% | 1.24% | 1.13% | 1.21% | **1.19%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |101.77 MiB | 102.30 MiB | 100.19 MiB | 100.18 MiB | 103.70 MiB | **101.63 MiB** |
| **exp-vulnerable-mongo-db-1** |202.85 MiB | 198.98 MiB | 193.17 MiB | 200.27 MiB | 199.08 MiB | **198.87 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.72 MiB | 45.62 MiB | 45.56 MiB | 47.08 MiB | 45.92 MiB | **45.98 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.81 MiB | 45.54 MiB | 46.68 MiB | 45.78 MiB | 45.44 MiB | **45.85 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.94 MiB | 45.96 MiB | 46.16 MiB | 46.30 MiB | 46.59 MiB | **46.39 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.57 MiB | 46.43 MiB | 47.05 MiB | 45.33 MiB | 45.09 MiB | **45.89 MiB** |
| **exp-vulnerable-postgres-db-1** |27.35 MiB | 27.30 MiB | 27.36 MiB | 27.36 MiB | 27.33 MiB | **27.34 MiB** |