# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=21)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 19:04:14

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 1260 | 6.072 ms | 0.00% |
| Run 2 | 1260 | 7.038 ms | 0.00% |
| Run 3 | 1260 | 6.808 ms | 0.00% |
| **PROMEDIO** | **1260.0** | **6.639 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |16.86% | 15.66% | 17.75% | **16.76%** |
| **exp-vulnerable-mongo-db-1** |51.32% | 79.39% | 50.52% | **60.41%** |
| **exp-vulnerable-ms-catalogo-1** |2.62% | 3.48% | 3.95% | **3.35%** |
| **exp-vulnerable-ms-ordenes-1** |3.18% | 12.01% | 5.19% | **6.79%** |
| **exp-vulnerable-ms-resenas-1** |3.15% | 3.02% | 5.48% | **3.88%** |
| **exp-vulnerable-ms-usuarios-1** |3.39% | 3.23% | 5.13% | **3.92%** |
| **exp-vulnerable-postgres-db-1** |3.88% | 4.23% | 4.40% | **4.17%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.84MiB (96.84 MiB)  | 96.68MiB (96.68 MiB)  | 96.74MiB (96.74 MiB)  |
| **exp-vulnerable-mongo-db-1** |349.2MiB (349.20 MiB)  | 339.1MiB (339.10 MiB)  | 339MiB (339.00 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.74MiB (45.74 MiB)  | 46.79MiB (46.79 MiB)  | 45.81MiB (45.81 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.7MiB (45.70 MiB)  | 53.77MiB (53.77 MiB)  | 45.76MiB (45.76 MiB)  |
| **exp-vulnerable-ms-resenas-1** |45.87MiB (45.87 MiB)  | 46.14MiB (46.14 MiB)  | 46.37MiB (46.37 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |46.66MiB (46.66 MiB)  | 46.09MiB (46.09 MiB)  | 45.71MiB (45.71 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.52MiB (27.52 MiB)  | 27.39MiB (27.39 MiB)  | 28.05MiB (28.05 MiB)  |