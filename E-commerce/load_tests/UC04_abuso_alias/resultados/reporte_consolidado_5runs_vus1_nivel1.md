# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-10 22:34:54

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 570.526 ms | 0.00% | 0.00% |
| Run 2 | 38 | 578.380 ms | 0.00% | 0.00% |
| Run 3 | 39 | 567.757 ms | 0.00% | 0.00% |
| Run 4 | 39 | 571.435 ms | 0.00% | 0.00% |
| Run 5 | 39 | 575.500 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.8** | **572.720 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |4.04% | 13.46% | 6.93% | 3.01% | 13.68% | **8.22%** |
| **exp-vulnerable-mongo-db-1** |117.62% | 111.01% | 78.43% | 89.88% | 134.34% | **106.26%** |
| **exp-vulnerable-ms-catalogo-1** |7.62% | 6.19% | 4.95% | 5.08% | 10.86% | **6.94%** |
| **exp-vulnerable-ms-ordenes-1** |6.54% | 16.66% | 5.56% | 7.34% | 8.05% | **8.83%** |
| **exp-vulnerable-ms-resenas-1** |5.21% | 10.23% | 6.27% | 4.68% | 10.07% | **7.29%** |
| **exp-vulnerable-ms-usuarios-1** |4.64% | 5.64% | 6.30% | 4.26% | 7.11% | **5.59%** |
| **exp-vulnerable-postgres-db-1** |5.59% | 9.61% | 6.76% | 6.24% | 7.56% | **7.15%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.51MiB (96.51 MiB)  | 96.36MiB (96.36 MiB)  | 95.94MiB (95.94 MiB)  | 97.38MiB (97.38 MiB)  | 96.27MiB (96.27 MiB)  |
| **exp-vulnerable-mongo-db-1** |351.2MiB (351.20 MiB)  | 343.9MiB (343.90 MiB)  | 343.6MiB (343.60 MiB)  | 349.5MiB (349.50 MiB)  | 343.2MiB (343.20 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.61MiB (46.61 MiB)  | 47.48MiB (47.48 MiB)  | 46.98MiB (46.98 MiB)  | 45.38MiB (45.38 MiB)  | 46.16MiB (46.16 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |49.01MiB (49.01 MiB)  | 48.58MiB (48.58 MiB)  | 48.98MiB (48.98 MiB)  | 48.93MiB (48.93 MiB)  | 49.3MiB (49.30 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47.73MiB (47.73 MiB)  | 45.78MiB (45.78 MiB)  | 45.45MiB (45.45 MiB)  | 46.68MiB (46.68 MiB)  | 47.06MiB (47.06 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |48.2MiB (48.20 MiB)  | 46.16MiB (46.16 MiB)  | 46.38MiB (46.38 MiB)  | 47.34MiB (47.34 MiB)  | 48.42MiB (48.42 MiB)  |
| **exp-vulnerable-postgres-db-1** |30.99MiB (30.99 MiB)  | 30.93MiB (30.93 MiB)  | 31.4MiB (31.40 MiB)  | 33.34MiB (33.34 MiB)  | 31MiB (31.00 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.76% | 0.99% | 0.72% | 0.61% | 1.03% | **0.82%** |
| **exp-vulnerable-mongo-db-1** |27.03% | 31.87% | 19.65% | 26.20% | 37.20% | **28.39%** |
| **exp-vulnerable-ms-catalogo-1** |1.36% | 1.34% | 1.26% | 1.17% | 1.51% | **1.33%** |
| **exp-vulnerable-ms-ordenes-1** |1.90% | 2.75% | 1.55% | 1.74% | 2.04% | **2.00%** |
| **exp-vulnerable-ms-resenas-1** |1.20% | 2.07% | 1.20% | 1.26% | 1.63% | **1.47%** |
| **exp-vulnerable-ms-usuarios-1** |1.14% | 1.51% | 1.21% | 1.13% | 1.56% | **1.31%** |
| **exp-vulnerable-postgres-db-1** |1.71% | 2.18% | 1.68% | 1.73% | 1.98% | **1.86%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.86 MiB | 64.97 MiB | 65.98 MiB | 65.86 MiB | 66.00 MiB | **66.13 MiB** |
| **exp-vulnerable-mongo-db-1** |220.32 MiB | 226.07 MiB | 207.17 MiB | 218.45 MiB | 220.19 MiB | **218.44 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.54 MiB | 47.35 MiB | 46.80 MiB | 45.25 MiB | 46.01 MiB | **46.19 MiB** |
| **exp-vulnerable-ms-ordenes-1** |48.30 MiB | 47.63 MiB | 48.10 MiB | 48.14 MiB | 48.48 MiB | **48.13 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.54 MiB | 45.67 MiB | 45.32 MiB | 46.53 MiB | 45.42 MiB | **45.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.80 MiB | 46.04 MiB | 46.28 MiB | 47.23 MiB | 46.86 MiB | **46.64 MiB** |
| **exp-vulnerable-postgres-db-1** |30.81 MiB | 30.73 MiB | 30.86 MiB | 30.96 MiB | 30.83 MiB | **30.84 MiB** |