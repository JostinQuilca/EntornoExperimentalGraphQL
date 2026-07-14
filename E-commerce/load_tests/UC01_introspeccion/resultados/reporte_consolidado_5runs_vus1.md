# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 22:07:22

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 60 | 6.734 ms | 0.00% |
| Run 2 | 60 | 6.219 ms | 0.00% |
| Run 3 | 60 | 6.221 ms | 0.00% |
| Run 4 | 60 | 6.029 ms | 0.00% |
| Run 5 | 60 | 5.913 ms | 0.00% |
| **PROMEDIO** | **60.0** | **6.223 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.52% | 1.92% | 2.52% | 4.91% | 1.04% | **2.38%** |
| **exp-vulnerable-mongo-db-1** |54.68% | 59.68% | 63.07% | 82.90% | 51.38% | **62.34%** |
| **exp-vulnerable-ms-catalogo-1** |4.92% | 3.80% | 4.23% | 3.53% | 3.58% | **4.01%** |
| **exp-vulnerable-ms-ordenes-1** |3.84% | 4.63% | 3.62% | 4.35% | 3.56% | **4.00%** |
| **exp-vulnerable-ms-resenas-1** |3.16% | 4.09% | 3.47% | 4.93% | 3.78% | **3.89%** |
| **exp-vulnerable-ms-usuarios-1** |2.91% | 4.19% | 3.65% | 4.32% | 3.80% | **3.77%** |
| **exp-vulnerable-postgres-db-1** |3.51% | 5.96% | 5.00% | 4.99% | 4.25% | **4.74%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |64.16MiB (64.16 MiB)  | 64.69MiB (64.69 MiB)  | 64.83MiB (64.83 MiB)  | 64.74MiB (64.74 MiB)  | 63.62MiB (63.62 MiB)  |
| **exp-vulnerable-mongo-db-1** |349.5MiB (349.50 MiB)  | 331.8MiB (331.80 MiB)  | 333.2MiB (333.20 MiB)  | 340MiB (340.00 MiB)  | 328.7MiB (328.70 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.75MiB (45.75 MiB)  | 46.26MiB (46.26 MiB)  | 46.46MiB (46.46 MiB)  | 46.24MiB (46.24 MiB)  | 45.41MiB (45.41 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |47.52MiB (47.52 MiB)  | 46.38MiB (46.38 MiB)  | 45.81MiB (45.81 MiB)  | 46.96MiB (46.96 MiB)  | 46.99MiB (46.99 MiB)  |
| **exp-vulnerable-ms-resenas-1** |45.57MiB (45.57 MiB)  | 45.69MiB (45.69 MiB)  | 48.18MiB (48.18 MiB)  | 45.7MiB (45.70 MiB)  | 45.79MiB (45.79 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |44.97MiB (44.97 MiB)  | 54.12MiB (54.12 MiB)  | 46.87MiB (46.87 MiB)  | 46.99MiB (46.99 MiB)  | 45.61MiB (45.61 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.42MiB (27.42 MiB)  | 28.94MiB (28.94 MiB)  | 27.38MiB (27.38 MiB)  | 28.45MiB (28.45 MiB)  | 27.41MiB (27.41 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.50% | 0.55% | 0.51% | 0.64% | 0.43% | **0.53%** |
| **exp-vulnerable-mongo-db-1** |15.23% | 17.31% | 16.81% | 17.49% | 15.67% | **16.50%** |
| **exp-vulnerable-ms-catalogo-1** |0.96% | 0.88% | 1.10% | 0.94% | 0.85% | **0.95%** |
| **exp-vulnerable-ms-ordenes-1** |0.90% | 1.01% | 0.86% | 0.93% | 0.89% | **0.92%** |
| **exp-vulnerable-ms-resenas-1** |0.92% | 0.96% | 0.85% | 0.94% | 0.92% | **0.92%** |
| **exp-vulnerable-ms-usuarios-1** |0.89% | 1.10% | 0.79% | 1.07% | 0.88% | **0.95%** |
| **exp-vulnerable-postgres-db-1** |1.01% | 1.22% | 1.20% | 1.31% | 1.21% | **1.19%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |63.43 MiB | 63.94 MiB | 64.08 MiB | 63.55 MiB | 62.99 MiB | **63.60 MiB** |
| **exp-vulnerable-mongo-db-1** |200.91 MiB | 196.23 MiB | 197.11 MiB | 197.82 MiB | 195.93 MiB | **197.60 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.61 MiB | 46.14 MiB | 46.28 MiB | 46.12 MiB | 45.29 MiB | **45.89 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.57 MiB | 46.26 MiB | 45.52 MiB | 46.84 MiB | 46.89 MiB | **46.42 MiB** |
| **exp-vulnerable-ms-resenas-1** |45.43 MiB | 45.57 MiB | 48.03 MiB | 45.58 MiB | 45.67 MiB | **46.06 MiB** |
| **exp-vulnerable-ms-usuarios-1** |44.85 MiB | 50.64 MiB | 46.76 MiB | 46.87 MiB | 45.49 MiB | **46.92 MiB** |
| **exp-vulnerable-postgres-db-1** |27.35 MiB | 27.43 MiB | 27.32 MiB | 27.39 MiB | 27.32 MiB | **27.36 MiB** |