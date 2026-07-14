# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 02:01:50

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 35 | 719.093 ms | 0.00% | 0.00% |
| Run 2 | 35 | 719.478 ms | 0.00% | 0.00% |
| Run 3 | 35 | 739.146 ms | 0.00% | 0.00% |
| Run 4 | 35 | 744.542 ms | 0.00% | 0.00% |
| Run 5 | 35 | 718.985 ms | 0.00% | 0.00% |
| **PROMEDIO** | **35.0** | **728.249 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |12.93% | 17.99% | 42.50% | 21.17% | 27.09% | **24.34%** |
| **exp-vulnerable-mongo-db-1** |134.90% | 96.80% | 98.72% | 114.90% | 125.23% | **114.11%** |
| **exp-vulnerable-ms-catalogo-1** |6.48% | 5.46% | 6.16% | 5.95% | 5.20% | **5.85%** |
| **exp-vulnerable-ms-ordenes-1** |41.05% | 20.51% | 28.34% | 35.74% | 68.56% | **38.84%** |
| **exp-vulnerable-ms-resenas-1** |7.42% | 4.14% | 5.08% | 5.84% | 5.56% | **5.61%** |
| **exp-vulnerable-ms-usuarios-1** |7.33% | 4.70% | 5.07% | 6.91% | 5.21% | **5.84%** |
| **exp-vulnerable-postgres-db-1** |78.77% | 37.15% | 51.86% | 89.19% | 119.79% | **75.35%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |99.73MiB (99.73 MiB)  | 97.36MiB (97.36 MiB)  | 70.11MiB (70.11 MiB)  | 70MiB (70.00 MiB)  | 69.35MiB (69.35 MiB)  |
| **exp-vulnerable-mongo-db-1** |350.6MiB (350.60 MiB)  | 349.5MiB (349.50 MiB)  | 346.5MiB (346.50 MiB)  | 340.3MiB (340.30 MiB)  | 345.6MiB (345.60 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |47.09MiB (47.09 MiB)  | 46.96MiB (46.96 MiB)  | 49.49MiB (49.49 MiB)  | 45.38MiB (45.38 MiB)  | 45.58MiB (45.58 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |88.88MiB (88.88 MiB)  | 90.2MiB (90.20 MiB)  | 87.34MiB (87.34 MiB)  | 89.57MiB (89.57 MiB)  | 88.2MiB (88.20 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47.39MiB (47.39 MiB)  | 48.01MiB (48.01 MiB)  | 46.48MiB (46.48 MiB)  | 46.5MiB (46.50 MiB)  | 48.79MiB (48.79 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.41MiB (45.41 MiB)  | 46.3MiB (46.30 MiB)  | 46.27MiB (46.27 MiB)  | 47.18MiB (47.18 MiB)  | 46.16MiB (46.16 MiB)  |
| **exp-vulnerable-postgres-db-1** |39.18MiB (39.18 MiB)  | 37.95MiB (37.95 MiB)  | 39.09MiB (39.09 MiB)  | 37.98MiB (37.98 MiB)  | 39.54MiB (39.54 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |2.42% | 1.94% | 3.22% | 2.62% | 2.64% | **2.57%** |
| **exp-vulnerable-mongo-db-1** |39.13% | 22.49% | 31.84% | 33.43% | 28.60% | **31.10%** |
| **exp-vulnerable-ms-catalogo-1** |1.59% | 1.16% | 1.54% | 1.31% | 1.23% | **1.37%** |
| **exp-vulnerable-ms-ordenes-1** |10.04% | 9.64% | 10.35% | 11.43% | 10.69% | **10.43%** |
| **exp-vulnerable-ms-resenas-1** |1.41% | 1.21% | 1.32% | 1.32% | 1.37% | **1.33%** |
| **exp-vulnerable-ms-usuarios-1** |1.59% | 1.22% | 1.29% | 1.25% | 1.30% | **1.33%** |
| **exp-vulnerable-postgres-db-1** |23.62% | 21.46% | 24.09% | 26.53% | 24.86% | **24.11%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |69.90 MiB | 68.90 MiB | 67.24 MiB | 67.94 MiB | 67.73 MiB | **68.34 MiB** |
| **exp-vulnerable-mongo-db-1** |205.00 MiB | 232.95 MiB | 231.80 MiB | 202.07 MiB | 221.49 MiB | **218.66 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.96 MiB | 46.85 MiB | 47.38 MiB | 45.27 MiB | 45.30 MiB | **46.35 MiB** |
| **exp-vulnerable-ms-ordenes-1** |73.20 MiB | 75.31 MiB | 73.66 MiB | 73.19 MiB | 73.69 MiB | **73.81 MiB** |
| **exp-vulnerable-ms-resenas-1** |47.27 MiB | 45.91 MiB | 46.38 MiB | 46.38 MiB | 47.92 MiB | **46.77 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.30 MiB | 45.98 MiB | 46.16 MiB | 47.06 MiB | 46.06 MiB | **46.11 MiB** |
| **exp-vulnerable-postgres-db-1** |37.34 MiB | 37.31 MiB | 37.39 MiB | 37.34 MiB | 37.38 MiB | **37.35 MiB** |