# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 22:03:33

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 480 | 8.568 ms | 0.00% | 100.00% |
| Run 2 | 481 | 10.634 ms | 0.00% | 100.00% |
| Run 3 | 481 | 9.186 ms | 0.00% | 100.00% |
| Run 4 | 481 | 10.095 ms | 0.00% | 100.00% |
| Run 5 | 481 | 9.554 ms | 0.00% | 100.00% |
| **PROMEDIO** | **480.8** | **9.608 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |24.85% | 37.08% | 14.80% | 13.20% | 36.26% | **25.24%** |
| **exp-protegido-mongo-db-1** |123.36% | 99.72% | 90.81% | 96.07% | 108.23% | **103.64%** |
| **exp-protegido-ms-catalogo-1** |7.12% | 4.78% | 4.14% | 5.45% | 11.58% | **6.61%** |
| **exp-protegido-ms-ordenes-1** |7.77% | 5.45% | 4.66% | 10.15% | 6.87% | **6.98%** |
| **exp-protegido-ms-resenas-1** |5.99% | 4.89% | 4.96% | 6.20% | 5.10% | **5.43%** |
| **exp-protegido-ms-usuarios-1** |44.09% | 49.18% | 34.98% | 42.86% | 5.28% | **35.28%** |
| **exp-protegido-postgres-db-1** |9.42% | 5.95% | 5.77% | 6.38% | 8.19% | **7.14%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |103.4MiB (103.40 MiB)  | 83.1MiB (83.10 MiB)  | 78.53MiB (78.53 MiB)  | 84.45MiB (84.45 MiB)  | 83.32MiB (83.32 MiB)  |
| **exp-protegido-mongo-db-1** |352.1MiB (352.10 MiB)  | 347.5MiB (347.50 MiB)  | 338.1MiB (338.10 MiB)  | 339.4MiB (339.40 MiB)  | 349.1MiB (349.10 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.74MiB (45.74 MiB)  | 46.98MiB (46.98 MiB)  | 47.04MiB (47.04 MiB)  | 45.89MiB (45.89 MiB)  | 47.22MiB (47.22 MiB)  |
| **exp-protegido-ms-ordenes-1** |47.95MiB (47.95 MiB)  | 45.76MiB (45.76 MiB)  | 45.6MiB (45.60 MiB)  | 47.35MiB (47.35 MiB)  | 47.3MiB (47.30 MiB)  |
| **exp-protegido-ms-resenas-1** |48.95MiB (48.95 MiB)  | 55.58MiB (55.58 MiB)  | 46.79MiB (46.79 MiB)  | 47.44MiB (47.44 MiB)  | 45.82MiB (45.82 MiB)  |
| **exp-protegido-ms-usuarios-1** |67MiB (67.00 MiB)  | 65.58MiB (65.58 MiB)  | 68.85MiB (68.85 MiB)  | 68.08MiB (68.08 MiB)  | 68.39MiB (68.39 MiB)  |
| **exp-protegido-postgres-db-1** |30.23MiB (30.23 MiB)  | 30.23MiB (30.23 MiB)  | 30.6MiB (30.60 MiB)  | 30.15MiB (30.15 MiB)  | 31.55MiB (31.55 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |5.48% | 5.99% | 4.98% | 4.27% | 6.21% | **5.39%** |
| **exp-protegido-mongo-db-1** |35.24% | 27.60% | 21.23% | 27.53% | 26.15% | **27.55%** |
| **exp-protegido-ms-catalogo-1** |1.35% | 1.26% | 1.30% | 1.13% | 1.87% | **1.38%** |
| **exp-protegido-ms-ordenes-1** |1.59% | 1.21% | 1.20% | 1.33% | 1.39% | **1.34%** |
| **exp-protegido-ms-resenas-1** |1.47% | 1.20% | 1.38% | 1.21% | 1.29% | **1.31%** |
| **exp-protegido-ms-usuarios-1** |3.32% | 3.00% | 2.38% | 2.82% | 1.31% | **2.57%** |
| **exp-protegido-postgres-db-1** |1.52% | 1.69% | 1.82% | 1.72% | 1.94% | **1.74%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |79.44 MiB | 78.24 MiB | 75.05 MiB | 77.76 MiB | 76.87 MiB | **77.47 MiB** |
| **exp-protegido-mongo-db-1** |216.61 MiB | 208.48 MiB | 198.32 MiB | 208.20 MiB | 222.90 MiB | **210.90 MiB** |
| **exp-protegido-ms-catalogo-1** |45.61 MiB | 46.88 MiB | 46.71 MiB | 45.53 MiB | 47.05 MiB | **46.36 MiB** |
| **exp-protegido-ms-ordenes-1** |46.80 MiB | 45.66 MiB | 45.35 MiB | 46.08 MiB | 46.04 MiB | **45.99 MiB** |
| **exp-protegido-ms-resenas-1** |46.69 MiB | 48.35 MiB | 46.51 MiB | 45.90 MiB | 45.71 MiB | **46.63 MiB** |
| **exp-protegido-ms-usuarios-1** |61.06 MiB | 65.56 MiB | 68.65 MiB | 68.06 MiB | 67.60 MiB | **66.19 MiB** |
| **exp-protegido-postgres-db-1** |30.20 MiB | 30.20 MiB | 30.18 MiB | 30.14 MiB | 30.12 MiB | **30.17 MiB** |