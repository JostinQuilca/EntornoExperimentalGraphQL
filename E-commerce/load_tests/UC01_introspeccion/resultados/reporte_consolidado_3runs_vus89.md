# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=89)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 19:39:30

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 5340 | 7.736 ms | 0.00% |
| Run 2 | 5340 | 8.044 ms | 0.00% |
| Run 3 | 5340 | 8.244 ms | 0.00% |
| **PROMEDIO** | **5340.0** | **8.008 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |37.01% | 31.52% | 31.89% | **33.47%** |
| **exp-vulnerable-mongo-db-1** |60.10% | 57.44% | 60.41% | **59.32%** |
| **exp-vulnerable-ms-catalogo-1** |3.74% | 3.71% | 3.45% | **3.63%** |
| **exp-vulnerable-ms-ordenes-1** |3.21% | 3.00% | 3.53% | **3.25%** |
| **exp-vulnerable-ms-resenas-1** |3.39% | 2.92% | 4.12% | **3.48%** |
| **exp-vulnerable-ms-usuarios-1** |3.12% | 3.30% | 3.75% | **3.39%** |
| **exp-vulnerable-postgres-db-1** |4.03% | 4.10% | 5.22% | **4.45%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |101.6MiB (101.60 MiB)  | 102.2MiB (102.20 MiB)  | 102.8MiB (102.80 MiB)  |
| **exp-vulnerable-mongo-db-1** |338.8MiB (338.80 MiB)  | 340.4MiB (340.40 MiB)  | 342.8MiB (342.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.46MiB (46.46 MiB)  | 45.06MiB (45.06 MiB)  | 46.06MiB (46.06 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |48.68MiB (48.68 MiB)  | 45.91MiB (45.91 MiB)  | 46.46MiB (46.46 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47MiB (47.00 MiB)  | 46.07MiB (46.07 MiB)  | 45.59MiB (45.59 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |50.18MiB (50.18 MiB)  | 45.79MiB (45.79 MiB)  | 46.03MiB (46.03 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.39MiB (27.39 MiB)  | 28.92MiB (28.92 MiB)  | 27.57MiB (27.57 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |17.94% | 18.75% | 16.40% | **17.70%** |
| **exp-vulnerable-mongo-db-1** |15.35% | 15.44% | 17.42% | **16.07%** |
| **exp-vulnerable-ms-catalogo-1** |0.80% | 0.78% | 0.97% | **0.85%** |
| **exp-vulnerable-ms-ordenes-1** |0.79% | 0.88% | 0.75% | **0.81%** |
| **exp-vulnerable-ms-resenas-1** |0.82% | 0.82% | 0.88% | **0.84%** |
| **exp-vulnerable-ms-usuarios-1** |0.86% | 0.85% | 0.72% | **0.81%** |
| **exp-vulnerable-postgres-db-1** |1.18% | 1.18% | 1.25% | **1.20%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |97.26 MiB | 97.20 MiB | 98.75 MiB | **97.74 MiB** |
| **exp-vulnerable-mongo-db-1** |197.07 MiB | 197.17 MiB | 199.42 MiB | **197.89 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.33 MiB | 44.93 MiB | 45.94 MiB | **45.73 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.11 MiB | 45.79 MiB | 46.29 MiB | **46.40 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.80 MiB | 45.96 MiB | 45.42 MiB | **46.06 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.59 MiB | 45.67 MiB | 45.77 MiB | **46.34 MiB** |
| **exp-vulnerable-postgres-db-1** |27.34 MiB | 27.42 MiB | 27.38 MiB | **27.38 MiB** |