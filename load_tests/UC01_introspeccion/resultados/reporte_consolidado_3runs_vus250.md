# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=250)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-22 23:44:01

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 14434 | 28.650 ms | 100.00% |
| Run 2 | 13368 | 128.936 ms | 100.00% |
| Run 3 | 11561 | 312.099 ms | 100.00% |
| **PROMEDIO** | **13121.0** | **156.562 ms** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |97.38% | 121.60% | 124.20% | **114.39%** |
| **mongo-db** |123.06% | 121.98% | 127.20% | **124.08%** |
| **ms-catalogo** |8.57% | 9.14% | 9.99% | **9.23%** |
| **ms-ordenes** |8.00% | 9.03% | 8.94% | **8.66%** |
| **ms-resenas** |7.06% | 14.08% | 9.13% | **10.09%** |
| **ms-usuarios** |6.94% | 11.70% | 11.41% | **10.02%** |
| **postgres-db** |8.74% | 12.41% | 16.30% | **12.48%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |198MiB (198.00 MiB)  | 207.1MiB (207.10 MiB)  | 209.6MiB (209.60 MiB)  |
| **mongo-db** |332.5MiB (332.50 MiB)  | 340.3MiB (340.30 MiB)  | 335.1MiB (335.10 MiB)  |
| **ms-catalogo** |50.75MiB (50.75 MiB)  | 51.18MiB (51.18 MiB)  | 51.03MiB (51.03 MiB)  |
| **ms-ordenes** |48.59MiB (48.59 MiB)  | 49.82MiB (49.82 MiB)  | 48.88MiB (48.88 MiB)  |
| **ms-resenas** |48.14MiB (48.14 MiB)  | 48.44MiB (48.44 MiB)  | 47.78MiB (47.78 MiB)  |
| **ms-usuarios** |48.08MiB (48.08 MiB)  | 48.7MiB (48.70 MiB)  | 48.36MiB (48.36 MiB)  |
| **postgres-db** |45.7MiB (45.70 MiB)  | 46.29MiB (46.29 MiB)  | 46.02MiB (46.02 MiB)  |