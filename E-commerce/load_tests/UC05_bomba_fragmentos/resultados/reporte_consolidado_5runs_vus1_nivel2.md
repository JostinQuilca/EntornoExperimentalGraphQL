# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 03:22:29

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 45 | 341.324 ms | 0.00% | 0.00% |
| Run 2 | 47 | 296.370 ms | 0.00% | 0.00% |
| Run 3 | 46 | 307.908 ms | 0.00% | 0.00% |
| Run 4 | 47 | 294.008 ms | 0.00% | 0.00% |
| Run 5 | 45 | 329.066 ms | 0.00% | 0.00% |
| **PROMEDIO** | **46.0** | **313.735 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |28.03% | 28.28% | 35.90% | 37.00% | 34.81% | **32.80%** |
| **exp-vulnerable-mongo-db-1** |81.43% | 92.95% | 93.24% | 82.95% | 95.58% | **89.23%** |
| **exp-vulnerable-ms-catalogo-1** |4.40% | 4.43% | 4.23% | 4.00% | 5.53% | **4.52%** |
| **exp-vulnerable-ms-ordenes-1** |7.16% | 4.92% | 7.96% | 15.71% | 6.26% | **8.40%** |
| **exp-vulnerable-ms-resenas-1** |5.63% | 4.69% | 5.34% | 19.68% | 5.26% | **8.12%** |
| **exp-vulnerable-ms-usuarios-1** |49.59% | 38.81% | 36.05% | 75.86% | 39.46% | **47.95%** |
| **exp-vulnerable-postgres-db-1** |7.01% | 6.29% | 5.63% | 12.44% | 7.87% | **7.85%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |109.3MiB (109.30 MiB)  | 178.7MiB (178.70 MiB)  | 179.9MiB (179.90 MiB)  | 179.4MiB (179.40 MiB)  | 106.2MiB (106.20 MiB)  |
| **exp-vulnerable-mongo-db-1** |325.2MiB (325.20 MiB)  | 350.1MiB (350.10 MiB)  | 346.3MiB (346.30 MiB)  | 345.7MiB (345.70 MiB)  | 344.4MiB (344.40 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |47.45MiB (47.45 MiB)  | 45.82MiB (45.82 MiB)  | 45.64MiB (45.64 MiB)  | 46.24MiB (46.24 MiB)  | 45.84MiB (45.84 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |53.76MiB (53.76 MiB)  | 46.04MiB (46.04 MiB)  | 48.06MiB (48.06 MiB)  | 48.49MiB (48.49 MiB)  | 46.61MiB (46.61 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47.03MiB (47.03 MiB)  | 45.95MiB (45.95 MiB)  | 45.54MiB (45.54 MiB)  | 49.17MiB (49.17 MiB)  | 46.84MiB (46.84 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |129.9MiB (129.90 MiB)  | 125.2MiB (125.20 MiB)  | 129.9MiB (129.90 MiB)  | 127.1MiB (127.10 MiB)  | 157.7MiB (157.70 MiB)  |
| **exp-vulnerable-postgres-db-1** |30.19MiB (30.19 MiB)  | 31.87MiB (31.87 MiB)  | 31.39MiB (31.39 MiB)  | 30.17MiB (30.17 MiB)  | 30.15MiB (30.15 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |13.07% | 9.38% | 10.69% | 10.40% | 13.71% | **11.45%** |
| **exp-vulnerable-mongo-db-1** |14.53% | 21.31% | 22.70% | 21.71% | 28.13% | **21.68%** |
| **exp-vulnerable-ms-catalogo-1** |1.24% | 1.16% | 1.07% | 1.01% | 1.37% | **1.17%** |
| **exp-vulnerable-ms-ordenes-1** |1.67% | 1.18% | 1.51% | 1.60% | 1.35% | **1.46%** |
| **exp-vulnerable-ms-resenas-1** |1.33% | 1.20% | 1.41% | 1.76% | 1.39% | **1.42%** |
| **exp-vulnerable-ms-usuarios-1** |21.07% | 18.86% | 17.73% | 20.20% | 19.73% | **19.52%** |
| **exp-vulnerable-postgres-db-1** |2.07% | 2.00% | 2.10% | 2.31% | 2.21% | **2.14%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |101.22 MiB | 121.51 MiB | 123.77 MiB | 126.50 MiB | 100.90 MiB | **114.78 MiB** |
| **exp-vulnerable-mongo-db-1** |208.85 MiB | 212.64 MiB | 212.28 MiB | 208.92 MiB | 205.81 MiB | **209.70 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.93 MiB | 45.70 MiB | 45.53 MiB | 46.11 MiB | 45.73 MiB | **46.00 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.65 MiB | 45.93 MiB | 46.58 MiB | 47.04 MiB | 46.50 MiB | **46.74 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.90 MiB | 45.83 MiB | 45.43 MiB | 47.72 MiB | 46.52 MiB | **46.48 MiB** |
| **exp-vulnerable-ms-usuarios-1** |120.08 MiB | 118.37 MiB | 120.61 MiB | 119.36 MiB | 126.92 MiB | **121.07 MiB** |
| **exp-vulnerable-postgres-db-1** |30.17 MiB | 30.23 MiB | 30.33 MiB | 30.16 MiB | 30.12 MiB | **30.20 MiB** |