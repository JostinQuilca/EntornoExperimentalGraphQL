# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 15:43:20

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 480 | 12.084 ms | 0.00% |
| Run 2 | 480 | 5.559 ms | 0.00% |
| Run 3 | 478 | 6.057 ms | 0.00% |
| Run 4 | 480 | 5.843 ms | 0.00% |
| Run 5 | 480 | 5.623 ms | 0.00% |
| **PROMEDIO** | **479.6** | **7.033 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |15.40% | 11.62% | 8.15% | 8.04% | 10.26% | **10.69%** |
| **exp-vulnerable-mongo-db-1** |139.90% | 79.82% | 69.65% | 111.66% | 54.64% | **91.13%** |
| **exp-vulnerable-ms-catalogo-1** |4.00% | 3.85% | 7.25% | 7.37% | 5.30% | **5.55%** |
| **exp-vulnerable-ms-ordenes-1** |4.00% | 3.11% | 5.05% | 3.39% | 3.94% | **3.90%** |
| **exp-vulnerable-ms-resenas-1** |3.99% | 3.55% | 4.64% | 3.42% | 3.77% | **3.87%** |
| **exp-vulnerable-ms-usuarios-1** |3.94% | 3.50% | 4.67% | 2.90% | 3.85% | **3.77%** |
| **exp-vulnerable-postgres-db-1** |11.72% | 4.33% | 3.72% | 7.70% | 6.78% | **6.85%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |107.1MiB (107.10 MiB)  | 81.95MiB (81.95 MiB)  | 81.67MiB (81.67 MiB)  | 81.5MiB (81.50 MiB)  | 81.69MiB (81.69 MiB)  |
| **exp-vulnerable-mongo-db-1** |446.6MiB (446.60 MiB)  | 341.2MiB (341.20 MiB)  | 346.6MiB (346.60 MiB)  | 342.7MiB (342.70 MiB)  | 348.9MiB (348.90 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |92.19MiB (92.19 MiB)  | 46.17MiB (46.17 MiB)  | 46.48MiB (46.48 MiB)  | 46.53MiB (46.53 MiB)  | 45.76MiB (45.76 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |106.3MiB (106.30 MiB)  | 45.78MiB (45.78 MiB)  | 45.98MiB (45.98 MiB)  | 46.05MiB (46.05 MiB)  | 46.94MiB (46.94 MiB)  |
| **exp-vulnerable-ms-resenas-1** |109.7MiB (109.70 MiB)  | 46.85MiB (46.85 MiB)  | 45.85MiB (45.85 MiB)  | 45.64MiB (45.64 MiB)  | 46.59MiB (46.59 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |99.42MiB (99.42 MiB)  | 45.86MiB (45.86 MiB)  | 46.37MiB (46.37 MiB)  | 45.52MiB (45.52 MiB)  | 46.79MiB (46.79 MiB)  |
| **exp-vulnerable-postgres-db-1** |42.71MiB (42.71 MiB)  | 27.33MiB (27.33 MiB)  | 28.21MiB (28.21 MiB)  | 27.74MiB (27.74 MiB)  | 27.38MiB (27.38 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |3.19% | 3.07% | 2.90% | 2.71% | 3.08% | **2.99%** |
| **exp-vulnerable-mongo-db-1** |19.25% | 17.35% | 19.37% | 20.30% | 15.89% | **18.43%** |
| **exp-vulnerable-ms-catalogo-1** |0.98% | 0.97% | 1.24% | 1.26% | 0.91% | **1.07%** |
| **exp-vulnerable-ms-ordenes-1** |0.79% | 0.71% | 1.03% | 0.81% | 0.93% | **0.85%** |
| **exp-vulnerable-ms-resenas-1** |0.87% | 1.06% | 0.93% | 0.81% | 0.97% | **0.93%** |
| **exp-vulnerable-ms-usuarios-1** |0.73% | 0.97% | 1.01% | 0.79% | 1.03% | **0.91%** |
| **exp-vulnerable-postgres-db-1** |1.87% | 1.04% | 1.04% | 1.26% | 1.37% | **1.32%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |88.47 MiB | 75.17 MiB | 74.56 MiB | 74.08 MiB | 74.88 MiB | **77.43 MiB** |
| **exp-vulnerable-mongo-db-1** |309.13 MiB | 204.54 MiB | 196.08 MiB | 196.73 MiB | 197.80 MiB | **220.86 MiB** |
| **exp-vulnerable-ms-catalogo-1** |92.06 MiB | 45.90 MiB | 46.28 MiB | 46.40 MiB | 45.62 MiB | **55.25 MiB** |
| **exp-vulnerable-ms-ordenes-1** |105.44 MiB | 45.66 MiB | 45.86 MiB | 45.92 MiB | 45.25 MiB | **57.63 MiB** |
| **exp-vulnerable-ms-resenas-1** |107.99 MiB | 46.32 MiB | 45.74 MiB | 45.52 MiB | 45.77 MiB | **58.27 MiB** |
| **exp-vulnerable-ms-usuarios-1** |99.28 MiB | 45.66 MiB | 46.26 MiB | 45.40 MiB | 45.38 MiB | **56.40 MiB** |
| **exp-vulnerable-postgres-db-1** |42.66 MiB | 27.29 MiB | 27.41 MiB | 27.33 MiB | 27.34 MiB | **30.41 MiB** |