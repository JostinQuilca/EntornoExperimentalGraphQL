# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 14:19:39

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 11 | 10370.339 ms | 9.09% | 0.00% |
| Run 2 | 11 | 11129.280 ms | 9.09% | 0.00% |
| Run 3 | 11 | 10272.693 ms | 9.09% | 0.00% |
| Run 4 | 11 | 10269.866 ms | 9.09% | 0.00% |
| Run 5 | 11 | 11317.033 ms | 9.09% | 0.00% |
| **PROMEDIO** | **11.0** | **10671.842 ms** | **9.09%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |123.97% | 139.57% | 163.97% | 130.69% | 149.24% | **141.49%** |
| **exp-protegido-mongo-db-1** |95.06% | 90.31% | 109.31% | 93.50% | 113.33% | **100.30%** |
| **exp-protegido-ms-catalogo-1** |3.78% | 4.82% | 16.82% | 4.25% | 6.39% | **7.21%** |
| **exp-protegido-ms-ordenes-1** |4.67% | 4.49% | 3.99% | 4.20% | 5.66% | **4.60%** |
| **exp-protegido-ms-resenas-1** |183.25% | 177.41% | 181.24% | 173.97% | 168.87% | **176.95%** |
| **exp-protegido-ms-usuarios-1** |259.74% | 215.42% | 214.31% | 236.60% | 235.03% | **232.22%** |
| **exp-protegido-postgres-db-1** |28.89% | 19.73% | 21.98% | 5.59% | 14.30% | **18.10%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |752.4MiB (752.40 MiB)  | 700.3MiB (700.30 MiB)  | 700.8MiB (700.80 MiB)  | 739.7MiB (739.70 MiB)  | 700.8MiB (700.80 MiB)  |
| **exp-protegido-mongo-db-1** |354.4MiB (354.40 MiB)  | 340.9MiB (340.90 MiB)  | 349.1MiB (349.10 MiB)  | 346.9MiB (346.90 MiB)  | 347.6MiB (347.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |71.04MiB (71.04 MiB)  | 46.07MiB (46.07 MiB)  | 53.58MiB (53.58 MiB)  | 54.03MiB (54.03 MiB)  | 45.89MiB (45.89 MiB)  |
| **exp-protegido-ms-ordenes-1** |71.44MiB (71.44 MiB)  | 45.9MiB (45.90 MiB)  | 47.73MiB (47.73 MiB)  | 47.32MiB (47.32 MiB)  | 46.65MiB (46.65 MiB)  |
| **exp-protegido-ms-resenas-1** |805.9MiB (805.90 MiB)  | 835.4MiB (835.40 MiB)  | 1022MiB (1022.00 MiB)  | 946.4MiB (946.40 MiB)  | 1022MiB (1022.00 MiB)  |
| **exp-protegido-ms-usuarios-1** |511.7MiB (511.70 MiB)  | 511.8MiB (511.80 MiB)  | 511.9MiB (511.90 MiB)  | 511.7MiB (511.70 MiB)  | 511.8MiB (511.80 MiB)  |
| **exp-protegido-postgres-db-1** |68.92MiB (68.92 MiB)  | 65.75MiB (65.75 MiB)  | 65.96MiB (65.96 MiB)  | 70.66MiB (70.66 MiB)  | 67.67MiB (67.67 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |51.25% | 48.83% | 55.57% | 47.57% | 57.15% | **52.07%** |
| **exp-protegido-mongo-db-1** |23.59% | 19.53% | 23.59% | 21.71% | 22.93% | **22.27%** |
| **exp-protegido-ms-catalogo-1** |0.86% | 1.30% | 1.40% | 0.95% | 1.07% | **1.12%** |
| **exp-protegido-ms-ordenes-1** |1.15% | 1.27% | 1.22% | 1.21% | 1.19% | **1.21%** |
| **exp-protegido-ms-resenas-1** |41.74% | 32.95% | 37.82% | 42.61% | 29.34% | **36.89%** |
| **exp-protegido-ms-usuarios-1** |43.88% | 30.36% | 37.05% | 37.25% | 35.63% | **36.83%** |
| **exp-protegido-postgres-db-1** |4.61% | 2.54% | 4.01% | 1.38% | 3.03% | **3.11%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |417.20 MiB | 415.03 MiB | 390.59 MiB | 437.72 MiB | 400.72 MiB | **412.25 MiB** |
| **exp-protegido-mongo-db-1** |221.23 MiB | 205.58 MiB | 210.34 MiB | 208.09 MiB | 207.17 MiB | **210.48 MiB** |
| **exp-protegido-ms-catalogo-1** |70.02 MiB | 45.96 MiB | 47.20 MiB | 52.28 MiB | 45.77 MiB | **52.25 MiB** |
| **exp-protegido-ms-ordenes-1** |71.13 MiB | 45.78 MiB | 46.47 MiB | 47.22 MiB | 46.19 MiB | **51.36 MiB** |
| **exp-protegido-ms-resenas-1** |655.83 MiB | 666.90 MiB | 752.96 MiB | 684.00 MiB | 629.39 MiB | **677.82 MiB** |
| **exp-protegido-ms-usuarios-1** |347.59 MiB | 343.59 MiB | 342.17 MiB | 338.02 MiB | 335.08 MiB | **341.29 MiB** |
| **exp-protegido-postgres-db-1** |66.17 MiB | 63.34 MiB | 63.41 MiB | 62.34 MiB | 63.40 MiB | **63.73 MiB** |