# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 00:32:32

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 38 | 579.832 ms | 0.00% | 0.00% |
| Run 2 | 39 | 575.539 ms | 0.00% | 0.00% |
| Run 3 | 39 | 573.554 ms | 0.00% | 0.00% |
| Run 4 | 39 | 574.634 ms | 0.00% | 0.00% |
| Run 5 | 39 | 575.722 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.8** | **575.856 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |18.98% | 8.85% | 2.86% | 9.11% | 5.57% | **9.07%** |
| **exp-protegido-mongo-db-1** |96.84% | 73.41% | 76.06% | 81.30% | 84.05% | **82.33%** |
| **exp-protegido-ms-catalogo-1** |5.98% | 5.05% | 7.89% | 5.05% | 4.56% | **5.71%** |
| **exp-protegido-ms-ordenes-1** |7.39% | 5.98% | 5.81% | 6.68% | 6.12% | **6.40%** |
| **exp-protegido-ms-resenas-1** |5.33% | 5.18% | 7.71% | 5.41% | 5.77% | **5.88%** |
| **exp-protegido-ms-usuarios-1** |4.82% | 5.20% | 6.21% | 5.32% | 3.85% | **5.08%** |
| **exp-protegido-postgres-db-1** |9.04% | 7.98% | 7.31% | 6.22% | 5.49% | **7.21%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |97.27MiB (97.27 MiB)  | 66.27MiB (66.27 MiB)  | 65.66MiB (65.66 MiB)  | 66.31MiB (66.31 MiB)  | 66.38MiB (66.38 MiB)  |
| **exp-protegido-mongo-db-1** |343.7MiB (343.70 MiB)  | 270.4MiB (270.40 MiB)  | 349.7MiB (349.70 MiB)  | 342.9MiB (342.90 MiB)  | 346.2MiB (346.20 MiB)  |
| **exp-protegido-ms-catalogo-1** |47.03MiB (47.03 MiB)  | 47.51MiB (47.51 MiB)  | 46.04MiB (46.04 MiB)  | 47.25MiB (47.25 MiB)  | 46.22MiB (46.22 MiB)  |
| **exp-protegido-ms-ordenes-1** |49.74MiB (49.74 MiB)  | 51.87MiB (51.87 MiB)  | 50.38MiB (50.38 MiB)  | 51.6MiB (51.60 MiB)  | 50.82MiB (50.82 MiB)  |
| **exp-protegido-ms-resenas-1** |48.2MiB (48.20 MiB)  | 46.7MiB (46.70 MiB)  | 53.5MiB (53.50 MiB)  | 45.51MiB (45.51 MiB)  | 48.84MiB (48.84 MiB)  |
| **exp-protegido-ms-usuarios-1** |47.14MiB (47.14 MiB)  | 45.72MiB (45.72 MiB)  | 47.68MiB (47.68 MiB)  | 46.64MiB (46.64 MiB)  | 46.52MiB (46.52 MiB)  |
| **exp-protegido-postgres-db-1** |37.55MiB (37.55 MiB)  | 39.04MiB (39.04 MiB)  | 37.59MiB (37.59 MiB)  | 39.23MiB (39.23 MiB)  | 37.77MiB (37.77 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.50% | 0.87% | 0.62% | 0.92% | 0.89% | **0.96%** |
| **exp-protegido-mongo-db-1** |29.04% | 18.89% | 18.69% | 18.82% | 21.36% | **21.36%** |
| **exp-protegido-ms-catalogo-1** |1.27% | 1.11% | 1.33% | 1.24% | 1.22% | **1.23%** |
| **exp-protegido-ms-ordenes-1** |2.54% | 1.91% | 1.71% | 2.25% | 2.17% | **2.12%** |
| **exp-protegido-ms-resenas-1** |1.46% | 1.02% | 1.56% | 1.30% | 1.14% | **1.30%** |
| **exp-protegido-ms-usuarios-1** |1.33% | 1.05% | 1.28% | 1.32% | 1.10% | **1.22%** |
| **exp-protegido-postgres-db-1** |3.06% | 2.67% | 2.73% | 2.72% | 2.51% | **2.74%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.78 MiB | 65.34 MiB | 64.42 MiB | 65.09 MiB | 65.37 MiB | **65.60 MiB** |
| **exp-protegido-mongo-db-1** |205.57 MiB | 196.06 MiB | 209.39 MiB | 202.32 MiB | 204.40 MiB | **203.55 MiB** |
| **exp-protegido-ms-catalogo-1** |45.99 MiB | 46.00 MiB | 45.94 MiB | 45.87 MiB | 46.12 MiB | **45.98 MiB** |
| **exp-protegido-ms-ordenes-1** |48.74 MiB | 50.22 MiB | 49.09 MiB | 50.12 MiB | 49.32 MiB | **49.50 MiB** |
| **exp-protegido-ms-resenas-1** |46.82 MiB | 46.59 MiB | 53.26 MiB | 45.41 MiB | 47.61 MiB | **47.94 MiB** |
| **exp-protegido-ms-usuarios-1** |45.85 MiB | 45.62 MiB | 47.23 MiB | 46.54 MiB | 46.23 MiB | **46.29 MiB** |
| **exp-protegido-postgres-db-1** |37.11 MiB | 37.41 MiB | 37.21 MiB | 37.44 MiB | 37.17 MiB | **37.27 MiB** |