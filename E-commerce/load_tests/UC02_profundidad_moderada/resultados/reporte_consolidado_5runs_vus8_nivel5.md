# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 15:49:15

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 72 | 7282.566 ms | 0.00% | 0.00% |
| Run 2 | 72 | 7715.550 ms | 0.00% | 0.00% |
| Run 3 | 64 | 7023.118 ms | 0.00% | 0.00% |
| Run 4 | 56 | 8067.106 ms | 0.00% | 0.00% |
| Run 5 | 64 | 7381.377 ms | 0.00% | 0.00% |
| **PROMEDIO** | **65.6** | **7493.944 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |7.21% | 7.72% | 27.31% | 5.79% | 8.98% | **11.40%** |
| **exp-vulnerable-mongo-db-1** |96.05% | 94.50% | 101.45% | 77.88% | 107.28% | **95.43%** |
| **exp-vulnerable-ms-catalogo-1** |5.33% | 4.12% | 4.13% | 4.58% | 5.99% | **4.83%** |
| **exp-vulnerable-ms-ordenes-1** |4.62% | 4.54% | 5.22% | 4.14% | 5.12% | **4.73%** |
| **exp-vulnerable-ms-resenas-1** |335.17% | 364.14% | 378.22% | 332.18% | 346.07% | **351.16%** |
| **exp-vulnerable-ms-usuarios-1** |4.75% | 4.09% | 5.06% | 4.19% | 5.27% | **4.67%** |
| **exp-vulnerable-postgres-db-1** |39.73% | 46.84% | 38.54% | 52.15% | 61.86% | **47.82%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |68.1MiB (68.10 MiB)  | 68.4MiB (68.40 MiB)  | 68.57MiB (68.57 MiB)  | 68.73MiB (68.73 MiB)  | 67.89MiB (67.89 MiB)  |
| **exp-vulnerable-mongo-db-1** |342.8MiB (342.80 MiB)  | 350.4MiB (350.40 MiB)  | 348.6MiB (348.60 MiB)  | 336.1MiB (336.10 MiB)  | 353.5MiB (353.50 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.3MiB (45.30 MiB)  | 46.74MiB (46.74 MiB)  | 47.22MiB (47.22 MiB)  | 47.09MiB (47.09 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.73MiB (46.73 MiB)  | 46.85MiB (46.85 MiB)  | 46.95MiB (46.95 MiB)  | 46.82MiB (46.82 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-vulnerable-ms-resenas-1** |1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.72MiB (45.72 MiB)  | 46.85MiB (46.85 MiB)  | 47.17MiB (47.17 MiB)  | 47.42MiB (47.42 MiB)  | 46.21MiB (46.21 MiB)  |
| **exp-vulnerable-postgres-db-1** |70.79MiB (70.79 MiB)  | 70.16MiB (70.16 MiB)  | 72.02MiB (72.02 MiB)  | 71MiB (71.00 MiB)  | 70.45MiB (70.45 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.67% | 0.58% | 1.78% | 0.42% | 0.77% | **0.84%** |
| **exp-vulnerable-mongo-db-1** |23.18% | 22.71% | 28.31% | 21.90% | 17.96% | **22.81%** |
| **exp-vulnerable-ms-catalogo-1** |0.95% | 1.12% | 1.09% | 1.07% | 1.11% | **1.07%** |
| **exp-vulnerable-ms-ordenes-1** |1.07% | 1.24% | 1.31% | 1.11% | 0.98% | **1.14%** |
| **exp-vulnerable-ms-resenas-1** |134.46% | 148.46% | 164.62% | 160.50% | 159.50% | **153.51%** |
| **exp-vulnerable-ms-usuarios-1** |1.19% | 1.07% | 1.24% | 1.14% | 1.11% | **1.15%** |
| **exp-vulnerable-postgres-db-1** |5.27% | 5.69% | 6.14% | 6.08% | 8.16% | **6.27%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.18 MiB | 65.76 MiB | 65.56 MiB | 65.79 MiB | 65.99 MiB | **66.06 MiB** |
| **exp-vulnerable-mongo-db-1** |203.64 MiB | 196.18 MiB | 206.84 MiB | 204.97 MiB | 219.45 MiB | **206.22 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.14 MiB | 45.51 MiB | 45.65 MiB | 46.96 MiB | 45.94 MiB | **45.84 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.50 MiB | 46.31 MiB | 46.78 MiB | 46.55 MiB | 45.96 MiB | **46.22 MiB** |
| **exp-vulnerable-ms-resenas-1** |851.30 MiB | 837.10 MiB | 842.11 MiB | 823.40 MiB | 849.45 MiB | **840.67 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.28 MiB | 45.61 MiB | 47.04 MiB | 47.30 MiB | 45.91 MiB | **46.23 MiB** |
| **exp-vulnerable-postgres-db-1** |63.97 MiB | 63.42 MiB | 64.24 MiB | 64.35 MiB | 64.90 MiB | **64.18 MiB** |