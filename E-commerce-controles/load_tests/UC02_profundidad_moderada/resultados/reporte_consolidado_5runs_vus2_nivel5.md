# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 17:25:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 44 | 1998.680 ms | 0.00% | 0.00% |
| Run 2 | 52 | 1332.720 ms | 0.00% | 0.00% |
| Run 3 | 0 | 0.000 ms | 0.00% | 0.00% |
| Run 4 | 50 | 1562.700 ms | 0.00% | 0.00% |
| Run 5 | 40 | 2149.690 ms | 0.00% | 0.00% |
| **PROMEDIO** | **37.2** | **1408.758 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |6.36% | 9.57% | 2.84% | 6.28% | 2.49% | **5.51%** |
| **exp-protegido-mongo-db-1** |96.67% | 109.14% | 124.92% | 74.13% | 82.02% | **97.38%** |
| **exp-protegido-ms-catalogo-1** |3.66% | 6.16% | 2.90% | 3.14% | 3.01% | **3.77%** |
| **exp-protegido-ms-ordenes-1** |3.69% | 8.41% | 5.50% | 3.19% | 3.54% | **4.87%** |
| **exp-protegido-ms-resenas-1** |172.01% | 204.56% | 123.49% | 277.78% | 162.95% | **188.16%** |
| **exp-protegido-ms-usuarios-1** |4.64% | 6.20% | 5.51% | 3.30% | 2.97% | **4.52%** |
| **exp-protegido-postgres-db-1** |24.61% | 22.38% | 15.35% | 26.82% | 19.22% | **21.68%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |94.99 MiB | 66.77 MiB | 66.54 MiB | 68.41 MiB | 68.00 MiB | **72.94 MiB** |
| **exp-protegido-mongo-db-1** |329.40 MiB | 352.40 MiB | 358.90 MiB | 278.50 MiB | 341.80 MiB | **332.20 MiB** |
| **exp-protegido-ms-catalogo-1** |75.35 MiB | 48.50 MiB | 49.51 MiB | 47.77 MiB | 49.51 MiB | **54.13 MiB** |
| **exp-protegido-ms-ordenes-1** |73.73 MiB | 49.16 MiB | 48.68 MiB | 48.08 MiB | 49.39 MiB | **53.81 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 256.00 MiB | 255.80 MiB | 255.90 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-protegido-ms-usuarios-1** |75.81 MiB | 48.84 MiB | 50.06 MiB | 47.27 MiB | 50.20 MiB | **54.44 MiB** |
| **exp-protegido-postgres-db-1** |65.41 MiB | 60.32 MiB | 61.32 MiB | 62.12 MiB | 60.91 MiB | **62.02 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.68% | 1.10% | 0.52% | 0.54% | 0.37% | **0.64%** |
| **exp-protegido-mongo-db-1** |96.67% | 109.14% | 124.92% | 74.13% | 82.02% | **97.38%** |
| **exp-protegido-ms-catalogo-1** |3.66% | 6.16% | 2.90% | 3.14% | 3.01% | **3.77%** |
| **exp-protegido-ms-ordenes-1** |3.69% | 8.41% | 5.50% | 3.19% | 3.54% | **4.87%** |
| **exp-protegido-ms-resenas-1** |172.01% | 204.56% | 123.49% | 277.78% | 162.95% | **188.16%** |
| **exp-protegido-ms-usuarios-1** |4.64% | 6.20% | 5.51% | 3.30% | 2.97% | **4.52%** |
| **exp-protegido-postgres-db-1** |24.61% | 22.38% | 15.35% | 26.82% | 19.22% | **21.68%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |68.59 MiB | 65.73 MiB | 66.16 MiB | 67.06 MiB | 67.25 MiB | **66.96 MiB** |
| **exp-protegido-mongo-db-1** |329.40 MiB | 352.40 MiB | 358.90 MiB | 278.50 MiB | 341.80 MiB | **332.20 MiB** |
| **exp-protegido-ms-catalogo-1** |75.35 MiB | 48.50 MiB | 49.51 MiB | 47.77 MiB | 49.51 MiB | **54.13 MiB** |
| **exp-protegido-ms-ordenes-1** |73.73 MiB | 49.16 MiB | 48.68 MiB | 48.08 MiB | 49.39 MiB | **53.81 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 256.00 MiB | 255.80 MiB | 255.90 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-protegido-ms-usuarios-1** |75.81 MiB | 48.84 MiB | 50.06 MiB | 47.27 MiB | 50.20 MiB | **54.44 MiB** |
| **exp-protegido-postgres-db-1** |65.41 MiB | 60.32 MiB | 61.32 MiB | 62.12 MiB | 60.91 MiB | **62.02 MiB** |
