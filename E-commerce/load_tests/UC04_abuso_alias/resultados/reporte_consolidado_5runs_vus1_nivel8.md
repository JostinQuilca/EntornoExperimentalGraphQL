# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 00:01:41

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 573.909 ms | 0.00% | 0.00% |
| Run 2 | 39 | 572.038 ms | 0.00% | 0.00% |
| Run 3 | 39 | 573.721 ms | 0.00% | 0.00% |
| Run 4 | 39 | 570.862 ms | 0.00% | 0.00% |
| Run 5 | 39 | 569.439 ms | 0.00% | 0.00% |
| **PROMEDIO** | **39.0** | **571.994 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.34% | 1.79% | 15.77% | 1.57% | 12.02% | **6.50%** |
| **exp-vulnerable-mongo-db-1** |98.77% | 78.30% | 75.51% | 76.17% | 80.14% | **81.78%** |
| **exp-vulnerable-ms-catalogo-1** |4.87% | 4.27% | 9.07% | 4.98% | 4.95% | **5.63%** |
| **exp-vulnerable-ms-ordenes-1** |7.80% | 6.78% | 6.14% | 6.17% | 6.06% | **6.59%** |
| **exp-vulnerable-ms-resenas-1** |6.29% | 3.79% | 5.57% | 5.98% | 4.63% | **5.25%** |
| **exp-vulnerable-ms-usuarios-1** |6.35% | 3.93% | 4.73% | 5.02% | 5.71% | **5.15%** |
| **exp-vulnerable-postgres-db-1** |7.87% | 5.81% | 6.35% | 6.56% | 6.97% | **6.71%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |66MiB (66.00 MiB)  | 96.31MiB (96.31 MiB)  | 66.46MiB (66.46 MiB)  | 96.95MiB (96.95 MiB)  | 65.65MiB (65.65 MiB)  |
| **exp-vulnerable-mongo-db-1** |340.8MiB (340.80 MiB)  | 349.1MiB (349.10 MiB)  | 352.1MiB (352.10 MiB)  | 351.6MiB (351.60 MiB)  | 342.8MiB (342.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |48.33MiB (48.33 MiB)  | 45.73MiB (45.73 MiB)  | 55.27MiB (55.27 MiB)  | 45.66MiB (45.66 MiB)  | 45.85MiB (45.85 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |49.76MiB (49.76 MiB)  | 49.56MiB (49.56 MiB)  | 51.77MiB (51.77 MiB)  | 49.51MiB (49.51 MiB)  | 50.07MiB (50.07 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.47MiB (46.47 MiB)  | 45.65MiB (45.65 MiB)  | 46.53MiB (46.53 MiB)  | 45.77MiB (45.77 MiB)  | 46.95MiB (46.95 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.75MiB (45.75 MiB)  | 46.22MiB (46.22 MiB)  | 45.63MiB (45.63 MiB)  | 45.77MiB (45.77 MiB)  | 56.17MiB (56.17 MiB)  |
| **exp-vulnerable-postgres-db-1** |39.39MiB (39.39 MiB)  | 37.6MiB (37.60 MiB)  | 39.26MiB (39.26 MiB)  | 38.22MiB (38.22 MiB)  | 37.89MiB (37.89 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.59% | 0.62% | 1.13% | 0.56% | 0.94% | **0.77%** |
| **exp-vulnerable-mongo-db-1** |25.57% | 19.05% | 19.54% | 19.08% | 21.46% | **20.94%** |
| **exp-vulnerable-ms-catalogo-1** |1.21% | 1.00% | 1.32% | 1.05% | 1.14% | **1.14%** |
| **exp-vulnerable-ms-ordenes-1** |2.28% | 1.92% | 2.01% | 2.19% | 1.96% | **2.07%** |
| **exp-vulnerable-ms-resenas-1** |1.40% | 1.09% | 1.13% | 1.38% | 0.94% | **1.19%** |
| **exp-vulnerable-ms-usuarios-1** |1.42% | 1.11% | 1.09% | 1.15% | 1.21% | **1.20%** |
| **exp-vulnerable-postgres-db-1** |2.36% | 2.13% | 2.20% | 2.22% | 2.33% | **2.25%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |64.69 MiB | 66.18 MiB | 65.43 MiB | 66.48 MiB | 65.04 MiB | **65.56 MiB** |
| **exp-vulnerable-mongo-db-1** |201.06 MiB | 213.25 MiB | 208.52 MiB | 209.54 MiB | 206.18 MiB | **207.71 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.91 MiB | 45.05 MiB | 54.36 MiB | 45.54 MiB | 45.73 MiB | **47.52 MiB** |
| **exp-vulnerable-ms-ordenes-1** |48.90 MiB | 48.58 MiB | 50.78 MiB | 48.49 MiB | 48.65 MiB | **49.08 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.35 MiB | 45.40 MiB | 46.41 MiB | 45.65 MiB | 46.81 MiB | **46.12 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.61 MiB | 45.95 MiB | 45.26 MiB | 45.64 MiB | 54.73 MiB | **47.44 MiB** |
| **exp-vulnerable-postgres-db-1** |37.35 MiB | 37.20 MiB | 37.44 MiB | 37.25 MiB | 37.29 MiB | **37.31 MiB** |