# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-07 21:00:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 184 | 1808.930 ms | 0.00% | 0.00% |
| Run 2 | 162 | 2066.180 ms | 9.87% | 0.00% |
| Run 3 | 176 | 2033.950 ms | 0.00% | 0.00% |
| Run 4 | 157 | 2068.890 ms | 0.00% | 0.00% |
| Run 5 | 168 | 2032.100 ms | 0.00% | 0.00% |
| **PROMEDIO** | **169.4** | **2002.010 ms** | **1.97%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |13.18% | 12.54% | 7.41% | 5.53% | 5.79% | **8.89%** |
| **exp-protegido-mongo-db-1** |82.36% | 108.26% | 94.97% | 100.36% | 74.45% | **92.08%** |
| **exp-protegido-ms-catalogo-1** |9.32% | 6.47% | 4.76% | 4.66% | 4.34% | **5.91%** |
| **exp-protegido-ms-ordenes-1** |6.90% | 6.36% | 4.58% | 4.44% | 4.38% | **5.33%** |
| **exp-protegido-ms-resenas-1** |242.35% | 240.64% | 249.55% | 271.37% | 234.15% | **247.61%** |
| **exp-protegido-ms-usuarios-1** |7.97% | 6.29% | 5.03% | 4.18% | 4.80% | **5.65%** |
| **exp-protegido-postgres-db-1** |79.69% | 74.71% | 19.61% | 47.77% | 56.43% | **55.64%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |72.96 MiB | 71.13 MiB | 70.22 MiB | 70.81 MiB | 70.38 MiB | **71.10 MiB** |
| **exp-protegido-mongo-db-1** |350.10 MiB | 343.90 MiB | 330.50 MiB | 349.70 MiB | 340.20 MiB | **342.88 MiB** |
| **exp-protegido-ms-catalogo-1** |53.97 MiB | 45.71 MiB | 45.98 MiB | 47.00 MiB | 45.80 MiB | **47.69 MiB** |
| **exp-protegido-ms-ordenes-1** |47.73 MiB | 46.44 MiB | 45.77 MiB | 46.28 MiB | 45.59 MiB | **46.36 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.80 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | **255.82 MiB** |
| **exp-protegido-ms-usuarios-1** |45.22 MiB | 47.09 MiB | 48.06 MiB | 54.23 MiB | 48.02 MiB | **48.52 MiB** |
| **exp-protegido-postgres-db-1** |70.34 MiB | 70.63 MiB | 75.56 MiB | 70.50 MiB | 67.55 MiB | **70.92 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.31% | 2.62% | 1.51% | 1.31% | 1.35% | **1.82%** |
| **exp-protegido-mongo-db-1** |82.36% | 108.26% | 94.97% | 100.36% | 74.45% | **92.08%** |
| **exp-protegido-ms-catalogo-1** |9.32% | 6.47% | 4.76% | 4.66% | 4.34% | **5.91%** |
| **exp-protegido-ms-ordenes-1** |6.90% | 6.36% | 4.58% | 4.44% | 4.38% | **5.33%** |
| **exp-protegido-ms-resenas-1** |242.35% | 240.64% | 249.55% | 271.37% | 234.15% | **247.61%** |
| **exp-protegido-ms-usuarios-1** |7.97% | 6.29% | 5.03% | 4.18% | 4.80% | **5.65%** |
| **exp-protegido-postgres-db-1** |79.69% | 74.71% | 19.61% | 47.77% | 56.43% | **55.64%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |68.88 MiB | 68.27 MiB | 67.68 MiB | 69.20 MiB | 68.17 MiB | **68.44 MiB** |
| **exp-protegido-mongo-db-1** |350.10 MiB | 343.90 MiB | 330.50 MiB | 349.70 MiB | 340.20 MiB | **342.88 MiB** |
| **exp-protegido-ms-catalogo-1** |53.97 MiB | 45.71 MiB | 45.98 MiB | 47.00 MiB | 45.80 MiB | **47.69 MiB** |
| **exp-protegido-ms-ordenes-1** |47.73 MiB | 46.44 MiB | 45.77 MiB | 46.28 MiB | 45.59 MiB | **46.36 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.80 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | **255.82 MiB** |
| **exp-protegido-ms-usuarios-1** |45.22 MiB | 47.09 MiB | 48.06 MiB | 54.23 MiB | 48.02 MiB | **48.52 MiB** |
| **exp-protegido-postgres-db-1** |70.34 MiB | 70.63 MiB | 75.56 MiB | 70.50 MiB | 67.55 MiB | **70.92 MiB** |
