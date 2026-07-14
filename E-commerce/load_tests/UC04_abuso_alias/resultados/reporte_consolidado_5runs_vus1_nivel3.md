# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-10 23:21:19

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 568.225 ms | 0.00% | 0.00% |
| Run 2 | 39 | 568.682 ms | 0.00% | 0.00% |
| Run 3 | 39 | 566.874 ms | 0.00% | 0.00% |
| Run 4 | 39 | 566.328 ms | 0.00% | 0.00% |
| Run 5 | 39 | 566.436 ms | 0.00% | 0.00% |
| **PROMEDIO** | **39.0** | **567.309 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |18.51% | 3.01% | 4.56% | 1.29% | 1.01% | **5.68%** |
| **exp-vulnerable-mongo-db-1** |79.91% | 79.49% | 77.73% | 75.20% | 72.71% | **77.01%** |
| **exp-vulnerable-ms-catalogo-1** |5.43% | 15.92% | 4.01% | 4.94% | 4.31% | **6.92%** |
| **exp-vulnerable-ms-ordenes-1** |5.98% | 5.44% | 6.14% | 6.08% | 4.66% | **5.66%** |
| **exp-vulnerable-ms-resenas-1** |4.80% | 4.64% | 5.34% | 5.06% | 5.24% | **5.02%** |
| **exp-vulnerable-ms-usuarios-1** |4.72% | 4.67% | 3.56% | 4.12% | 5.22% | **4.46%** |
| **exp-vulnerable-postgres-db-1** |5.56% | 4.84% | 6.14% | 5.53% | 7.44% | **5.90%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.42MiB (96.42 MiB)  | 64.3MiB (64.30 MiB)  | 65.18MiB (65.18 MiB)  | 64.77MiB (64.77 MiB)  | 65.96MiB (65.96 MiB)  |
| **exp-vulnerable-mongo-db-1** |340.4MiB (340.40 MiB)  | 352.9MiB (352.90 MiB)  | 350.4MiB (350.40 MiB)  | 349.8MiB (349.80 MiB)  | 350.1MiB (350.10 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |47.06MiB (47.06 MiB)  | 54.27MiB (54.27 MiB)  | 46.95MiB (46.95 MiB)  | 45.99MiB (45.99 MiB)  | 45.83MiB (45.83 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |49.48MiB (49.48 MiB)  | 49.87MiB (49.87 MiB)  | 49.95MiB (49.95 MiB)  | 49.35MiB (49.35 MiB)  | 49.15MiB (49.15 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.2MiB (46.20 MiB)  | 46.62MiB (46.62 MiB)  | 45.48MiB (45.48 MiB)  | 45.62MiB (45.62 MiB)  | 45.58MiB (45.58 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |46.37MiB (46.37 MiB)  | 53.86MiB (53.86 MiB)  | 46.28MiB (46.28 MiB)  | 46.08MiB (46.08 MiB)  | 46.45MiB (46.45 MiB)  |
| **exp-vulnerable-postgres-db-1** |34.73MiB (34.73 MiB)  | 34.48MiB (34.48 MiB)  | 34.35MiB (34.35 MiB)  | 35.77MiB (35.77 MiB)  | 34.29MiB (34.29 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.26% | 0.65% | 0.68% | 0.51% | 0.50% | **0.72%** |
| **exp-vulnerable-mongo-db-1** |24.84% | 19.61% | 20.33% | 22.03% | 18.77% | **21.12%** |
| **exp-vulnerable-ms-catalogo-1** |1.13% | 1.43% | 0.76% | 1.12% | 1.11% | **1.11%** |
| **exp-vulnerable-ms-ordenes-1** |1.85% | 1.74% | 1.80% | 1.70% | 1.59% | **1.74%** |
| **exp-vulnerable-ms-resenas-1** |1.41% | 1.15% | 1.25% | 1.18% | 1.16% | **1.23%** |
| **exp-vulnerable-ms-usuarios-1** |1.44% | 1.11% | 0.90% | 0.97% | 1.19% | **1.12%** |
| **exp-vulnerable-postgres-db-1** |1.74% | 1.72% | 1.81% | 1.73% | 1.73% | **1.75%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.30 MiB | 63.62 MiB | 64.49 MiB | 64.05 MiB | 65.17 MiB | **64.93 MiB** |
| **exp-vulnerable-mongo-db-1** |204.70 MiB | 217.84 MiB | 202.04 MiB | 211.80 MiB | 207.31 MiB | **208.74 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.49 MiB | 47.44 MiB | 46.17 MiB | 45.82 MiB | 45.71 MiB | **46.13 MiB** |
| **exp-vulnerable-ms-ordenes-1** |48.60 MiB | 49.03 MiB | 48.40 MiB | 48.57 MiB | 48.15 MiB | **48.55 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.08 MiB | 45.50 MiB | 45.19 MiB | 45.50 MiB | 45.46 MiB | **45.55 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.25 MiB | 53.83 MiB | 46.16 MiB | 45.74 MiB | 46.33 MiB | **47.66 MiB** |
| **exp-vulnerable-postgres-db-1** |33.98 MiB | 33.96 MiB | 34.06 MiB | 34.06 MiB | 33.99 MiB | **34.01 MiB** |