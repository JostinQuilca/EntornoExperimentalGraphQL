# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-10 23:32:22

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 570.091 ms | 0.00% | 0.00% |
| Run 2 | 39 | 568.382 ms | 0.00% | 0.00% |
| Run 3 | 39 | 568.471 ms | 0.00% | 0.00% |
| Run 4 | 39 | 568.298 ms | 0.00% | 0.00% |
| Run 5 | 39 | 567.173 ms | 0.00% | 0.00% |
| **PROMEDIO** | **39.0** | **568.483 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |11.07% | 4.02% | 4.50% | 1.25% | 4.77% | **5.12%** |
| **exp-protegido-mongo-db-1** |77.89% | 76.33% | 100.85% | 73.06% | 75.88% | **80.80%** |
| **exp-protegido-ms-catalogo-1** |4.91% | 4.15% | 4.80% | 3.39% | 5.34% | **4.52%** |
| **exp-protegido-ms-ordenes-1** |6.91% | 5.00% | 6.22% | 6.03% | 5.14% | **5.86%** |
| **exp-protegido-ms-resenas-1** |5.29% | 3.96% | 5.60% | 5.06% | 3.95% | **4.77%** |
| **exp-protegido-ms-usuarios-1** |5.53% | 3.41% | 4.98% | 5.40% | 4.43% | **4.75%** |
| **exp-protegido-postgres-db-1** |7.01% | 6.14% | 7.85% | 5.19% | 5.68% | **6.37%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |96.76MiB (96.76 MiB)  | 65.88MiB (65.88 MiB)  | 66.09MiB (66.09 MiB)  | 65.52MiB (65.52 MiB)  | 66.25MiB (66.25 MiB)  |
| **exp-protegido-mongo-db-1** |333.3MiB (333.30 MiB)  | 347.1MiB (347.10 MiB)  | 345.6MiB (345.60 MiB)  | 343.1MiB (343.10 MiB)  | 343.5MiB (343.50 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.84MiB (45.84 MiB)  | 47.02MiB (47.02 MiB)  | 46.75MiB (46.75 MiB)  | 47.04MiB (47.04 MiB)  | 45.66MiB (45.66 MiB)  |
| **exp-protegido-ms-ordenes-1** |55.48MiB (55.48 MiB)  | 49.16MiB (49.16 MiB)  | 48.92MiB (48.92 MiB)  | 49.28MiB (49.28 MiB)  | 49.54MiB (49.54 MiB)  |
| **exp-protegido-ms-resenas-1** |45.92MiB (45.92 MiB)  | 48.23MiB (48.23 MiB)  | 46.77MiB (46.77 MiB)  | 46.4MiB (46.40 MiB)  | 45.4MiB (45.40 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.93MiB (45.93 MiB)  | 47.06MiB (47.06 MiB)  | 46.64MiB (46.64 MiB)  | 46.85MiB (46.85 MiB)  | 45.54MiB (45.54 MiB)  |
| **exp-protegido-postgres-db-1** |35.77MiB (35.77 MiB)  | 34.32MiB (34.32 MiB)  | 36MiB (36.00 MiB)  | 35.76MiB (35.76 MiB)  | 34.31MiB (34.31 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.13% | 0.56% | 0.64% | 0.51% | 0.68% | **0.70%** |
| **exp-protegido-mongo-db-1** |21.07% | 20.19% | 23.03% | 21.16% | 20.58% | **21.21%** |
| **exp-protegido-ms-catalogo-1** |1.09% | 0.95% | 1.11% | 0.99% | 1.07% | **1.04%** |
| **exp-protegido-ms-ordenes-1** |2.13% | 1.70% | 1.91% | 1.98% | 1.66% | **1.88%** |
| **exp-protegido-ms-resenas-1** |1.41% | 1.07% | 1.33% | 1.25% | 1.08% | **1.23%** |
| **exp-protegido-ms-usuarios-1** |1.47% | 0.95% | 1.19% | 1.42% | 1.15% | **1.24%** |
| **exp-protegido-postgres-db-1** |1.88% | 1.70% | 1.84% | 1.65% | 1.66% | **1.75%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |68.03 MiB | 64.98 MiB | 64.97 MiB | 64.56 MiB | 65.17 MiB | **65.54 MiB** |
| **exp-protegido-mongo-db-1** |201.67 MiB | 207.64 MiB | 209.19 MiB | 208.09 MiB | 214.42 MiB | **208.20 MiB** |
| **exp-protegido-ms-catalogo-1** |45.57 MiB | 45.55 MiB | 45.83 MiB | 46.93 MiB | 45.55 MiB | **45.89 MiB** |
| **exp-protegido-ms-ordenes-1** |48.73 MiB | 48.24 MiB | 48.10 MiB | 48.52 MiB | 48.74 MiB | **48.47 MiB** |
| **exp-protegido-ms-resenas-1** |45.78 MiB | 46.51 MiB | 45.40 MiB | 46.30 MiB | 45.31 MiB | **45.86 MiB** |
| **exp-protegido-ms-usuarios-1** |45.79 MiB | 46.97 MiB | 45.89 MiB | 46.76 MiB | 45.44 MiB | **46.17 MiB** |
| **exp-protegido-postgres-db-1** |34.10 MiB | 34.06 MiB | 34.23 MiB | 34.07 MiB | 34.02 MiB | **34.10 MiB** |