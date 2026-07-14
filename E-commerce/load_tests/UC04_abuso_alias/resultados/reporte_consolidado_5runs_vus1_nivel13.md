# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 00:21:39

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 38 | 579.469 ms | 0.00% | 0.00% |
| Run 2 | 39 | 576.067 ms | 0.00% | 0.00% |
| Run 3 | 39 | 575.130 ms | 0.00% | 0.00% |
| Run 4 | 39 | 577.019 ms | 0.00% | 0.00% |
| Run 5 | 38 | 578.266 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.6** | **577.190 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |7.18% | 2.61% | 3.66% | 14.95% | 2.95% | **6.27%** |
| **exp-vulnerable-mongo-db-1** |98.56% | 69.93% | 86.22% | 101.39% | 88.11% | **88.84%** |
| **exp-vulnerable-ms-catalogo-1** |5.73% | 4.62% | 4.68% | 4.62% | 5.29% | **4.99%** |
| **exp-vulnerable-ms-ordenes-1** |7.35% | 5.69% | 7.38% | 14.19% | 7.25% | **8.37%** |
| **exp-vulnerable-ms-resenas-1** |4.42% | 5.37% | 4.70% | 10.71% | 4.93% | **6.03%** |
| **exp-vulnerable-ms-usuarios-1** |5.67% | 5.42% | 5.88% | 5.93% | 5.89% | **5.76%** |
| **exp-vulnerable-postgres-db-1** |11.02% | 7.76% | 6.95% | 7.34% | 6.49% | **7.91%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |66.25MiB (66.25 MiB)  | 65.88MiB (65.88 MiB)  | 65.98MiB (65.98 MiB)  | 67.25MiB (67.25 MiB)  | 66.05MiB (66.05 MiB)  |
| **exp-vulnerable-mongo-db-1** |346.5MiB (346.50 MiB)  | 350.1MiB (350.10 MiB)  | 344.6MiB (344.60 MiB)  | 340.6MiB (340.60 MiB)  | 350.4MiB (350.40 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |49.67MiB (49.67 MiB)  | 45.65MiB (45.65 MiB)  | 45.53MiB (45.53 MiB)  | 47.18MiB (47.18 MiB)  | 47.22MiB (47.22 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |59.9MiB (59.90 MiB)  | 50.97MiB (50.97 MiB)  | 50.34MiB (50.34 MiB)  | 50.6MiB (50.60 MiB)  | 49.99MiB (49.99 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47.33MiB (47.33 MiB)  | 45.64MiB (45.64 MiB)  | 46.02MiB (46.02 MiB)  | 46.05MiB (46.05 MiB)  | 46.41MiB (46.41 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.84MiB (45.84 MiB)  | 46.65MiB (46.65 MiB)  | 45.95MiB (45.95 MiB)  | 45.66MiB (45.66 MiB)  | 46.27MiB (46.27 MiB)  |
| **exp-vulnerable-postgres-db-1** |37.67MiB (37.67 MiB)  | 38.17MiB (38.17 MiB)  | 39.13MiB (39.13 MiB)  | 39.45MiB (39.45 MiB)  | 37.71MiB (37.71 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.01% | 0.70% | 0.62% | 1.35% | 0.69% | **0.87%** |
| **exp-vulnerable-mongo-db-1** |15.35% | 20.44% | 22.29% | 19.81% | 23.06% | **20.19%** |
| **exp-vulnerable-ms-catalogo-1** |1.19% | 1.13% | 1.25% | 1.04% | 1.13% | **1.15%** |
| **exp-vulnerable-ms-ordenes-1** |2.51% | 2.30% | 2.29% | 2.73% | 2.24% | **2.41%** |
| **exp-vulnerable-ms-resenas-1** |1.09% | 1.32% | 1.09% | 1.36% | 1.04% | **1.18%** |
| **exp-vulnerable-ms-usuarios-1** |1.24% | 1.33% | 1.30% | 1.20% | 1.24% | **1.26%** |
| **exp-vulnerable-postgres-db-1** |3.56% | 2.65% | 2.70% | 2.83% | 2.44% | **2.84%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.23 MiB | 64.73 MiB | 65.08 MiB | 66.20 MiB | 64.20 MiB | **65.09 MiB** |
| **exp-vulnerable-mongo-db-1** |207.24 MiB | 204.61 MiB | 207.96 MiB | 204.64 MiB | 208.19 MiB | **206.53 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.86 MiB | 45.54 MiB | 45.37 MiB | 45.98 MiB | 45.71 MiB | **45.89 MiB** |
| **exp-vulnerable-ms-ordenes-1** |52.92 MiB | 48.92 MiB | 49.32 MiB | 49.38 MiB | 48.94 MiB | **49.90 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.87 MiB | 45.50 MiB | 45.87 MiB | 45.93 MiB | 46.17 MiB | **46.07 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.55 MiB | 46.33 MiB | 45.58 MiB | 44.76 MiB | 46.04 MiB | **45.65 MiB** |
| **exp-vulnerable-postgres-db-1** |37.16 MiB | 37.30 MiB | 37.34 MiB | 37.37 MiB | 37.28 MiB | **37.29 MiB** |