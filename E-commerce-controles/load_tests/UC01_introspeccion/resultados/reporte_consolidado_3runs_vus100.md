# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=100)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-23 00:04:52

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 4841 | 17.967 ms | 100.00% |
| Run 2 | 6000 | 9.946 ms | 100.00% |
| Run 3 | 6000 | 9.975 ms | 100.00% |
| **PROMEDIO** | **5613.7** | **12.629 ms** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |77.03% | 41.09% | 40.28% | **52.80%** |
| **mongo-db** |71.91% | 58.72% | 78.16% | **69.60%** |
| **ms-catalogo** |4.94% | 7.83% | 8.61% | **7.13%** |
| **ms-ordenes** |5.89% | 6.03% | 7.94% | **6.62%** |
| **ms-resenas** |5.62% | 5.97% | 8.96% | **6.85%** |
| **ms-usuarios** |5.86% | 6.31% | 8.20% | **6.79%** |
| **postgres-db** |5.78% | 7.74% | 9.76% | **7.76%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |108.3MiB (108.30 MiB)  | 109.1MiB (109.10 MiB)  | 109.4MiB (109.40 MiB)  |
| **mongo-db** |331.4MiB (331.40 MiB)  | 343.6MiB (343.60 MiB)  | 333.3MiB (333.30 MiB)  |
| **ms-catalogo** |51.14MiB (51.14 MiB)  | 51.24MiB (51.24 MiB)  | 52.95MiB (52.95 MiB)  |
| **ms-ordenes** |49.04MiB (49.04 MiB)  | 48.69MiB (48.69 MiB)  | 50.23MiB (50.23 MiB)  |
| **ms-resenas** |51.22MiB (51.22 MiB)  | 48.63MiB (48.63 MiB)  | 49.95MiB (49.95 MiB)  |
| **ms-usuarios** |48.59MiB (48.59 MiB)  | 48.31MiB (48.31 MiB)  | 49.2MiB (49.20 MiB)  |
| **postgres-db** |47.56MiB (47.56 MiB)  | 46.17MiB (46.17 MiB)  | 48.05MiB (48.05 MiB)  |