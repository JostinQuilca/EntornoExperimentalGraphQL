# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 22:46:48

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 180 | 6.398 ms | 0.00% |
| Run 2 | 180 | 6.154 ms | 0.00% |
| Run 3 | 180 | 6.843 ms | 0.00% |
| Run 4 | 180 | 6.097 ms | 0.00% |
| Run 5 | 180 | 6.574 ms | 0.00% |
| **PROMEDIO** | **180.0** | **6.413 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |3.97% | 3.07% | 3.45% | 3.50% | 3.52% | **3.50%** |
| **exp-vulnerable-mongo-db-1** |62.41% | 54.11% | 71.98% | 56.04% | 52.01% | **59.31%** |
| **exp-vulnerable-ms-catalogo-1** |4.28% | 3.24% | 3.73% | 4.25% | 4.21% | **3.94%** |
| **exp-vulnerable-ms-ordenes-1** |3.92% | 3.12% | 3.61% | 4.69% | 3.29% | **3.73%** |
| **exp-vulnerable-ms-resenas-1** |3.73% | 3.37% | 4.46% | 4.19% | 2.81% | **3.71%** |
| **exp-vulnerable-ms-usuarios-1** |3.57% | 3.58% | 3.81% | 3.42% | 3.01% | **3.48%** |
| **exp-vulnerable-postgres-db-1** |4.58% | 4.44% | 4.48% | 4.18% | 4.07% | **4.35%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |66.63MiB (66.63 MiB)  | 66.53MiB (66.53 MiB)  | 66.46MiB (66.46 MiB)  | 66MiB (66.00 MiB)  | 65.73MiB (65.73 MiB)  |
| **exp-vulnerable-mongo-db-1** |331.4MiB (331.40 MiB)  | 335.5MiB (335.50 MiB)  | 338.8MiB (338.80 MiB)  | 348.5MiB (348.50 MiB)  | 332.8MiB (332.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.5MiB (46.50 MiB)  | 45.7MiB (45.70 MiB)  | 47.4MiB (47.40 MiB)  | 46.6MiB (46.60 MiB)  | 46.44MiB (46.44 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.23MiB (45.23 MiB)  | 45.75MiB (45.75 MiB)  | 47.11MiB (47.11 MiB)  | 54.29MiB (54.29 MiB)  | 46.17MiB (46.17 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.95MiB (46.95 MiB)  | 46.17MiB (46.17 MiB)  | 45.84MiB (45.84 MiB)  | 47.05MiB (47.05 MiB)  | 45.52MiB (45.52 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.67MiB (45.67 MiB)  | 46.35MiB (46.35 MiB)  | 46.17MiB (46.17 MiB)  | 47.59MiB (47.59 MiB)  | 47.56MiB (47.56 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.39MiB (27.39 MiB)  | 28.8MiB (28.80 MiB)  | 28.78MiB (28.78 MiB)  | 27.33MiB (27.33 MiB)  | 27.43MiB (27.43 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.17% | 1.19% | 1.41% | 1.27% | 1.40% | **1.29%** |
| **exp-vulnerable-mongo-db-1** |16.05% | 16.69% | 18.13% | 15.99% | 14.39% | **16.25%** |
| **exp-vulnerable-ms-catalogo-1** |1.00% | 0.77% | 1.13% | 1.11% | 0.96% | **0.99%** |
| **exp-vulnerable-ms-ordenes-1** |1.06% | 0.84% | 1.02% | 1.05% | 0.75% | **0.94%** |
| **exp-vulnerable-ms-resenas-1** |0.97% | 0.88% | 1.02% | 0.99% | 0.78% | **0.93%** |
| **exp-vulnerable-ms-usuarios-1** |0.96% | 0.88% | 0.99% | 0.88% | 0.81% | **0.90%** |
| **exp-vulnerable-postgres-db-1** |1.07% | 1.28% | 1.19% | 1.23% | 1.02% | **1.16%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.08 MiB | 65.04 MiB | 65.05 MiB | 64.27 MiB | 64.30 MiB | **64.75 MiB** |
| **exp-vulnerable-mongo-db-1** |196.66 MiB | 196.18 MiB | 196.98 MiB | 201.73 MiB | 192.27 MiB | **196.76 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.39 MiB | 45.57 MiB | 45.87 MiB | 45.23 MiB | 46.33 MiB | **45.88 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.11 MiB | 45.58 MiB | 47.00 MiB | 47.36 MiB | 46.06 MiB | **46.22 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.82 MiB | 46.06 MiB | 45.72 MiB | 46.68 MiB | 45.41 MiB | **46.14 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.51 MiB | 46.19 MiB | 46.05 MiB | 45.74 MiB | 47.45 MiB | **46.19 MiB** |
| **exp-vulnerable-postgres-db-1** |27.33 MiB | 27.42 MiB | 27.36 MiB | 27.28 MiB | 27.39 MiB | **27.36 MiB** |