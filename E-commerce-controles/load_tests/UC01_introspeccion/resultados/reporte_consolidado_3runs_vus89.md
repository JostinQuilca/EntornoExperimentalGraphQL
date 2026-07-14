# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=89)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 19:47:26

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 5340 | 8.778 ms | 0.00% |
| Run 2 | 5340 | 9.555 ms | 0.00% |
| Run 3 | 5340 | 9.242 ms | 0.00% |
| **PROMEDIO** | **5340.0** | **9.192 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |41.96% | 49.35% | 36.82% | **42.71%** |
| **exp-protegido-mongo-db-1** |58.18% | 92.80% | 59.66% | **70.21%** |
| **exp-protegido-ms-catalogo-1** |4.14% | 4.85% | 2.71% | **3.90%** |
| **exp-protegido-ms-ordenes-1** |3.20% | 3.34% | 2.95% | **3.16%** |
| **exp-protegido-ms-resenas-1** |3.35% | 3.31% | 3.73% | **3.46%** |
| **exp-protegido-ms-usuarios-1** |2.94% | 3.29% | 3.67% | **3.30%** |
| **exp-protegido-postgres-db-1** |4.35% | 4.82% | 3.97% | **4.38%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |104.4MiB (104.40 MiB)  | 102.2MiB (102.20 MiB)  | 105MiB (105.00 MiB)  |
| **exp-protegido-mongo-db-1** |320.2MiB (320.20 MiB)  | 347.9MiB (347.90 MiB)  | 330MiB (330.00 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.07MiB (46.07 MiB)  | 45.92MiB (45.92 MiB)  | 46.18MiB (46.18 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.05MiB (46.05 MiB)  | 46.47MiB (46.47 MiB)  | 45.74MiB (45.74 MiB)  |
| **exp-protegido-ms-resenas-1** |45.75MiB (45.75 MiB)  | 46.46MiB (46.46 MiB)  | 45.7MiB (45.70 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.42MiB (46.42 MiB)  | 45.75MiB (45.75 MiB)  | 46.03MiB (46.03 MiB)  |
| **exp-protegido-postgres-db-1** |27.93MiB (27.93 MiB)  | 28.21MiB (28.21 MiB)  | 28.88MiB (28.88 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |23.19% | 24.69% | 21.42% | **23.10%** |
| **exp-protegido-mongo-db-1** |15.29% | 20.48% | 17.05% | **17.61%** |
| **exp-protegido-ms-catalogo-1** |0.88% | 1.13% | 0.76% | **0.92%** |
| **exp-protegido-ms-ordenes-1** |0.95% | 0.83% | 0.75% | **0.84%** |
| **exp-protegido-ms-resenas-1** |0.97% | 0.86% | 0.94% | **0.92%** |
| **exp-protegido-ms-usuarios-1** |0.83% | 0.81% | 0.86% | **0.83%** |
| **exp-protegido-postgres-db-1** |1.22% | 0.93% | 0.96% | **1.04%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |99.22 MiB | 97.65 MiB | 98.99 MiB | **98.62 MiB** |
| **exp-protegido-mongo-db-1** |192.70 MiB | 201.14 MiB | 192.70 MiB | **195.51 MiB** |
| **exp-protegido-ms-catalogo-1** |45.94 MiB | 45.81 MiB | 46.08 MiB | **45.94 MiB** |
| **exp-protegido-ms-ordenes-1** |45.93 MiB | 46.36 MiB | 45.65 MiB | **45.98 MiB** |
| **exp-protegido-ms-resenas-1** |45.63 MiB | 46.36 MiB | 45.60 MiB | **45.86 MiB** |
| **exp-protegido-ms-usuarios-1** |46.30 MiB | 45.64 MiB | 45.93 MiB | **45.96 MiB** |
| **exp-protegido-postgres-db-1** |27.78 MiB | 28.01 MiB | 28.06 MiB | **27.95 MiB** |