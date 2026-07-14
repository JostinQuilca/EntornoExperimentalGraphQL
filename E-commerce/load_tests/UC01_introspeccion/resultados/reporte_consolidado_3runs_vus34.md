# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=34)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 19:16:06

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 2038 | 6.802 ms | 0.00% |
| Run 2 | 2040 | 6.966 ms | 0.00% |
| Run 3 | 2040 | 6.823 ms | 0.00% |
| **PROMEDIO** | **2039.3** | **6.864 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |18.83% | 21.74% | 22.01% | **20.86%** |
| **exp-vulnerable-mongo-db-1** |65.97% | 59.98% | 54.35% | **60.10%** |
| **exp-vulnerable-ms-catalogo-1** |2.98% | 3.94% | 5.19% | **4.04%** |
| **exp-vulnerable-ms-ordenes-1** |3.24% | 3.77% | 2.62% | **3.21%** |
| **exp-vulnerable-ms-resenas-1** |3.94% | 4.35% | 3.17% | **3.82%** |
| **exp-vulnerable-ms-usuarios-1** |3.79% | 3.63% | 2.72% | **3.38%** |
| **exp-vulnerable-postgres-db-1** |4.95% | 4.33% | 4.15% | **4.48%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |98.11MiB (98.11 MiB)  | 100.7MiB (100.70 MiB)  | 97.96MiB (97.96 MiB)  |
| **exp-vulnerable-mongo-db-1** |335.7MiB (335.70 MiB)  | 343.5MiB (343.50 MiB)  | 340.8MiB (340.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.09MiB (46.09 MiB)  | 46.75MiB (46.75 MiB)  | 46.93MiB (46.93 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.89MiB (45.89 MiB)  | 45.77MiB (45.77 MiB)  | 46.06MiB (46.06 MiB)  |
| **exp-vulnerable-ms-resenas-1** |45.99MiB (45.99 MiB)  | 46.71MiB (46.71 MiB)  | 46.5MiB (46.50 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |46.3MiB (46.30 MiB)  | 45.83MiB (45.83 MiB)  | 46.43MiB (46.43 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.34MiB (27.34 MiB)  | 27.35MiB (27.35 MiB)  | 27.37MiB (27.37 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |8.33% | 9.21% | 9.63% | **9.06%** |
| **exp-vulnerable-mongo-db-1** |16.41% | 16.70% | 15.51% | **16.21%** |
| **exp-vulnerable-ms-catalogo-1** |0.71% | 1.00% | 0.91% | **0.87%** |
| **exp-vulnerable-ms-ordenes-1** |0.99% | 0.85% | 0.78% | **0.87%** |
| **exp-vulnerable-ms-resenas-1** |1.18% | 0.85% | 0.85% | **0.96%** |
| **exp-vulnerable-ms-usuarios-1** |1.09% | 0.87% | 0.83% | **0.93%** |
| **exp-vulnerable-postgres-db-1** |1.39% | 1.12% | 1.14% | **1.22%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |91.17 MiB | 92.48 MiB | 85.95 MiB | **89.87 MiB** |
| **exp-vulnerable-mongo-db-1** |201.73 MiB | 207.71 MiB | 195.17 MiB | **201.54 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.97 MiB | 46.64 MiB | 46.81 MiB | **46.47 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.77 MiB | 45.61 MiB | 45.94 MiB | **45.77 MiB** |
| **exp-vulnerable-ms-resenas-1** |45.87 MiB | 46.49 MiB | 46.38 MiB | **46.25 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.18 MiB | 45.67 MiB | 46.32 MiB | **46.06 MiB** |
| **exp-vulnerable-postgres-db-1** |27.28 MiB | 27.32 MiB | 27.32 MiB | **27.31 MiB** |