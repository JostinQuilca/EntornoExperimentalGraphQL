# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 22:47:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 180 | 12.660 ms | 0.00% | 100.00% |
| Run 2 | 180 | 8.390 ms | 0.00% | 100.00% |
| Run 3 | 180 | 8.610 ms | 0.00% | 100.00% |
| Run 4 | 180 | 8.780 ms | 0.00% | 100.00% |
| Run 5 | 179 | 11.870 ms | 0.00% | 100.00% |
| **PROMEDIO** | **179.8** | **10.062 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |23.46% | 5.80% | 8.53% | 10.84% | 8.03% | **11.33%** |
| **exp-protegido-mongo-db-1** |130.81% | 90.74% | 102.36% | 110.98% | 116.46% | **110.27%** |
| **exp-protegido-ms-catalogo-1** |7.78% | 4.47% | 4.89% | 11.39% | 5.72% | **6.85%** |
| **exp-protegido-ms-ordenes-1** |8.74% | 5.97% | 4.70% | 5.64% | 4.95% | **6.00%** |
| **exp-protegido-ms-resenas-1** |5.68% | 6.56% | 4.99% | 6.18% | 8.74% | **6.43%** |
| **exp-protegido-ms-usuarios-1** |8.03% | 4.84% | 4.25% | 5.43% | 4.38% | **5.39%** |
| **exp-protegido-postgres-db-1** |6.86% | 6.33% | 5.30% | 5.99% | 6.38% | **6.17%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |96.86 MiB | 71.56 MiB | 70.09 MiB | 70.36 MiB | 69.84 MiB | **75.74 MiB** |
| **exp-protegido-mongo-db-1** |349.90 MiB | 345.80 MiB | 349.80 MiB | 337.90 MiB | 346.30 MiB | **345.94 MiB** |
| **exp-protegido-ms-catalogo-1** |45.62 MiB | 46.30 MiB | 46.27 MiB | 54.32 MiB | 46.21 MiB | **47.74 MiB** |
| **exp-protegido-ms-ordenes-1** |47.84 MiB | 46.36 MiB | 45.93 MiB | 46.48 MiB | 47.03 MiB | **46.73 MiB** |
| **exp-protegido-ms-resenas-1** |47.59 MiB | 46.63 MiB | 45.79 MiB | 47.00 MiB | 47.07 MiB | **46.82 MiB** |
| **exp-protegido-ms-usuarios-1** |45.98 MiB | 45.68 MiB | 46.29 MiB | 45.90 MiB | 54.48 MiB | **47.67 MiB** |
| **exp-protegido-postgres-db-1** |28.71 MiB | 29.13 MiB | 27.48 MiB | 28.79 MiB | 27.39 MiB | **28.30 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |3.18% | 1.64% | 1.71% | 2.02% | 2.19% | **2.15%** |
| **exp-protegido-mongo-db-1** |130.81% | 90.74% | 102.36% | 110.98% | 116.46% | **110.27%** |
| **exp-protegido-ms-catalogo-1** |7.78% | 4.47% | 4.89% | 11.39% | 5.72% | **6.85%** |
| **exp-protegido-ms-ordenes-1** |8.74% | 5.97% | 4.70% | 5.64% | 4.95% | **6.00%** |
| **exp-protegido-ms-resenas-1** |5.68% | 6.56% | 4.99% | 6.18% | 8.74% | **6.43%** |
| **exp-protegido-ms-usuarios-1** |8.03% | 4.84% | 4.25% | 5.43% | 4.38% | **5.39%** |
| **exp-protegido-postgres-db-1** |6.86% | 6.33% | 5.30% | 5.99% | 6.38% | **6.17%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |70.59 MiB | 68.33 MiB | 67.34 MiB | 67.70 MiB | 67.25 MiB | **68.24 MiB** |
| **exp-protegido-mongo-db-1** |349.90 MiB | 345.80 MiB | 349.80 MiB | 337.90 MiB | 346.30 MiB | **345.94 MiB** |
| **exp-protegido-ms-catalogo-1** |45.62 MiB | 46.30 MiB | 46.27 MiB | 54.32 MiB | 46.21 MiB | **47.74 MiB** |
| **exp-protegido-ms-ordenes-1** |47.84 MiB | 46.36 MiB | 45.93 MiB | 46.48 MiB | 47.03 MiB | **46.73 MiB** |
| **exp-protegido-ms-resenas-1** |47.59 MiB | 46.63 MiB | 45.79 MiB | 47.00 MiB | 47.07 MiB | **46.82 MiB** |
| **exp-protegido-ms-usuarios-1** |45.98 MiB | 45.68 MiB | 46.29 MiB | 45.90 MiB | 54.48 MiB | **47.67 MiB** |
| **exp-protegido-postgres-db-1** |28.71 MiB | 29.13 MiB | 27.48 MiB | 28.79 MiB | 27.39 MiB | **28.30 MiB** |
