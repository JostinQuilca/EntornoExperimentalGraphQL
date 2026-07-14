# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=3)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 18:15:06

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 180 | 7.230 ms | 0.00% |
| Run 2 | 180 | 6.824 ms | 0.00% |
| Run 3 | 180 | 7.007 ms | 0.00% |
| **PROMEDIO** | **180.0** | **7.020 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |8.19% | 4.07% | 3.49% | **5.25%** |
| **exp-protegido-mongo-db-1** |69.34% | 63.98% | 57.02% | **63.45%** |
| **exp-protegido-ms-catalogo-1** |4.34% | 3.06% | 3.16% | **3.52%** |
| **exp-protegido-ms-ordenes-1** |3.19% | 3.24% | 4.46% | **3.63%** |
| **exp-protegido-ms-resenas-1** |3.49% | 3.09% | 4.07% | **3.55%** |
| **exp-protegido-ms-usuarios-1** |3.48% | 3.06% | 3.83% | **3.46%** |
| **exp-protegido-postgres-db-1** |5.29% | 5.53% | 4.69% | **5.17%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |69.54MiB (69.54 MiB)  | 69.99MiB (69.99 MiB)  | 68.94MiB (68.94 MiB)  |
| **exp-protegido-mongo-db-1** |340.1MiB (340.10 MiB)  | 342.4MiB (342.40 MiB)  | 340.3MiB (340.30 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.21MiB (46.21 MiB)  | 46.96MiB (46.96 MiB)  | 46.77MiB (46.77 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.02MiB (46.02 MiB)  | 45.79MiB (45.79 MiB)  | 45.78MiB (45.78 MiB)  |
| **exp-protegido-ms-resenas-1** |45.91MiB (45.91 MiB)  | 45.47MiB (45.47 MiB)  | 45.8MiB (45.80 MiB)  |
| **exp-protegido-ms-usuarios-1** |54.49MiB (54.49 MiB)  | 45.79MiB (45.79 MiB)  | 46.09MiB (46.09 MiB)  |
| **exp-protegido-postgres-db-1** |28.05MiB (28.05 MiB)  | 30.21MiB (30.21 MiB)  | 29.32MiB (29.32 MiB)  |