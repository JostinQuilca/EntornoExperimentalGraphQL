# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=50)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-22 14:25:07

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 3000 | 7.364 ms | 0.00% |
| Run 2 | 3000 | 6.150 ms | 0.00% |
| Run 3 | 2350 | 7.010 ms | 0.00% |
| **PROMEDIO** | **2783.3** | **6.841 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |17.74% | 19.79% | 16.50% | **18.01%** |
| **mongo-db** |61.71% | 59.68% | 93.81% | **71.73%** |
| **ms-catalogo** |4.43% | 5.23% | 4.35% | **4.67%** |
| **ms-ordenes** |5.49% | 5.33% | 5.92% | **5.58%** |
| **ms-resenas** |4.44% | 6.14% | 3.19% | **4.59%** |
| **ms-usuarios** |5.72% | 4.61% | 4.73% | **5.02%** |
| **postgres-db** |5.21% | 7.24% | 5.35% | **5.93%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |103.6MiB (103.60 MiB)  | 104.7MiB (104.70 MiB)  | 105.5MiB (105.50 MiB)  |
| **mongo-db** |476.1MiB (476.10 MiB)  | 477.1MiB (477.10 MiB)  | 460.6MiB (460.60 MiB)  |
| **ms-catalogo** |108MiB (108.00 MiB)  | 108MiB (108.00 MiB)  | 108.1MiB (108.10 MiB)  |
| **ms-ordenes** |65.89MiB (65.89 MiB)  | 66.07MiB (66.07 MiB)  | 66.57MiB (66.57 MiB)  |
| **ms-resenas** |67.01MiB (67.01 MiB)  | 67.17MiB (67.17 MiB)  | 67.16MiB (67.16 MiB)  |
| **ms-usuarios** |65.21MiB (65.21 MiB)  | 65.4MiB (65.40 MiB)  | 66.23MiB (66.23 MiB)  |
| **postgres-db** |45.71MiB (45.71 MiB)  | 45.69MiB (45.69 MiB)  | 45.7MiB (45.70 MiB)  |