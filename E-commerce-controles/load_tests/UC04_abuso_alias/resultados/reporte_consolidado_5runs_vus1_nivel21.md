# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 00:52:24

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 38 | 590.261 ms | 0.00% | 0.00% |
| Run 2 | 38 | 580.538 ms | 0.00% | 0.00% |
| Run 3 | 38 | 579.738 ms | 0.00% | 0.00% |
| Run 4 | 38 | 586.241 ms | 0.00% | 0.00% |
| Run 5 | 38 | 583.762 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.0** | **584.108 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |8.60% | 2.29% | 5.26% | 6.09% | 9.59% | **6.37%** |
| **exp-protegido-mongo-db-1** |110.58% | 72.89% | 76.90% | 74.99% | 74.54% | **81.98%** |
| **exp-protegido-ms-catalogo-1** |6.05% | 3.74% | 4.33% | 3.80% | 3.56% | **4.30%** |
| **exp-protegido-ms-ordenes-1** |8.06% | 5.21% | 6.37% | 7.89% | 6.93% | **6.89%** |
| **exp-protegido-ms-resenas-1** |5.15% | 4.06% | 4.16% | 7.26% | 5.25% | **5.18%** |
| **exp-protegido-ms-usuarios-1** |5.34% | 4.29% | 5.72% | 7.38% | 3.45% | **5.24%** |
| **exp-protegido-postgres-db-1** |10.87% | 7.92% | 7.72% | 14.20% | 7.94% | **9.73%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |66.5MiB (66.50 MiB)  | 66.67MiB (66.67 MiB)  | 67.85MiB (67.85 MiB)  | 66.52MiB (66.52 MiB)  | 66.52MiB (66.52 MiB)  |
| **exp-protegido-mongo-db-1** |349.8MiB (349.80 MiB)  | 340.9MiB (340.90 MiB)  | 347.9MiB (347.90 MiB)  | 341.3MiB (341.30 MiB)  | 341.8MiB (341.80 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.51MiB (46.51 MiB)  | 47.03MiB (47.03 MiB)  | 45.73MiB (45.73 MiB)  | 46.41MiB (46.41 MiB)  | 45.83MiB (45.83 MiB)  |
| **exp-protegido-ms-ordenes-1** |51.72MiB (51.72 MiB)  | 51.99MiB (51.99 MiB)  | 52.79MiB (52.79 MiB)  | 51.22MiB (51.22 MiB)  | 51.29MiB (51.29 MiB)  |
| **exp-protegido-ms-resenas-1** |46.02MiB (46.02 MiB)  | 49.17MiB (49.17 MiB)  | 46.39MiB (46.39 MiB)  | 54.54MiB (54.54 MiB)  | 47.11MiB (47.11 MiB)  |
| **exp-protegido-ms-usuarios-1** |47.31MiB (47.31 MiB)  | 46.86MiB (46.86 MiB)  | 54.29MiB (54.29 MiB)  | 47.47MiB (47.47 MiB)  | 46.92MiB (46.92 MiB)  |
| **exp-protegido-postgres-db-1** |37.78MiB (37.78 MiB)  | 37.68MiB (37.68 MiB)  | 39.45MiB (39.45 MiB)  | 39.43MiB (39.43 MiB)  | 37.8MiB (37.80 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.29% | 0.59% | 0.77% | 0.89% | 1.00% | **0.91%** |
| **exp-protegido-mongo-db-1** |31.75% | 21.58% | 18.97% | 20.11% | 20.80% | **22.64%** |
| **exp-protegido-ms-catalogo-1** |1.21% | 1.13% | 0.95% | 1.05% | 0.92% | **1.05%** |
| **exp-protegido-ms-ordenes-1** |3.31% | 2.16% | 2.59% | 2.79% | 2.67% | **2.70%** |
| **exp-protegido-ms-resenas-1** |1.33% | 1.14% | 1.18% | 1.50% | 1.13% | **1.26%** |
| **exp-protegido-ms-usuarios-1** |1.29% | 1.15% | 1.39% | 1.47% | 0.94% | **1.25%** |
| **exp-protegido-postgres-db-1** |5.12% | 3.52% | 3.52% | 4.04% | 3.67% | **3.97%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.29 MiB | 65.75 MiB | 66.88 MiB | 65.34 MiB | 65.39 MiB | **65.73 MiB** |
| **exp-protegido-mongo-db-1** |212.54 MiB | 205.94 MiB | 203.80 MiB | 205.06 MiB | 206.01 MiB | **206.67 MiB** |
| **exp-protegido-ms-catalogo-1** |46.38 MiB | 45.97 MiB | 45.64 MiB | 46.31 MiB | 45.48 MiB | **45.96 MiB** |
| **exp-protegido-ms-ordenes-1** |50.50 MiB | 50.24 MiB | 50.19 MiB | 49.96 MiB | 50.00 MiB | **50.18 MiB** |
| **exp-protegido-ms-resenas-1** |45.90 MiB | 47.64 MiB | 45.78 MiB | 47.86 MiB | 45.75 MiB | **46.59 MiB** |
| **exp-protegido-ms-usuarios-1** |47.19 MiB | 46.42 MiB | 51.49 MiB | 45.85 MiB | 46.49 MiB | **47.49 MiB** |
| **exp-protegido-postgres-db-1** |37.29 MiB | 37.30 MiB | 37.29 MiB | 37.40 MiB | 37.30 MiB | **37.32 MiB** |