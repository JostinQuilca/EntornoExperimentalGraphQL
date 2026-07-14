# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 20:27:14

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 458 | 56.144 ms | 0.00% | 0.00% |
| Run 2 | 455 | 65.744 ms | 0.00% | 0.00% |
| Run 3 | 457 | 57.792 ms | 0.00% | 0.00% |
| Run 4 | 458 | 58.580 ms | 0.00% | 0.00% |
| Run 5 | 458 | 55.799 ms | 0.00% | 0.00% |
| **PROMEDIO** | **457.2** | **58.812 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |25.69% | 25.45% | 26.88% | 46.15% | 32.72% | **31.38%** |
| **exp-vulnerable-mongo-db-1** |129.37% | 112.61% | 99.25% | 96.65% | 73.60% | **102.30%** |
| **exp-vulnerable-ms-catalogo-1** |5.03% | 18.61% | 8.99% | 5.21% | 5.38% | **8.64%** |
| **exp-vulnerable-ms-ordenes-1** |10.98% | 11.11% | 9.14% | 10.08% | 5.69% | **9.40%** |
| **exp-vulnerable-ms-resenas-1** |12.63% | 28.20% | 26.00% | 19.36% | 14.95% | **20.23%** |
| **exp-vulnerable-ms-usuarios-1** |43.17% | 42.66% | 44.91% | 44.14% | 54.64% | **45.90%** |
| **exp-vulnerable-postgres-db-1** |51.57% | 69.35% | 59.94% | 41.76% | 27.71% | **50.07%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |118.1MiB (118.10 MiB)  | 113.9MiB (113.90 MiB)  | 101.4MiB (101.40 MiB)  | 117MiB (117.00 MiB)  | 109.3MiB (109.30 MiB)  |
| **exp-vulnerable-mongo-db-1** |464.3MiB (464.30 MiB)  | 348.2MiB (348.20 MiB)  | 338.6MiB (338.60 MiB)  | 349.9MiB (349.90 MiB)  | 346.6MiB (346.60 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |91.91MiB (91.91 MiB)  | 46.73MiB (46.73 MiB)  | 47.77MiB (47.77 MiB)  | 46.68MiB (46.68 MiB)  | 47.2MiB (47.20 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |111.7MiB (111.70 MiB)  | 46.82MiB (46.82 MiB)  | 46.98MiB (46.98 MiB)  | 45.72MiB (45.72 MiB)  | 46.33MiB (46.33 MiB)  |
| **exp-vulnerable-ms-resenas-1** |138MiB (138.00 MiB)  | 69.84MiB (69.84 MiB)  | 71.22MiB (71.22 MiB)  | 72.52MiB (72.52 MiB)  | 71.34MiB (71.34 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |136.9MiB (136.90 MiB)  | 72.08MiB (72.08 MiB)  | 70.88MiB (70.88 MiB)  | 72.21MiB (72.21 MiB)  | 72.24MiB (72.24 MiB)  |
| **exp-vulnerable-postgres-db-1** |85.63MiB (85.63 MiB)  | 70.04MiB (70.04 MiB)  | 74.26MiB (74.26 MiB)  | 69.72MiB (69.72 MiB)  | 70.33MiB (70.33 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |9.73% | 10.75% | 11.02% | 13.17% | 9.98% | **10.93%** |
| **exp-vulnerable-mongo-db-1** |26.74% | 27.04% | 27.42% | 28.76% | 21.54% | **26.30%** |
| **exp-vulnerable-ms-catalogo-1** |1.13% | 2.15% | 1.75% | 1.29% | 1.32% | **1.53%** |
| **exp-vulnerable-ms-ordenes-1** |1.41% | 1.89% | 1.87% | 1.69% | 1.41% | **1.65%** |
| **exp-vulnerable-ms-resenas-1** |6.73% | 8.26% | 8.59% | 7.07% | 6.68% | **7.47%** |
| **exp-vulnerable-ms-usuarios-1** |6.18% | 7.55% | 7.12% | 7.17% | 6.75% | **6.95%** |
| **exp-vulnerable-postgres-db-1** |17.06% | 19.47% | 19.63% | 18.13% | 16.29% | **18.12%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |114.88 MiB | 95.01 MiB | 94.60 MiB | 92.13 MiB | 89.06 MiB | **97.14 MiB** |
| **exp-vulnerable-mongo-db-1** |331.58 MiB | 221.79 MiB | 203.76 MiB | 215.10 MiB | 221.68 MiB | **238.78 MiB** |
| **exp-vulnerable-ms-catalogo-1** |91.77 MiB | 45.54 MiB | 46.04 MiB | 46.57 MiB | 45.77 MiB | **55.14 MiB** |
| **exp-vulnerable-ms-ordenes-1** |109.60 MiB | 45.27 MiB | 46.87 MiB | 45.61 MiB | 45.75 MiB | **58.62 MiB** |
| **exp-vulnerable-ms-resenas-1** |130.68 MiB | 64.41 MiB | 65.79 MiB | 67.72 MiB | 65.28 MiB | **78.78 MiB** |
| **exp-vulnerable-ms-usuarios-1** |130.08 MiB | 67.00 MiB | 66.53 MiB | 66.73 MiB | 67.38 MiB | **79.54 MiB** |
| **exp-vulnerable-postgres-db-1** |81.29 MiB | 67.14 MiB | 73.44 MiB | 66.94 MiB | 68.66 MiB | **71.49 MiB** |