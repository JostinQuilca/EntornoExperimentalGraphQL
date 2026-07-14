# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=34)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 19:22:25

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 2040 | 7.086 ms | 0.00% |
| Run 2 | 2040 | 7.430 ms | 0.00% |
| Run 3 | 2040 | 7.677 ms | 0.00% |
| **PROMEDIO** | **2040.0** | **7.398 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |28.79% | 16.71% | 28.25% | **24.58%** |
| **exp-protegido-mongo-db-1** |55.08% | 53.51% | 57.25% | **55.28%** |
| **exp-protegido-ms-catalogo-1** |3.54% | 3.20% | 4.32% | **3.69%** |
| **exp-protegido-ms-ordenes-1** |3.50% | 3.70% | 3.71% | **3.64%** |
| **exp-protegido-ms-resenas-1** |3.35% | 4.24% | 4.41% | **4.00%** |
| **exp-protegido-ms-usuarios-1** |3.12% | 3.65% | 7.44% | **4.74%** |
| **exp-protegido-postgres-db-1** |4.74% | 4.13% | 4.48% | **4.45%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |102.2MiB (102.20 MiB)  | 99.38MiB (99.38 MiB)  | 99.28MiB (99.28 MiB)  |
| **exp-protegido-mongo-db-1** |333.9MiB (333.90 MiB)  | 340.8MiB (340.80 MiB)  | 340.7MiB (340.70 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.21MiB (46.21 MiB)  | 46.21MiB (46.21 MiB)  | 46.38MiB (46.38 MiB)  |
| **exp-protegido-ms-ordenes-1** |48.17MiB (48.17 MiB)  | 46.77MiB (46.77 MiB)  | 49.82MiB (49.82 MiB)  |
| **exp-protegido-ms-resenas-1** |46.73MiB (46.73 MiB)  | 54.39MiB (54.39 MiB)  | 46.47MiB (46.47 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.65MiB (45.65 MiB)  | 46.47MiB (46.47 MiB)  | 47.34MiB (47.34 MiB)  |
| **exp-protegido-postgres-db-1** |28.08MiB (28.08 MiB)  | 28.02MiB (28.02 MiB)  | 28.03MiB (28.03 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |11.32% | 10.01% | 9.39% | **10.24%** |
| **exp-protegido-mongo-db-1** |14.54% | 14.89% | 13.42% | **14.28%** |
| **exp-protegido-ms-catalogo-1** |0.78% | 0.94% | 0.96% | **0.89%** |
| **exp-protegido-ms-ordenes-1** |0.94% | 0.90% | 0.94% | **0.93%** |
| **exp-protegido-ms-resenas-1** |0.93% | 0.93% | 0.94% | **0.93%** |
| **exp-protegido-ms-usuarios-1** |0.99% | 0.81% | 1.09% | **0.96%** |
| **exp-protegido-postgres-db-1** |1.15% | 1.09% | 1.04% | **1.09%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |92.07 MiB | 89.46 MiB | 88.73 MiB | **90.09 MiB** |
| **exp-protegido-mongo-db-1** |200.60 MiB | 203.28 MiB | 199.04 MiB | **200.97 MiB** |
| **exp-protegido-ms-catalogo-1** |46.07 MiB | 46.10 MiB | 46.28 MiB | **46.15 MiB** |
| **exp-protegido-ms-ordenes-1** |46.61 MiB | 46.67 MiB | 48.09 MiB | **47.12 MiB** |
| **exp-protegido-ms-resenas-1** |46.28 MiB | 47.39 MiB | 46.34 MiB | **46.67 MiB** |
| **exp-protegido-ms-usuarios-1** |45.35 MiB | 46.37 MiB | 45.66 MiB | **45.79 MiB** |
| **exp-protegido-postgres-db-1** |27.82 MiB | 27.98 MiB | 28.03 MiB | **27.94 MiB** |