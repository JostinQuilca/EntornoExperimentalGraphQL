# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 04:02:43

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 46 | 302.630 ms | 0.00% | 0.00% |
| Run 2 | 47 | 280.428 ms | 0.00% | 0.00% |
| Run 3 | 47 | 291.208 ms | 0.00% | 0.00% |
| Run 4 | 46 | 316.152 ms | 0.00% | 0.00% |
| Run 5 | 47 | 286.947 ms | 0.00% | 0.00% |
| **PROMEDIO** | **46.6** | **295.473 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |41.72% | 19.93% | 31.53% | 34.16% | 33.20% | **32.11%** |
| **exp-vulnerable-mongo-db-1** |89.48% | 78.66% | 122.59% | 83.86% | 82.96% | **91.51%** |
| **exp-vulnerable-ms-catalogo-1** |4.50% | 7.58% | 3.75% | 5.02% | 4.45% | **5.06%** |
| **exp-vulnerable-ms-ordenes-1** |9.34% | 5.83% | 3.93% | 6.86% | 4.83% | **6.16%** |
| **exp-vulnerable-ms-resenas-1** |4.63% | 5.43% | 4.20% | 8.47% | 4.69% | **5.48%** |
| **exp-vulnerable-ms-usuarios-1** |60.56% | 40.26% | 38.75% | 43.69% | 40.03% | **44.66%** |
| **exp-vulnerable-postgres-db-1** |6.01% | 17.18% | 6.01% | 15.00% | 6.19% | **10.08%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |181.5MiB (181.50 MiB)  | 187.3MiB (187.30 MiB)  | 106.1MiB (106.10 MiB)  | 179.4MiB (179.40 MiB)  | 106.3MiB (106.30 MiB)  |
| **exp-vulnerable-mongo-db-1** |342.6MiB (342.60 MiB)  | 341.8MiB (341.80 MiB)  | 351.6MiB (351.60 MiB)  | 343.1MiB (343.10 MiB)  | 351.8MiB (351.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.95MiB (45.95 MiB)  | 48.37MiB (48.37 MiB)  | 47.86MiB (47.86 MiB)  | 46.75MiB (46.75 MiB)  | 47.95MiB (47.95 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |53.52MiB (53.52 MiB)  | 46.8MiB (46.80 MiB)  | 46.79MiB (46.79 MiB)  | 45.25MiB (45.25 MiB)  | 45.72MiB (45.72 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.2MiB (46.20 MiB)  | 47.05MiB (47.05 MiB)  | 46.33MiB (46.33 MiB)  | 47.36MiB (47.36 MiB)  | 46.57MiB (46.57 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |127.3MiB (127.30 MiB)  | 129.9MiB (129.90 MiB)  | 131.9MiB (131.90 MiB)  | 129.2MiB (129.20 MiB)  | 130.9MiB (130.90 MiB)  |
| **exp-vulnerable-postgres-db-1** |30.21MiB (30.21 MiB)  | 32.39MiB (32.39 MiB)  | 30.22MiB (30.22 MiB)  | 30.48MiB (30.48 MiB)  | 30.39MiB (30.39 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |12.61% | 9.29% | 13.87% | 11.62% | 13.11% | **12.10%** |
| **exp-vulnerable-mongo-db-1** |24.19% | 21.99% | 24.06% | 17.76% | 22.16% | **22.03%** |
| **exp-vulnerable-ms-catalogo-1** |1.02% | 1.25% | 0.95% | 1.18% | 1.07% | **1.09%** |
| **exp-vulnerable-ms-ordenes-1** |1.39% | 1.18% | 1.12% | 1.40% | 1.13% | **1.24%** |
| **exp-vulnerable-ms-resenas-1** |1.04% | 1.23% | 1.15% | 1.48% | 1.17% | **1.21%** |
| **exp-vulnerable-ms-usuarios-1** |22.01% | 18.62% | 18.45% | 18.03% | 19.34% | **19.29%** |
| **exp-vulnerable-postgres-db-1** |1.95% | 2.32% | 2.01% | 2.32% | 1.88% | **2.10%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |131.21 MiB | 138.16 MiB | 100.73 MiB | 129.12 MiB | 100.65 MiB | **119.97 MiB** |
| **exp-vulnerable-mongo-db-1** |200.18 MiB | 209.13 MiB | 207.01 MiB | 213.26 MiB | 215.94 MiB | **209.10 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.83 MiB | 47.73 MiB | 47.73 MiB | 46.63 MiB | 46.24 MiB | **46.83 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.30 MiB | 46.68 MiB | 45.57 MiB | 45.14 MiB | 45.62 MiB | **45.86 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.07 MiB | 46.74 MiB | 46.21 MiB | 46.16 MiB | 46.46 MiB | **46.33 MiB** |
| **exp-vulnerable-ms-usuarios-1** |120.24 MiB | 119.17 MiB | 119.48 MiB | 117.82 MiB | 120.39 MiB | **119.42 MiB** |
| **exp-vulnerable-postgres-db-1** |30.18 MiB | 30.27 MiB | 30.20 MiB | 30.09 MiB | 30.14 MiB | **30.18 MiB** |