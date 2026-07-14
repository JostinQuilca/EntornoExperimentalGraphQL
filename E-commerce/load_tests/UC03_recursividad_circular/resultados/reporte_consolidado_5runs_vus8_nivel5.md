# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 21:29:18

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 32 | 16891.111 ms | 0.00% | 0.00% |
| Run 2 | 42 | 11823.535 ms | 0.00% | 0.00% |
| Run 3 | 42 | 11305.882 ms | 0.00% | 0.00% |
| Run 4 | 37 | 13391.074 ms | 0.00% | 0.00% |
| Run 5 | 39 | 12802.601 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.4** | **13242.841 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |147.37% | 157.23% | 232.74% | 158.74% | 150.36% | **169.29%** |
| **exp-vulnerable-mongo-db-1** |129.03% | 83.65% | 98.97% | 128.49% | 108.21% | **109.67%** |
| **exp-vulnerable-ms-catalogo-1** |7.84% | 3.80% | 5.25% | 6.44% | 6.75% | **6.02%** |
| **exp-vulnerable-ms-ordenes-1** |8.96% | 6.40% | 8.40% | 5.02% | 11.48% | **8.05%** |
| **exp-vulnerable-ms-resenas-1** |201.03% | 185.45% | 187.56% | 194.33% | 180.90% | **189.85%** |
| **exp-vulnerable-ms-usuarios-1** |34.49% | 32.13% | 5.19% | 44.86% | 60.86% | **35.51%** |
| **exp-vulnerable-postgres-db-1** |42.96% | 18.37% | 7.89% | 10.93% | 15.08% | **19.05%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |410MiB (410.00 MiB)  | 454.6MiB (454.60 MiB)  | 371.8MiB (371.80 MiB)  | 477.8MiB (477.80 MiB)  | 360.2MiB (360.20 MiB)  |
| **exp-vulnerable-mongo-db-1** |352.6MiB (352.60 MiB)  | 352.1MiB (352.10 MiB)  | 346.4MiB (346.40 MiB)  | 350.1MiB (350.10 MiB)  | 334.9MiB (334.90 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.73MiB (46.73 MiB)  | 47.79MiB (47.79 MiB)  | 47.38MiB (47.38 MiB)  | 45.9MiB (45.90 MiB)  | 48.04MiB (48.04 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.82MiB (45.82 MiB)  | 46.91MiB (46.91 MiB)  | 46.24MiB (46.24 MiB)  | 46.77MiB (46.77 MiB)  | 46.6MiB (46.60 MiB)  |
| **exp-vulnerable-ms-resenas-1** |498.3MiB (498.30 MiB)  | 513.4MiB (513.40 MiB)  | 444.7MiB (444.70 MiB)  | 495.8MiB (495.80 MiB)  | 497.4MiB (497.40 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |69.29MiB (69.29 MiB)  | 71.14MiB (71.14 MiB)  | 65.55MiB (65.55 MiB)  | 72.08MiB (72.08 MiB)  | 72.16MiB (72.16 MiB)  |
| **exp-vulnerable-postgres-db-1** |70.4MiB (70.40 MiB)  | 68.48MiB (68.48 MiB)  | 68.54MiB (68.54 MiB)  | 68.19MiB (68.19 MiB)  | 68.5MiB (68.50 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |51.74% | 54.94% | 50.89% | 52.72% | 51.57% | **52.37%** |
| **exp-vulnerable-mongo-db-1** |35.67% | 17.05% | 22.01% | 42.05% | 16.20% | **26.60%** |
| **exp-vulnerable-ms-catalogo-1** |1.68% | 1.24% | 1.21% | 1.49% | 1.48% | **1.42%** |
| **exp-vulnerable-ms-ordenes-1** |1.67% | 1.45% | 1.53% | 1.36% | 1.54% | **1.51%** |
| **exp-vulnerable-ms-resenas-1** |113.56% | 101.78% | 109.57% | 114.03% | 120.52% | **111.89%** |
| **exp-vulnerable-ms-usuarios-1** |3.02% | 2.56% | 1.71% | 4.19% | 3.70% | **3.04%** |
| **exp-vulnerable-postgres-db-1** |4.60% | 2.97% | 2.29% | 2.81% | 2.49% | **3.03%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |233.08 MiB | 240.27 MiB | 202.30 MiB | 267.04 MiB | 204.36 MiB | **229.41 MiB** |
| **exp-vulnerable-mongo-db-1** |205.02 MiB | 211.05 MiB | 213.89 MiB | 232.24 MiB | 210.94 MiB | **214.63 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.42 MiB | 45.97 MiB | 47.25 MiB | 45.77 MiB | 47.90 MiB | **46.46 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.67 MiB | 46.78 MiB | 45.98 MiB | 45.77 MiB | 45.36 MiB | **45.91 MiB** |
| **exp-vulnerable-ms-resenas-1** |293.71 MiB | 325.35 MiB | 317.49 MiB | 345.05 MiB | 303.85 MiB | **317.09 MiB** |
| **exp-vulnerable-ms-usuarios-1** |69.12 MiB | 66.60 MiB | 62.58 MiB | 63.11 MiB | 70.02 MiB | **66.29 MiB** |
| **exp-vulnerable-postgres-db-1** |69.09 MiB | 66.32 MiB | 66.33 MiB | 66.88 MiB | 66.56 MiB | **67.04 MiB** |