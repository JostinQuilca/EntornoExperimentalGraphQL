# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=20)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-22 09:27:12

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 1200 | 5.840 ms | 0.00% |
| Run 2 | 1200 | 5.636 ms | 0.00% |
| Run 3 | 1200 | 5.788 ms | 0.00% |
| **PROMEDIO** | **1200.0** | **5.755 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |20.94% | 13.17% | 13.57% | **15.89%** |
| **minikube** |0.38% | 1.50% | 0.29% | **0.72%** |
| **mongo-db** |69.56% | 80.15% | 82.79% | **77.50%** |
| **ms-catalogo** |6.79% | 5.66% | 5.39% | **5.95%** |
| **ms-ordenes** |7.17% | 5.65% | 5.26% | **6.03%** |
| **ms-resenas** |6.63% | 5.25% | 8.38% | **6.75%** |
| **ms-usuarios** |6.62% | 6.92% | 10.53% | **8.02%** |
| **postgres-db** |7.67% | 6.32% | 10.60% | **8.20%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |99.62MiB (99.62 MiB)  | 101.3MiB (101.30 MiB)  | 102MiB (102.00 MiB)  |
| **minikube** |116.8MiB (116.80 MiB)  | 116.8MiB (116.80 MiB)  | 117MiB (117.00 MiB)  |
| **mongo-db** |459.4MiB (459.40 MiB)  | 458.7MiB (458.70 MiB)  | 457.2MiB (457.20 MiB)  |
| **ms-catalogo** |111.4MiB (111.40 MiB)  | 109.8MiB (109.80 MiB)  | 109.2MiB (109.20 MiB)  |
| **ms-ordenes** |71.1MiB (71.10 MiB)  | 67.73MiB (67.73 MiB)  | 67.86MiB (67.86 MiB)  |
| **ms-resenas** |69.94MiB (69.94 MiB)  | 68.47MiB (68.47 MiB)  | 67.91MiB (67.91 MiB)  |
| **ms-usuarios** |72.02MiB (72.02 MiB)  | 69.68MiB (69.68 MiB)  | 69.87MiB (69.87 MiB)  |
| **postgres-db** |47.74MiB (47.74 MiB)  | 46.15MiB (46.15 MiB)  | 46.13MiB (46.13 MiB)  |