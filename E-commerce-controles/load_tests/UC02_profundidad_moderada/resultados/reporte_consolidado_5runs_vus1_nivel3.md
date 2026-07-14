# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 10:39:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 25 | 1414.040 ms | 0.00% | 0.00% |
| Run 2 | 29 | 1095.930 ms | 0.00% | 0.00% |
| Run 3 | 27 | 1255.930 ms | 0.00% | 0.00% |
| Run 4 | 30 | 1029.030 ms | 0.00% | 0.00% |
| Run 5 | 30 | 1034.140 ms | 0.00% | 0.00% |
| **PROMEDIO** | **28.2** | **1165.814 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |4.39% | 4.11% | 5.16% | 4.18% | 2.75% | **4.12%** |
| **exp-protegido-mongo-db-1** |118.32% | 119.10% | 121.66% | 129.74% | 86.94% | **115.15%** |
| **exp-protegido-ms-catalogo-1** |9.71% | 17.30% | 6.07% | 4.97% | 7.35% | **9.08%** |
| **exp-protegido-ms-ordenes-1** |11.68% | 11.70% | 13.66% | 8.55% | 3.81% | **9.88%** |
| **exp-protegido-ms-resenas-1** |192.68% | 197.57% | 189.75% | 200.72% | 193.75% | **194.89%** |
| **exp-protegido-ms-usuarios-1** |9.33% | 12.51% | 8.49% | 6.37% | 4.76% | **8.29%** |
| **exp-protegido-postgres-db-1** |36.73% | 24.65% | 34.33% | 19.55% | 26.88% | **28.43%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.18 MiB | 65.05 MiB | 65.46 MiB | 65.01 MiB | 65.38 MiB | **65.22 MiB** |
| **exp-protegido-mongo-db-1** |346.70 MiB | 347.90 MiB | 350.10 MiB | 349.00 MiB | 337.50 MiB | **346.24 MiB** |
| **exp-protegido-ms-catalogo-1** |54.55 MiB | 47.38 MiB | 45.84 MiB | 45.18 MiB | 45.98 MiB | **47.79 MiB** |
| **exp-protegido-ms-ordenes-1** |46.88 MiB | 54.12 MiB | 46.31 MiB | 47.89 MiB | 46.45 MiB | **48.33 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-protegido-ms-usuarios-1** |45.94 MiB | 45.64 MiB | 45.68 MiB | 46.66 MiB | 45.73 MiB | **45.93 MiB** |
| **exp-protegido-postgres-db-1** |58.31 MiB | 57.28 MiB | 56.84 MiB | 59.58 MiB | 58.18 MiB | **58.04 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.79% | 0.89% | 0.86% | 0.66% | 0.44% | **0.73%** |
| **exp-protegido-mongo-db-1** |118.32% | 119.10% | 121.66% | 129.74% | 86.94% | **115.15%** |
| **exp-protegido-ms-catalogo-1** |9.71% | 17.30% | 6.07% | 4.97% | 7.35% | **9.08%** |
| **exp-protegido-ms-ordenes-1** |11.68% | 11.70% | 13.66% | 8.55% | 3.81% | **9.88%** |
| **exp-protegido-ms-resenas-1** |192.68% | 197.57% | 189.75% | 200.72% | 193.75% | **194.89%** |
| **exp-protegido-ms-usuarios-1** |9.33% | 12.51% | 8.49% | 6.37% | 4.76% | **8.29%** |
| **exp-protegido-postgres-db-1** |36.73% | 24.65% | 34.33% | 19.55% | 26.88% | **28.43%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |64.19 MiB | 64.39 MiB | 64.57 MiB | 64.31 MiB | 64.73 MiB | **64.44 MiB** |
| **exp-protegido-mongo-db-1** |346.70 MiB | 347.90 MiB | 350.10 MiB | 349.00 MiB | 337.50 MiB | **346.24 MiB** |
| **exp-protegido-ms-catalogo-1** |54.55 MiB | 47.38 MiB | 45.84 MiB | 45.18 MiB | 45.98 MiB | **47.79 MiB** |
| **exp-protegido-ms-ordenes-1** |46.88 MiB | 54.12 MiB | 46.31 MiB | 47.89 MiB | 46.45 MiB | **48.33 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-protegido-ms-usuarios-1** |45.94 MiB | 45.64 MiB | 45.68 MiB | 46.66 MiB | 45.73 MiB | **45.93 MiB** |
| **exp-protegido-postgres-db-1** |58.31 MiB | 57.28 MiB | 56.84 MiB | 59.58 MiB | 58.18 MiB | **58.04 MiB** |
