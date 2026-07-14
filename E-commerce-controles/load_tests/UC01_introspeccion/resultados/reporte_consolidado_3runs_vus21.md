# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=21)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 19:10:29

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 1260 | 6.986 ms | 0.00% |
| Run 2 | 1260 | 7.085 ms | 0.00% |
| Run 3 | 1260 | 10.125 ms | 0.00% |
| **PROMEDIO** | **1260.0** | **8.066 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |29.70% | 13.92% | 22.40% | **22.01%** |
| **exp-protegido-mongo-db-1** |61.17% | 63.82% | 102.32% | **75.77%** |
| **exp-protegido-ms-catalogo-1** |2.84% | 3.06% | 5.05% | **3.65%** |
| **exp-protegido-ms-ordenes-1** |3.89% | 3.70% | 5.94% | **4.51%** |
| **exp-protegido-ms-resenas-1** |4.35% | 4.22% | 6.77% | **5.11%** |
| **exp-protegido-ms-usuarios-1** |3.59% | 3.56% | 7.38% | **4.84%** |
| **exp-protegido-postgres-db-1** |7.70% | 5.92% | 6.60% | **6.74%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |100.6MiB (100.60 MiB)  | 86.14MiB (86.14 MiB)  | 86.83MiB (86.83 MiB)  |
| **exp-protegido-mongo-db-1** |332.6MiB (332.60 MiB)  | 333MiB (333.00 MiB)  | 348.6MiB (348.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |47.16MiB (47.16 MiB)  | 47.17MiB (47.17 MiB)  | 45.81MiB (45.81 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.81MiB (45.81 MiB)  | 45.62MiB (45.62 MiB)  | 45.91MiB (45.91 MiB)  |
| **exp-protegido-ms-resenas-1** |47.45MiB (47.45 MiB)  | 46.1MiB (46.10 MiB)  | 45.7MiB (45.70 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.64MiB (46.64 MiB)  | 45.68MiB (45.68 MiB)  | 48.39MiB (48.39 MiB)  |
| **exp-protegido-postgres-db-1** |27.96MiB (27.96 MiB)  | 28.43MiB (28.43 MiB)  | 30.12MiB (30.12 MiB)  |