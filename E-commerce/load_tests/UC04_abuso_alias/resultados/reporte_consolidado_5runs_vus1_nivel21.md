# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 00:41:36

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 38 | 587.454 ms | 0.00% | 0.00% |
| Run 2 | 38 | 599.346 ms | 0.00% | 0.00% |
| Run 3 | 38 | 586.946 ms | 0.00% | 0.00% |
| Run 4 | 38 | 581.709 ms | 0.00% | 0.00% |
| Run 5 | 38 | 583.953 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.0** | **587.881 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |9.84% | 2.70% | 8.70% | 2.25% | 29.27% | **10.55%** |
| **exp-vulnerable-mongo-db-1** |74.90% | 116.37% | 79.46% | 75.06% | 127.91% | **94.74%** |
| **exp-vulnerable-ms-catalogo-1** |4.72% | 7.20% | 4.85% | 3.64% | 6.81% | **5.44%** |
| **exp-vulnerable-ms-ordenes-1** |16.11% | 13.13% | 8.04% | 7.01% | 9.27% | **10.71%** |
| **exp-vulnerable-ms-resenas-1** |5.72% | 7.09% | 5.83% | 4.91% | 4.48% | **5.61%** |
| **exp-vulnerable-ms-usuarios-1** |5.50% | 7.35% | 5.52% | 4.87% | 4.14% | **5.48%** |
| **exp-vulnerable-postgres-db-1** |8.93% | 18.65% | 13.06% | 10.97% | 9.54% | **12.23%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.68MiB (96.68 MiB)  | 97.44MiB (97.44 MiB)  | 97.29MiB (97.29 MiB)  | 96.18MiB (96.18 MiB)  | 65.6MiB (65.60 MiB)  |
| **exp-vulnerable-mongo-db-1** |335.4MiB (335.40 MiB)  | 343.3MiB (343.30 MiB)  | 350.7MiB (350.70 MiB)  | 348.9MiB (348.90 MiB)  | 344.8MiB (344.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.36MiB (45.36 MiB)  | 47.25MiB (47.25 MiB)  | 45.73MiB (45.73 MiB)  | 46.68MiB (46.68 MiB)  | 53.82MiB (53.82 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |60.23MiB (60.23 MiB)  | 58.98MiB (58.98 MiB)  | 51.89MiB (51.89 MiB)  | 51.73MiB (51.73 MiB)  | 60.02MiB (60.02 MiB)  |
| **exp-vulnerable-ms-resenas-1** |45.47MiB (45.47 MiB)  | 45.45MiB (45.45 MiB)  | 53.46MiB (53.46 MiB)  | 47.61MiB (47.61 MiB)  | 46.37MiB (46.37 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.27MiB (45.27 MiB)  | 45.83MiB (45.83 MiB)  | 46.13MiB (46.13 MiB)  | 55.59MiB (55.59 MiB)  | 49.56MiB (49.56 MiB)  |
| **exp-vulnerable-postgres-db-1** |37.74MiB (37.74 MiB)  | 39.04MiB (39.04 MiB)  | 39.24MiB (39.24 MiB)  | 37.62MiB (37.62 MiB)  | 38.18MiB (38.18 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.13% | 0.83% | 1.41% | 0.66% | 1.84% | **1.17%** |
| **exp-vulnerable-mongo-db-1** |21.05% | 31.33% | 27.60% | 20.84% | 23.06% | **24.78%** |
| **exp-vulnerable-ms-catalogo-1** |1.05% | 1.51% | 1.10% | 1.03% | 1.23% | **1.18%** |
| **exp-vulnerable-ms-ordenes-1** |3.84% | 3.30% | 3.01% | 2.43% | 2.87% | **3.09%** |
| **exp-vulnerable-ms-resenas-1** |1.57% | 1.43% | 1.29% | 1.05% | 1.16% | **1.30%** |
| **exp-vulnerable-ms-usuarios-1** |1.56% | 1.35% | 1.34% | 1.06% | 1.07% | **1.28%** |
| **exp-vulnerable-postgres-db-1** |4.48% | 4.63% | 4.60% | 3.75% | 4.13% | **4.32%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |68.41 MiB | 66.95 MiB | 65.87 MiB | 66.23 MiB | 64.29 MiB | **66.35 MiB** |
| **exp-vulnerable-mongo-db-1** |200.18 MiB | 205.00 MiB | 201.17 MiB | 210.21 MiB | 212.41 MiB | **205.79 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.23 MiB | 46.06 MiB | 45.60 MiB | 46.54 MiB | 48.44 MiB | **46.37 MiB** |
| **exp-vulnerable-ms-ordenes-1** |53.06 MiB | 51.81 MiB | 50.47 MiB | 50.07 MiB | 52.62 MiB | **51.61 MiB** |
| **exp-vulnerable-ms-resenas-1** |45.35 MiB | 45.35 MiB | 45.62 MiB | 46.18 MiB | 46.24 MiB | **45.75 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.15 MiB | 45.71 MiB | 46.02 MiB | 54.70 MiB | 49.44 MiB | **48.20 MiB** |
| **exp-vulnerable-postgres-db-1** |37.26 MiB | 37.27 MiB | 37.48 MiB | 37.21 MiB | 37.40 MiB | **37.32 MiB** |