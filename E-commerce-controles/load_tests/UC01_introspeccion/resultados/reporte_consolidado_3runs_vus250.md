# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=250)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-22 23:45:44

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 11500 | 309.926 ms | 100.00% |
| Run 2 | 12988 | 162.021 ms | 100.00% |
| Run 3 | 14717 | 26.740 ms | 100.00% |
| **PROMEDIO** | **13068.3** | **166.229 ms** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |123.56% | 124.20% | 108.45% | **118.74%** |
| **mongo-db** |121.98% | 128.09% | 133.33% | **127.80%** |
| **ms-catalogo** |10.52% | 24.54% | 7.07% | **14.04%** |
| **ms-ordenes** |9.57% | 9.95% | 11.57% | **10.36%** |
| **ms-resenas** |14.08% | 10.77% | 13.59% | **12.81%** |
| **ms-usuarios** |11.70% | 8.17% | 12.30% | **10.72%** |
| **postgres-db** |12.41% | 17.93% | 12.94% | **14.43%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |207.1MiB (207.10 MiB)  | 206.2MiB (206.20 MiB)  | 196.1MiB (196.10 MiB)  |
| **mongo-db** |340.3MiB (340.30 MiB)  | 331.6MiB (331.60 MiB)  | 341.4MiB (341.40 MiB)  |
| **ms-catalogo** |51.03MiB (51.03 MiB)  | 50.55MiB (50.55 MiB)  | 50.84MiB (50.84 MiB)  |
| **ms-ordenes** |49.82MiB (49.82 MiB)  | 48.2MiB (48.20 MiB)  | 48.46MiB (48.46 MiB)  |
| **ms-resenas** |48.27MiB (48.27 MiB)  | 48.88MiB (48.88 MiB)  | 48.09MiB (48.09 MiB)  |
| **ms-usuarios** |48.7MiB (48.70 MiB)  | 48.99MiB (48.99 MiB)  | 47.92MiB (47.92 MiB)  |
| **postgres-db** |46.29MiB (46.29 MiB)  | 46.02MiB (46.02 MiB)  | 46.04MiB (46.04 MiB)  |