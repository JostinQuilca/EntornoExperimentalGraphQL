# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 22:33:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 48 | 2789.210 ms | 12.50% | 0.00% |
| Run 2 | 60 | 2001.660 ms | 5.00% | 0.00% |
| Run 3 | 45 | 2997.060 ms | 6.66% | 0.00% |
| Run 4 | 48 | 3329.440 ms | 18.75% | 0.00% |
| Run 5 | 66 | 1858.580 ms | 4.54% | 0.00% |
| **PROMEDIO** | **53.4** | **2595.190 ms** | **9.49%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |18.50% | 16.89% | 9.49% | 4.74% | 8.44% | **11.61%** |
| **exp-vulnerable-mongo-db-1** |114.12% | 106.14% | 101.03% | 111.23% | 109.77% | **108.46%** |
| **exp-vulnerable-ms-catalogo-1** |8.25% | 4.87% | 5.40% | 5.44% | 5.76% | **5.94%** |
| **exp-vulnerable-ms-ordenes-1** |14.83% | 5.13% | 7.79% | 5.95% | 4.90% | **7.72%** |
| **exp-vulnerable-ms-resenas-1** |209.68% | 215.34% | 211.57% | 192.93% | 220.44% | **209.99%** |
| **exp-vulnerable-ms-usuarios-1** |20.91% | 5.30% | 5.65% | 6.88% | 6.51% | **9.05%** |
| **exp-vulnerable-postgres-db-1** |54.80% | 40.63% | 32.05% | 43.57% | 48.45% | **43.90%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |97.00 MiB | 68.05 MiB | 65.40 MiB | 66.18 MiB | 70.59 MiB | **73.44 MiB** |
| **exp-vulnerable-mongo-db-1** |349.20 MiB | 349.00 MiB | 355.20 MiB | 350.20 MiB | 343.70 MiB | **349.46 MiB** |
| **exp-vulnerable-ms-catalogo-1** |47.57 MiB | 45.77 MiB | 47.68 MiB | 45.70 MiB | 45.52 MiB | **46.45 MiB** |
| **exp-vulnerable-ms-ordenes-1** |49.07 MiB | 47.23 MiB | 47.95 MiB | 48.45 MiB | 45.53 MiB | **47.65 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.80 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.25 MiB | 45.23 MiB | 48.49 MiB | 45.71 MiB | 46.16 MiB | **46.77 MiB** |
| **exp-vulnerable-postgres-db-1** |64.55 MiB | 60.09 MiB | 64.80 MiB | 60.14 MiB | 61.68 MiB | **62.25 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.53% | 1.50% | 1.11% | 0.63% | 1.30% | **1.21%** |
| **exp-vulnerable-mongo-db-1** |114.12% | 106.14% | 101.03% | 111.23% | 109.77% | **108.46%** |
| **exp-vulnerable-ms-catalogo-1** |8.25% | 4.87% | 5.40% | 5.44% | 5.76% | **5.94%** |
| **exp-vulnerable-ms-ordenes-1** |14.83% | 5.13% | 7.79% | 5.95% | 4.90% | **7.72%** |
| **exp-vulnerable-ms-resenas-1** |209.68% | 215.34% | 211.57% | 192.93% | 220.44% | **209.99%** |
| **exp-vulnerable-ms-usuarios-1** |20.91% | 5.30% | 5.65% | 6.88% | 6.51% | **9.05%** |
| **exp-vulnerable-postgres-db-1** |54.80% | 40.63% | 32.05% | 43.57% | 48.45% | **43.90%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.42 MiB | 65.87 MiB | 64.54 MiB | 65.10 MiB | 66.01 MiB | **65.79 MiB** |
| **exp-vulnerable-mongo-db-1** |349.20 MiB | 349.00 MiB | 355.20 MiB | 350.20 MiB | 343.70 MiB | **349.46 MiB** |
| **exp-vulnerable-ms-catalogo-1** |47.57 MiB | 45.77 MiB | 47.68 MiB | 45.70 MiB | 45.52 MiB | **46.45 MiB** |
| **exp-vulnerable-ms-ordenes-1** |49.07 MiB | 47.23 MiB | 47.95 MiB | 48.45 MiB | 45.53 MiB | **47.65 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.80 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.25 MiB | 45.23 MiB | 48.49 MiB | 45.71 MiB | 46.16 MiB | **46.77 MiB** |
| **exp-vulnerable-postgres-db-1** |64.55 MiB | 60.09 MiB | 64.80 MiB | 60.14 MiB | 61.68 MiB | **62.25 MiB** |
