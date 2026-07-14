# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 21:01:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 42 | 1876.710 ms | 0.00% | 0.00% |
| Run 2 | 46 | 1650.030 ms | 0.00% | 0.00% |
| Run 3 | 50 | 1535.380 ms | 0.00% | 0.00% |
| Run 4 | 48 | 1504.300 ms | 0.00% | 0.00% |
| Run 5 | 46 | 1856.580 ms | 0.00% | 0.00% |
| **PROMEDIO** | **46.4** | **1684.600 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |8.74% | 2.24% | 1.99% | 6.96% | 7.50% | **5.49%** |
| **exp-protegido-mongo-db-1** |105.36% | 107.26% | 106.31% | 81.76% | 108.54% | **101.85%** |
| **exp-protegido-ms-catalogo-1** |7.10% | 4.84% | 4.94% | 5.20% | 4.77% | **5.37%** |
| **exp-protegido-ms-ordenes-1** |6.75% | 4.33% | 5.31% | 6.41% | 4.81% | **5.52%** |
| **exp-protegido-ms-resenas-1** |207.05% | 207.91% | 207.01% | 193.39% | 201.03% | **203.28%** |
| **exp-protegido-ms-usuarios-1** |8.30% | 6.07% | 4.82% | 5.41% | 5.15% | **5.95%** |
| **exp-protegido-postgres-db-1** |34.23% | 34.23% | 25.76% | 34.74% | 27.05% | **31.20%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |104.00 MiB | 66.54 MiB | 66.04 MiB | 66.52 MiB | 68.07 MiB | **74.23 MiB** |
| **exp-protegido-mongo-db-1** |336.30 MiB | 349.40 MiB | 349.60 MiB | 345.60 MiB | 349.40 MiB | **346.06 MiB** |
| **exp-protegido-ms-catalogo-1** |89.37 MiB | 45.91 MiB | 46.46 MiB | 51.46 MiB | 47.58 MiB | **56.16 MiB** |
| **exp-protegido-ms-ordenes-1** |101.50 MiB | 45.54 MiB | 47.32 MiB | 45.52 MiB | 46.21 MiB | **57.22 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-protegido-ms-usuarios-1** |92.05 MiB | 46.88 MiB | 45.54 MiB | 48.37 MiB | 46.20 MiB | **55.81 MiB** |
| **exp-protegido-postgres-db-1** |58.78 MiB | 58.53 MiB | 60.22 MiB | 58.53 MiB | 58.53 MiB | **58.92 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.46% | 0.53% | 0.57% | 0.85% | 0.92% | **0.87%** |
| **exp-protegido-mongo-db-1** |105.36% | 107.26% | 106.31% | 81.76% | 108.54% | **101.85%** |
| **exp-protegido-ms-catalogo-1** |7.10% | 4.84% | 4.94% | 5.20% | 4.77% | **5.37%** |
| **exp-protegido-ms-ordenes-1** |6.75% | 4.33% | 5.31% | 6.41% | 4.81% | **5.52%** |
| **exp-protegido-ms-resenas-1** |207.05% | 207.91% | 207.01% | 193.39% | 201.03% | **203.28%** |
| **exp-protegido-ms-usuarios-1** |8.30% | 6.07% | 4.82% | 5.41% | 5.15% | **5.95%** |
| **exp-protegido-postgres-db-1** |34.23% | 34.23% | 25.76% | 34.74% | 27.05% | **31.20%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |74.71 MiB | 65.42 MiB | 64.85 MiB | 65.52 MiB | 65.80 MiB | **67.26 MiB** |
| **exp-protegido-mongo-db-1** |336.30 MiB | 349.40 MiB | 349.60 MiB | 345.60 MiB | 349.40 MiB | **346.06 MiB** |
| **exp-protegido-ms-catalogo-1** |89.37 MiB | 45.91 MiB | 46.46 MiB | 51.46 MiB | 47.58 MiB | **56.16 MiB** |
| **exp-protegido-ms-ordenes-1** |101.50 MiB | 45.54 MiB | 47.32 MiB | 45.52 MiB | 46.21 MiB | **57.22 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-protegido-ms-usuarios-1** |92.05 MiB | 46.88 MiB | 45.54 MiB | 48.37 MiB | 46.20 MiB | **55.81 MiB** |
| **exp-protegido-postgres-db-1** |58.78 MiB | 58.53 MiB | 60.22 MiB | 58.53 MiB | 58.53 MiB | **58.92 MiB** |
