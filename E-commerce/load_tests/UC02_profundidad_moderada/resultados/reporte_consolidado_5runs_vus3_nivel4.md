# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 12:54:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 60 | 2152.490 ms | 0.00% | 0.00% |
| Run 2 | 54 | 2972.720 ms | 0.00% | 0.00% |
| Run 3 | 54 | 2745.570 ms | 5.55% | 0.00% |
| Run 4 | 64 | 1985.610 ms | 0.00% | 0.00% |
| Run 5 | 60 | 2027.620 ms | 0.00% | 0.00% |
| **PROMEDIO** | **58.4** | **2376.802 ms** | **1.11%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |6.70% | 2.75% | 7.22% | 4.17% | 13.75% | **6.92%** |
| **exp-vulnerable-mongo-db-1** |98.40% | 118.90% | 112.53% | 92.30% | 97.23% | **103.87%** |
| **exp-vulnerable-ms-catalogo-1** |4.41% | 8.30% | 3.77% | 3.53% | 6.42% | **5.29%** |
| **exp-vulnerable-ms-ordenes-1** |8.95% | 9.07% | 4.00% | 5.99% | 5.53% | **6.71%** |
| **exp-vulnerable-ms-resenas-1** |207.98% | 205.34% | 208.97% | 220.41% | 216.58% | **211.86%** |
| **exp-vulnerable-ms-usuarios-1** |7.55% | 8.89% | 4.44% | 6.40% | 7.92% | **7.04%** |
| **exp-vulnerable-postgres-db-1** |26.26% | 31.22% | 49.49% | 34.64% | 34.81% | **35.28%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |70.64 MiB | 66.02 MiB | 66.95 MiB | 66.58 MiB | 69.88 MiB | **68.01 MiB** |
| **exp-vulnerable-mongo-db-1** |344.30 MiB | 339.10 MiB | 349.10 MiB | 335.30 MiB | 344.80 MiB | **342.52 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.20 MiB | 45.79 MiB | 46.00 MiB | 47.36 MiB | 46.54 MiB | **46.38 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.34 MiB | 46.02 MiB | 45.83 MiB | 48.29 MiB | 47.64 MiB | **46.82 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.80 MiB | 255.90 MiB | 255.80 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.44 MiB | 55.21 MiB | 45.85 MiB | 47.13 MiB | 45.87 MiB | **48.30 MiB** |
| **exp-vulnerable-postgres-db-1** |63.42 MiB | 60.20 MiB | 62.25 MiB | 60.15 MiB | 69.09 MiB | **63.02 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.78% | 0.35% | 0.97% | 0.62% | 1.56% | **0.86%** |
| **exp-vulnerable-mongo-db-1** |98.40% | 118.90% | 112.53% | 92.30% | 97.23% | **103.87%** |
| **exp-vulnerable-ms-catalogo-1** |4.41% | 8.30% | 3.77% | 3.53% | 6.42% | **5.29%** |
| **exp-vulnerable-ms-ordenes-1** |8.95% | 9.07% | 4.00% | 5.99% | 5.53% | **6.71%** |
| **exp-vulnerable-ms-resenas-1** |207.98% | 205.34% | 208.97% | 220.41% | 216.58% | **211.86%** |
| **exp-vulnerable-ms-usuarios-1** |7.55% | 8.89% | 4.44% | 6.40% | 7.92% | **7.04%** |
| **exp-vulnerable-postgres-db-1** |26.26% | 31.22% | 49.49% | 34.64% | 34.81% | **35.28%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.61 MiB | 64.85 MiB | 65.44 MiB | 65.14 MiB | 65.43 MiB | **65.29 MiB** |
| **exp-vulnerable-mongo-db-1** |344.30 MiB | 339.10 MiB | 349.10 MiB | 335.30 MiB | 344.80 MiB | **342.52 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.20 MiB | 45.79 MiB | 46.00 MiB | 47.36 MiB | 46.54 MiB | **46.38 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.34 MiB | 46.02 MiB | 45.83 MiB | 48.29 MiB | 47.64 MiB | **46.82 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.80 MiB | 255.90 MiB | 255.80 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.44 MiB | 55.21 MiB | 45.85 MiB | 47.13 MiB | 45.87 MiB | **48.30 MiB** |
| **exp-vulnerable-postgres-db-1** |63.42 MiB | 60.20 MiB | 62.25 MiB | 60.15 MiB | 69.09 MiB | **63.02 MiB** |
