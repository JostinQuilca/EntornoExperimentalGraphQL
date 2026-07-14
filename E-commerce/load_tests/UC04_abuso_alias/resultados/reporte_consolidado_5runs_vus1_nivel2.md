# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-10 22:55:08

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 571.778 ms | 0.00% | 0.00% |
| Run 2 | 39 | 566.980 ms | 0.00% | 0.00% |
| Run 3 | 39 | 566.625 ms | 0.00% | 0.00% |
| Run 4 | 39 | 566.985 ms | 0.00% | 0.00% |
| Run 5 | 38 | 578.723 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.8** | **570.218 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.59% | 1.44% | 7.19% | 1.14% | 36.32% | **9.54%** |
| **exp-vulnerable-mongo-db-1** |91.81% | 77.13% | 72.83% | 77.19% | 89.39% | **81.67%** |
| **exp-vulnerable-ms-catalogo-1** |13.22% | 3.93% | 4.57% | 7.46% | 5.17% | **6.87%** |
| **exp-vulnerable-ms-ordenes-1** |5.52% | 5.08% | 4.36% | 5.32% | 6.07% | **5.27%** |
| **exp-vulnerable-ms-resenas-1** |7.29% | 4.29% | 5.16% | 4.91% | 5.09% | **5.35%** |
| **exp-vulnerable-ms-usuarios-1** |4.85% | 4.34% | 4.99% | 3.73% | 6.63% | **4.91%** |
| **exp-vulnerable-postgres-db-1** |6.47% | 7.04% | 5.64% | 5.18% | 15.74% | **8.01%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.96MiB (96.96 MiB)  | 97.29MiB (97.29 MiB)  | 96.5MiB (96.50 MiB)  | 96.25MiB (96.25 MiB)  | 96.88MiB (96.88 MiB)  |
| **exp-vulnerable-mongo-db-1** |351MiB (351.00 MiB)  | 332MiB (332.00 MiB)  | 333.8MiB (333.80 MiB)  | 350.2MiB (350.20 MiB)  | 350.4MiB (350.40 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.93MiB (45.93 MiB)  | 47.02MiB (47.02 MiB)  | 46.09MiB (46.09 MiB)  | 48.2MiB (48.20 MiB)  | 47.82MiB (47.82 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |49.38MiB (49.38 MiB)  | 49.44MiB (49.44 MiB)  | 49.09MiB (49.09 MiB)  | 49.41MiB (49.41 MiB)  | 49.4MiB (49.40 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.43MiB (46.43 MiB)  | 47.18MiB (47.18 MiB)  | 46.18MiB (46.18 MiB)  | 46.23MiB (46.23 MiB)  | 49.61MiB (49.61 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.93MiB (45.93 MiB)  | 48MiB (48.00 MiB)  | 47.59MiB (47.59 MiB)  | 46.85MiB (46.85 MiB)  | 48.23MiB (48.23 MiB)  |
| **exp-vulnerable-postgres-db-1** |32.63MiB (32.63 MiB)  | 34.51MiB (34.51 MiB)  | 32.62MiB (32.62 MiB)  | 32.63MiB (32.63 MiB)  | 32.59MiB (32.59 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.51% | 0.52% | 0.68% | 0.50% | 2.17% | **0.88%** |
| **exp-vulnerable-mongo-db-1** |25.99% | 18.66% | 21.75% | 18.74% | 20.81% | **21.19%** |
| **exp-vulnerable-ms-catalogo-1** |1.60% | 0.98% | 1.01% | 1.19% | 1.40% | **1.24%** |
| **exp-vulnerable-ms-ordenes-1** |1.86% | 1.58% | 1.48% | 1.75% | 1.84% | **1.70%** |
| **exp-vulnerable-ms-resenas-1** |1.43% | 1.20% | 1.39% | 1.28% | 1.29% | **1.32%** |
| **exp-vulnerable-ms-usuarios-1** |1.39% | 1.18% | 1.17% | 0.91% | 1.49% | **1.23%** |
| **exp-vulnerable-postgres-db-1** |1.94% | 1.80% | 1.57% | 1.59% | 2.55% | **1.89%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.72 MiB | 66.36 MiB | 65.83 MiB | 65.40 MiB | 65.57 MiB | **66.18 MiB** |
| **exp-vulnerable-mongo-db-1** |215.34 MiB | 204.40 MiB | 204.49 MiB | 208.86 MiB | 220.35 MiB | **210.69 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.63 MiB | 46.89 MiB | 45.77 MiB | 46.72 MiB | 46.06 MiB | **46.21 MiB** |
| **exp-vulnerable-ms-ordenes-1** |48.55 MiB | 48.24 MiB | 48.18 MiB | 48.46 MiB | 48.47 MiB | **48.38 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.13 MiB | 45.84 MiB | 46.02 MiB | 45.70 MiB | 47.96 MiB | **46.33 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.82 MiB | 46.00 MiB | 46.35 MiB | 46.73 MiB | 46.28 MiB | **46.24 MiB** |
| **exp-vulnerable-postgres-db-1** |32.39 MiB | 32.48 MiB | 32.39 MiB | 32.40 MiB | 32.35 MiB | **32.40 MiB** |