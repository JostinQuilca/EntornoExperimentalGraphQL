# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=3)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 18:08:55

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 180 | 5.946 ms | 0.00% |
| Run 2 | 180 | 5.815 ms | 0.00% |
| Run 3 | 180 | 5.699 ms | 0.00% |
| **PROMEDIO** | **180.0** | **5.820 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |5.15% | 3.32% | 13.17% | **7.21%** |
| **exp-vulnerable-mongo-db-1** |60.36% | 65.38% | 53.16% | **59.63%** |
| **exp-vulnerable-ms-catalogo-1** |3.22% | 3.35% | 2.92% | **3.16%** |
| **exp-vulnerable-ms-ordenes-1** |4.31% | 4.74% | 3.37% | **4.14%** |
| **exp-vulnerable-ms-resenas-1** |4.62% | 4.06% | 3.20% | **3.96%** |
| **exp-vulnerable-ms-usuarios-1** |4.15% | 4.58% | 3.57% | **4.10%** |
| **exp-vulnerable-postgres-db-1** |4.54% | 5.65% | 4.61% | **4.93%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |66.4MiB (66.40 MiB)  | 66.95MiB (66.95 MiB)  | 66.82MiB (66.82 MiB)  |
| **exp-vulnerable-mongo-db-1** |332.8MiB (332.80 MiB)  | 340.8MiB (340.80 MiB)  | 338.2MiB (338.20 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.42MiB (45.42 MiB)  | 46.84MiB (46.84 MiB)  | 48.94MiB (48.94 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.26MiB (46.26 MiB)  | 46.29MiB (46.29 MiB)  | 46.79MiB (46.79 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47.65MiB (47.65 MiB)  | 47.21MiB (47.21 MiB)  | 46.29MiB (46.29 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |48.31MiB (48.31 MiB)  | 45.53MiB (45.53 MiB)  | 47.6MiB (47.60 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.44MiB (27.44 MiB)  | 28.63MiB (28.63 MiB)  | 27.35MiB (27.35 MiB)  |