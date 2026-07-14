# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=144)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 19:56:07

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 8640 | 9.717 ms | 0.00% |
| Run 2 | 8471 | 24.400 ms | 0.00% |
| Run 3 | 8640 | 11.297 ms | 43.20% |
| **PROMEDIO** | **8583.7** | **15.138 ms** | **14.40%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **--** |0.00% | 0.00% | 0.00% | **0.00%** |
| **exp-vulnerable-api-gateway-1** |36.94% | 61.40% | 72.28% | **56.87%** |
| **exp-vulnerable-mongo-db-1** |82.11% | 69.27% | 97.74% | **83.04%** |
| **exp-vulnerable-mongo-init-1** |0.00% | 0.00% | 33.37% | **11.12%** |
| **exp-vulnerable-ms-catalogo-1** |3.34% | 4.39% | 151.40% | **53.04%** |
| **exp-vulnerable-ms-ordenes-1** |3.28% | 18.76% | 122.63% | **48.22%** |
| **exp-vulnerable-ms-resenas-1** |3.21% | 8.94% | 111.53% | **41.23%** |
| **exp-vulnerable-ms-usuarios-1** |3.40% | 6.28% | 117.54% | **42.41%** |
| **exp-vulnerable-postgres-db-1** |4.75% | 6.81% | 9.08% | **6.88%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **--** |N/A | N/A | (0.00 MiB)  |
| **exp-vulnerable-api-gateway-1** |105.3MiB (105.30 MiB)  | 110.9MiB (110.90 MiB)  | 107.1MiB (107.10 MiB)  |
| **exp-vulnerable-mongo-db-1** |342.2MiB (342.20 MiB)  | 331.9MiB (331.90 MiB)  | 344.4MiB (344.40 MiB)  |
| **exp-vulnerable-mongo-init-1** |N/A | N/A | 144.8MiB (144.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.8MiB (45.80 MiB)  | 47.32MiB (47.32 MiB)  | 163.9MiB (163.90 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |47.46MiB (47.46 MiB)  | 45.72MiB (45.72 MiB)  | 123.6MiB (123.60 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.72MiB (46.72 MiB)  | 46.06MiB (46.06 MiB)  | 124.2MiB (124.20 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |45.62MiB (45.62 MiB)  | 47.04MiB (47.04 MiB)  | 124.6MiB (124.60 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.47MiB (27.47 MiB)  | 27.39MiB (27.39 MiB)  | 27.35MiB (27.35 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **--** |0.00% | 0.00% | 0.00% | **0.00%** |
| **exp-vulnerable-api-gateway-1** |25.71% | 33.24% | 34.11% | **31.02%** |
| **exp-vulnerable-mongo-db-1** |19.81% | 19.29% | 18.56% | **19.22%** |
| **exp-vulnerable-mongo-init-1** |0.00% | 0.00% | 16.68% | **5.56%** |
| **exp-vulnerable-ms-catalogo-1** |1.00% | 0.93% | 8.79% | **3.57%** |
| **exp-vulnerable-ms-ordenes-1** |0.80% | 1.50% | 10.94% | **4.41%** |
| **exp-vulnerable-ms-resenas-1** |0.71% | 1.09% | 10.95% | **4.25%** |
| **exp-vulnerable-ms-usuarios-1** |0.87% | 0.96% | 11.15% | **4.33%** |
| **exp-vulnerable-postgres-db-1** |1.11% | 1.28% | 1.41% | **1.27%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **--** |0.00 MiB | 0.00 MiB | 0.00 MiB | **0.00 MiB** |
| **exp-vulnerable-api-gateway-1** |101.25 MiB | 104.28 MiB | 93.77 MiB | **99.77 MiB** |
| **exp-vulnerable-mongo-db-1** |209.14 MiB | 206.12 MiB | 194.66 MiB | **203.31 MiB** |
| **exp-vulnerable-mongo-init-1** |0.00 MiB | 0.00 MiB | 72.76 MiB | **24.25 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.68 MiB | 45.87 MiB | 52.45 MiB | **48.00 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.34 MiB | 45.60 MiB | 50.83 MiB | **47.92 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.60 MiB | 45.94 MiB | 51.09 MiB | **47.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.36 MiB | 46.91 MiB | 49.74 MiB | **47.34 MiB** |
| **exp-vulnerable-postgres-db-1** |27.40 MiB | 27.35 MiB | 25.96 MiB | **26.90 MiB** |