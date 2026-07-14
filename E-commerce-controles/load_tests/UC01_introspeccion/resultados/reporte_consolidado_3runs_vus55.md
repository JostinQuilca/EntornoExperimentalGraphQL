# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=55)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 19:34:06

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 3300 | 9.327 ms | 0.00% |
| Run 2 | 3300 | 7.938 ms | 0.00% |
| Run 3 | 3300 | 8.041 ms | 0.00% |
| **PROMEDIO** | **3300.0** | **8.435 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |35.15% | 28.11% | 28.90% | **30.72%** |
| **exp-protegido-mongo-db-1** |65.07% | 57.57% | 60.06% | **60.90%** |
| **exp-protegido-ms-catalogo-1** |3.11% | 3.23% | 3.62% | **3.32%** |
| **exp-protegido-ms-ordenes-1** |5.44% | 3.48% | 3.53% | **4.15%** |
| **exp-protegido-ms-resenas-1** |5.44% | 3.45% | 3.68% | **4.19%** |
| **exp-protegido-ms-usuarios-1** |4.78% | 3.31% | 3.57% | **3.89%** |
| **exp-protegido-postgres-db-1** |4.73% | 4.17% | 4.13% | **4.34%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |116.5MiB (116.50 MiB)  | 103.5MiB (103.50 MiB)  | 101.9MiB (101.90 MiB)  |
| **exp-protegido-mongo-db-1** |349.8MiB (349.80 MiB)  | 344.7MiB (344.70 MiB)  | 333MiB (333.00 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.48MiB (46.48 MiB)  | 46.15MiB (46.15 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.92MiB (46.92 MiB)  | 45.61MiB (45.61 MiB)  | 45.71MiB (45.71 MiB)  |
| **exp-protegido-ms-resenas-1** |46.64MiB (46.64 MiB)  | 46.07MiB (46.07 MiB)  | 46.33MiB (46.33 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.8MiB (46.80 MiB)  | 46.25MiB (46.25 MiB)  | 44.93MiB (44.93 MiB)  |
| **exp-protegido-postgres-db-1** |28.11MiB (28.11 MiB)  | 29.53MiB (29.53 MiB)  | 28.04MiB (28.04 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |16.91% | 15.03% | 16.74% | **16.23%** |
| **exp-protegido-mongo-db-1** |17.75% | 17.35% | 15.19% | **16.76%** |
| **exp-protegido-ms-catalogo-1** |0.80% | 0.84% | 0.91% | **0.85%** |
| **exp-protegido-ms-ordenes-1** |1.03% | 0.86% | 0.92% | **0.94%** |
| **exp-protegido-ms-resenas-1** |1.03% | 0.89% | 0.92% | **0.95%** |
| **exp-protegido-ms-usuarios-1** |1.02% | 0.83% | 0.91% | **0.92%** |
| **exp-protegido-postgres-db-1** |1.18% | 1.17% | 1.08% | **1.14%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |107.98 MiB | 96.98 MiB | 95.26 MiB | **100.07 MiB** |
| **exp-protegido-mongo-db-1** |204.20 MiB | 199.59 MiB | 196.48 MiB | **200.09 MiB** |
| **exp-protegido-ms-catalogo-1** |46.35 MiB | 46.04 MiB | 45.96 MiB | **46.12 MiB** |
| **exp-protegido-ms-ordenes-1** |46.78 MiB | 45.51 MiB | 45.35 MiB | **45.88 MiB** |
| **exp-protegido-ms-resenas-1** |46.46 MiB | 45.97 MiB | 45.97 MiB | **46.13 MiB** |
| **exp-protegido-ms-usuarios-1** |45.28 MiB | 46.15 MiB | 44.83 MiB | **45.42 MiB** |
| **exp-protegido-postgres-db-1** |27.85 MiB | 28.00 MiB | 27.92 MiB | **27.92 MiB** |