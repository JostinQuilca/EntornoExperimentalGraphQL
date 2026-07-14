# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 01:41:39

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 37 | 658.046 ms | 0.00% | 0.00% |
| Run 2 | 37 | 641.988 ms | 0.00% | 0.00% |
| Run 3 | 37 | 633.978 ms | 0.00% | 0.00% |
| Run 4 | 37 | 643.946 ms | 0.00% | 0.00% |
| Run 5 | 37 | 634.193 ms | 0.00% | 0.00% |
| **PROMEDIO** | **37.0** | **642.430 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |10.38% | 10.76% | 10.06% | 8.93% | 19.22% | **11.87%** |
| **exp-vulnerable-mongo-db-1** |113.22% | 80.53% | 71.92% | 72.77% | 68.13% | **81.31%** |
| **exp-vulnerable-ms-catalogo-1** |9.72% | 4.60% | 4.07% | 5.24% | 4.37% | **5.60%** |
| **exp-vulnerable-ms-ordenes-1** |13.27% | 11.85% | 10.69% | 20.51% | 12.68% | **13.80%** |
| **exp-vulnerable-ms-resenas-1** |4.58% | 4.37% | 4.08% | 4.77% | 4.52% | **4.46%** |
| **exp-vulnerable-ms-usuarios-1** |5.15% | 4.68% | 4.10% | 4.74% | 4.70% | **4.67%** |
| **exp-vulnerable-postgres-db-1** |29.00% | 23.49% | 24.79% | 38.80% | 24.20% | **28.06%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |97.3MiB (97.30 MiB)  | 67.24MiB (67.24 MiB)  | 97.3MiB (97.30 MiB)  | 96.33MiB (96.33 MiB)  | 67.64MiB (67.64 MiB)  |
| **exp-vulnerable-mongo-db-1** |340.6MiB (340.60 MiB)  | 356.4MiB (356.40 MiB)  | 336.5MiB (336.50 MiB)  | 343.5MiB (343.50 MiB)  | 341.3MiB (341.30 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.61MiB (45.61 MiB)  | 47.57MiB (47.57 MiB)  | 46.89MiB (46.89 MiB)  | 48.35MiB (48.35 MiB)  | 46.39MiB (46.39 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |71.72MiB (71.72 MiB)  | 72.33MiB (72.33 MiB)  | 71.94MiB (71.94 MiB)  | 72.85MiB (72.85 MiB)  | 72.68MiB (72.68 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.77MiB (46.77 MiB)  | 45.79MiB (45.79 MiB)  | 46.33MiB (46.33 MiB)  | 46.48MiB (46.48 MiB)  | 46.38MiB (46.38 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.88MiB (45.88 MiB)  | 46.88MiB (46.88 MiB)  | 45.75MiB (45.75 MiB)  | 45.72MiB (45.72 MiB)  | 46.09MiB (46.09 MiB)  |
| **exp-vulnerable-postgres-db-1** |39.92MiB (39.92 MiB)  | 37.87MiB (37.87 MiB)  | 39.31MiB (39.31 MiB)  | 37.77MiB (37.77 MiB)  | 37.62MiB (37.62 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.60% | 1.33% | 1.44% | 1.22% | 1.59% | **1.44%** |
| **exp-vulnerable-mongo-db-1** |30.14% | 18.94% | 20.02% | 20.99% | 17.07% | **21.43%** |
| **exp-vulnerable-ms-catalogo-1** |1.35% | 1.12% | 1.15% | 1.15% | 1.12% | **1.18%** |
| **exp-vulnerable-ms-ordenes-1** |6.10% | 5.65% | 5.72% | 5.79% | 5.48% | **5.75%** |
| **exp-vulnerable-ms-resenas-1** |1.31% | 1.16% | 1.09% | 1.24% | 1.00% | **1.16%** |
| **exp-vulnerable-ms-usuarios-1** |1.24% | 1.15% | 1.10% | 1.29% | 1.02% | **1.16%** |
| **exp-vulnerable-postgres-db-1** |13.96% | 13.13% | 13.57% | 13.38% | 12.50% | **13.31%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |70.78 MiB | 65.74 MiB | 69.13 MiB | 67.29 MiB | 66.43 MiB | **67.87 MiB** |
| **exp-vulnerable-mongo-db-1** |208.95 MiB | 216.23 MiB | 208.27 MiB | 212.79 MiB | 205.20 MiB | **210.29 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.48 MiB | 45.94 MiB | 46.07 MiB | 46.21 MiB | 45.99 MiB | **45.94 MiB** |
| **exp-vulnerable-ms-ordenes-1** |65.42 MiB | 65.78 MiB | 65.78 MiB | 65.76 MiB | 65.67 MiB | **65.68 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.65 MiB | 45.67 MiB | 46.22 MiB | 46.37 MiB | 46.26 MiB | **46.23 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.75 MiB | 46.76 MiB | 45.64 MiB | 45.60 MiB | 45.97 MiB | **45.94 MiB** |
| **exp-vulnerable-postgres-db-1** |37.30 MiB | 37.23 MiB | 37.33 MiB | 37.26 MiB | 37.21 MiB | **37.27 MiB** |