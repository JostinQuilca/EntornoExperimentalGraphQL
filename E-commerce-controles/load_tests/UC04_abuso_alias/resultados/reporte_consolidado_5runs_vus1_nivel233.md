# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 02:33:11

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 33 | 815.487 ms | 0.00% | 0.00% |
| Run 2 | 35 | 739.862 ms | 0.00% | 0.00% |
| Run 3 | 35 | 728.950 ms | 0.00% | 0.00% |
| Run 4 | 35 | 749.894 ms | 0.00% | 0.00% |
| Run 5 | 35 | 734.896 ms | 0.00% | 0.00% |
| **PROMEDIO** | **34.6** | **753.818 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |60.38% | 8.24% | 10.31% | 33.10% | 11.11% | **24.63%** |
| **exp-protegido-mongo-db-1** |96.32% | 79.82% | 75.74% | 85.23% | 85.56% | **84.53%** |
| **exp-protegido-ms-catalogo-1** |6.05% | 4.35% | 3.70% | 5.98% | 3.91% | **4.80%** |
| **exp-protegido-ms-ordenes-1** |35.62% | 23.58% | 21.08% | 23.50% | 18.78% | **24.51%** |
| **exp-protegido-ms-resenas-1** |4.81% | 4.01% | 4.11% | 7.11% | 5.31% | **5.07%** |
| **exp-protegido-ms-usuarios-1** |5.29% | 3.61% | 3.98% | 3.52% | 5.05% | **4.29%** |
| **exp-protegido-postgres-db-1** |70.03% | 53.74% | 52.92% | 59.80% | 48.69% | **57.04%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |98.41MiB (98.41 MiB)  | 82.07MiB (82.07 MiB)  | 81.27MiB (81.27 MiB)  | 77MiB (77.00 MiB)  | 76.7MiB (76.70 MiB)  |
| **exp-protegido-mongo-db-1** |341.6MiB (341.60 MiB)  | 343MiB (343.00 MiB)  | 343.5MiB (343.50 MiB)  | 340.2MiB (340.20 MiB)  | 348.7MiB (348.70 MiB)  |
| **exp-protegido-ms-catalogo-1** |47.28MiB (47.28 MiB)  | 47.17MiB (47.17 MiB)  | 48.46MiB (48.46 MiB)  | 46.34MiB (46.34 MiB)  | 47.26MiB (47.26 MiB)  |
| **exp-protegido-ms-ordenes-1** |96.93MiB (96.93 MiB)  | 97.51MiB (97.51 MiB)  | 97.52MiB (97.52 MiB)  | 100.2MiB (100.20 MiB)  | 99.68MiB (99.68 MiB)  |
| **exp-protegido-ms-resenas-1** |47.16MiB (47.16 MiB)  | 46.66MiB (46.66 MiB)  | 45.91MiB (45.91 MiB)  | 45.71MiB (45.71 MiB)  | 46.94MiB (46.94 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.53MiB (45.53 MiB)  | 46.82MiB (46.82 MiB)  | 46.11MiB (46.11 MiB)  | 46.15MiB (46.15 MiB)  | 47.79MiB (47.79 MiB)  |
| **exp-protegido-postgres-db-1** |37.97MiB (37.97 MiB)  | 38.02MiB (38.02 MiB)  | 38.47MiB (38.47 MiB)  | 37.73MiB (37.73 MiB)  | 37.86MiB (37.86 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |4.87% | 1.21% | 1.18% | 2.35% | 1.56% | **2.23%** |
| **exp-protegido-mongo-db-1** |33.60% | 22.96% | 20.14% | 23.38% | 19.81% | **23.98%** |
| **exp-protegido-ms-catalogo-1** |1.36% | 1.10% | 1.04% | 1.33% | 1.09% | **1.18%** |
| **exp-protegido-ms-ordenes-1** |11.99% | 9.70% | 9.15% | 10.70% | 10.04% | **10.32%** |
| **exp-protegido-ms-resenas-1** |1.19% | 1.02% | 1.18% | 1.27% | 1.33% | **1.20%** |
| **exp-protegido-ms-usuarios-1** |1.28% | 1.07% | 1.17% | 1.00% | 1.34% | **1.17%** |
| **exp-protegido-postgres-db-1** |29.91% | 25.46% | 25.12% | 27.29% | 27.61% | **27.08%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |71.84 MiB | 75.24 MiB | 75.16 MiB | 73.53 MiB | 71.69 MiB | **73.49 MiB** |
| **exp-protegido-mongo-db-1** |211.96 MiB | 207.22 MiB | 206.83 MiB | 211.36 MiB | 205.93 MiB | **208.66 MiB** |
| **exp-protegido-ms-catalogo-1** |45.50 MiB | 47.06 MiB | 46.79 MiB | 46.22 MiB | 46.03 MiB | **46.32 MiB** |
| **exp-protegido-ms-ordenes-1** |85.54 MiB | 86.39 MiB | 86.40 MiB | 87.82 MiB | 86.91 MiB | **86.61 MiB** |
| **exp-protegido-ms-resenas-1** |47.03 MiB | 46.24 MiB | 45.82 MiB | 45.41 MiB | 45.57 MiB | **46.01 MiB** |
| **exp-protegido-ms-usuarios-1** |45.16 MiB | 46.28 MiB | 46.01 MiB | 46.06 MiB | 46.05 MiB | **45.91 MiB** |
| **exp-protegido-postgres-db-1** |37.30 MiB | 37.42 MiB | 37.39 MiB | 37.35 MiB | 37.25 MiB | **37.34 MiB** |