# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 03:13:25

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 46 | 318.430 ms | 0.00% | 0.00% |
| Run 2 | 45 | 354.396 ms | 0.00% | 0.00% |
| Run 3 | 47 | 279.703 ms | 0.00% | 0.00% |
| Run 4 | 48 | 260.819 ms | 0.00% | 0.00% |
| Run 5 | 47 | 281.796 ms | 0.00% | 0.00% |
| **PROMEDIO** | **46.6** | **299.029 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |30.74% | 37.55% | 29.90% | 24.74% | 29.21% | **30.43%** |
| **exp-protegido-mongo-db-1** |91.93% | 114.73% | 77.89% | 75.64% | 82.92% | **88.62%** |
| **exp-protegido-ms-catalogo-1** |5.01% | 6.45% | 4.54% | 4.07% | 3.22% | **4.66%** |
| **exp-protegido-ms-ordenes-1** |4.77% | 6.44% | 4.25% | 4.77% | 18.53% | **7.75%** |
| **exp-protegido-ms-resenas-1** |3.76% | 7.90% | 4.46% | 4.99% | 4.47% | **5.12%** |
| **exp-protegido-ms-usuarios-1** |52.84% | 43.54% | 39.25% | 32.91% | 53.07% | **44.32%** |
| **exp-protegido-postgres-db-1** |10.01% | 9.15% | 6.03% | 6.15% | 8.29% | **7.93%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |109.9MiB (109.90 MiB)  | 107.8MiB (107.80 MiB)  | 110.8MiB (110.80 MiB)  | 105.9MiB (105.90 MiB)  | 106MiB (106.00 MiB)  |
| **exp-protegido-mongo-db-1** |345.9MiB (345.90 MiB)  | 341.5MiB (341.50 MiB)  | 343.7MiB (343.70 MiB)  | 329.5MiB (329.50 MiB)  | 340.6MiB (340.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.04MiB (46.04 MiB)  | 47.13MiB (47.13 MiB)  | 45.21MiB (45.21 MiB)  | 46MiB (46.00 MiB)  | 46.33MiB (46.33 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.34MiB (46.34 MiB)  | 45.89MiB (45.89 MiB)  | 46.28MiB (46.28 MiB)  | 46.26MiB (46.26 MiB)  | 46.46MiB (46.46 MiB)  |
| **exp-protegido-ms-resenas-1** |45.88MiB (45.88 MiB)  | 48.27MiB (48.27 MiB)  | 46.05MiB (46.05 MiB)  | 46.21MiB (46.21 MiB)  | 45.54MiB (45.54 MiB)  |
| **exp-protegido-ms-usuarios-1** |130.3MiB (130.30 MiB)  | 127.8MiB (127.80 MiB)  | 132.3MiB (132.30 MiB)  | 124.6MiB (124.60 MiB)  | 136.7MiB (136.70 MiB)  |
| **exp-protegido-postgres-db-1** |30.16MiB (30.16 MiB)  | 32.39MiB (32.39 MiB)  | 31.1MiB (31.10 MiB)  | 30.46MiB (30.46 MiB)  | 30.47MiB (30.47 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |14.59% | 14.79% | 12.76% | 11.18% | 12.65% | **13.19%** |
| **exp-protegido-mongo-db-1** |22.69% | 38.54% | 22.19% | 18.57% | 21.10% | **24.62%** |
| **exp-protegido-ms-catalogo-1** |1.27% | 1.45% | 1.08% | 0.99% | 0.91% | **1.14%** |
| **exp-protegido-ms-ordenes-1** |1.27% | 1.55% | 0.93% | 1.10% | 1.52% | **1.27%** |
| **exp-protegido-ms-resenas-1** |1.08% | 1.61% | 1.01% | 1.08% | 1.13% | **1.18%** |
| **exp-protegido-ms-usuarios-1** |19.01% | 21.24% | 18.14% | 17.54% | 18.26% | **18.84%** |
| **exp-protegido-postgres-db-1** |2.31% | 2.50% | 1.85% | 1.95% | 2.19% | **2.16%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |100.22 MiB | 103.23 MiB | 101.91 MiB | 100.51 MiB | 100.59 MiB | **101.29 MiB** |
| **exp-protegido-mongo-db-1** |202.94 MiB | 224.17 MiB | 214.94 MiB | 203.49 MiB | 206.18 MiB | **210.34 MiB** |
| **exp-protegido-ms-catalogo-1** |45.90 MiB | 45.56 MiB | 45.12 MiB | 45.90 MiB | 46.23 MiB | **45.74 MiB** |
| **exp-protegido-ms-ordenes-1** |45.59 MiB | 45.78 MiB | 46.19 MiB | 46.16 MiB | 45.55 MiB | **45.85 MiB** |
| **exp-protegido-ms-resenas-1** |45.74 MiB | 48.16 MiB | 45.90 MiB | 46.11 MiB | 45.44 MiB | **46.27 MiB** |
| **exp-protegido-ms-usuarios-1** |119.57 MiB | 122.79 MiB | 122.78 MiB | 116.52 MiB | 121.36 MiB | **120.60 MiB** |
| **exp-protegido-postgres-db-1** |30.04 MiB | 30.26 MiB | 30.23 MiB | 30.21 MiB | 30.24 MiB | **30.20 MiB** |