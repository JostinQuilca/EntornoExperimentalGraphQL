# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 11:12:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 72 | 1551.740 ms | 0.00% | 0.00% |
| Run 2 | 45 | 3550.570 ms | 6.66% | 0.00% |
| Run 3 | 57 | 2328.550 ms | 5.26% | 0.00% |
| Run 4 | 66 | 1767.350 ms | 0.00% | 0.00% |
| Run 5 | 57 | 2330.510 ms | 5.26% | 0.00% |
| **PROMEDIO** | **59.4** | **2305.744 ms** | **3.44%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |24.91% | 3.87% | 4.42% | 4.72% | 3.12% | **8.21%** |
| **exp-vulnerable-mongo-db-1** |122.02% | 105.92% | 104.52% | 75.96% | 84.86% | **98.66%** |
| **exp-vulnerable-ms-catalogo-1** |5.59% | 9.54% | 7.14% | 7.66% | 3.97% | **6.78%** |
| **exp-vulnerable-ms-ordenes-1** |3.87% | 4.50% | 7.07% | 2.97% | 4.50% | **4.58%** |
| **exp-vulnerable-ms-resenas-1** |238.70% | 171.95% | 209.43% | 177.01% | 188.43% | **197.10%** |
| **exp-vulnerable-ms-usuarios-1** |6.73% | 4.26% | 6.71% | 4.02% | 3.28% | **5.00%** |
| **exp-vulnerable-postgres-db-1** |48.68% | 24.71% | 25.05% | 36.20% | 19.51% | **30.83%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.36 MiB | 65.43 MiB | 66.36 MiB | 66.76 MiB | 98.26 MiB | **72.83 MiB** |
| **exp-vulnerable-mongo-db-1** |343.00 MiB | 338.70 MiB | 350.00 MiB | 344.80 MiB | 349.10 MiB | **345.12 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.55 MiB | 45.39 MiB | 45.89 MiB | 45.36 MiB | 46.88 MiB | **46.01 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.60 MiB | 46.38 MiB | 47.12 MiB | 46.29 MiB | 45.41 MiB | **46.56 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.22 MiB | 45.91 MiB | 47.40 MiB | 54.46 MiB | 48.19 MiB | **48.64 MiB** |
| **exp-vulnerable-postgres-db-1** |60.21 MiB | 60.79 MiB | 60.14 MiB | 62.15 MiB | 60.22 MiB | **60.70 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.64% | 0.54% | 0.74% | 0.71% | 0.70% | **0.87%** |
| **exp-vulnerable-mongo-db-1** |122.02% | 105.92% | 104.52% | 75.96% | 84.86% | **98.66%** |
| **exp-vulnerable-ms-catalogo-1** |5.59% | 9.54% | 7.14% | 7.66% | 3.97% | **6.78%** |
| **exp-vulnerable-ms-ordenes-1** |3.87% | 4.50% | 7.07% | 2.97% | 4.50% | **4.58%** |
| **exp-vulnerable-ms-resenas-1** |238.70% | 171.95% | 209.43% | 177.01% | 188.43% | **197.10%** |
| **exp-vulnerable-ms-usuarios-1** |6.73% | 4.26% | 6.71% | 4.02% | 3.28% | **5.00%** |
| **exp-vulnerable-postgres-db-1** |48.68% | 24.71% | 25.05% | 36.20% | 19.51% | **30.83%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.76 MiB | 64.83 MiB | 64.85 MiB | 65.50 MiB | 91.60 MiB | **70.51 MiB** |
| **exp-vulnerable-mongo-db-1** |343.00 MiB | 338.70 MiB | 350.00 MiB | 344.80 MiB | 349.10 MiB | **345.12 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.55 MiB | 45.39 MiB | 45.89 MiB | 45.36 MiB | 46.88 MiB | **46.01 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.60 MiB | 46.38 MiB | 47.12 MiB | 46.29 MiB | 45.41 MiB | **46.56 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.22 MiB | 45.91 MiB | 47.40 MiB | 54.46 MiB | 48.19 MiB | **48.64 MiB** |
| **exp-vulnerable-postgres-db-1** |60.21 MiB | 60.79 MiB | 60.14 MiB | 62.15 MiB | 60.22 MiB | **60.70 MiB** |
