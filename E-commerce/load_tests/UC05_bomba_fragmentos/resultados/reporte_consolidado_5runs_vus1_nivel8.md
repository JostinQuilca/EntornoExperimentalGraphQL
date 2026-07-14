# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 04:22:42

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 44 | 376.087 ms | 0.00% | 0.00% |
| Run 2 | 47 | 293.643 ms | 0.00% | 0.00% |
| Run 3 | 47 | 288.712 ms | 0.00% | 0.00% |
| Run 4 | 46 | 302.013 ms | 0.00% | 0.00% |
| Run 5 | 47 | 289.382 ms | 0.00% | 0.00% |
| **PROMEDIO** | **46.2** | **309.967 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |49.42% | 40.00% | 33.77% | 25.77% | 23.39% | **34.47%** |
| **exp-vulnerable-mongo-db-1** |100.72% | 81.07% | 70.66% | 74.87% | 73.54% | **80.17%** |
| **exp-vulnerable-ms-catalogo-1** |5.41% | 3.68% | 3.87% | 4.55% | 4.08% | **4.32%** |
| **exp-vulnerable-ms-ordenes-1** |4.71% | 4.12% | 4.51% | 4.69% | 3.96% | **4.40%** |
| **exp-vulnerable-ms-resenas-1** |4.47% | 4.20% | 4.38% | 4.35% | 3.94% | **4.27%** |
| **exp-vulnerable-ms-usuarios-1** |65.66% | 37.74% | 39.21% | 37.40% | 32.10% | **42.42%** |
| **exp-vulnerable-postgres-db-1** |8.63% | 5.82% | 5.24% | 6.27% | 5.18% | **6.23%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |119.3MiB (119.30 MiB)  | 179.5MiB (179.50 MiB)  | 180MiB (180.00 MiB)  | 109.4MiB (109.40 MiB)  | 106.8MiB (106.80 MiB)  |
| **exp-vulnerable-mongo-db-1** |343.5MiB (343.50 MiB)  | 342.4MiB (342.40 MiB)  | 305.2MiB (305.20 MiB)  | 347.7MiB (347.70 MiB)  | 347.8MiB (347.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.14MiB (46.14 MiB)  | 47.03MiB (47.03 MiB)  | 45.6MiB (45.60 MiB)  | 46.55MiB (46.55 MiB)  | 46.11MiB (46.11 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.81MiB (45.81 MiB)  | 53.98MiB (53.98 MiB)  | 47.13MiB (47.13 MiB)  | 46.73MiB (46.73 MiB)  | 45.7MiB (45.70 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47.72MiB (47.72 MiB)  | 46.22MiB (46.22 MiB)  | 45.34MiB (45.34 MiB)  | 47.51MiB (47.51 MiB)  | 47MiB (47.00 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |135.7MiB (135.70 MiB)  | 135.1MiB (135.10 MiB)  | 128.9MiB (128.90 MiB)  | 126.7MiB (126.70 MiB)  | 129.4MiB (129.40 MiB)  |
| **exp-vulnerable-postgres-db-1** |30.93MiB (30.93 MiB)  | 30.58MiB (30.58 MiB)  | 30.2MiB (30.20 MiB)  | 30.17MiB (30.17 MiB)  | 30.29MiB (30.29 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |12.75% | 11.29% | 12.04% | 12.09% | 12.29% | **12.09%** |
| **exp-vulnerable-mongo-db-1** |28.73% | 21.97% | 17.05% | 20.24% | 22.34% | **22.07%** |
| **exp-vulnerable-ms-catalogo-1** |1.38% | 0.90% | 0.91% | 1.06% | 1.08% | **1.07%** |
| **exp-vulnerable-ms-ordenes-1** |1.25% | 1.00% | 1.18% | 1.15% | 1.14% | **1.14%** |
| **exp-vulnerable-ms-resenas-1** |1.37% | 1.01% | 1.16% | 1.07% | 1.16% | **1.15%** |
| **exp-vulnerable-ms-usuarios-1** |19.93% | 19.55% | 18.26% | 19.13% | 17.32% | **18.84%** |
| **exp-vulnerable-postgres-db-1** |2.34% | 1.91% | 1.76% | 1.91% | 1.75% | **1.93%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |109.21 MiB | 119.18 MiB | 118.40 MiB | 100.53 MiB | 99.66 MiB | **109.40 MiB** |
| **exp-vulnerable-mongo-db-1** |216.24 MiB | 204.08 MiB | 197.79 MiB | 213.42 MiB | 211.24 MiB | **208.55 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.02 MiB | 46.89 MiB | 45.40 MiB | 46.43 MiB | 45.98 MiB | **46.14 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.69 MiB | 48.24 MiB | 47.01 MiB | 46.25 MiB | 45.58 MiB | **46.55 MiB** |
| **exp-vulnerable-ms-resenas-1** |47.60 MiB | 46.10 MiB | 45.23 MiB | 46.05 MiB | 46.89 MiB | **46.37 MiB** |
| **exp-vulnerable-ms-usuarios-1** |121.27 MiB | 125.66 MiB | 121.16 MiB | 118.59 MiB | 118.60 MiB | **121.06 MiB** |
| **exp-vulnerable-postgres-db-1** |30.20 MiB | 30.23 MiB | 30.18 MiB | 30.15 MiB | 30.09 MiB | **30.17 MiB** |