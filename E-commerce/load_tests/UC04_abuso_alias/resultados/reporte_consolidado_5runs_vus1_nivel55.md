# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 01:21:28

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 37 | 622.318 ms | 0.00% | 0.00% |
| Run 2 | 38 | 614.187 ms | 0.00% | 0.00% |
| Run 3 | 38 | 617.322 ms | 0.00% | 0.00% |
| Run 4 | 38 | 615.562 ms | 0.00% | 0.00% |
| Run 5 | 38 | 614.124 ms | 0.00% | 0.00% |
| **PROMEDIO** | **37.8** | **616.702 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |20.59% | 7.43% | 3.52% | 8.90% | 6.41% | **9.37%** |
| **exp-vulnerable-mongo-db-1** |80.17% | 81.68% | 85.47% | 78.49% | 73.18% | **79.80%** |
| **exp-vulnerable-ms-catalogo-1** |4.65% | 4.05% | 4.41% | 3.99% | 3.83% | **4.19%** |
| **exp-vulnerable-ms-ordenes-1** |12.45% | 11.71% | 11.85% | 9.17% | 12.72% | **11.58%** |
| **exp-vulnerable-ms-resenas-1** |4.87% | 9.54% | 4.74% | 4.72% | 4.93% | **5.76%** |
| **exp-vulnerable-ms-usuarios-1** |4.87% | 4.79% | 4.75% | 4.98% | 4.96% | **4.87%** |
| **exp-vulnerable-postgres-db-1** |18.64% | 17.68% | 16.07% | 16.20% | 19.83% | **17.68%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |97.38MiB (97.38 MiB)  | 95.95MiB (95.95 MiB)  | 97.54MiB (97.54 MiB)  | 66.77MiB (66.77 MiB)  | 96.28MiB (96.28 MiB)  |
| **exp-vulnerable-mongo-db-1** |343MiB (343.00 MiB)  | 350.7MiB (350.70 MiB)  | 353.3MiB (353.30 MiB)  | 351.8MiB (351.80 MiB)  | 334.8MiB (334.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |47.27MiB (47.27 MiB)  | 46.14MiB (46.14 MiB)  | 45.85MiB (45.85 MiB)  | 46.37MiB (46.37 MiB)  | 46.58MiB (46.58 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |58.77MiB (58.77 MiB)  | 64.77MiB (64.77 MiB)  | 62.24MiB (62.24 MiB)  | 59.02MiB (59.02 MiB)  | 60.44MiB (60.44 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47.95MiB (47.95 MiB)  | 45.62MiB (45.62 MiB)  | 46.43MiB (46.43 MiB)  | 47.16MiB (47.16 MiB)  | 46.3MiB (46.30 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |48.53MiB (48.53 MiB)  | 48.14MiB (48.14 MiB)  | 54.91MiB (54.91 MiB)  | 45.86MiB (45.86 MiB)  | 46.59MiB (46.59 MiB)  |
| **exp-vulnerable-postgres-db-1** |37.93MiB (37.93 MiB)  | 37.94MiB (37.94 MiB)  | 38.92MiB (38.92 MiB)  | 38.61MiB (38.61 MiB)  | 37.59MiB (37.59 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.73% | 1.20% | 0.87% | 1.21% | 1.30% | **1.26%** |
| **exp-vulnerable-mongo-db-1** |21.18% | 20.39% | 23.16% | 19.86% | 22.68% | **21.45%** |
| **exp-vulnerable-ms-catalogo-1** |1.08% | 0.89% | 0.96% | 1.07% | 0.96% | **0.99%** |
| **exp-vulnerable-ms-ordenes-1** |4.71% | 4.37% | 4.06% | 4.44% | 4.58% | **4.43%** |
| **exp-vulnerable-ms-resenas-1** |1.21% | 1.53% | 1.19% | 1.15% | 1.16% | **1.25%** |
| **exp-vulnerable-ms-usuarios-1** |1.29% | 1.27% | 1.37% | 1.13% | 1.18% | **1.25%** |
| **exp-vulnerable-postgres-db-1** |9.04% | 8.78% | 8.08% | 9.05% | 9.21% | **8.83%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |69.06 MiB | 66.67 MiB | 67.63 MiB | 65.58 MiB | 67.06 MiB | **67.20 MiB** |
| **exp-vulnerable-mongo-db-1** |211.99 MiB | 205.57 MiB | 206.47 MiB | 210.98 MiB | 202.90 MiB | **207.58 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.78 MiB | 46.02 MiB | 45.73 MiB | 46.24 MiB | 46.44 MiB | **46.04 MiB** |
| **exp-vulnerable-ms-ordenes-1** |54.83 MiB | 57.75 MiB | 57.35 MiB | 55.80 MiB | 56.34 MiB | **56.41 MiB** |
| **exp-vulnerable-ms-resenas-1** |47.77 MiB | 45.51 MiB | 46.31 MiB | 47.04 MiB | 46.08 MiB | **46.54 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.28 MiB | 46.65 MiB | 48.36 MiB | 45.74 MiB | 46.06 MiB | **46.82 MiB** |
| **exp-vulnerable-postgres-db-1** |37.29 MiB | 37.23 MiB | 37.42 MiB | 37.24 MiB | 37.18 MiB | **37.27 MiB** |