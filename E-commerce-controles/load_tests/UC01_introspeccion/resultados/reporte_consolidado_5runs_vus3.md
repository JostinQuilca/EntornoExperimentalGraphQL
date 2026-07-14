# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 22:57:38

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 180 | 9.876 ms | 0.00% |
| Run 2 | 180 | 6.052 ms | 0.00% |
| Run 3 | 180 | 6.735 ms | 0.00% |
| Run 4 | 180 | 6.773 ms | 0.00% |
| Run 5 | 180 | 6.445 ms | 0.00% |
| **PROMEDIO** | **180.0** | **7.176 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |19.62% | 3.38% | 5.69% | 4.08% | 8.09% | **8.17%** |
| **exp-protegido-mongo-db-1** |127.96% | 54.67% | 65.47% | 68.78% | 69.44% | **77.26%** |
| **exp-protegido-ms-catalogo-1** |6.13% | 5.80% | 4.76% | 3.67% | 3.00% | **4.67%** |
| **exp-protegido-ms-ordenes-1** |5.76% | 3.13% | 3.10% | 3.89% | 3.85% | **3.95%** |
| **exp-protegido-ms-resenas-1** |6.89% | 3.18% | 3.43% | 4.11% | 4.66% | **4.45%** |
| **exp-protegido-ms-usuarios-1** |6.47% | 3.31% | 3.04% | 3.96% | 4.08% | **4.17%** |
| **exp-protegido-postgres-db-1** |4.95% | 4.13% | 6.12% | 4.62% | 4.54% | **4.87%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |69.57MiB (69.57 MiB)  | 69.94MiB (69.94 MiB)  | 69.3MiB (69.30 MiB)  | 69.77MiB (69.77 MiB)  | 69.96MiB (69.96 MiB)  |
| **exp-protegido-mongo-db-1** |350.1MiB (350.10 MiB)  | 349.3MiB (349.30 MiB)  | 351.2MiB (351.20 MiB)  | 340MiB (340.00 MiB)  | 333.6MiB (333.60 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.86MiB (45.86 MiB)  | 45.99MiB (45.99 MiB)  | 46.01MiB (46.01 MiB)  | 47.88MiB (47.88 MiB)  | 45.79MiB (45.79 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.13MiB (46.13 MiB)  | 45.77MiB (45.77 MiB)  | 47MiB (47.00 MiB)  | 45.99MiB (45.99 MiB)  | 45.51MiB (45.51 MiB)  |
| **exp-protegido-ms-resenas-1** |45.81MiB (45.81 MiB)  | 46.85MiB (46.85 MiB)  | 47MiB (47.00 MiB)  | 46.04MiB (46.04 MiB)  | 46.14MiB (46.14 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.84MiB (45.84 MiB)  | 46.45MiB (46.45 MiB)  | 46.74MiB (46.74 MiB)  | 45.34MiB (45.34 MiB)  | 45.36MiB (45.36 MiB)  |
| **exp-protegido-postgres-db-1** |27.99MiB (27.99 MiB)  | 27.95MiB (27.95 MiB)  | 29.08MiB (29.08 MiB)  | 27.95MiB (27.95 MiB)  | 29.71MiB (29.71 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.35% | 1.32% | 1.45% | 1.25% | 1.61% | **1.60%** |
| **exp-protegido-mongo-db-1** |29.94% | 15.48% | 17.35% | 17.67% | 16.56% | **19.40%** |
| **exp-protegido-ms-catalogo-1** |1.03% | 1.10% | 0.95% | 0.93% | 0.83% | **0.97%** |
| **exp-protegido-ms-ordenes-1** |1.29% | 0.92% | 0.84% | 1.03% | 0.85% | **0.99%** |
| **exp-protegido-ms-resenas-1** |1.23% | 0.86% | 0.87% | 0.99% | 0.96% | **0.98%** |
| **exp-protegido-ms-usuarios-1** |1.27% | 0.87% | 0.84% | 0.98% | 0.86% | **0.96%** |
| **exp-protegido-postgres-db-1** |1.24% | 1.09% | 1.34% | 1.24% | 1.35% | **1.25%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.11 MiB | 67.28 MiB | 66.68 MiB | 66.80 MiB | 67.28 MiB | **67.03 MiB** |
| **exp-protegido-mongo-db-1** |210.50 MiB | 201.76 MiB | 199.13 MiB | 196.34 MiB | 196.49 MiB | **200.84 MiB** |
| **exp-protegido-ms-catalogo-1** |45.73 MiB | 45.89 MiB | 45.91 MiB | 46.26 MiB | 45.68 MiB | **45.89 MiB** |
| **exp-protegido-ms-ordenes-1** |46.01 MiB | 45.68 MiB | 46.89 MiB | 45.90 MiB | 45.42 MiB | **45.98 MiB** |
| **exp-protegido-ms-resenas-1** |45.70 MiB | 46.75 MiB | 46.90 MiB | 45.94 MiB | 46.04 MiB | **46.27 MiB** |
| **exp-protegido-ms-usuarios-1** |45.58 MiB | 46.35 MiB | 46.64 MiB | 45.24 MiB | 45.26 MiB | **45.81 MiB** |
| **exp-protegido-postgres-db-1** |27.87 MiB | 27.94 MiB | 28.02 MiB | 27.94 MiB | 28.04 MiB | **27.96 MiB** |