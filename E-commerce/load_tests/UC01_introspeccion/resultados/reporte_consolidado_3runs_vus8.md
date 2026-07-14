# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=8)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 18:32:19

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 480 | 6.135 ms | 0.00% |
| Run 2 | 480 | 5.957 ms | 0.00% |
| Run 3 | 480 | 5.463 ms | 0.00% |
| **PROMEDIO** | **480.0** | **5.852 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |5.46% | 7.96% | 6.79% | **6.74%** |
| **exp-vulnerable-mongo-db-1** |53.92% | 48.64% | 61.22% | **54.59%** |
| **exp-vulnerable-ms-catalogo-1** |4.11% | 3.55% | 3.75% | **3.80%** |
| **exp-vulnerable-ms-ordenes-1** |4.54% | 3.38% | 3.06% | **3.66%** |
| **exp-vulnerable-ms-resenas-1** |3.59% | 4.00% | 3.32% | **3.64%** |
| **exp-vulnerable-ms-usuarios-1** |5.13% | 2.96% | 2.98% | **3.69%** |
| **exp-vulnerable-postgres-db-1** |4.43% | 4.29% | 3.93% | **4.22%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |80.83MiB (80.83 MiB)  | 80.91MiB (80.91 MiB)  | 81.82MiB (81.82 MiB)  |
| **exp-vulnerable-mongo-db-1** |331.7MiB (331.70 MiB)  | 337.3MiB (337.30 MiB)  | 348.9MiB (348.90 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.09MiB (46.09 MiB)  | 45.58MiB (45.58 MiB)  | 45.64MiB (45.64 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.63MiB (45.63 MiB)  | 48.04MiB (48.04 MiB)  | 46.45MiB (46.45 MiB)  |
| **exp-vulnerable-ms-resenas-1** |45.76MiB (45.76 MiB)  | 45.87MiB (45.87 MiB)  | 46.9MiB (46.90 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |46.18MiB (46.18 MiB)  | 45.99MiB (45.99 MiB)  | 46.21MiB (46.21 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.38MiB (27.38 MiB)  | 29.04MiB (29.04 MiB)  | 27.45MiB (27.45 MiB)  |