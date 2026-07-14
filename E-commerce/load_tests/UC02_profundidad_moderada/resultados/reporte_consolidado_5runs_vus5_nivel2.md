# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 20:47:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 130 | 1330.870 ms | 0.00% | 0.00% |
| Run 2 | 136 | 1470.570 ms | 0.00% | 0.00% |
| Run 3 | 135 | 1271.930 ms | 0.00% | 0.00% |
| Run 4 | 131 | 1315.130 ms | 0.00% | 0.00% |
| Run 5 | 120 | 1533.540 ms | 0.00% | 0.00% |
| **PROMEDIO** | **130.4** | **1384.408 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |22.61% | 13.07% | 12.93% | 19.17% | 10.19% | **15.59%** |
| **exp-vulnerable-mongo-db-1** |131.41% | 95.25% | 93.59% | 106.68% | 104.46% | **106.28%** |
| **exp-vulnerable-ms-catalogo-1** |6.32% | 6.80% | 5.82% | 5.23% | 5.10% | **5.85%** |
| **exp-vulnerable-ms-ordenes-1** |6.31% | 5.50% | 4.68% | 5.30% | 5.98% | **5.55%** |
| **exp-vulnerable-ms-resenas-1** |363.03% | 247.11% | 209.89% | 231.45% | 209.51% | **252.20%** |
| **exp-vulnerable-ms-usuarios-1** |6.26% | 6.45% | 11.91% | 5.71% | 6.32% | **7.33%** |
| **exp-vulnerable-postgres-db-1** |46.86% | 90.01% | 77.28% | 68.92% | 72.54% | **71.12%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |107.80 MiB | 70.31 MiB | 70.37 MiB | 70.01 MiB | 68.33 MiB | **77.36 MiB** |
| **exp-vulnerable-mongo-db-1** |463.70 MiB | 341.60 MiB | 335.50 MiB | 348.30 MiB | 343.20 MiB | **366.46 MiB** |
| **exp-vulnerable-ms-catalogo-1** |93.41 MiB | 45.64 MiB | 46.58 MiB | 46.45 MiB | 47.82 MiB | **55.98 MiB** |
| **exp-vulnerable-ms-ordenes-1** |110.20 MiB | 71.80 MiB | 47.06 MiB | 47.97 MiB | 46.29 MiB | **64.66 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.70 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |109.80 MiB | 45.54 MiB | 53.80 MiB | 47.16 MiB | 49.20 MiB | **61.10 MiB** |
| **exp-vulnerable-postgres-db-1** |90.80 MiB | 69.19 MiB | 79.12 MiB | 70.91 MiB | 74.12 MiB | **76.83 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |2.98% | 2.00% | 1.97% | 2.61% | 2.23% | **2.36%** |
| **exp-vulnerable-mongo-db-1** |131.41% | 95.25% | 93.59% | 106.68% | 104.46% | **106.28%** |
| **exp-vulnerable-ms-catalogo-1** |6.32% | 6.80% | 5.82% | 5.23% | 5.10% | **5.85%** |
| **exp-vulnerable-ms-ordenes-1** |6.31% | 5.50% | 4.68% | 5.30% | 5.98% | **5.55%** |
| **exp-vulnerable-ms-resenas-1** |363.03% | 247.11% | 209.89% | 231.45% | 209.51% | **252.20%** |
| **exp-vulnerable-ms-usuarios-1** |6.26% | 6.45% | 11.91% | 5.71% | 6.32% | **7.33%** |
| **exp-vulnerable-postgres-db-1** |46.86% | 90.01% | 77.28% | 68.92% | 72.54% | **71.12%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |91.88 MiB | 67.68 MiB | 67.21 MiB | 67.40 MiB | 66.27 MiB | **72.09 MiB** |
| **exp-vulnerable-mongo-db-1** |463.70 MiB | 341.60 MiB | 335.50 MiB | 348.30 MiB | 343.20 MiB | **366.46 MiB** |
| **exp-vulnerable-ms-catalogo-1** |93.41 MiB | 45.64 MiB | 46.58 MiB | 46.45 MiB | 47.82 MiB | **55.98 MiB** |
| **exp-vulnerable-ms-ordenes-1** |110.20 MiB | 71.80 MiB | 47.06 MiB | 47.97 MiB | 46.29 MiB | **64.66 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.70 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |109.80 MiB | 45.54 MiB | 53.80 MiB | 47.16 MiB | 49.20 MiB | **61.10 MiB** |
| **exp-vulnerable-postgres-db-1** |90.80 MiB | 69.19 MiB | 79.12 MiB | 70.91 MiB | 74.12 MiB | **76.83 MiB** |
