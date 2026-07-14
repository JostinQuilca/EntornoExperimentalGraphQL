# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-08 22:25:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 25 | 1381.970 ms | 0.00% | 0.00% |
| Run 2 | 20 | 2147.270 ms | 0.00% | 0.00% |
| Run 3 | 24 | 1523.630 ms | 0.00% | 0.00% |
| Run 4 | 23 | 1581.960 ms | 0.00% | 0.00% |
| Run 5 | 20 | 2030.330 ms | 0.00% | 0.00% |
| **PROMEDIO** | **22.4** | **1733.032 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |118.09% | 126.12% | 93.81% | 92.77% | 103.65% | **106.89%** |
| **exp-protegido-mongo-db-1** |83.80% | 112.07% | 106.28% | 80.45% | 89.88% | **94.50%** |
| **exp-protegido-ms-catalogo-1** |4.67% | 3.94% | 4.36% | 3.88% | 2.63% | **3.90%** |
| **exp-protegido-ms-ordenes-1** |3.87% | 7.64% | 3.25% | 3.83% | 4.67% | **4.65%** |
| **exp-protegido-ms-resenas-1** |135.69% | 138.97% | 139.85% | 133.17% | 136.55% | **136.85%** |
| **exp-protegido-ms-usuarios-1** |4.07% | 5.37% | 3.38% | 4.68% | 4.68% | **4.44%** |
| **exp-protegido-postgres-db-1** |13.35% | 16.85% | 13.06% | 11.22% | 12.67% | **13.43%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |233.10 MiB | 275.70 MiB | 369.90 MiB | 220.60 MiB | 307.90 MiB | **281.44 MiB** |
| **exp-protegido-mongo-db-1** |357.10 MiB | 350.10 MiB | 341.50 MiB | 333.60 MiB | 334.00 MiB | **343.26 MiB** |
| **exp-protegido-ms-catalogo-1** |91.32 MiB | 47.11 MiB | 46.07 MiB | 46.06 MiB | 45.60 MiB | **55.23 MiB** |
| **exp-protegido-ms-ordenes-1** |95.32 MiB | 45.88 MiB | 47.41 MiB | 48.29 MiB | 46.80 MiB | **56.74 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 256.00 MiB | 255.80 MiB | 255.80 MiB | 256.00 MiB | **255.92 MiB** |
| **exp-protegido-ms-usuarios-1** |94.16 MiB | 46.05 MiB | 47.37 MiB | 48.86 MiB | 48.44 MiB | **56.98 MiB** |
| **exp-protegido-postgres-db-1** |60.19 MiB | 56.78 MiB | 59.11 MiB | 60.07 MiB | 60.19 MiB | **59.27 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |13.03% | 11.45% | 10.80% | 11.02% | 13.71% | **12.00%** |
| **exp-protegido-mongo-db-1** |83.80% | 112.07% | 106.28% | 80.45% | 89.88% | **94.50%** |
| **exp-protegido-ms-catalogo-1** |4.67% | 3.94% | 4.36% | 3.88% | 2.63% | **3.90%** |
| **exp-protegido-ms-ordenes-1** |3.87% | 7.64% | 3.25% | 3.83% | 4.67% | **4.65%** |
| **exp-protegido-ms-resenas-1** |135.69% | 138.97% | 139.85% | 133.17% | 136.55% | **136.85%** |
| **exp-protegido-ms-usuarios-1** |4.07% | 5.37% | 3.38% | 4.68% | 4.68% | **4.44%** |
| **exp-protegido-postgres-db-1** |13.35% | 16.85% | 13.06% | 11.22% | 12.67% | **13.43%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |197.03 MiB | 161.70 MiB | 209.19 MiB | 187.95 MiB | 228.18 MiB | **196.81 MiB** |
| **exp-protegido-mongo-db-1** |357.10 MiB | 350.10 MiB | 341.50 MiB | 333.60 MiB | 334.00 MiB | **343.26 MiB** |
| **exp-protegido-ms-catalogo-1** |91.32 MiB | 47.11 MiB | 46.07 MiB | 46.06 MiB | 45.60 MiB | **55.23 MiB** |
| **exp-protegido-ms-ordenes-1** |95.32 MiB | 45.88 MiB | 47.41 MiB | 48.29 MiB | 46.80 MiB | **56.74 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 256.00 MiB | 255.80 MiB | 255.80 MiB | 256.00 MiB | **255.92 MiB** |
| **exp-protegido-ms-usuarios-1** |94.16 MiB | 46.05 MiB | 47.37 MiB | 48.86 MiB | 48.44 MiB | **56.98 MiB** |
| **exp-protegido-postgres-db-1** |60.19 MiB | 56.78 MiB | 59.11 MiB | 60.07 MiB | 60.19 MiB | **59.27 MiB** |
