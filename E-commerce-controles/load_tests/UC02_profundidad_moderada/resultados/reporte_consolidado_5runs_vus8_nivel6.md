# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 00:41:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 480 | 8.560 ms | 0.00% | 100.00% |
| Run 2 | 480 | 8.330 ms | 0.00% | 100.00% |
| Run 3 | 480 | 8.770 ms | 0.00% | 100.00% |
| Run 4 | 480 | 8.510 ms | 0.00% | 100.00% |
| Run 5 | 480 | 10.920 ms | 0.00% | 100.00% |
| **PROMEDIO** | **480.0** | **9.018 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |12.79% | 8.38% | 8.32% | 11.19% | 13.94% | **10.92%** |
| **exp-protegido-mongo-db-1** |77.98% | 97.13% | 70.00% | 66.55% | 110.37% | **84.41%** |
| **exp-protegido-ms-catalogo-1** |5.09% | 4.77% | 4.43% | 4.25% | 9.96% | **5.70%** |
| **exp-protegido-ms-ordenes-1** |3.58% | 4.25% | 3.76% | 5.09% | 7.92% | **4.92%** |
| **exp-protegido-ms-resenas-1** |4.20% | 3.65% | 4.05% | 5.97% | 5.27% | **4.63%** |
| **exp-protegido-ms-usuarios-1** |4.00% | 4.01% | 4.35% | 5.65% | 8.80% | **5.36%** |
| **exp-protegido-postgres-db-1** |6.77% | 4.81% | 6.40% | 6.77% | 9.11% | **6.77%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |81.69 MiB | 81.68 MiB | 76.36 MiB | 75.95 MiB | 75.71 MiB | **78.28 MiB** |
| **exp-protegido-mongo-db-1** |338.60 MiB | 281.40 MiB | 333.70 MiB | 272.00 MiB | 348.70 MiB | **314.88 MiB** |
| **exp-protegido-ms-catalogo-1** |46.41 MiB | 46.73 MiB | 47.50 MiB | 46.55 MiB | 46.59 MiB | **46.76 MiB** |
| **exp-protegido-ms-ordenes-1** |46.35 MiB | 47.22 MiB | 45.42 MiB | 47.23 MiB | 48.00 MiB | **46.84 MiB** |
| **exp-protegido-ms-resenas-1** |47.16 MiB | 46.21 MiB | 46.46 MiB | 47.48 MiB | 47.87 MiB | **47.04 MiB** |
| **exp-protegido-ms-usuarios-1** |48.21 MiB | 47.04 MiB | 45.54 MiB | 53.85 MiB | 55.41 MiB | **50.01 MiB** |
| **exp-protegido-postgres-db-1** |27.38 MiB | 28.83 MiB | 28.89 MiB | 27.45 MiB | 27.41 MiB | **27.99 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |4.90% | 4.31% | 4.30% | 4.73% | 5.98% | **4.84%** |
| **exp-protegido-mongo-db-1** |77.98% | 97.13% | 70.00% | 66.55% | 110.37% | **84.41%** |
| **exp-protegido-ms-catalogo-1** |5.09% | 4.77% | 4.43% | 4.25% | 9.96% | **5.70%** |
| **exp-protegido-ms-ordenes-1** |3.58% | 4.25% | 3.76% | 5.09% | 7.92% | **4.92%** |
| **exp-protegido-ms-resenas-1** |4.20% | 3.65% | 4.05% | 5.97% | 5.27% | **4.63%** |
| **exp-protegido-ms-usuarios-1** |4.00% | 4.01% | 4.35% | 5.65% | 8.80% | **5.36%** |
| **exp-protegido-postgres-db-1** |6.77% | 4.81% | 6.40% | 6.77% | 9.11% | **6.77%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |73.97 MiB | 75.09 MiB | 73.28 MiB | 72.93 MiB | 72.59 MiB | **73.57 MiB** |
| **exp-protegido-mongo-db-1** |338.60 MiB | 281.40 MiB | 333.70 MiB | 272.00 MiB | 348.70 MiB | **314.88 MiB** |
| **exp-protegido-ms-catalogo-1** |46.41 MiB | 46.73 MiB | 47.50 MiB | 46.55 MiB | 46.59 MiB | **46.76 MiB** |
| **exp-protegido-ms-ordenes-1** |46.35 MiB | 47.22 MiB | 45.42 MiB | 47.23 MiB | 48.00 MiB | **46.84 MiB** |
| **exp-protegido-ms-resenas-1** |47.16 MiB | 46.21 MiB | 46.46 MiB | 47.48 MiB | 47.87 MiB | **47.04 MiB** |
| **exp-protegido-ms-usuarios-1** |48.21 MiB | 47.04 MiB | 45.54 MiB | 53.85 MiB | 55.41 MiB | **50.01 MiB** |
| **exp-protegido-postgres-db-1** |27.38 MiB | 28.83 MiB | 28.89 MiB | 27.45 MiB | 27.41 MiB | **27.99 MiB** |
