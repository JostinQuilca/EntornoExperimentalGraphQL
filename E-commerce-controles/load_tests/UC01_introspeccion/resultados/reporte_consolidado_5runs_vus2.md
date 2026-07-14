# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 22:37:54

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 120 | 6.521 ms | 0.00% |
| Run 2 | 120 | 6.220 ms | 0.00% |
| Run 3 | 120 | 6.168 ms | 0.00% |
| Run 4 | 120 | 6.671 ms | 0.00% |
| Run 5 | 120 | 6.969 ms | 0.00% |
| **PROMEDIO** | **120.0** | **6.510 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |8.51% | 3.17% | 2.85% | 2.85% | 3.28% | **4.13%** |
| **exp-protegido-mongo-db-1** |59.49% | 59.84% | 52.11% | 51.04% | 54.19% | **55.33%** |
| **exp-protegido-ms-catalogo-1** |6.02% | 4.57% | 3.52% | 3.47% | 5.05% | **4.53%** |
| **exp-protegido-ms-ordenes-1** |4.94% | 3.40% | 3.74% | 3.91% | 3.53% | **3.90%** |
| **exp-protegido-ms-resenas-1** |4.28% | 3.96% | 4.00% | 5.61% | 3.93% | **4.36%** |
| **exp-protegido-ms-usuarios-1** |4.35% | 3.39% | 4.12% | 4.01% | 3.62% | **3.90%** |
| **exp-protegido-postgres-db-1** |4.46% | 3.75% | 5.08% | 4.65% | 4.70% | **4.53%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.99MiB (65.99 MiB)  | 66.55MiB (66.55 MiB)  | 65.14MiB (65.14 MiB)  | 65.99MiB (65.99 MiB)  | 65.28MiB (65.28 MiB)  |
| **exp-protegido-mongo-db-1** |337.4MiB (337.40 MiB)  | 333.8MiB (333.80 MiB)  | 342.3MiB (342.30 MiB)  | 335.1MiB (335.10 MiB)  | 340.3MiB (340.30 MiB)  |
| **exp-protegido-ms-catalogo-1** |55.05MiB (55.05 MiB)  | 46.3MiB (46.30 MiB)  | 45.96MiB (45.96 MiB)  | 46.35MiB (46.35 MiB)  | 46.22MiB (46.22 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.83MiB (46.83 MiB)  | 46.89MiB (46.89 MiB)  | 45.76MiB (45.76 MiB)  | 45.36MiB (45.36 MiB)  | 45.94MiB (45.94 MiB)  |
| **exp-protegido-ms-resenas-1** |45.38MiB (45.38 MiB)  | 45.63MiB (45.63 MiB)  | 48.88MiB (48.88 MiB)  | 45.44MiB (45.44 MiB)  | 46.42MiB (46.42 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.54MiB (46.54 MiB)  | 45.84MiB (45.84 MiB)  | 45.79MiB (45.79 MiB)  | 45.53MiB (45.53 MiB)  | 46.2MiB (46.20 MiB)  |
| **exp-protegido-postgres-db-1** |28.23MiB (28.23 MiB)  | 28.08MiB (28.08 MiB)  | 28.37MiB (28.37 MiB)  | 28.38MiB (28.38 MiB)  | 28.12MiB (28.12 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.57% | 0.98% | 0.90% | 1.03% | 1.04% | **1.10%** |
| **exp-protegido-mongo-db-1** |14.73% | 15.92% | 16.39% | 14.98% | 15.59% | **15.52%** |
| **exp-protegido-ms-catalogo-1** |1.04% | 1.03% | 0.95% | 0.87% | 1.01% | **0.98%** |
| **exp-protegido-ms-ordenes-1** |1.00% | 0.79% | 0.95% | 0.97% | 0.82% | **0.91%** |
| **exp-protegido-ms-resenas-1** |1.03% | 0.89% | 0.97% | 1.08% | 0.84% | **0.96%** |
| **exp-protegido-ms-usuarios-1** |1.08% | 0.79% | 0.97% | 0.96% | 0.89% | **0.94%** |
| **exp-protegido-postgres-db-1** |1.21% | 1.12% | 1.12% | 1.17% | 1.29% | **1.18%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |64.97 MiB | 65.44 MiB | 64.13 MiB | 65.02 MiB | 64.28 MiB | **64.77 MiB** |
| **exp-protegido-mongo-db-1** |202.95 MiB | 196.34 MiB | 199.74 MiB | 200.09 MiB | 196.65 MiB | **199.15 MiB** |
| **exp-protegido-ms-catalogo-1** |47.06 MiB | 46.21 MiB | 45.81 MiB | 46.24 MiB | 46.11 MiB | **46.29 MiB** |
| **exp-protegido-ms-ordenes-1** |45.42 MiB | 46.78 MiB | 45.65 MiB | 45.25 MiB | 45.85 MiB | **45.79 MiB** |
| **exp-protegido-ms-resenas-1** |45.10 MiB | 45.53 MiB | 48.78 MiB | 45.14 MiB | 46.32 MiB | **46.17 MiB** |
| **exp-protegido-ms-usuarios-1** |46.25 MiB | 45.73 MiB | 45.69 MiB | 45.42 MiB | 46.10 MiB | **45.84 MiB** |
| **exp-protegido-postgres-db-1** |27.87 MiB | 28.04 MiB | 28.00 MiB | 28.00 MiB | 27.97 MiB | **27.98 MiB** |