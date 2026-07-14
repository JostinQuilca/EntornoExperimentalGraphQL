# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-10 23:41:30

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 570.763 ms | 0.00% | 0.00% |
| Run 2 | 39 | 569.242 ms | 0.00% | 0.00% |
| Run 3 | 39 | 570.175 ms | 0.00% | 0.00% |
| Run 4 | 39 | 569.557 ms | 0.00% | 0.00% |
| Run 5 | 39 | 569.137 ms | 0.00% | 0.00% |
| **PROMEDIO** | **39.0** | **569.775 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |16.57% | 4.11% | 3.23% | 9.07% | 7.36% | **8.07%** |
| **exp-vulnerable-mongo-db-1** |125.82% | 76.98% | 83.90% | 79.07% | 74.08% | **87.97%** |
| **exp-vulnerable-ms-catalogo-1** |4.31% | 3.94% | 4.49% | 3.83% | 4.96% | **4.31%** |
| **exp-vulnerable-ms-ordenes-1** |6.82% | 4.81% | 6.07% | 5.49% | 13.32% | **7.30%** |
| **exp-vulnerable-ms-resenas-1** |7.18% | 3.94% | 5.30% | 4.52% | 18.11% | **7.81%** |
| **exp-vulnerable-ms-usuarios-1** |6.67% | 4.49% | 5.17% | 4.60% | 15.17% | **7.22%** |
| **exp-vulnerable-postgres-db-1** |9.16% | 5.58% | 5.76% | 5.57% | 6.02% | **6.42%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.41MiB (96.41 MiB)  | 65.34MiB (65.34 MiB)  | 65.5MiB (65.50 MiB)  | 96.59MiB (96.59 MiB)  | 96.58MiB (96.58 MiB)  |
| **exp-vulnerable-mongo-db-1** |350.6MiB (350.60 MiB)  | 350.2MiB (350.20 MiB)  | 352MiB (352.00 MiB)  | 342.5MiB (342.50 MiB)  | 339MiB (339.00 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.11MiB (46.11 MiB)  | 45.94MiB (45.94 MiB)  | 45.98MiB (45.98 MiB)  | 45.89MiB (45.89 MiB)  | 47.67MiB (47.67 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |50.84MiB (50.84 MiB)  | 50.79MiB (50.79 MiB)  | 49.61MiB (49.61 MiB)  | 49.34MiB (49.34 MiB)  | 50.16MiB (50.16 MiB)  |
| **exp-vulnerable-ms-resenas-1** |54.02MiB (54.02 MiB)  | 47.3MiB (47.30 MiB)  | 46.08MiB (46.08 MiB)  | 48.04MiB (48.04 MiB)  | 47.71MiB (47.71 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |46.45MiB (46.45 MiB)  | 46.66MiB (46.66 MiB)  | 46.05MiB (46.05 MiB)  | 47.23MiB (47.23 MiB)  | 47.17MiB (47.17 MiB)  |
| **exp-vulnerable-postgres-db-1** |37.74MiB (37.74 MiB)  | 37.82MiB (37.82 MiB)  | 38.42MiB (38.42 MiB)  | 37.67MiB (37.67 MiB)  | 39.18MiB (39.18 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.23% | 0.68% | 0.69% | 0.79% | 0.72% | **0.82%** |
| **exp-vulnerable-mongo-db-1** |29.84% | 21.11% | 19.68% | 21.28% | 20.99% | **22.58%** |
| **exp-vulnerable-ms-catalogo-1** |1.01% | 1.00% | 1.10% | 0.96% | 1.09% | **1.03%** |
| **exp-vulnerable-ms-ordenes-1** |1.99% | 1.82% | 1.84% | 1.68% | 2.19% | **1.90%** |
| **exp-vulnerable-ms-resenas-1** |1.60% | 1.18% | 1.23% | 1.14% | 1.72% | **1.37%** |
| **exp-vulnerable-ms-usuarios-1** |1.48% | 1.23% | 1.26% | 1.15% | 1.68% | **1.36%** |
| **exp-vulnerable-postgres-db-1** |2.21% | 2.05% | 1.85% | 1.93% | 1.83% | **1.97%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.74 MiB | 64.47 MiB | 64.83 MiB | 65.13 MiB | 69.72 MiB | **66.38 MiB** |
| **exp-vulnerable-mongo-db-1** |215.07 MiB | 211.08 MiB | 214.03 MiB | 215.47 MiB | 203.54 MiB | **211.84 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.98 MiB | 45.81 MiB | 45.85 MiB | 45.37 MiB | 47.51 MiB | **46.10 MiB** |
| **exp-vulnerable-ms-ordenes-1** |49.77 MiB | 49.73 MiB | 48.82 MiB | 48.40 MiB | 48.22 MiB | **48.99 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.75 MiB | 45.82 MiB | 45.86 MiB | 46.43 MiB | 46.18 MiB | **46.21 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.47 MiB | 46.17 MiB | 45.69 MiB | 46.12 MiB | 45.51 MiB | **45.79 MiB** |
| **exp-vulnerable-postgres-db-1** |37.31 MiB | 37.41 MiB | 37.24 MiB | 37.26 MiB | 37.38 MiB | **37.32 MiB** |