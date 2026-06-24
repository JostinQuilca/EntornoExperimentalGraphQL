# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=50)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-23 00:01:30

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 3000 | 7.789 ms | 100.00% |
| Run 2 | 3000 | 7.194 ms | 100.00% |
| Run 3 | 3000 | 8.638 ms | 100.00% |
| **PROMEDIO** | **3000.0** | **7.874 ms** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |27.01% | 19.36% | 20.98% | **22.45%** |
| **mongo-db** |80.36% | 58.89% | 55.32% | **64.86%** |
| **ms-catalogo** |4.05% | 7.92% | 6.48% | **6.15%** |
| **ms-ordenes** |5.94% | 5.40% | 6.23% | **5.86%** |
| **ms-resenas** |6.02% | 6.38% | 5.32% | **5.91%** |
| **ms-usuarios** |6.00% | 6.16% | 6.26% | **6.14%** |
| **postgres-db** |6.44% | 7.09% | 7.15% | **6.89%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |107.9MiB (107.90 MiB)  | 108.2MiB (108.20 MiB)  | 108.6MiB (108.60 MiB)  |
| **mongo-db** |328.1MiB (328.10 MiB)  | 333.7MiB (333.70 MiB)  | 325.8MiB (325.80 MiB)  |
| **ms-catalogo** |51.37MiB (51.37 MiB)  | 51.48MiB (51.48 MiB)  | 51.08MiB (51.08 MiB)  |
| **ms-ordenes** |49.54MiB (49.54 MiB)  | 50.3MiB (50.30 MiB)  | 48.67MiB (48.67 MiB)  |
| **ms-resenas** |49.99MiB (49.99 MiB)  | 50.27MiB (50.27 MiB)  | 48.6MiB (48.60 MiB)  |
| **ms-usuarios** |49.48MiB (49.48 MiB)  | 49.79MiB (49.79 MiB)  | 49.03MiB (49.03 MiB)  |
| **postgres-db** |47.41MiB (47.41 MiB)  | 46.91MiB (46.91 MiB)  | 46.13MiB (46.13 MiB)  |