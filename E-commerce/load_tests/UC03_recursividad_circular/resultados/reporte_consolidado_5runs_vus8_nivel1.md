# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 18:18:27

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 454 | 50.743 ms | 0.00% | 0.00% |
| Run 2 | 465 | 43.597 ms | 0.00% | 0.00% |
| Run 3 | 465 | 43.755 ms | 0.00% | 0.00% |
| Run 4 | 465 | 40.536 ms | 0.00% | 0.00% |
| Run 5 | 465 | 42.954 ms | 0.00% | 0.00% |
| **PROMEDIO** | **462.8** | **44.317 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |16.07% | 17.91% | 12.22% | 19.48% | 20.14% | **17.16%** |
| **exp-vulnerable-mongo-db-1** |67.14% | 72.14% | 97.21% | 101.69% | 74.79% | **82.59%** |
| **exp-vulnerable-ms-catalogo-1** |4.08% | 3.63% | 5.66% | 5.54% | 3.47% | **4.48%** |
| **exp-vulnerable-ms-ordenes-1** |4.63% | 4.43% | 5.02% | 6.25% | 5.70% | **5.21%** |
| **exp-vulnerable-ms-resenas-1** |11.77% | 9.87% | 13.04% | 11.23% | 13.84% | **11.95%** |
| **exp-vulnerable-ms-usuarios-1** |30.19% | 7.89% | 30.89% | 24.88% | 31.53% | **25.08%** |
| **exp-vulnerable-postgres-db-1** |26.22% | 19.45% | 23.45% | 21.70% | 40.72% | **26.31%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |98.43MiB (98.43 MiB)  | 99.17MiB (99.17 MiB)  | 98.97MiB (98.97 MiB)  | 98.64MiB (98.64 MiB)  | 99.04MiB (99.04 MiB)  |
| **exp-vulnerable-mongo-db-1** |344.4MiB (344.40 MiB)  | 346.8MiB (346.80 MiB)  | 343.2MiB (343.20 MiB)  | 330.5MiB (330.50 MiB)  | 344MiB (344.00 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |48.23MiB (48.23 MiB)  | 47.06MiB (47.06 MiB)  | 45.06MiB (45.06 MiB)  | 47.45MiB (47.45 MiB)  | 45.82MiB (45.82 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |48.31MiB (48.31 MiB)  | 46.34MiB (46.34 MiB)  | 46.44MiB (46.44 MiB)  | 47.03MiB (47.03 MiB)  | 47.06MiB (47.06 MiB)  |
| **exp-vulnerable-ms-resenas-1** |63.29MiB (63.29 MiB)  | 63.6MiB (63.60 MiB)  | 64.11MiB (64.11 MiB)  | 62.57MiB (62.57 MiB)  | 63.66MiB (63.66 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |70.42MiB (70.42 MiB)  | 72.16MiB (72.16 MiB)  | 66.65MiB (66.65 MiB)  | 73.39MiB (73.39 MiB)  | 73.94MiB (73.94 MiB)  |
| **exp-vulnerable-postgres-db-1** |70.07MiB (70.07 MiB)  | 74.39MiB (74.39 MiB)  | 71.93MiB (71.93 MiB)  | 71.9MiB (71.90 MiB)  | 68.35MiB (68.35 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |7.25% | 6.96% | 6.43% | 6.67% | 7.39% | **6.94%** |
| **exp-vulnerable-mongo-db-1** |17.88% | 17.50% | 21.62% | 18.76% | 19.36% | **19.02%** |
| **exp-vulnerable-ms-catalogo-1** |0.95% | 0.87% | 1.19% | 1.05% | 0.91% | **0.99%** |
| **exp-vulnerable-ms-ordenes-1** |0.90% | 0.90% | 1.12% | 1.08% | 1.21% | **1.04%** |
| **exp-vulnerable-ms-resenas-1** |4.32% | 4.19% | 5.13% | 4.62% | 4.77% | **4.61%** |
| **exp-vulnerable-ms-usuarios-1** |5.08% | 3.95% | 5.41% | 4.98% | 5.60% | **5.00%** |
| **exp-vulnerable-postgres-db-1** |13.31% | 12.26% | 12.89% | 12.83% | 13.96% | **13.05%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |90.47 MiB | 90.17 MiB | 89.90 MiB | 90.60 MiB | 90.73 MiB | **90.37 MiB** |
| **exp-vulnerable-mongo-db-1** |203.61 MiB | 203.82 MiB | 207.86 MiB | 194.11 MiB | 213.03 MiB | **204.49 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.28 MiB | 46.78 MiB | 44.93 MiB | 47.22 MiB | 45.70 MiB | **46.18 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.97 MiB | 45.89 MiB | 46.23 MiB | 46.76 MiB | 45.55 MiB | **46.28 MiB** |
| **exp-vulnerable-ms-resenas-1** |59.01 MiB | 58.37 MiB | 59.78 MiB | 58.35 MiB | 58.95 MiB | **58.89 MiB** |
| **exp-vulnerable-ms-usuarios-1** |66.21 MiB | 67.16 MiB | 62.42 MiB | 67.92 MiB | 66.37 MiB | **66.02 MiB** |
| **exp-vulnerable-postgres-db-1** |68.71 MiB | 72.03 MiB | 68.92 MiB | 71.36 MiB | 67.06 MiB | **69.62 MiB** |