# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=233)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 20:19:08

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 13874 | 14.505 ms | 0.13% |
| Run 2 | 13904 | 13.811 ms | 0.05% |
| Run 3 | 13893 | 14.049 ms | 0.00% |
| **PROMEDIO** | **13890.3** | **14.121 ms** | **0.06%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |70.84% | 82.81% | 73.88% | **75.84%** |
| **exp-protegido-mongo-db-1** |54.47% | 62.30% | 56.06% | **57.61%** |
| **exp-protegido-ms-catalogo-1** |5.79% | 3.66% | 3.78% | **4.41%** |
| **exp-protegido-ms-ordenes-1** |4.06% | 3.31% | 3.36% | **3.58%** |
| **exp-protegido-ms-resenas-1** |4.00% | 3.21% | 3.76% | **3.66%** |
| **exp-protegido-ms-usuarios-1** |3.25% | 2.76% | 3.36% | **3.12%** |
| **exp-protegido-postgres-db-1** |4.23% | 4.67% | 4.00% | **4.30%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |168.7MiB (168.70 MiB)  | 119.2MiB (119.20 MiB)  | 115.9MiB (115.90 MiB)  |
| **exp-protegido-mongo-db-1** |339.2MiB (339.20 MiB)  | 331.8MiB (331.80 MiB)  | 338.1MiB (338.10 MiB)  |
| **exp-protegido-ms-catalogo-1** |46MiB (46.00 MiB)  | 46.85MiB (46.85 MiB)  | 46.69MiB (46.69 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.05MiB (46.05 MiB)  | 48.93MiB (48.93 MiB)  | 47.19MiB (47.19 MiB)  |
| **exp-protegido-ms-resenas-1** |46.23MiB (46.23 MiB)  | 47.41MiB (47.41 MiB)  | 46.5MiB (46.50 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.21MiB (46.21 MiB)  | 47.19MiB (47.19 MiB)  | 46.66MiB (46.66 MiB)  |
| **exp-protegido-postgres-db-1** |28.67MiB (28.67 MiB)  | 28MiB (28.00 MiB)  | 27.92MiB (27.92 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |49.52% | 47.66% | 43.90% | **47.03%** |
| **exp-protegido-mongo-db-1** |15.53% | 15.35% | 16.44% | **15.77%** |
| **exp-protegido-ms-catalogo-1** |0.82% | 0.78% | 0.78% | **0.79%** |
| **exp-protegido-ms-ordenes-1** |0.90% | 0.81% | 0.91% | **0.87%** |
| **exp-protegido-ms-resenas-1** |0.90% | 0.77% | 0.91% | **0.86%** |
| **exp-protegido-ms-usuarios-1** |0.90% | 0.73% | 0.86% | **0.83%** |
| **exp-protegido-postgres-db-1** |1.21% | 1.07% | 1.02% | **1.10%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |124.33 MiB | 108.50 MiB | 108.05 MiB | **113.63 MiB** |
| **exp-protegido-mongo-db-1** |204.24 MiB | 200.07 MiB | 196.34 MiB | **200.22 MiB** |
| **exp-protegido-ms-catalogo-1** |45.86 MiB | 46.76 MiB | 46.59 MiB | **46.40 MiB** |
| **exp-protegido-ms-ordenes-1** |45.95 MiB | 47.03 MiB | 47.09 MiB | **46.69 MiB** |
| **exp-protegido-ms-resenas-1** |46.11 MiB | 47.10 MiB | 46.39 MiB | **46.53 MiB** |
| **exp-protegido-ms-usuarios-1** |46.09 MiB | 45.70 MiB | 46.56 MiB | **46.12 MiB** |
| **exp-protegido-postgres-db-1** |27.85 MiB | 27.98 MiB | 27.92 MiB | **27.92 MiB** |