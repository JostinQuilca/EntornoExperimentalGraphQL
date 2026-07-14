# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=21)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 19:16:53

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 1260 | 5.808 ms | 0.00% |
| Run 2 | 1260 | 5.874 ms | 0.00% |
| Run 3 | 1260 | 5.773 ms | 0.00% |
| Run 4 | 1260 | 6.041 ms | 0.00% |
| Run 5 | 1260 | 6.208 ms | 0.00% |
| **PROMEDIO** | **1260.0** | **5.941 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |15.44% | 11.65% | 17.72% | 22.64% | 13.12% | **16.11%** |
| **exp-vulnerable-mongo-db-1** |77.61% | 71.03% | 54.53% | 72.04% | 62.01% | **67.44%** |
| **exp-vulnerable-ms-catalogo-1** |5.59% | 4.35% | 3.66% | 3.08% | 3.25% | **3.99%** |
| **exp-vulnerable-ms-ordenes-1** |5.47% | 3.83% | 3.04% | 4.31% | 3.02% | **3.93%** |
| **exp-vulnerable-ms-resenas-1** |5.36% | 4.05% | 3.50% | 4.27% | 2.95% | **4.03%** |
| **exp-vulnerable-ms-usuarios-1** |5.17% | 4.28% | 3.22% | 4.00% | 3.61% | **4.06%** |
| **exp-vulnerable-postgres-db-1** |4.87% | 4.77% | 4.93% | 4.04% | 5.90% | **4.90%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |104.2MiB (104.20 MiB)  | 96.41MiB (96.41 MiB)  | 96.45MiB (96.45 MiB)  | 96.91MiB (96.91 MiB)  | 96.22MiB (96.22 MiB)  |
| **exp-vulnerable-mongo-db-1** |340.1MiB (340.10 MiB)  | 350.8MiB (350.80 MiB)  | 338.8MiB (338.80 MiB)  | 329.8MiB (329.80 MiB)  | 349.2MiB (349.20 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |90.32MiB (90.32 MiB)  | 47.5MiB (47.50 MiB)  | 46.06MiB (46.06 MiB)  | 46.77MiB (46.77 MiB)  | 45.92MiB (45.92 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |101.6MiB (101.60 MiB)  | 46.75MiB (46.75 MiB)  | 46.57MiB (46.57 MiB)  | 47.68MiB (47.68 MiB)  | 45.62MiB (45.62 MiB)  |
| **exp-vulnerable-ms-resenas-1** |93.95MiB (93.95 MiB)  | 46.53MiB (46.53 MiB)  | 46.74MiB (46.74 MiB)  | 47.23MiB (47.23 MiB)  | 46.11MiB (46.11 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |93.32MiB (93.32 MiB)  | 46.06MiB (46.06 MiB)  | 47.37MiB (47.37 MiB)  | 45.97MiB (45.97 MiB)  | 45.7MiB (45.70 MiB)  |
| **exp-vulnerable-postgres-db-1** |29.28MiB (29.28 MiB)  | 27.59MiB (27.59 MiB)  | 27.46MiB (27.46 MiB)  | 27.65MiB (27.65 MiB)  | 28.63MiB (28.63 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |6.27% | 5.00% | 5.74% | 6.98% | 5.65% | **5.93%** |
| **exp-vulnerable-mongo-db-1** |16.13% | 17.47% | 16.85% | 17.60% | 16.83% | **16.98%** |
| **exp-vulnerable-ms-catalogo-1** |1.04% | 1.03% | 0.79% | 0.80% | 0.90% | **0.91%** |
| **exp-vulnerable-ms-ordenes-1** |1.14% | 1.06% | 0.84% | 0.79% | 0.82% | **0.93%** |
| **exp-vulnerable-ms-resenas-1** |1.15% | 1.03% | 0.92% | 0.95% | 0.81% | **0.97%** |
| **exp-vulnerable-ms-usuarios-1** |1.11% | 1.11% | 0.88% | 0.81% | 0.95% | **0.97%** |
| **exp-vulnerable-postgres-db-1** |1.46% | 1.26% | 1.30% | 0.96% | 1.38% | **1.27%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |93.94 MiB | 84.99 MiB | 86.64 MiB | 87.21 MiB | 83.54 MiB | **87.26 MiB** |
| **exp-vulnerable-mongo-db-1** |200.65 MiB | 204.75 MiB | 199.58 MiB | 196.01 MiB | 202.77 MiB | **200.75 MiB** |
| **exp-vulnerable-ms-catalogo-1** |89.96 MiB | 45.68 MiB | 45.94 MiB | 45.50 MiB | 45.80 MiB | **54.58 MiB** |
| **exp-vulnerable-ms-ordenes-1** |93.07 MiB | 46.64 MiB | 46.45 MiB | 47.09 MiB | 45.50 MiB | **55.75 MiB** |
| **exp-vulnerable-ms-resenas-1** |92.66 MiB | 46.42 MiB | 46.62 MiB | 46.65 MiB | 46.00 MiB | **55.67 MiB** |
| **exp-vulnerable-ms-usuarios-1** |92.86 MiB | 45.95 MiB | 47.25 MiB | 45.70 MiB | 45.58 MiB | **55.47 MiB** |
| **exp-vulnerable-postgres-db-1** |27.60 MiB | 27.40 MiB | 27.38 MiB | 27.36 MiB | 27.34 MiB | **27.42 MiB** |