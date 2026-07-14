# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 02:22:15

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 35 | 762.635 ms | 0.00% | 0.00% |
| Run 2 | 35 | 752.576 ms | 0.00% | 0.00% |
| Run 3 | 35 | 745.140 ms | 0.00% | 0.00% |
| Run 4 | 34 | 772.855 ms | 0.00% | 0.00% |
| Run 5 | 34 | 765.835 ms | 0.00% | 0.00% |
| **PROMEDIO** | **34.6** | **759.808 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |30.92% | 39.09% | 24.97% | 29.54% | 46.37% | **34.18%** |
| **exp-vulnerable-mongo-db-1** |89.76% | 75.88% | 78.00% | 93.60% | 91.08% | **85.66%** |
| **exp-vulnerable-ms-catalogo-1** |3.96% | 12.86% | 4.46% | 5.01% | 4.31% | **6.12%** |
| **exp-vulnerable-ms-ordenes-1** |21.23% | 47.16% | 26.76% | 36.23% | 27.50% | **31.78%** |
| **exp-vulnerable-ms-resenas-1** |5.79% | 4.86% | 4.86% | 6.10% | 4.31% | **5.18%** |
| **exp-vulnerable-ms-usuarios-1** |4.39% | 4.56% | 4.67% | 6.99% | 4.04% | **4.93%** |
| **exp-vulnerable-postgres-db-1** |53.94% | 144.43% | 73.59% | 69.75% | 62.49% | **80.84%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |82.33MiB (82.33 MiB)  | 78.01MiB (78.01 MiB)  | 82.12MiB (82.12 MiB)  | 81.76MiB (81.76 MiB)  | 75.66MiB (75.66 MiB)  |
| **exp-vulnerable-mongo-db-1** |352.1MiB (352.10 MiB)  | 351MiB (351.00 MiB)  | 342.6MiB (342.60 MiB)  | 356.5MiB (356.50 MiB)  | 351.3MiB (351.30 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.71MiB (45.71 MiB)  | 45.4MiB (45.40 MiB)  | 47.3MiB (47.30 MiB)  | 46.73MiB (46.73 MiB)  | 47.42MiB (47.42 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |98.81MiB (98.81 MiB)  | 95.4MiB (95.40 MiB)  | 97.2MiB (97.20 MiB)  | 96.86MiB (96.86 MiB)  | 96.23MiB (96.23 MiB)  |
| **exp-vulnerable-ms-resenas-1** |54.04MiB (54.04 MiB)  | 47.12MiB (47.12 MiB)  | 46.39MiB (46.39 MiB)  | 45.81MiB (45.81 MiB)  | 45.84MiB (45.84 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |48.29MiB (48.29 MiB)  | 46.44MiB (46.44 MiB)  | 46.5MiB (46.50 MiB)  | 54.01MiB (54.01 MiB)  | 46.13MiB (46.13 MiB)  |
| **exp-vulnerable-postgres-db-1** |38.12MiB (38.12 MiB)  | 38.05MiB (38.05 MiB)  | 37.72MiB (37.72 MiB)  | 37.97MiB (37.97 MiB)  | 37.81MiB (37.81 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |2.09% | 2.75% | 2.27% | 2.63% | 2.97% | **2.54%** |
| **exp-vulnerable-mongo-db-1** |22.52% | 20.85% | 22.94% | 28.91% | 24.12% | **23.87%** |
| **exp-vulnerable-ms-catalogo-1** |1.09% | 1.46% | 1.17% | 1.26% | 1.18% | **1.23%** |
| **exp-vulnerable-ms-ordenes-1** |10.67% | 11.04% | 10.38% | 10.66% | 10.98% | **10.75%** |
| **exp-vulnerable-ms-resenas-1** |1.50% | 1.23% | 1.28% | 1.38% | 1.18% | **1.31%** |
| **exp-vulnerable-ms-usuarios-1** |1.03% | 1.19% | 1.22% | 1.30% | 1.15% | **1.18%** |
| **exp-vulnerable-postgres-db-1** |27.77% | 29.98% | 28.71% | 26.57% | 27.56% | **28.12%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |76.10 MiB | 72.74 MiB | 75.62 MiB | 74.71 MiB | 72.45 MiB | **74.32 MiB** |
| **exp-vulnerable-mongo-db-1** |217.31 MiB | 213.97 MiB | 212.99 MiB | 227.20 MiB | 204.82 MiB | **215.26 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.59 MiB | 45.29 MiB | 47.19 MiB | 46.08 MiB | 46.49 MiB | **46.13 MiB** |
| **exp-vulnerable-ms-ordenes-1** |87.86 MiB | 86.12 MiB | 86.96 MiB | 85.23 MiB | 85.84 MiB | **86.40 MiB** |
| **exp-vulnerable-ms-resenas-1** |48.47 MiB | 46.49 MiB | 46.15 MiB | 45.69 MiB | 45.72 MiB | **46.50 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.46 MiB | 46.33 MiB | 46.01 MiB | 53.99 MiB | 46.01 MiB | **47.56 MiB** |
| **exp-vulnerable-postgres-db-1** |37.26 MiB | 37.37 MiB | 37.31 MiB | 37.32 MiB | 37.18 MiB | **37.29 MiB** |