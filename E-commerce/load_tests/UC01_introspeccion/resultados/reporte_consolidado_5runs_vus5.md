# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 23:06:37

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 300 | 5.739 ms | 0.00% |
| Run 2 | 300 | 5.624 ms | 0.00% |
| Run 3 | 300 | 5.456 ms | 0.00% |
| Run 4 | 300 | 6.220 ms | 0.00% |
| Run 5 | 300 | 5.722 ms | 0.00% |
| **PROMEDIO** | **300.0** | **5.752 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |4.53% | 4.94% | 7.34% | 6.68% | 4.27% | **5.55%** |
| **exp-vulnerable-mongo-db-1** |76.69% | 53.95% | 53.94% | 54.93% | 53.08% | **58.52%** |
| **exp-vulnerable-ms-catalogo-1** |5.08% | 3.29% | 3.35% | 3.15% | 3.53% | **3.68%** |
| **exp-vulnerable-ms-ordenes-1** |4.45% | 3.68% | 3.58% | 3.98% | 4.44% | **4.03%** |
| **exp-vulnerable-ms-resenas-1** |3.44% | 3.61% | 3.70% | 3.26% | 3.83% | **3.57%** |
| **exp-vulnerable-ms-usuarios-1** |3.55% | 4.01% | 3.67% | 3.47% | 4.34% | **3.81%** |
| **exp-vulnerable-postgres-db-1** |4.09% | 4.61% | 4.68% | 4.33% | 6.03% | **4.75%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |74.34MiB (74.34 MiB)  | 71.84MiB (71.84 MiB)  | 74.21MiB (74.21 MiB)  | 73.95MiB (73.95 MiB)  | 72.74MiB (72.74 MiB)  |
| **exp-vulnerable-mongo-db-1** |348.2MiB (348.20 MiB)  | 344.2MiB (344.20 MiB)  | 334.7MiB (334.70 MiB)  | 340.5MiB (340.50 MiB)  | 347.6MiB (347.60 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.88MiB (46.88 MiB)  | 46.53MiB (46.53 MiB)  | 46.12MiB (46.12 MiB)  | 47.15MiB (47.15 MiB)  | 45.98MiB (45.98 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.76MiB (45.76 MiB)  | 45.76MiB (45.76 MiB)  | 45.76MiB (45.76 MiB)  | 46.61MiB (46.61 MiB)  | 53.51MiB (53.51 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.67MiB (46.67 MiB)  | 45.88MiB (45.88 MiB)  | 47.01MiB (47.01 MiB)  | 46.15MiB (46.15 MiB)  | 45.93MiB (45.93 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.65MiB (45.65 MiB)  | 46.84MiB (46.84 MiB)  | 46.34MiB (46.34 MiB)  | 46.58MiB (46.58 MiB)  | 46.25MiB (46.25 MiB)  |
| **exp-vulnerable-postgres-db-1** |28.86MiB (28.86 MiB)  | 27.37MiB (27.37 MiB)  | 27.38MiB (27.38 MiB)  | 28.62MiB (28.62 MiB)  | 28.64MiB (28.64 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.82% | 1.98% | 1.80% | 2.31% | 1.82% | **1.95%** |
| **exp-vulnerable-mongo-db-1** |19.79% | 16.79% | 15.41% | 15.50% | 15.28% | **16.55%** |
| **exp-vulnerable-ms-catalogo-1** |1.15% | 0.97% | 0.75% | 0.76% | 0.86% | **0.90%** |
| **exp-vulnerable-ms-ordenes-1** |1.11% | 0.86% | 0.93% | 1.03% | 0.95% | **0.98%** |
| **exp-vulnerable-ms-resenas-1** |0.92% | 0.84% | 0.89% | 0.97% | 0.92% | **0.91%** |
| **exp-vulnerable-ms-usuarios-1** |0.90% | 0.87% | 0.85% | 0.96% | 0.96% | **0.91%** |
| **exp-vulnerable-postgres-db-1** |1.21% | 1.17% | 1.07% | 1.23% | 1.29% | **1.19%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |69.78 MiB | 68.52 MiB | 69.78 MiB | 69.31 MiB | 68.50 MiB | **69.18 MiB** |
| **exp-vulnerable-mongo-db-1** |202.74 MiB | 203.07 MiB | 192.65 MiB | 199.09 MiB | 203.83 MiB | **200.28 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.74 MiB | 46.42 MiB | 45.99 MiB | 45.55 MiB | 45.86 MiB | **46.11 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.64 MiB | 45.65 MiB | 45.64 MiB | 46.31 MiB | 53.48 MiB | **47.34 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.56 MiB | 45.77 MiB | 46.89 MiB | 46.01 MiB | 45.82 MiB | **46.21 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.54 MiB | 46.73 MiB | 46.22 MiB | 46.23 MiB | 46.11 MiB | **46.17 MiB** |
| **exp-vulnerable-postgres-db-1** |27.37 MiB | 27.33 MiB | 27.33 MiB | 27.44 MiB | 27.35 MiB | **27.36 MiB** |