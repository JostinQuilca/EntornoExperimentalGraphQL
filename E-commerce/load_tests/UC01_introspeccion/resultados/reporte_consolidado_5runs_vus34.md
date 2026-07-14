# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=34)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 19:40:41

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 2040 | 6.864 ms | 0.00% |
| Run 2 | 2040 | 6.547 ms | 0.00% |
| Run 3 | 1519 | 6.631 ms | 0.00% |
| Run 4 | 2040 | 6.230 ms | 0.00% |
| Run 5 | 0 | 0.000 ms | 0.00% |
| **PROMEDIO** | **1527.8** | **5.254 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |28.86% | 13.33% | 27.46% | 18.13% | 13.16% | **20.19%** |
| **exp-vulnerable-mongo-db-1** |72.63% | 63.44% | 57.12% | 50.90% | 50.47% | **58.91%** |
| **exp-vulnerable-ms-catalogo-1** |4.68% | 4.11% | 4.44% | 3.11% | 3.37% | **3.94%** |
| **exp-vulnerable-ms-ordenes-1** |3.18% | 3.38% | 3.32% | 3.02% | 4.71% | **3.52%** |
| **exp-vulnerable-ms-resenas-1** |3.01% | 3.29% | 3.89% | 3.37% | 4.04% | **3.52%** |
| **exp-vulnerable-ms-usuarios-1** |3.13% | 5.81% | 3.18% | 3.36% | 3.42% | **3.78%** |
| **exp-vulnerable-postgres-db-1** |6.01% | 4.21% | 4.17% | 4.46% | 3.65% | **4.50%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |98.25MiB (98.25 MiB)  | 100.8MiB (100.80 MiB)  | 99.07MiB (99.07 MiB)  | 98.95MiB (98.95 MiB)  | 98.49MiB (98.49 MiB)  |
| **exp-vulnerable-mongo-db-1** |324.9MiB (324.90 MiB)  | 345.5MiB (345.50 MiB)  | 333MiB (333.00 MiB)  | 334.6MiB (334.60 MiB)  | 329MiB (329.00 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.84MiB (45.84 MiB)  | 46.1MiB (46.10 MiB)  | 45.77MiB (45.77 MiB)  | 46.36MiB (46.36 MiB)  | 46.2MiB (46.20 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.29MiB (46.29 MiB)  | 46.85MiB (46.85 MiB)  | 45.44MiB (45.44 MiB)  | 45.31MiB (45.31 MiB)  | 46.9MiB (46.90 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.7MiB (46.70 MiB)  | 46.14MiB (46.14 MiB)  | 46.27MiB (46.27 MiB)  | 45.22MiB (45.22 MiB)  | 47.56MiB (47.56 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |47.09MiB (47.09 MiB)  | 47.52MiB (47.52 MiB)  | 45.81MiB (45.81 MiB)  | 47.25MiB (47.25 MiB)  | 47.41MiB (47.41 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.44MiB (27.44 MiB)  | 27.35MiB (27.35 MiB)  | 28.68MiB (28.68 MiB)  | 27.36MiB (27.36 MiB)  | 27.35MiB (27.35 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |9.72% | 8.10% | 9.29% | 7.32% | 8.24% | **8.53%** |
| **exp-vulnerable-mongo-db-1** |15.22% | 14.90% | 16.66% | 15.18% | 14.66% | **15.32%** |
| **exp-vulnerable-ms-catalogo-1** |1.17% | 0.87% | 1.07% | 0.89% | 0.80% | **0.96%** |
| **exp-vulnerable-ms-ordenes-1** |0.83% | 0.93% | 0.97% | 0.97% | 1.31% | **1.00%** |
| **exp-vulnerable-ms-resenas-1** |0.67% | 0.98% | 0.96% | 0.90% | 1.21% | **0.94%** |
| **exp-vulnerable-ms-usuarios-1** |0.78% | 1.01% | 0.96% | 0.88% | 1.11% | **0.95%** |
| **exp-vulnerable-postgres-db-1** |1.18% | 1.24% | 1.32% | 1.32% | 1.21% | **1.25%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |87.48 MiB | 87.23 MiB | 89.61 MiB | 91.52 MiB | 86.95 MiB | **88.56 MiB** |
| **exp-vulnerable-mongo-db-1** |195.83 MiB | 202.67 MiB | 195.58 MiB | 194.26 MiB | 194.74 MiB | **196.62 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.69 MiB | 45.98 MiB | 45.66 MiB | 45.67 MiB | 46.12 MiB | **45.82 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.60 MiB | 46.74 MiB | 45.34 MiB | 45.19 MiB | 46.80 MiB | **45.93 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.50 MiB | 46.03 MiB | 46.17 MiB | 45.10 MiB | 47.46 MiB | **46.25 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.25 MiB | 46.08 MiB | 45.72 MiB | 47.03 MiB | 45.36 MiB | **45.89 MiB** |
| **exp-vulnerable-postgres-db-1** |27.28 MiB | 27.30 MiB | 27.44 MiB | 27.30 MiB | 27.28 MiB | **27.32 MiB** |