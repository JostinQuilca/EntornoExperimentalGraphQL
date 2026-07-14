# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 11:02:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 50 | 1433.990 ms | 0.00% | 0.00% |
| Run 2 | 52 | 1573.760 ms | 0.00% | 0.00% |
| Run 3 | 53 | 1234.510 ms | 0.00% | 0.00% |
| Run 4 | 47 | 1560.460 ms | 0.00% | 0.00% |
| Run 5 | 48 | 1767.550 ms | 0.00% | 0.00% |
| **PROMEDIO** | **50.0** | **1514.054 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |10.55% | 7.58% | 4.82% | 2.30% | 6.11% | **6.27%** |
| **exp-protegido-mongo-db-1** |113.63% | 98.93% | 115.93% | 114.98% | 103.17% | **109.33%** |
| **exp-protegido-ms-catalogo-1** |4.18% | 5.05% | 5.63% | 5.32% | 5.27% | **5.09%** |
| **exp-protegido-ms-ordenes-1** |5.30% | 4.27% | 4.38% | 3.56% | 12.56% | **6.01%** |
| **exp-protegido-ms-resenas-1** |190.91% | 193.64% | 202.10% | 193.81% | 196.14% | **195.32%** |
| **exp-protegido-ms-usuarios-1** |6.52% | 3.89% | 4.80% | 5.42% | 8.50% | **5.83%** |
| **exp-protegido-postgres-db-1** |37.18% | 23.11% | 33.29% | 24.65% | 17.14% | **27.07%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |96.74 MiB | 66.43 MiB | 66.40 MiB | 66.56 MiB | 68.11 MiB | **72.85 MiB** |
| **exp-protegido-mongo-db-1** |342.70 MiB | 347.60 MiB | 347.90 MiB | 349.40 MiB | 334.50 MiB | **344.42 MiB** |
| **exp-protegido-ms-catalogo-1** |47.21 MiB | 46.38 MiB | 46.21 MiB | 45.79 MiB | 46.58 MiB | **46.43 MiB** |
| **exp-protegido-ms-ordenes-1** |48.28 MiB | 46.50 MiB | 47.20 MiB | 46.84 MiB | 47.20 MiB | **47.20 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 255.90 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-protegido-ms-usuarios-1** |45.64 MiB | 48.04 MiB | 46.36 MiB | 47.81 MiB | 46.25 MiB | **46.82 MiB** |
| **exp-protegido-postgres-db-1** |58.54 MiB | 61.53 MiB | 59.46 MiB | 58.48 MiB | 63.52 MiB | **60.31 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.12% | 0.86% | 0.94% | 0.64% | 0.70% | **0.85%** |
| **exp-protegido-mongo-db-1** |113.63% | 98.93% | 115.93% | 114.98% | 103.17% | **109.33%** |
| **exp-protegido-ms-catalogo-1** |4.18% | 5.05% | 5.63% | 5.32% | 5.27% | **5.09%** |
| **exp-protegido-ms-ordenes-1** |5.30% | 4.27% | 4.38% | 3.56% | 12.56% | **6.01%** |
| **exp-protegido-ms-resenas-1** |190.91% | 193.64% | 202.10% | 193.81% | 196.14% | **195.32%** |
| **exp-protegido-ms-usuarios-1** |6.52% | 3.89% | 4.80% | 5.42% | 8.50% | **5.83%** |
| **exp-protegido-postgres-db-1** |37.18% | 23.11% | 33.29% | 24.65% | 17.14% | **27.07%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |69.06 MiB | 64.75 MiB | 65.33 MiB | 65.18 MiB | 65.76 MiB | **66.02 MiB** |
| **exp-protegido-mongo-db-1** |342.70 MiB | 347.60 MiB | 347.90 MiB | 349.40 MiB | 334.50 MiB | **344.42 MiB** |
| **exp-protegido-ms-catalogo-1** |47.21 MiB | 46.38 MiB | 46.21 MiB | 45.79 MiB | 46.58 MiB | **46.43 MiB** |
| **exp-protegido-ms-ordenes-1** |48.28 MiB | 46.50 MiB | 47.20 MiB | 46.84 MiB | 47.20 MiB | **47.20 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 255.90 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-protegido-ms-usuarios-1** |45.64 MiB | 48.04 MiB | 46.36 MiB | 47.81 MiB | 46.25 MiB | **46.82 MiB** |
| **exp-protegido-postgres-db-1** |58.54 MiB | 61.53 MiB | 59.46 MiB | 58.48 MiB | 63.52 MiB | **60.31 MiB** |
