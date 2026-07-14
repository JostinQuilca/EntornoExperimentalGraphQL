# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 20:38:26

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 460 | 51.932 ms | 0.00% | 0.00% |
| Run 2 | 458 | 58.925 ms | 0.00% | 0.00% |
| Run 3 | 461 | 51.917 ms | 0.00% | 0.00% |
| Run 4 | 457 | 59.951 ms | 0.00% | 0.00% |
| Run 5 | 457 | 58.422 ms | 0.00% | 0.00% |
| **PROMEDIO** | **458.6** | **56.230 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |16.05% | 23.28% | 19.03% | 22.35% | 23.47% | **20.84%** |
| **exp-protegido-mongo-db-1** |87.40% | 104.07% | 96.38% | 129.53% | 105.21% | **104.52%** |
| **exp-protegido-ms-catalogo-1** |6.45% | 5.27% | 8.68% | 5.91% | 5.78% | **6.42%** |
| **exp-protegido-ms-ordenes-1** |5.80% | 6.52% | 4.24% | 6.10% | 7.20% | **5.97%** |
| **exp-protegido-ms-resenas-1** |15.83% | 20.66% | 16.99% | 14.91% | 13.12% | **16.30%** |
| **exp-protegido-ms-usuarios-1** |17.20% | 41.87% | 29.53% | 19.94% | 40.83% | **29.87%** |
| **exp-protegido-postgres-db-1** |34.64% | 30.13% | 24.23% | 35.05% | 46.49% | **34.11%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |105MiB (105.00 MiB)  | 99.74MiB (99.74 MiB)  | 100.3MiB (100.30 MiB)  | 100.3MiB (100.30 MiB)  | 100.4MiB (100.40 MiB)  |
| **exp-protegido-mongo-db-1** |342.6MiB (342.60 MiB)  | 339.6MiB (339.60 MiB)  | 345.5MiB (345.50 MiB)  | 343.4MiB (343.40 MiB)  | 342.5MiB (342.50 MiB)  |
| **exp-protegido-ms-catalogo-1** |91.58MiB (91.58 MiB)  | 47.51MiB (47.51 MiB)  | 48.56MiB (48.56 MiB)  | 47.86MiB (47.86 MiB)  | 46.44MiB (46.44 MiB)  |
| **exp-protegido-ms-ordenes-1** |94.47MiB (94.47 MiB)  | 46.16MiB (46.16 MiB)  | 45.82MiB (45.82 MiB)  | 45.09MiB (45.09 MiB)  | 45.79MiB (45.79 MiB)  |
| **exp-protegido-ms-resenas-1** |115.7MiB (115.70 MiB)  | 69.82MiB (69.82 MiB)  | 69.74MiB (69.74 MiB)  | 69.76MiB (69.76 MiB)  | 70.2MiB (70.20 MiB)  |
| **exp-protegido-ms-usuarios-1** |118.8MiB (118.80 MiB)  | 74.47MiB (74.47 MiB)  | 71.1MiB (71.10 MiB)  | 70.48MiB (70.48 MiB)  | 69.68MiB (69.68 MiB)  |
| **exp-protegido-postgres-db-1** |70.46MiB (70.46 MiB)  | 69.23MiB (69.23 MiB)  | 68.64MiB (68.64 MiB)  | 68.7MiB (68.70 MiB)  | 68.71MiB (68.71 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |8.07% | 10.57% | 8.90% | 9.50% | 10.54% | **9.52%** |
| **exp-protegido-mongo-db-1** |26.30% | 24.04% | 25.45% | 35.58% | 31.18% | **28.51%** |
| **exp-protegido-ms-catalogo-1** |1.74% | 1.39% | 1.45% | 1.37% | 1.19% | **1.43%** |
| **exp-protegido-ms-ordenes-1** |1.46% | 1.41% | 1.32% | 1.56% | 1.31% | **1.41%** |
| **exp-protegido-ms-resenas-1** |6.54% | 6.56% | 6.44% | 7.35% | 6.93% | **6.76%** |
| **exp-protegido-ms-usuarios-1** |5.32% | 6.96% | 6.25% | 6.16% | 6.63% | **6.26%** |
| **exp-protegido-postgres-db-1** |16.76% | 18.67% | 16.79% | 18.33% | 17.85% | **17.68%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |96.69 MiB | 92.36 MiB | 92.16 MiB | 92.45 MiB | 92.35 MiB | **93.20 MiB** |
| **exp-protegido-mongo-db-1** |209.06 MiB | 210.30 MiB | 204.11 MiB | 227.20 MiB | 208.59 MiB | **211.85 MiB** |
| **exp-protegido-ms-catalogo-1** |90.25 MiB | 46.46 MiB | 46.18 MiB | 47.76 MiB | 46.35 MiB | **55.40 MiB** |
| **exp-protegido-ms-ordenes-1** |94.34 MiB | 46.06 MiB | 45.72 MiB | 44.99 MiB | 45.69 MiB | **55.36 MiB** |
| **exp-protegido-ms-resenas-1** |106.96 MiB | 61.03 MiB | 60.93 MiB | 60.76 MiB | 61.45 MiB | **70.23 MiB** |
| **exp-protegido-ms-usuarios-1** |113.30 MiB | 69.17 MiB | 66.69 MiB | 65.63 MiB | 65.83 MiB | **76.12 MiB** |
| **exp-protegido-postgres-db-1** |68.98 MiB | 67.13 MiB | 67.02 MiB | 67.00 MiB | 67.76 MiB | **67.58 MiB** |