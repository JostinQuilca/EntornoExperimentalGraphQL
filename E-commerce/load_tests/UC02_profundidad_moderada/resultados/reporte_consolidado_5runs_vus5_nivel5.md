# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 21:14:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 100 | 2581.840 ms | 5.00% | 0.00% |
| Run 2 | 103 | 1933.610 ms | 4.85% | 0.00% |
| Run 3 | 91 | 2690.030 ms | 10.98% | 0.00% |
| Run 4 | 94 | 2437.140 ms | 5.31% | 0.00% |
| Run 5 | 90 | 2610.820 ms | 11.11% | 0.00% |
| **PROMEDIO** | **95.6** | **2450.688 ms** | **7.45%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |50.41% | 15.93% | 8.87% | 7.60% | 15.73% | **19.71%** |
| **exp-vulnerable-mongo-db-1** |111.95% | 101.92% | 106.64% | 106.32% | 98.34% | **105.03%** |
| **exp-vulnerable-ms-catalogo-1** |6.11% | 5.48% | 5.99% | 5.82% | 12.28% | **7.14%** |
| **exp-vulnerable-ms-ordenes-1** |7.53% | 6.06% | 6.47% | 5.66% | 6.45% | **6.43%** |
| **exp-vulnerable-ms-resenas-1** |250.98% | 222.19% | 237.04% | 266.14% | 247.40% | **244.75%** |
| **exp-vulnerable-ms-usuarios-1** |12.54% | 7.34% | 8.01% | 5.62% | 7.78% | **8.26%** |
| **exp-vulnerable-postgres-db-1** |50.94% | 73.14% | 79.42% | 74.17% | 68.37% | **69.21%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |97.07 MiB | 71.04 MiB | 69.59 MiB | 69.85 MiB | 97.79 MiB | **81.07 MiB** |
| **exp-vulnerable-mongo-db-1** |353.40 MiB | 350.40 MiB | 341.20 MiB | 342.80 MiB | 346.30 MiB | **346.82 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.85 MiB | 47.27 MiB | 46.29 MiB | 54.32 MiB | 46.97 MiB | **48.14 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.45 MiB | 45.97 MiB | 48.70 MiB | 46.70 MiB | 45.89 MiB | **46.94 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.36 MiB | 46.75 MiB | 45.94 MiB | 46.76 MiB | 46.15 MiB | **46.59 MiB** |
| **exp-vulnerable-postgres-db-1** |73.49 MiB | 73.93 MiB | 77.72 MiB | 72.88 MiB | 72.96 MiB | **74.20 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |4.23% | 2.51% | 1.82% | 1.33% | 2.30% | **2.44%** |
| **exp-vulnerable-mongo-db-1** |111.95% | 101.92% | 106.64% | 106.32% | 98.34% | **105.03%** |
| **exp-vulnerable-ms-catalogo-1** |6.11% | 5.48% | 5.99% | 5.82% | 12.28% | **7.14%** |
| **exp-vulnerable-ms-ordenes-1** |7.53% | 6.06% | 6.47% | 5.66% | 6.45% | **6.43%** |
| **exp-vulnerable-ms-resenas-1** |250.98% | 222.19% | 237.04% | 266.14% | 247.40% | **244.75%** |
| **exp-vulnerable-ms-usuarios-1** |12.54% | 7.34% | 8.01% | 5.62% | 7.78% | **8.26%** |
| **exp-vulnerable-postgres-db-1** |50.94% | 73.14% | 79.42% | 74.17% | 68.37% | **69.21%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.65 MiB | 67.38 MiB | 67.44 MiB | 66.39 MiB | 75.57 MiB | **68.89 MiB** |
| **exp-vulnerable-mongo-db-1** |353.40 MiB | 350.40 MiB | 341.20 MiB | 342.80 MiB | 346.30 MiB | **346.82 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.85 MiB | 47.27 MiB | 46.29 MiB | 54.32 MiB | 46.97 MiB | **48.14 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.45 MiB | 45.97 MiB | 48.70 MiB | 46.70 MiB | 45.89 MiB | **46.94 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.36 MiB | 46.75 MiB | 45.94 MiB | 46.76 MiB | 46.15 MiB | **46.59 MiB** |
| **exp-vulnerable-postgres-db-1** |73.49 MiB | 73.93 MiB | 77.72 MiB | 72.88 MiB | 72.96 MiB | **74.20 MiB** |
