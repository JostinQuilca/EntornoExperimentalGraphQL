# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 21:40:24

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 481 | 7.044 ms | 0.00% | 100.00% |
| Run 2 | 481 | 8.437 ms | 0.00% | 100.00% |
| Run 3 | 481 | 6.981 ms | 0.00% | 100.00% |
| Run 4 | 481 | 7.917 ms | 0.00% | 100.00% |
| Run 5 | 481 | 7.295 ms | 0.00% | 100.00% |
| **PROMEDIO** | **481.0** | **7.535 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |12.87% | 6.50% | 20.47% | 38.57% | 22.18% | **20.12%** |
| **exp-protegido-mongo-db-1** |111.65% | 75.84% | 97.81% | 107.78% | 90.25% | **96.67%** |
| **exp-protegido-ms-catalogo-1** |5.08% | 11.04% | 4.44% | 4.85% | 5.40% | **6.16%** |
| **exp-protegido-ms-ordenes-1** |4.13% | 5.03% | 7.85% | 4.58% | 4.98% | **5.31%** |
| **exp-protegido-ms-resenas-1** |5.40% | 5.29% | 8.64% | 5.20% | 5.05% | **5.92%** |
| **exp-protegido-ms-usuarios-1** |62.00% | 43.16% | 35.98% | 50.48% | 38.45% | **46.01%** |
| **exp-protegido-postgres-db-1** |14.65% | 6.20% | 8.12% | 5.90% | 5.50% | **8.07%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |83.94MiB (83.94 MiB)  | 79.08MiB (79.08 MiB)  | 84.97MiB (84.97 MiB)  | 83.07MiB (83.07 MiB)  | 84.12MiB (84.12 MiB)  |
| **exp-protegido-mongo-db-1** |345.4MiB (345.40 MiB)  | 341.2MiB (341.20 MiB)  | 345.9MiB (345.90 MiB)  | 340.6MiB (340.60 MiB)  | 349.1MiB (349.10 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.66MiB (45.66 MiB)  | 45.99MiB (45.99 MiB)  | 46.27MiB (46.27 MiB)  | 45.98MiB (45.98 MiB)  | 46.98MiB (46.98 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.58MiB (46.58 MiB)  | 47.07MiB (47.07 MiB)  | 46.18MiB (46.18 MiB)  | 46.19MiB (46.19 MiB)  | 46.41MiB (46.41 MiB)  |
| **exp-protegido-ms-resenas-1** |45.54MiB (45.54 MiB)  | 47.47MiB (47.47 MiB)  | 47.51MiB (47.51 MiB)  | 46.54MiB (46.54 MiB)  | 45.77MiB (45.77 MiB)  |
| **exp-protegido-ms-usuarios-1** |71.8MiB (71.80 MiB)  | 64.58MiB (64.58 MiB)  | 70.02MiB (70.02 MiB)  | 68.52MiB (68.52 MiB)  | 71.96MiB (71.96 MiB)  |
| **exp-protegido-postgres-db-1** |31.72MiB (31.72 MiB)  | 30.18MiB (30.18 MiB)  | 31.87MiB (31.87 MiB)  | 31.5MiB (31.50 MiB)  | 31.81MiB (31.81 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |4.08% | 3.33% | 3.78% | 5.17% | 4.84% | **4.24%** |
| **exp-protegido-mongo-db-1** |26.76% | 20.23% | 23.10% | 26.76% | 24.16% | **24.20%** |
| **exp-protegido-ms-catalogo-1** |1.18% | 1.47% | 1.23% | 1.40% | 1.31% | **1.32%** |
| **exp-protegido-ms-ordenes-1** |1.01% | 1.22% | 1.41% | 1.35% | 1.21% | **1.24%** |
| **exp-protegido-ms-resenas-1** |1.34% | 1.21% | 1.42% | 1.31% | 1.21% | **1.30%** |
| **exp-protegido-ms-usuarios-1** |3.46% | 2.76% | 2.57% | 3.06% | 2.37% | **2.84%** |
| **exp-protegido-postgres-db-1** |2.00% | 1.69% | 1.76% | 1.81% | 1.51% | **1.75%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |78.52 MiB | 75.57 MiB | 79.34 MiB | 76.56 MiB | 78.49 MiB | **77.70 MiB** |
| **exp-protegido-mongo-db-1** |218.39 MiB | 207.07 MiB | 217.21 MiB | 205.72 MiB | 203.42 MiB | **210.36 MiB** |
| **exp-protegido-ms-catalogo-1** |45.54 MiB | 45.82 MiB | 46.17 MiB | 45.89 MiB | 46.88 MiB | **46.06 MiB** |
| **exp-protegido-ms-ordenes-1** |46.46 MiB | 46.97 MiB | 46.08 MiB | 46.07 MiB | 46.32 MiB | **46.38 MiB** |
| **exp-protegido-ms-resenas-1** |45.42 MiB | 46.08 MiB | 46.19 MiB | 46.44 MiB | 45.67 MiB | **45.96 MiB** |
| **exp-protegido-ms-usuarios-1** |71.76 MiB | 64.56 MiB | 68.53 MiB | 68.50 MiB | 70.50 MiB | **68.77 MiB** |
| **exp-protegido-postgres-db-1** |30.17 MiB | 30.14 MiB | 30.29 MiB | 30.21 MiB | 30.24 MiB | **30.21 MiB** |