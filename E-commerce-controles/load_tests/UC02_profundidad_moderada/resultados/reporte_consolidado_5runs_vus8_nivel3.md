# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-07 21:41:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 144 | 2402.500 ms | 5.55% | 0.00% |
| Run 2 | 152 | 2361.120 ms | 0.00% | 0.00% |
| Run 3 | 193 | 1934.660 ms | 4.14% | 0.00% |
| Run 4 | 170 | 2152.140 ms | 9.41% | 0.00% |
| Run 5 | 161 | 2539.170 ms | 4.96% | 0.00% |
| **PROMEDIO** | **164.0** | **2277.918 ms** | **4.81%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |13.00% | 6.83% | 8.13% | 8.88% | 10.80% | **9.53%** |
| **exp-protegido-mongo-db-1** |109.90% | 106.12% | 97.14% | 53.27% | 100.40% | **93.37%** |
| **exp-protegido-ms-catalogo-1** |4.80% | 4.34% | 4.51% | 5.34% | 5.26% | **4.85%** |
| **exp-protegido-ms-ordenes-1** |4.29% | 4.70% | 4.34% | 5.54% | 4.59% | **4.69%** |
| **exp-protegido-ms-resenas-1** |226.76% | 174.37% | 221.42% | 228.78% | 234.14% | **217.09%** |
| **exp-protegido-ms-usuarios-1** |5.50% | 4.09% | 3.86% | 4.93% | 4.33% | **4.54%** |
| **exp-protegido-postgres-db-1** |57.41% | 27.29% | 43.45% | 39.71% | 40.36% | **41.64%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |97.35 MiB | 70.96 MiB | 71.94 MiB | 72.57 MiB | 73.43 MiB | **77.25 MiB** |
| **exp-protegido-mongo-db-1** |349.90 MiB | 349.80 MiB | 340.40 MiB | 333.40 MiB | 340.40 MiB | **342.78 MiB** |
| **exp-protegido-ms-catalogo-1** |46.05 MiB | 45.10 MiB | 48.82 MiB | 47.62 MiB | 47.49 MiB | **47.02 MiB** |
| **exp-protegido-ms-ordenes-1** |46.28 MiB | 45.50 MiB | 46.09 MiB | 46.14 MiB | 46.27 MiB | **46.06 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.80 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | **255.84 MiB** |
| **exp-protegido-ms-usuarios-1** |45.75 MiB | 45.93 MiB | 45.64 MiB | 47.32 MiB | 46.87 MiB | **46.30 MiB** |
| **exp-protegido-postgres-db-1** |78.09 MiB | 79.12 MiB | 69.84 MiB | 69.26 MiB | 74.13 MiB | **74.09 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.06% | 1.28% | 1.55% | 1.88% | 1.69% | **1.69%** |
| **exp-protegido-mongo-db-1** |109.90% | 106.12% | 97.14% | 53.27% | 100.40% | **93.37%** |
| **exp-protegido-ms-catalogo-1** |4.80% | 4.34% | 4.51% | 5.34% | 5.26% | **4.85%** |
| **exp-protegido-ms-ordenes-1** |4.29% | 4.70% | 4.34% | 5.54% | 4.59% | **4.69%** |
| **exp-protegido-ms-resenas-1** |226.76% | 174.37% | 221.42% | 228.78% | 234.14% | **217.09%** |
| **exp-protegido-ms-usuarios-1** |5.50% | 4.09% | 3.86% | 4.93% | 4.33% | **4.54%** |
| **exp-protegido-postgres-db-1** |57.41% | 27.29% | 43.45% | 39.71% | 40.36% | **41.64%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |72.67 MiB | 69.10 MiB | 69.62 MiB | 70.39 MiB | 69.40 MiB | **70.24 MiB** |
| **exp-protegido-mongo-db-1** |349.90 MiB | 349.80 MiB | 340.40 MiB | 333.40 MiB | 340.40 MiB | **342.78 MiB** |
| **exp-protegido-ms-catalogo-1** |46.05 MiB | 45.10 MiB | 48.82 MiB | 47.62 MiB | 47.49 MiB | **47.02 MiB** |
| **exp-protegido-ms-ordenes-1** |46.28 MiB | 45.50 MiB | 46.09 MiB | 46.14 MiB | 46.27 MiB | **46.06 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.80 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | **255.84 MiB** |
| **exp-protegido-ms-usuarios-1** |45.75 MiB | 45.93 MiB | 45.64 MiB | 47.32 MiB | 46.87 MiB | **46.30 MiB** |
| **exp-protegido-postgres-db-1** |78.09 MiB | 79.12 MiB | 69.84 MiB | 69.26 MiB | 74.13 MiB | **74.09 MiB** |
