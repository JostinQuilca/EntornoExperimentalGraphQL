# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=1)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 17:38:46

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 60 | 6.851 ms | 0.00% |
| Run 2 | 60 | 6.395 ms | 0.00% |
| Run 3 | 60 | 7.227 ms | 0.00% |
| **PROMEDIO** | **60.0** | **6.824 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.28% | 1.48% | 1.59% | **1.78%** |
| **exp-protegido-mongo-db-1** |68.73% | 71.11% | 73.83% | **71.22%** |
| **exp-protegido-ms-catalogo-1** |4.21% | 3.99% | 5.12% | **4.44%** |
| **exp-protegido-ms-ordenes-1** |4.58% | 3.91% | 3.72% | **4.07%** |
| **exp-protegido-ms-resenas-1** |4.98% | 4.71% | 3.85% | **4.51%** |
| **exp-protegido-ms-usuarios-1** |4.78% | 4.05% | 3.80% | **4.21%** |
| **exp-protegido-postgres-db-1** |6.44% | 4.90% | 6.03% | **5.79%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |70.64MiB (70.64 MiB)  | 64.95MiB (64.95 MiB)  | 64.86MiB (64.86 MiB)  |
| **exp-protegido-mongo-db-1** |332.4MiB (332.40 MiB)  | 332.9MiB (332.90 MiB)  | 333.6MiB (333.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |97.71MiB (97.71 MiB)  | 47.42MiB (47.42 MiB)  | 45.73MiB (45.73 MiB)  |
| **exp-protegido-ms-ordenes-1** |92.17MiB (92.17 MiB)  | 48.17MiB (48.17 MiB)  | 47.35MiB (47.35 MiB)  |
| **exp-protegido-ms-resenas-1** |92.9MiB (92.90 MiB)  | 46.77MiB (46.77 MiB)  | 47.2MiB (47.20 MiB)  |
| **exp-protegido-ms-usuarios-1** |94.16MiB (94.16 MiB)  | 47.11MiB (47.11 MiB)  | 46.46MiB (46.46 MiB)  |
| **exp-protegido-postgres-db-1** |28.54MiB (28.54 MiB)  | 31.11MiB (31.11 MiB)  | 28.02MiB (28.02 MiB)  |