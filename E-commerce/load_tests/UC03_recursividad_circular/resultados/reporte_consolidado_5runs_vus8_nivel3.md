# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 20:47:46

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 438 | 103.662 ms | 0.00% | 0.00% |
| Run 2 | 445 | 86.504 ms | 0.00% | 0.00% |
| Run 3 | 450 | 75.728 ms | 0.00% | 0.00% |
| Run 4 | 452 | 70.468 ms | 0.00% | 0.00% |
| Run 5 | 450 | 77.124 ms | 0.00% | 0.00% |
| **PROMEDIO** | **447.0** | **82.697 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |60.42% | 38.37% | 61.31% | 43.06% | 35.22% | **47.68%** |
| **exp-vulnerable-mongo-db-1** |63.70% | 105.28% | 98.10% | 114.20% | 101.37% | **96.53%** |
| **exp-vulnerable-ms-catalogo-1** |12.25% | 6.72% | 6.58% | 19.73% | 4.98% | **10.05%** |
| **exp-vulnerable-ms-ordenes-1** |8.34% | 7.84% | 5.31% | 5.93% | 6.81% | **6.85%** |
| **exp-vulnerable-ms-resenas-1** |54.04% | 29.69% | 28.58% | 39.94% | 28.22% | **36.09%** |
| **exp-vulnerable-ms-usuarios-1** |67.67% | 48.34% | 74.31% | 40.11% | 35.36% | **53.16%** |
| **exp-vulnerable-postgres-db-1** |46.07% | 26.09% | 27.90% | 40.34% | 37.81% | **35.64%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |137.4MiB (137.40 MiB)  | 105.4MiB (105.40 MiB)  | 105.9MiB (105.90 MiB)  | 187.1MiB (187.10 MiB)  | 187.6MiB (187.60 MiB)  |
| **exp-vulnerable-mongo-db-1** |331.5MiB (331.50 MiB)  | 335.5MiB (335.50 MiB)  | 340.8MiB (340.80 MiB)  | 346.7MiB (346.70 MiB)  | 346.1MiB (346.10 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |47.18MiB (47.18 MiB)  | 47.7MiB (47.70 MiB)  | 46.9MiB (46.90 MiB)  | 46.6MiB (46.60 MiB)  | 45.98MiB (45.98 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.16MiB (46.16 MiB)  | 46.26MiB (46.26 MiB)  | 47.36MiB (47.36 MiB)  | 46.94MiB (46.94 MiB)  | 46.35MiB (46.35 MiB)  |
| **exp-vulnerable-ms-resenas-1** |93.21MiB (93.21 MiB)  | 91.78MiB (91.78 MiB)  | 93.82MiB (93.82 MiB)  | 117.8MiB (117.80 MiB)  | 94.13MiB (94.13 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |70.04MiB (70.04 MiB)  | 70.01MiB (70.01 MiB)  | 72.45MiB (72.45 MiB)  | 75.42MiB (75.42 MiB)  | 71.02MiB (71.02 MiB)  |
| **exp-vulnerable-postgres-db-1** |68.43MiB (68.43 MiB)  | 71.59MiB (71.59 MiB)  | 68.48MiB (68.48 MiB)  | 70.16MiB (70.16 MiB)  | 68.91MiB (68.91 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |20.09% | 20.53% | 20.10% | 14.93% | 17.25% | **18.58%** |
| **exp-vulnerable-mongo-db-1** |17.19% | 28.19% | 18.90% | 28.16% | 23.90% | **23.27%** |
| **exp-vulnerable-ms-catalogo-1** |2.16% | 1.62% | 1.37% | 1.80% | 1.09% | **1.61%** |
| **exp-vulnerable-ms-ordenes-1** |1.62% | 1.76% | 1.27% | 1.29% | 1.46% | **1.48%** |
| **exp-vulnerable-ms-resenas-1** |18.67% | 15.41% | 14.74% | 14.30% | 15.53% | **15.73%** |
| **exp-vulnerable-ms-usuarios-1** |8.64% | 7.58% | 7.51% | 6.09% | 6.65% | **7.29%** |
| **exp-vulnerable-postgres-db-1** |20.12% | 17.28% | 16.38% | 17.12% | 17.82% | **17.74%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |115.86 MiB | 101.46 MiB | 102.14 MiB | 135.54 MiB | 120.51 MiB | **115.10 MiB** |
| **exp-vulnerable-mongo-db-1** |198.83 MiB | 200.77 MiB | 206.61 MiB | 210.43 MiB | 198.92 MiB | **203.11 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.74 MiB | 47.59 MiB | 46.53 MiB | 46.47 MiB | 45.86 MiB | **46.44 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.03 MiB | 46.14 MiB | 45.82 MiB | 45.45 MiB | 46.22 MiB | **45.93 MiB** |
| **exp-vulnerable-ms-resenas-1** |86.97 MiB | 85.20 MiB | 86.40 MiB | 100.40 MiB | 87.65 MiB | **89.32 MiB** |
| **exp-vulnerable-ms-usuarios-1** |63.83 MiB | 65.91 MiB | 66.63 MiB | 70.47 MiB | 64.15 MiB | **66.20 MiB** |
| **exp-vulnerable-postgres-db-1** |66.83 MiB | 68.83 MiB | 66.66 MiB | 69.90 MiB | 66.07 MiB | **67.66 MiB** |