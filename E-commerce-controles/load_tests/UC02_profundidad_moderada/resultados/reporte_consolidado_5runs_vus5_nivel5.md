# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 21:28:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 122 | 1489.030 ms | 0.00% | 0.00% |
| Run 2 | 120 | 1781.080 ms | 4.16% | 0.00% |
| Run 3 | 148 | 1115.170 ms | 0.00% | 0.00% |
| Run 4 | 100 | 2375.450 ms | 10.00% | 0.00% |
| Run 5 | 135 | 1459.370 ms | 0.00% | 0.00% |
| **PROMEDIO** | **125.0** | **1644.020 ms** | **2.83%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |18.55% | 12.41% | 12.43% | 11.35% | 10.48% | **13.04%** |
| **exp-protegido-mongo-db-1** |114.15% | 110.62% | 97.51% | 95.93% | 113.81% | **106.40%** |
| **exp-protegido-ms-catalogo-1** |11.30% | 7.29% | 5.50% | 5.26% | 6.74% | **7.22%** |
| **exp-protegido-ms-ordenes-1** |12.78% | 7.50% | 6.02% | 5.82% | 5.79% | **7.58%** |
| **exp-protegido-ms-resenas-1** |239.60% | 238.48% | 252.47% | 226.93% | 260.99% | **243.69%** |
| **exp-protegido-ms-usuarios-1** |7.72% | 6.69% | 7.02% | 6.01% | 8.13% | **7.11%** |
| **exp-protegido-postgres-db-1** |116.57% | 84.42% | 75.14% | 81.59% | 64.41% | **84.43%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |70.34 MiB | 71.12 MiB | 71.10 MiB | 69.64 MiB | 71.41 MiB | **70.72 MiB** |
| **exp-protegido-mongo-db-1** |349.80 MiB | 349.40 MiB | 348.20 MiB | 338.00 MiB | 350.40 MiB | **347.16 MiB** |
| **exp-protegido-ms-catalogo-1** |45.45 MiB | 46.06 MiB | 46.39 MiB | 47.43 MiB | 45.29 MiB | **46.12 MiB** |
| **exp-protegido-ms-ordenes-1** |47.26 MiB | 46.71 MiB | 46.09 MiB | 46.53 MiB | 46.70 MiB | **46.66 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.80 MiB | 255.90 MiB | 255.80 MiB | 256.00 MiB | **255.86 MiB** |
| **exp-protegido-ms-usuarios-1** |47.45 MiB | 47.62 MiB | 46.38 MiB | 46.74 MiB | 47.69 MiB | **47.18 MiB** |
| **exp-protegido-postgres-db-1** |71.13 MiB | 67.73 MiB | 80.30 MiB | 73.92 MiB | 77.64 MiB | **74.14 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |3.13% | 2.29% | 2.60% | 1.48% | 1.97% | **2.29%** |
| **exp-protegido-mongo-db-1** |114.15% | 110.62% | 97.51% | 95.93% | 113.81% | **106.40%** |
| **exp-protegido-ms-catalogo-1** |11.30% | 7.29% | 5.50% | 5.26% | 6.74% | **7.22%** |
| **exp-protegido-ms-ordenes-1** |12.78% | 7.50% | 6.02% | 5.82% | 5.79% | **7.58%** |
| **exp-protegido-ms-resenas-1** |239.60% | 238.48% | 252.47% | 226.93% | 260.99% | **243.69%** |
| **exp-protegido-ms-usuarios-1** |7.72% | 6.69% | 7.02% | 6.01% | 8.13% | **7.11%** |
| **exp-protegido-postgres-db-1** |116.57% | 84.42% | 75.14% | 81.59% | 64.41% | **84.43%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.45 MiB | 68.42 MiB | 67.49 MiB | 67.19 MiB | 67.67 MiB | **67.64 MiB** |
| **exp-protegido-mongo-db-1** |349.80 MiB | 349.40 MiB | 348.20 MiB | 338.00 MiB | 350.40 MiB | **347.16 MiB** |
| **exp-protegido-ms-catalogo-1** |45.45 MiB | 46.06 MiB | 46.39 MiB | 47.43 MiB | 45.29 MiB | **46.12 MiB** |
| **exp-protegido-ms-ordenes-1** |47.26 MiB | 46.71 MiB | 46.09 MiB | 46.53 MiB | 46.70 MiB | **46.66 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.80 MiB | 255.90 MiB | 255.80 MiB | 256.00 MiB | **255.86 MiB** |
| **exp-protegido-ms-usuarios-1** |47.45 MiB | 47.62 MiB | 46.38 MiB | 46.74 MiB | 47.69 MiB | **47.18 MiB** |
| **exp-protegido-postgres-db-1** |71.13 MiB | 67.73 MiB | 80.30 MiB | 73.92 MiB | 77.64 MiB | **74.14 MiB** |
