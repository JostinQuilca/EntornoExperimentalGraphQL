# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=89)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 20:20:37

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 5318 | 11.762 ms | 0.00% |
| Run 2 | 5340 | 9.359 ms | 0.00% |
| Run 3 | 5340 | 8.419 ms | 0.00% |
| Run 4 | 5340 | 8.466 ms | 0.00% |
| Run 5 | 5340 | 8.141 ms | 0.00% |
| **PROMEDIO** | **5335.6** | **9.229 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |62.90% | 42.40% | 32.58% | 35.58% | 27.05% | **40.10%** |
| **exp-vulnerable-mongo-db-1** |100.22% | 73.30% | 51.95% | 57.86% | 54.59% | **67.58%** |
| **exp-vulnerable-ms-catalogo-1** |10.26% | 2.66% | 3.66% | 3.24% | 3.74% | **4.71%** |
| **exp-vulnerable-ms-ordenes-1** |15.16% | 2.97% | 3.45% | 3.64% | 5.49% | **6.14%** |
| **exp-vulnerable-ms-resenas-1** |4.07% | 12.96% | 3.42% | 3.97% | 5.84% | **6.05%** |
| **exp-vulnerable-ms-usuarios-1** |7.50% | 4.52% | 3.46% | 4.35% | 5.20% | **5.01%** |
| **exp-vulnerable-postgres-db-1** |16.53% | 3.94% | 5.05% | 4.80% | 5.00% | **7.06%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |104.8MiB (104.80 MiB)  | 101.1MiB (101.10 MiB)  | 103.4MiB (103.40 MiB)  | 101.6MiB (101.60 MiB)  | 101MiB (101.00 MiB)  |
| **exp-vulnerable-mongo-db-1** |340.9MiB (340.90 MiB)  | 340.2MiB (340.20 MiB)  | 342.4MiB (342.40 MiB)  | 344.8MiB (344.80 MiB)  | 340.6MiB (340.60 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.8MiB (45.80 MiB)  | 45.94MiB (45.94 MiB)  | 46.35MiB (46.35 MiB)  | 45.11MiB (45.11 MiB)  | 46.34MiB (46.34 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.32MiB (46.32 MiB)  | 47.5MiB (47.50 MiB)  | 45.85MiB (45.85 MiB)  | 46.14MiB (46.14 MiB)  | 47.73MiB (47.73 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.49MiB (46.49 MiB)  | 54.39MiB (54.39 MiB)  | 45.7MiB (45.70 MiB)  | 46.23MiB (46.23 MiB)  | 48.45MiB (48.45 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |47.36MiB (47.36 MiB)  | 47.09MiB (47.09 MiB)  | 46MiB (46.00 MiB)  | 46.29MiB (46.29 MiB)  | 48.1MiB (48.10 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.45MiB (27.45 MiB)  | 27.41MiB (27.41 MiB)  | 27.38MiB (27.38 MiB)  | 27.4MiB (27.40 MiB)  | 27.35MiB (27.35 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |25.91% | 21.88% | 18.16% | 19.61% | 18.23% | **20.76%** |
| **exp-vulnerable-mongo-db-1** |18.61% | 16.40% | 14.94% | 16.70% | 14.97% | **16.32%** |
| **exp-vulnerable-ms-catalogo-1** |1.40% | 0.75% | 0.90% | 0.90% | 0.77% | **0.94%** |
| **exp-vulnerable-ms-ordenes-1** |1.36% | 0.90% | 0.95% | 1.09% | 0.93% | **1.05%** |
| **exp-vulnerable-ms-resenas-1** |1.03% | 1.45% | 0.94% | 0.91% | 0.97% | **1.06%** |
| **exp-vulnerable-ms-usuarios-1** |1.14% | 0.86% | 0.89% | 1.15% | 0.87% | **0.98%** |
| **exp-vulnerable-postgres-db-1** |1.73% | 0.99% | 1.19% | 1.18% | 1.28% | **1.27%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |99.47 MiB | 97.43 MiB | 99.09 MiB | 97.62 MiB | 97.34 MiB | **98.19 MiB** |
| **exp-vulnerable-mongo-db-1** |195.14 MiB | 206.40 MiB | 196.68 MiB | 204.47 MiB | 202.69 MiB | **201.08 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.67 MiB | 45.82 MiB | 46.23 MiB | 44.99 MiB | 46.22 MiB | **45.79 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.20 MiB | 46.16 MiB | 45.32 MiB | 46.02 MiB | 45.95 MiB | **45.93 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.35 MiB | 46.90 MiB | 45.57 MiB | 46.11 MiB | 47.00 MiB | **46.39 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.22 MiB | 46.97 MiB | 45.87 MiB | 46.17 MiB | 46.39 MiB | **46.52 MiB** |
| **exp-vulnerable-postgres-db-1** |27.32 MiB | 27.37 MiB | 27.33 MiB | 27.35 MiB | 27.31 MiB | **27.34 MiB** |