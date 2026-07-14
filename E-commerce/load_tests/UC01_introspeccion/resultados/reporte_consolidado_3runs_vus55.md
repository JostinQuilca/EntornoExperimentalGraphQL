# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=55)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 19:27:49

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 3300 | 7.285 ms | 0.00% |
| Run 2 | 3300 | 7.765 ms | 0.00% |
| Run 3 | 3300 | 8.472 ms | 0.00% |
| **PROMEDIO** | **3300.0** | **7.841 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |29.02% | 34.69% | 26.40% | **30.04%** |
| **exp-vulnerable-mongo-db-1** |58.62% | 68.54% | 56.57% | **61.24%** |
| **exp-vulnerable-ms-catalogo-1** |3.37% | 4.94% | 4.06% | **4.12%** |
| **exp-vulnerable-ms-ordenes-1** |3.51% | 3.15% | 3.43% | **3.36%** |
| **exp-vulnerable-ms-resenas-1** |3.64% | 3.53% | 3.11% | **3.43%** |
| **exp-vulnerable-ms-usuarios-1** |3.67% | 3.41% | 3.97% | **3.68%** |
| **exp-vulnerable-postgres-db-1** |6.57% | 6.95% | 5.85% | **6.46%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |99.73MiB (99.73 MiB)  | 101MiB (101.00 MiB)  | 101MiB (101.00 MiB)  |
| **exp-vulnerable-mongo-db-1** |349.7MiB (349.70 MiB)  | 340.7MiB (340.70 MiB)  | 351.6MiB (351.60 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.41MiB (45.41 MiB)  | 46.1MiB (46.10 MiB)  | 46.3MiB (46.30 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.3MiB (46.30 MiB)  | 46.59MiB (46.59 MiB)  | 48.18MiB (48.18 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.05MiB (46.05 MiB)  | 46.25MiB (46.25 MiB)  | 46.53MiB (46.53 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |46.02MiB (46.02 MiB)  | 45.79MiB (45.79 MiB)  | 46.25MiB (46.25 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.38MiB (27.38 MiB)  | 27.38MiB (27.38 MiB)  | 28.86MiB (28.86 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |13.53% | 13.81% | 13.68% | **13.67%** |
| **exp-vulnerable-mongo-db-1** |15.51% | 17.34% | 16.22% | **16.36%** |
| **exp-vulnerable-ms-catalogo-1** |1.00% | 0.93% | 0.86% | **0.93%** |
| **exp-vulnerable-ms-ordenes-1** |0.96% | 0.89% | 0.89% | **0.91%** |
| **exp-vulnerable-ms-resenas-1** |0.92% | 0.90% | 0.94% | **0.92%** |
| **exp-vulnerable-ms-usuarios-1** |1.07% | 0.89% | 0.91% | **0.96%** |
| **exp-vulnerable-postgres-db-1** |1.35% | 1.42% | 1.19% | **1.32%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |94.99 MiB | 94.93 MiB | 94.83 MiB | **94.92 MiB** |
| **exp-vulnerable-mongo-db-1** |197.14 MiB | 195.18 MiB | 205.22 MiB | **199.18 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.28 MiB | 45.98 MiB | 46.18 MiB | **45.81 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.17 MiB | 46.48 MiB | 47.96 MiB | **46.87 MiB** |
| **exp-vulnerable-ms-resenas-1** |45.92 MiB | 46.13 MiB | 45.60 MiB | **45.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.68 MiB | 45.68 MiB | 45.59 MiB | **45.65 MiB** |
| **exp-vulnerable-postgres-db-1** |27.32 MiB | 27.32 MiB | 27.41 MiB | **27.35 MiB** |