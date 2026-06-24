# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=20)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-22 23:57:40

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 944 | 112.874 ms | 100.00% |
| Run 2 | 1200 | 6.849 ms | 100.00% |
| Run 3 | 1200 | 6.399 ms | 100.00% |
| **PROMEDIO** | **1114.7** | **42.041 ms** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |11.42% | 12.44% | 17.69% | **13.85%** |
| **mongo-db** |145.16% | 53.33% | 60.86% | **86.45%** |
| **ms-catalogo** |5.50% | 3.94% | 4.34% | **4.59%** |
| **ms-ordenes** |4.50% | 3.59% | 4.44% | **4.18%** |
| **ms-resenas** |11.95% | 5.82% | 6.28% | **8.02%** |
| **ms-usuarios** |24.13% | 5.40% | 6.88% | **12.14%** |
| **postgres-db** |15.02% | 6.87% | 6.78% | **9.56%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |102MiB (102.00 MiB)  | 106.1MiB (106.10 MiB)  | 106.8MiB (106.80 MiB)  |
| **mongo-db** |337.6MiB (337.60 MiB)  | 337.7MiB (337.70 MiB)  | 342.7MiB (342.70 MiB)  |
| **ms-catalogo** |51.52MiB (51.52 MiB)  | 51.16MiB (51.16 MiB)  | 50.84MiB (50.84 MiB)  |
| **ms-ordenes** |48.94MiB (48.94 MiB)  | 49.02MiB (49.02 MiB)  | 48.63MiB (48.63 MiB)  |
| **ms-resenas** |47.91MiB (47.91 MiB)  | 48.27MiB (48.27 MiB)  | 48.38MiB (48.38 MiB)  |
| **ms-usuarios** |48.47MiB (48.47 MiB)  | 47.9MiB (47.90 MiB)  | 48.11MiB (48.11 MiB)  |
| **postgres-db** |46.04MiB (46.04 MiB)  | 46.14MiB (46.14 MiB)  | 46.08MiB (46.08 MiB)  |