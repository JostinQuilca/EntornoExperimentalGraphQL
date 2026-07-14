# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 15:54:35

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 480 | 8.684 ms | 0.00% |
| Run 2 | 480 | 7.047 ms | 0.00% |
| Run 3 | 480 | 7.330 ms | 0.00% |
| Run 4 | 480 | 7.477 ms | 0.00% |
| Run 5 | 480 | 6.812 ms | 0.00% |
| **PROMEDIO** | **480.0** | **7.470 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |18.20% | 7.02% | 6.74% | 9.49% | 8.77% | **10.04%** |
| **exp-protegido-mongo-db-1** |55.81% | 68.31% | 66.33% | 72.17% | 67.71% | **66.07%** |
| **exp-protegido-ms-catalogo-1** |6.79% | 3.45% | 3.46% | 4.11% | 3.98% | **4.36%** |
| **exp-protegido-ms-ordenes-1** |4.00% | 3.45% | 4.79% | 4.61% | 4.03% | **4.18%** |
| **exp-protegido-ms-resenas-1** |7.34% | 3.69% | 4.04% | 3.79% | 4.39% | **4.65%** |
| **exp-protegido-ms-usuarios-1** |3.77% | 3.72% | 4.97% | 4.07% | 4.61% | **4.23%** |
| **exp-protegido-postgres-db-1** |5.60% | 5.72% | 5.13% | 5.98% | 7.40% | **5.97%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |102MiB (102.00 MiB)  | 75.79MiB (75.79 MiB)  | 74.54MiB (74.54 MiB)  | 75.13MiB (75.13 MiB)  | 75.56MiB (75.56 MiB)  |
| **exp-protegido-mongo-db-1** |351MiB (351.00 MiB)  | 340.9MiB (340.90 MiB)  | 340MiB (340.00 MiB)  | 350.3MiB (350.30 MiB)  | 309.6MiB (309.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |89.75MiB (89.75 MiB)  | 46.02MiB (46.02 MiB)  | 46.8MiB (46.80 MiB)  | 47.06MiB (47.06 MiB)  | 47.78MiB (47.78 MiB)  |
| **exp-protegido-ms-ordenes-1** |93.36MiB (93.36 MiB)  | 45.62MiB (45.62 MiB)  | 46.99MiB (46.99 MiB)  | 45.56MiB (45.56 MiB)  | 47.09MiB (47.09 MiB)  |
| **exp-protegido-ms-resenas-1** |99.56MiB (99.56 MiB)  | 47.28MiB (47.28 MiB)  | 46.46MiB (46.46 MiB)  | 45.91MiB (45.91 MiB)  | 45.3MiB (45.30 MiB)  |
| **exp-protegido-ms-usuarios-1** |92.64MiB (92.64 MiB)  | 45.65MiB (45.65 MiB)  | 46.65MiB (46.65 MiB)  | 45.82MiB (45.82 MiB)  | 45.9MiB (45.90 MiB)  |
| **exp-protegido-postgres-db-1** |29.78MiB (29.78 MiB)  | 29.43MiB (29.43 MiB)  | 28.32MiB (28.32 MiB)  | 28.01MiB (28.01 MiB)  | 28.03MiB (28.03 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |4.52% | 3.47% | 3.30% | 3.79% | 3.40% | **3.70%** |
| **exp-protegido-mongo-db-1** |16.98% | 18.57% | 19.12% | 20.08% | 18.22% | **18.59%** |
| **exp-protegido-ms-catalogo-1** |1.28% | 0.82% | 0.88% | 0.92% | 1.06% | **0.99%** |
| **exp-protegido-ms-ordenes-1** |0.94% | 0.87% | 0.98% | 0.85% | 0.80% | **0.89%** |
| **exp-protegido-ms-resenas-1** |1.22% | 0.83% | 0.94% | 0.96% | 0.79% | **0.95%** |
| **exp-protegido-ms-usuarios-1** |0.90% | 0.98% | 1.00% | 0.95% | 0.82% | **0.93%** |
| **exp-protegido-postgres-db-1** |1.65% | 1.68% | 1.35% | 1.58% | 1.79% | **1.61%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |80.83 MiB | 72.51 MiB | 71.75 MiB | 71.88 MiB | 72.15 MiB | **73.82 MiB** |
| **exp-protegido-mongo-db-1** |199.49 MiB | 192.79 MiB | 196.01 MiB | 204.76 MiB | 193.63 MiB | **197.34 MiB** |
| **exp-protegido-ms-catalogo-1** |89.61 MiB | 45.92 MiB | 46.65 MiB | 46.77 MiB | 46.40 MiB | **55.07 MiB** |
| **exp-protegido-ms-ordenes-1** |93.25 MiB | 45.21 MiB | 46.90 MiB | 45.46 MiB | 46.99 MiB | **55.56 MiB** |
| **exp-protegido-ms-resenas-1** |94.07 MiB | 46.92 MiB | 46.37 MiB | 45.81 MiB | 45.20 MiB | **55.67 MiB** |
| **exp-protegido-ms-usuarios-1** |92.51 MiB | 45.34 MiB | 46.56 MiB | 45.72 MiB | 45.58 MiB | **55.14 MiB** |
| **exp-protegido-postgres-db-1** |28.32 MiB | 27.99 MiB | 27.94 MiB | 28.01 MiB | 27.95 MiB | **28.04 MiB** |