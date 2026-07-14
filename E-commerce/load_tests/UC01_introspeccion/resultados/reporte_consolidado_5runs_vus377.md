# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=377)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 21:47:10

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 22426 | 16.519 ms | 0.66% |
| Run 2 | 22447 | 13.892 ms | 0.73% |
| Run 3 | 22435 | 14.481 ms | 0.76% |
| Run 4 | 22438 | 14.970 ms | 0.73% |
| Run 5 | 22479 | 13.443 ms | 0.72% |
| **PROMEDIO** | **22445.0** | **14.661 ms** | **0.72%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |91.20% | 84.91% | 87.31% | 79.01% | 95.74% | **87.63%** |
| **exp-vulnerable-mongo-db-1** |88.94% | 70.52% | 76.57% | 84.83% | 77.35% | **79.64%** |
| **exp-vulnerable-ms-catalogo-1** |5.36% | 3.09% | 2.62% | 3.12% | 3.54% | **3.55%** |
| **exp-vulnerable-ms-ordenes-1** |3.47% | 4.12% | 4.85% | 6.20% | 3.82% | **4.49%** |
| **exp-vulnerable-ms-resenas-1** |3.39% | 3.80% | 4.63% | 3.93% | 3.40% | **3.83%** |
| **exp-vulnerable-ms-usuarios-1** |3.47% | 3.41% | 4.32% | 5.12% | 3.22% | **3.91%** |
| **exp-vulnerable-postgres-db-1** |3.93% | 5.41% | 3.68% | 5.66% | 5.03% | **4.74%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |202.1MiB (202.10 MiB)  | 202.2MiB (202.20 MiB)  | 189.5MiB (189.50 MiB)  | 200.9MiB (200.90 MiB)  | 201.4MiB (201.40 MiB)  |
| **exp-vulnerable-mongo-db-1** |329.5MiB (329.50 MiB)  | 349.1MiB (349.10 MiB)  | 347.9MiB (347.90 MiB)  | 348.5MiB (348.50 MiB)  | 347.4MiB (347.40 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |47.93MiB (47.93 MiB)  | 45.43MiB (45.43 MiB)  | 45.7MiB (45.70 MiB)  | 45.14MiB (45.14 MiB)  | 46.32MiB (46.32 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.07MiB (46.07 MiB)  | 45.88MiB (45.88 MiB)  | 46.57MiB (46.57 MiB)  | 48.39MiB (48.39 MiB)  | 46.19MiB (46.19 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.25MiB (46.25 MiB)  | 46.5MiB (46.50 MiB)  | 46.14MiB (46.14 MiB)  | 45.64MiB (45.64 MiB)  | 46.17MiB (46.17 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.31MiB (45.31 MiB)  | 46.73MiB (46.73 MiB)  | 45.72MiB (45.72 MiB)  | 46.11MiB (46.11 MiB)  | 45.6MiB (45.60 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.73MiB (27.73 MiB)  | 29.02MiB (29.02 MiB)  | 27.44MiB (27.44 MiB)  | 27.39MiB (27.39 MiB)  | 28.55MiB (28.55 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |57.62% | 52.93% | 55.45% | 53.80% | 56.02% | **55.16%** |
| **exp-vulnerable-mongo-db-1** |19.72% | 18.81% | 19.67% | 22.32% | 19.51% | **20.01%** |
| **exp-vulnerable-ms-catalogo-1** |1.10% | 0.74% | 0.72% | 0.81% | 0.85% | **0.84%** |
| **exp-vulnerable-ms-ordenes-1** |0.97% | 1.10% | 1.18% | 1.13% | 0.93% | **1.06%** |
| **exp-vulnerable-ms-resenas-1** |0.93% | 1.02% | 1.19% | 0.93% | 0.96% | **1.01%** |
| **exp-vulnerable-ms-usuarios-1** |0.92% | 1.02% | 1.14% | 1.03% | 0.92% | **1.01%** |
| **exp-vulnerable-postgres-db-1** |0.91% | 1.20% | 1.07% | 1.23% | 1.25% | **1.13%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |147.32 MiB | 154.68 MiB | 145.19 MiB | 134.15 MiB | 141.76 MiB | **144.62 MiB** |
| **exp-vulnerable-mongo-db-1** |203.99 MiB | 207.97 MiB | 199.18 MiB | 207.40 MiB | 202.83 MiB | **204.27 MiB** |
| **exp-vulnerable-ms-catalogo-1** |47.79 MiB | 45.30 MiB | 45.57 MiB | 45.02 MiB | 46.19 MiB | **45.97 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.94 MiB | 45.59 MiB | 46.45 MiB | 46.95 MiB | 46.06 MiB | **46.20 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.13 MiB | 46.16 MiB | 46.02 MiB | 45.52 MiB | 46.05 MiB | **45.98 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.19 MiB | 46.62 MiB | 45.60 MiB | 45.92 MiB | 45.47 MiB | **45.76 MiB** |
| **exp-vulnerable-postgres-db-1** |27.39 MiB | 27.43 MiB | 27.39 MiB | 27.35 MiB | 27.34 MiB | **27.38 MiB** |