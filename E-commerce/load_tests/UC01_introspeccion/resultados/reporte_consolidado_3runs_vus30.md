# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=30)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-22 14:16:37

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 1800 | 8.077 ms | 0.00% |
| Run 2 | 1800 | 6.193 ms | 0.00% |
| Run 3 | 1800 | 6.432 ms | 0.00% |
| **PROMEDIO** | **1800.0** | **6.900 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |34.78% | 16.59% | 24.15% | **25.17%** |
| **mongo-db** |61.13% | 59.12% | 52.94% | **57.73%** |
| **ms-catalogo** |4.35% | 3.66% | 6.12% | **4.71%** |
| **ms-ordenes** |6.23% | 5.52% | 5.05% | **5.60%** |
| **ms-resenas** |4.18% | 8.56% | 4.33% | **5.69%** |
| **ms-usuarios** |5.61% | 5.24% | 5.17% | **5.34%** |
| **postgres-db** |5.81% | 5.17% | 7.07% | **6.02%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |98.72MiB (98.72 MiB)  | 99.79MiB (99.79 MiB)  | 101.8MiB (101.80 MiB)  |
| **mongo-db** |454.2MiB (454.20 MiB)  | 468.1MiB (468.10 MiB)  | 459.5MiB (459.50 MiB)  |
| **ms-catalogo** |109.5MiB (109.50 MiB)  | 109.8MiB (109.80 MiB)  | 107.8MiB (107.80 MiB)  |
| **ms-ordenes** |66.11MiB (66.11 MiB)  | 65.73MiB (65.73 MiB)  | 67.2MiB (67.20 MiB)  |
| **ms-resenas** |67.15MiB (67.15 MiB)  | 66.33MiB (66.33 MiB)  | 66.44MiB (66.44 MiB)  |
| **ms-usuarios** |65.75MiB (65.75 MiB)  | 65.13MiB (65.13 MiB)  | 66.23MiB (66.23 MiB)  |
| **postgres-db** |46.71MiB (46.71 MiB)  | 47.45MiB (47.45 MiB)  | 45.64MiB (45.64 MiB)  |