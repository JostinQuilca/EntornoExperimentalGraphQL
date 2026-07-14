# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 18:33:34

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 465 | 38.883 ms | 0.00% | 0.00% |
| Run 2 | 465 | 44.634 ms | 0.00% | 0.00% |
| Run 3 | 465 | 43.457 ms | 0.00% | 0.00% |
| Run 4 | 465 | 41.925 ms | 0.00% | 0.00% |
| Run 5 | 465 | 39.672 ms | 0.00% | 0.00% |
| **PROMEDIO** | **465.0** | **41.714 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |23.65% | 14.67% | 22.04% | 20.07% | 16.38% | **19.36%** |
| **exp-protegido-mongo-db-1** |59.84% | 58.52% | 61.53% | 60.57% | 70.85% | **62.26%** |
| **exp-protegido-ms-catalogo-1** |3.40% | 3.95% | 4.05% | 5.17% | 3.75% | **4.06%** |
| **exp-protegido-ms-ordenes-1** |10.31% | 3.32% | 3.10% | 3.41% | 2.99% | **4.63%** |
| **exp-protegido-ms-resenas-1** |16.78% | 9.94% | 7.12% | 9.08% | 7.95% | **10.17%** |
| **exp-protegido-ms-usuarios-1** |25.15% | 7.02% | 6.81% | 24.47% | 7.24% | **14.14%** |
| **exp-protegido-postgres-db-1** |22.34% | 38.57% | 25.21% | 19.23% | 21.18% | **25.31%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |104.7MiB (104.70 MiB)  | 99.24MiB (99.24 MiB)  | 99.09MiB (99.09 MiB)  | 99.06MiB (99.06 MiB)  | 98.7MiB (98.70 MiB)  |
| **exp-protegido-mongo-db-1** |355.5MiB (355.50 MiB)  | 335.4MiB (335.40 MiB)  | 341.9MiB (341.90 MiB)  | 350.3MiB (350.30 MiB)  | 349.2MiB (349.20 MiB)  |
| **exp-protegido-ms-catalogo-1** |47.42MiB (47.42 MiB)  | 46.5MiB (46.50 MiB)  | 46.54MiB (46.54 MiB)  | 46.78MiB (46.78 MiB)  | 47.01MiB (47.01 MiB)  |
| **exp-protegido-ms-ordenes-1** |47.3MiB (47.30 MiB)  | 45.57MiB (45.57 MiB)  | 46.91MiB (46.91 MiB)  | 47.41MiB (47.41 MiB)  | 46.61MiB (46.61 MiB)  |
| **exp-protegido-ms-resenas-1** |63.48MiB (63.48 MiB)  | 64.66MiB (64.66 MiB)  | 63.99MiB (63.99 MiB)  | 62.71MiB (62.71 MiB)  | 62.6MiB (62.60 MiB)  |
| **exp-protegido-ms-usuarios-1** |67.43MiB (67.43 MiB)  | 71.82MiB (71.82 MiB)  | 71.6MiB (71.60 MiB)  | 69.2MiB (69.20 MiB)  | 75.64MiB (75.64 MiB)  |
| **exp-protegido-postgres-db-1** |69.27MiB (69.27 MiB)  | 70.15MiB (70.15 MiB)  | 70.09MiB (70.09 MiB)  | 71.89MiB (71.89 MiB)  | 70.67MiB (70.67 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |7.35% | 6.52% | 6.68% | 6.59% | 5.90% | **6.61%** |
| **exp-protegido-mongo-db-1** |15.71% | 15.34% | 14.35% | 15.79% | 17.07% | **15.65%** |
| **exp-protegido-ms-catalogo-1** |0.88% | 0.88% | 0.88% | 0.97% | 0.87% | **0.90%** |
| **exp-protegido-ms-ordenes-1** |1.12% | 0.84% | 0.74% | 0.90% | 0.82% | **0.88%** |
| **exp-protegido-ms-resenas-1** |4.63% | 4.15% | 4.03% | 4.39% | 3.99% | **4.24%** |
| **exp-protegido-ms-usuarios-1** |4.88% | 3.76% | 3.73% | 4.87% | 3.75% | **4.20%** |
| **exp-protegido-postgres-db-1** |12.50% | 12.16% | 13.10% | 12.57% | 12.11% | **12.49%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |91.06 MiB | 89.68 MiB | 89.82 MiB | 90.27 MiB | 89.73 MiB | **90.11 MiB** |
| **exp-protegido-mongo-db-1** |205.80 MiB | 197.61 MiB | 199.82 MiB | 198.14 MiB | 193.92 MiB | **199.06 MiB** |
| **exp-protegido-ms-catalogo-1** |47.28 MiB | 46.38 MiB | 46.42 MiB | 46.68 MiB | 46.91 MiB | **46.73 MiB** |
| **exp-protegido-ms-ordenes-1** |47.17 MiB | 45.47 MiB | 46.50 MiB | 46.59 MiB | 46.19 MiB | **46.38 MiB** |
| **exp-protegido-ms-resenas-1** |57.35 MiB | 58.15 MiB | 58.26 MiB | 57.65 MiB | 57.17 MiB | **57.72 MiB** |
| **exp-protegido-ms-usuarios-1** |63.46 MiB | 67.22 MiB | 62.47 MiB | 64.58 MiB | 67.27 MiB | **65.00 MiB** |
| **exp-protegido-postgres-db-1** |68.43 MiB | 67.61 MiB | 68.64 MiB | 71.45 MiB | 68.64 MiB | **68.95 MiB** |