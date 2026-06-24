# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=100)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-22 14:28:46

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 6000 | 7.248 ms | 0.00% |
| Run 2 | 6000 | 7.440 ms | 0.00% |
| Run 3 | 6000 | 6.714 ms | 0.00% |
| **PROMEDIO** | **6000.0** | **7.134 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |29.29% | 25.84% | 34.92% | **30.02%** |
| **mongo-db** |54.12% | 97.18% | 67.10% | **72.80%** |
| **ms-catalogo** |4.33% | 4.51% | 4.50% | **4.45%** |
| **ms-ordenes** |4.63% | 4.42% | 4.26% | **4.44%** |
| **ms-resenas** |5.02% | 3.47% | 3.84% | **4.11%** |
| **ms-usuarios** |4.41% | 4.88% | 4.45% | **4.58%** |
| **postgres-db** |6.04% | 5.61% | 5.91% | **5.85%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |104.7MiB (104.70 MiB)  | 105.8MiB (105.80 MiB)  | 107.9MiB (107.90 MiB)  |
| **mongo-db** |461.2MiB (461.20 MiB)  | 475.1MiB (475.10 MiB)  | 469MiB (469.00 MiB)  |
| **ms-catalogo** |108.4MiB (108.40 MiB)  | 107.8MiB (107.80 MiB)  | 107.9MiB (107.90 MiB)  |
| **ms-ordenes** |66.2MiB (66.20 MiB)  | 65.86MiB (65.86 MiB)  | 66.05MiB (66.05 MiB)  |
| **ms-resenas** |67.98MiB (67.98 MiB)  | 66.87MiB (66.87 MiB)  | 67.18MiB (67.18 MiB)  |
| **ms-usuarios** |65.96MiB (65.96 MiB)  | 65.11MiB (65.11 MiB)  | 65.38MiB (65.38 MiB)  |
| **postgres-db** |45.53MiB (45.53 MiB)  | 45.86MiB (45.86 MiB)  | 45.57MiB (45.57 MiB)  |