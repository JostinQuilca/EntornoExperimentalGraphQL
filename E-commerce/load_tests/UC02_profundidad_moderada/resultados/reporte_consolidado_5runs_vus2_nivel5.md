# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 17:05:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 38 | 2243.850 ms | 0.00% | 0.00% |
| Run 2 | 48 | 1596.900 ms | 0.00% | 0.00% |
| Run 3 | 50 | 1420.260 ms | 0.00% | 0.00% |
| Run 4 | 42 | 2231.270 ms | 0.00% | 0.00% |
| Run 5 | 42 | 2124.300 ms | 0.00% | 0.00% |
| **PROMEDIO** | **44.0** | **1923.316 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |18.77% | 5.02% | 4.40% | 2.10% | 2.52% | **6.56%** |
| **exp-vulnerable-mongo-db-1** |99.26% | 85.98% | 92.66% | 317.85% | 106.89% | **140.53%** |
| **exp-vulnerable-ms-catalogo-1** |4.84% | 5.36% | 6.23% | 4.36% | 6.45% | **5.45%** |
| **exp-vulnerable-ms-ordenes-1** |7.65% | 5.59% | 8.65% | 4.40% | 5.46% | **6.35%** |
| **exp-vulnerable-ms-resenas-1** |203.53% | 184.41% | 181.65% | 164.34% | 176.91% | **182.17%** |
| **exp-vulnerable-ms-usuarios-1** |5.60% | 5.62% | 79.01% | 5.81% | 5.02% | **20.21%** |
| **exp-vulnerable-postgres-db-1** |16.26% | 24.86% | 27.04% | 24.68% | 16.43% | **21.85%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |100.20 MiB | 68.93 MiB | 71.46 MiB | 67.68 MiB | 67.78 MiB | **75.21 MiB** |
| **exp-vulnerable-mongo-db-1** |347.60 MiB | 340.40 MiB | 345.50 MiB | 349.00 MiB | 350.60 MiB | **346.62 MiB** |
| **exp-vulnerable-ms-catalogo-1** |61.30 MiB | 50.00 MiB | 53.02 MiB | 58.01 MiB | 54.44 MiB | **55.35 MiB** |
| **exp-vulnerable-ms-ordenes-1** |60.36 MiB | 53.47 MiB | 51.41 MiB | 59.91 MiB | 50.28 MiB | **55.09 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-vulnerable-ms-usuarios-1** |60.48 MiB | 52.42 MiB | 50.88 MiB | 60.99 MiB | 55.59 MiB | **56.07 MiB** |
| **exp-vulnerable-postgres-db-1** |61.97 MiB | 60.99 MiB | 66.09 MiB | 66.22 MiB | 60.05 MiB | **63.06 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.07% | 0.63% | 0.69% | 0.39% | 0.41% | **0.64%** |
| **exp-vulnerable-mongo-db-1** |99.26% | 85.98% | 92.66% | 317.85% | 106.89% | **140.53%** |
| **exp-vulnerable-ms-catalogo-1** |4.84% | 5.36% | 6.23% | 4.36% | 6.45% | **5.45%** |
| **exp-vulnerable-ms-ordenes-1** |7.65% | 5.59% | 8.65% | 4.40% | 5.46% | **6.35%** |
| **exp-vulnerable-ms-resenas-1** |203.53% | 184.41% | 181.65% | 164.34% | 176.91% | **182.17%** |
| **exp-vulnerable-ms-usuarios-1** |5.60% | 5.62% | 79.01% | 5.81% | 5.02% | **20.21%** |
| **exp-vulnerable-postgres-db-1** |16.26% | 24.86% | 27.04% | 24.68% | 16.43% | **21.85%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |71.80 MiB | 67.81 MiB | 70.55 MiB | 66.79 MiB | 66.61 MiB | **68.71 MiB** |
| **exp-vulnerable-mongo-db-1** |347.60 MiB | 340.40 MiB | 345.50 MiB | 349.00 MiB | 350.60 MiB | **346.62 MiB** |
| **exp-vulnerable-ms-catalogo-1** |61.30 MiB | 50.00 MiB | 53.02 MiB | 58.01 MiB | 54.44 MiB | **55.35 MiB** |
| **exp-vulnerable-ms-ordenes-1** |60.36 MiB | 53.47 MiB | 51.41 MiB | 59.91 MiB | 50.28 MiB | **55.09 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-vulnerable-ms-usuarios-1** |60.48 MiB | 52.42 MiB | 50.88 MiB | 60.99 MiB | 55.59 MiB | **56.07 MiB** |
| **exp-vulnerable-postgres-db-1** |61.97 MiB | 60.99 MiB | 66.09 MiB | 66.22 MiB | 60.05 MiB | **63.06 MiB** |
