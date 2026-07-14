# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 08:52:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 60 | 7.630 ms | 0.00% | 100.00% |
| Run 2 | 60 | 7.530 ms | 0.00% | 100.00% |
| Run 3 | 60 | 7.390 ms | 0.00% | 100.00% |
| Run 4 | 60 | 6.760 ms | 0.00% | 100.00% |
| Run 5 | 0 | 0.000 ms | 0.00% | 0.00% |
| **PROMEDIO** | **48.0** | **5.862 ms** | **0.00%** | **80.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.95% | 1.71% | 2.75% | 2.04% | 0.91% | **1.87%** |
| **exp-protegido-mongo-db-1** |74.12% | 68.50% | 74.64% | 72.65% | 42.87% | **66.56%** |
| **exp-protegido-ms-catalogo-1** |4.91% | 5.49% | 4.38% | 4.28% | 2.56% | **4.32%** |
| **exp-protegido-ms-ordenes-1** |3.97% | 3.66% | 4.09% | 5.44% | 2.72% | **3.98%** |
| **exp-protegido-ms-resenas-1** |4.26% | 4.06% | 4.10% | 3.22% | 2.50% | **3.63%** |
| **exp-protegido-ms-usuarios-1** |3.70% | 4.15% | 4.29% | 5.41% | 2.76% | **4.06%** |
| **exp-protegido-postgres-db-1** |5.94% | 7.45% | 4.42% | 4.87% | 3.17% | **5.17%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |64.29 MiB | 65.70 MiB | 64.53 MiB | 65.22 MiB | 64.35 MiB | **64.82 MiB** |
| **exp-protegido-mongo-db-1** |332.20 MiB | 340.80 MiB | 343.00 MiB | 345.60 MiB | 332.50 MiB | **338.82 MiB** |
| **exp-protegido-ms-catalogo-1** |46.18 MiB | 46.70 MiB | 45.84 MiB | 47.64 MiB | 46.19 MiB | **46.51 MiB** |
| **exp-protegido-ms-ordenes-1** |47.32 MiB | 46.15 MiB | 47.00 MiB | 47.41 MiB | 46.72 MiB | **46.92 MiB** |
| **exp-protegido-ms-resenas-1** |46.95 MiB | 46.61 MiB | 46.70 MiB | 45.82 MiB | 45.96 MiB | **46.41 MiB** |
| **exp-protegido-ms-usuarios-1** |46.55 MiB | 46.07 MiB | 46.60 MiB | 47.77 MiB | 45.25 MiB | **46.45 MiB** |
| **exp-protegido-postgres-db-1** |29.53 MiB | 27.70 MiB | 27.48 MiB | 27.37 MiB | 27.34 MiB | **27.88 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.52% | 0.53% | 0.57% | 0.59% | 0.39% | **0.52%** |
| **exp-protegido-mongo-db-1** |74.12% | 68.50% | 74.64% | 72.65% | 42.87% | **66.56%** |
| **exp-protegido-ms-catalogo-1** |4.91% | 5.49% | 4.38% | 4.28% | 2.56% | **4.32%** |
| **exp-protegido-ms-ordenes-1** |3.97% | 3.66% | 4.09% | 5.44% | 2.72% | **3.98%** |
| **exp-protegido-ms-resenas-1** |4.26% | 4.06% | 4.10% | 3.22% | 2.50% | **3.63%** |
| **exp-protegido-ms-usuarios-1** |3.70% | 4.15% | 4.29% | 5.41% | 2.76% | **4.06%** |
| **exp-protegido-postgres-db-1** |5.94% | 7.45% | 4.42% | 4.87% | 3.17% | **5.17%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |63.38 MiB | 64.72 MiB | 63.66 MiB | 64.60 MiB | 64.01 MiB | **64.07 MiB** |
| **exp-protegido-mongo-db-1** |332.20 MiB | 340.80 MiB | 343.00 MiB | 345.60 MiB | 332.50 MiB | **338.82 MiB** |
| **exp-protegido-ms-catalogo-1** |46.18 MiB | 46.70 MiB | 45.84 MiB | 47.64 MiB | 46.19 MiB | **46.51 MiB** |
| **exp-protegido-ms-ordenes-1** |47.32 MiB | 46.15 MiB | 47.00 MiB | 47.41 MiB | 46.72 MiB | **46.92 MiB** |
| **exp-protegido-ms-resenas-1** |46.95 MiB | 46.61 MiB | 46.70 MiB | 45.82 MiB | 45.96 MiB | **46.41 MiB** |
| **exp-protegido-ms-usuarios-1** |46.55 MiB | 46.07 MiB | 46.60 MiB | 47.77 MiB | 45.25 MiB | **46.45 MiB** |
| **exp-protegido-postgres-db-1** |29.53 MiB | 27.70 MiB | 27.48 MiB | 27.37 MiB | 27.34 MiB | **27.88 MiB** |
