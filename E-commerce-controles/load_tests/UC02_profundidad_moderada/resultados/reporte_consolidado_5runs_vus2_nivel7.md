# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 10:23:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 120 | 7.300 ms | 0.00% | 100.00% |
| Run 2 | 120 | 6.470 ms | 0.00% | 100.00% |
| Run 3 | 120 | 7.490 ms | 0.00% | 100.00% |
| Run 4 | 120 | 7.360 ms | 0.00% | 100.00% |
| Run 5 | 120 | 7.380 ms | 0.00% | 100.00% |
| **PROMEDIO** | **120.0** | **7.200 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |6.26% | 4.15% | 2.46% | 4.71% | 4.57% | **4.43%** |
| **exp-protegido-mongo-db-1** |54.36% | 64.75% | 52.55% | 48.41% | 52.45% | **54.50%** |
| **exp-protegido-ms-catalogo-1** |3.50% | 3.27% | 3.75% | 4.01% | 4.03% | **3.71%** |
| **exp-protegido-ms-ordenes-1** |3.56% | 3.39% | 3.65% | 4.54% | 4.88% | **4.00%** |
| **exp-protegido-ms-resenas-1** |3.32% | 3.44% | 3.54% | 4.90% | 4.34% | **3.91%** |
| **exp-protegido-ms-usuarios-1** |3.89% | 4.58% | 3.28% | 3.74% | 4.11% | **3.92%** |
| **exp-protegido-postgres-db-1** |4.33% | 4.21% | 4.25% | 4.32% | 5.66% | **4.55%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.71 MiB | 66.06 MiB | 66.07 MiB | 65.71 MiB | 65.36 MiB | **65.78 MiB** |
| **exp-protegido-mongo-db-1** |271.00 MiB | 341.30 MiB | 343.30 MiB | 331.80 MiB | 331.80 MiB | **323.84 MiB** |
| **exp-protegido-ms-catalogo-1** |46.21 MiB | 46.14 MiB | 45.70 MiB | 47.36 MiB | 45.88 MiB | **46.26 MiB** |
| **exp-protegido-ms-ordenes-1** |46.29 MiB | 45.89 MiB | 45.95 MiB | 46.55 MiB | 46.95 MiB | **46.33 MiB** |
| **exp-protegido-ms-resenas-1** |47.28 MiB | 46.06 MiB | 47.50 MiB | 48.06 MiB | 45.91 MiB | **46.96 MiB** |
| **exp-protegido-ms-usuarios-1** |47.77 MiB | 45.88 MiB | 47.59 MiB | 46.95 MiB | 54.03 MiB | **48.44 MiB** |
| **exp-protegido-postgres-db-1** |27.34 MiB | 27.51 MiB | 28.84 MiB | 27.38 MiB | 27.61 MiB | **27.74 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.49% | 1.18% | 1.01% | 1.29% | 1.31% | **1.26%** |
| **exp-protegido-mongo-db-1** |54.36% | 64.75% | 52.55% | 48.41% | 52.45% | **54.50%** |
| **exp-protegido-ms-catalogo-1** |3.50% | 3.27% | 3.75% | 4.01% | 4.03% | **3.71%** |
| **exp-protegido-ms-ordenes-1** |3.56% | 3.39% | 3.65% | 4.54% | 4.88% | **4.00%** |
| **exp-protegido-ms-resenas-1** |3.32% | 3.44% | 3.54% | 4.90% | 4.34% | **3.91%** |
| **exp-protegido-ms-usuarios-1** |3.89% | 4.58% | 3.28% | 3.74% | 4.11% | **3.92%** |
| **exp-protegido-postgres-db-1** |4.33% | 4.21% | 4.25% | 4.32% | 5.66% | **4.55%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |64.45 MiB | 64.94 MiB | 64.92 MiB | 64.46 MiB | 64.26 MiB | **64.61 MiB** |
| **exp-protegido-mongo-db-1** |271.00 MiB | 341.30 MiB | 343.30 MiB | 331.80 MiB | 331.80 MiB | **323.84 MiB** |
| **exp-protegido-ms-catalogo-1** |46.21 MiB | 46.14 MiB | 45.70 MiB | 47.36 MiB | 45.88 MiB | **46.26 MiB** |
| **exp-protegido-ms-ordenes-1** |46.29 MiB | 45.89 MiB | 45.95 MiB | 46.55 MiB | 46.95 MiB | **46.33 MiB** |
| **exp-protegido-ms-resenas-1** |47.28 MiB | 46.06 MiB | 47.50 MiB | 48.06 MiB | 45.91 MiB | **46.96 MiB** |
| **exp-protegido-ms-usuarios-1** |47.77 MiB | 45.88 MiB | 47.59 MiB | 46.95 MiB | 54.03 MiB | **48.44 MiB** |
| **exp-protegido-postgres-db-1** |27.34 MiB | 27.51 MiB | 28.84 MiB | 27.38 MiB | 27.61 MiB | **27.74 MiB** |
