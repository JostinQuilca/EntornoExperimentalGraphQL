# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 21:19:28

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 481 | 9.073 ms | 0.00% | 100.00% |
| Run 2 | 481 | 9.313 ms | 0.00% | 100.00% |
| Run 3 | 481 | 11.524 ms | 0.00% | 100.00% |
| Run 4 | 481 | 8.381 ms | 0.00% | 100.00% |
| Run 5 | 481 | 6.744 ms | 0.00% | 100.00% |
| **PROMEDIO** | **481.0** | **9.007 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |18.66% | 20.63% | 24.45% | 39.90% | 13.54% | **23.44%** |
| **exp-protegido-mongo-db-1** |100.28% | 113.88% | 136.46% | 130.69% | 72.53% | **110.77%** |
| **exp-protegido-ms-catalogo-1** |4.53% | 24.50% | 10.75% | 11.92% | 4.56% | **11.25%** |
| **exp-protegido-ms-ordenes-1** |4.32% | 6.56% | 21.13% | 8.13% | 5.20% | **9.07%** |
| **exp-protegido-ms-resenas-1** |6.25% | 5.10% | 32.19% | 8.98% | 4.98% | **11.50%** |
| **exp-protegido-ms-usuarios-1** |9.45% | 6.99% | 33.28% | 66.29% | 5.37% | **24.28%** |
| **exp-protegido-postgres-db-1** |6.30% | 14.06% | 26.32% | 12.56% | 6.96% | **13.24%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |101.2MiB (101.20 MiB)  | 82.59MiB (82.59 MiB)  | 84.06MiB (84.06 MiB)  | 84.87MiB (84.87 MiB)  | 83.86MiB (83.86 MiB)  |
| **exp-protegido-mongo-db-1** |345.6MiB (345.60 MiB)  | 346.7MiB (346.70 MiB)  | 342.5MiB (342.50 MiB)  | 349.6MiB (349.60 MiB)  | 342MiB (342.00 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.04MiB (46.04 MiB)  | 54.68MiB (54.68 MiB)  | 47.59MiB (47.59 MiB)  | 46.4MiB (46.40 MiB)  | 46.08MiB (46.08 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.57MiB (46.57 MiB)  | 45.8MiB (45.80 MiB)  | 46.52MiB (46.52 MiB)  | 54.42MiB (54.42 MiB)  | 46.09MiB (46.09 MiB)  |
| **exp-protegido-ms-resenas-1** |47.26MiB (47.26 MiB)  | 45.78MiB (45.78 MiB)  | 45.87MiB (45.87 MiB)  | 46.55MiB (46.55 MiB)  | 46.43MiB (46.43 MiB)  |
| **exp-protegido-ms-usuarios-1** |70.2MiB (70.20 MiB)  | 68.97MiB (68.97 MiB)  | 66MiB (66.00 MiB)  | 67.14MiB (67.14 MiB)  | 67.6MiB (67.60 MiB)  |
| **exp-protegido-postgres-db-1** |30.22MiB (30.22 MiB)  | 30.4MiB (30.40 MiB)  | 30.36MiB (30.36 MiB)  | 30.31MiB (30.31 MiB)  | 30.31MiB (30.31 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |4.45% | 4.86% | 4.94% | 5.34% | 3.71% | **4.66%** |
| **exp-protegido-mongo-db-1** |21.94% | 24.49% | 24.44% | 36.39% | 23.27% | **26.11%** |
| **exp-protegido-ms-catalogo-1** |1.16% | 2.28% | 1.41% | 1.62% | 1.12% | **1.52%** |
| **exp-protegido-ms-ordenes-1** |1.20% | 1.47% | 2.22% | 1.80% | 0.90% | **1.52%** |
| **exp-protegido-ms-resenas-1** |1.62% | 1.36% | 2.28% | 1.53% | 1.10% | **1.58%** |
| **exp-protegido-ms-usuarios-1** |1.47% | 1.41% | 3.57% | 3.46% | 1.13% | **2.21%** |
| **exp-protegido-postgres-db-1** |1.69% | 1.85% | 2.46% | 2.22% | 1.58% | **1.96%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |75.70 MiB | 75.30 MiB | 77.67 MiB | 77.32 MiB | 78.39 MiB | **76.88 MiB** |
| **exp-protegido-mongo-db-1** |206.56 MiB | 211.48 MiB | 210.64 MiB | 205.32 MiB | 198.71 MiB | **206.54 MiB** |
| **exp-protegido-ms-catalogo-1** |45.92 MiB | 47.24 MiB | 47.46 MiB | 45.92 MiB | 45.97 MiB | **46.50 MiB** |
| **exp-protegido-ms-ordenes-1** |46.45 MiB | 45.26 MiB | 46.39 MiB | 47.44 MiB | 45.99 MiB | **46.31 MiB** |
| **exp-protegido-ms-resenas-1** |46.07 MiB | 45.68 MiB | 45.74 MiB | 46.46 MiB | 46.33 MiB | **46.06 MiB** |
| **exp-protegido-ms-usuarios-1** |68.29 MiB | 66.11 MiB | 65.85 MiB | 67.12 MiB | 66.80 MiB | **66.83 MiB** |
| **exp-protegido-postgres-db-1** |30.10 MiB | 30.07 MiB | 30.21 MiB | 30.16 MiB | 30.06 MiB | **30.12 MiB** |