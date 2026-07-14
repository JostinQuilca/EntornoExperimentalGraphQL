# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 10:48:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 180 | 7.180 ms | 0.00% | 100.00% |
| Run 2 | 180 | 6.790 ms | 0.00% | 100.00% |
| Run 3 | 180 | 6.760 ms | 0.00% | 100.00% |
| Run 4 | 180 | 6.870 ms | 0.00% | 100.00% |
| Run 5 | 180 | 7.610 ms | 0.00% | 100.00% |
| **PROMEDIO** | **180.0** | **7.042 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |8.55% | 4.59% | 4.74% | 3.96% | 3.30% | **5.03%** |
| **exp-protegido-mongo-db-1** |57.68% | 51.67% | 57.19% | 64.01% | 54.47% | **57.00%** |
| **exp-protegido-ms-catalogo-1** |4.59% | 3.30% | 3.32% | 3.81% | 4.72% | **3.95%** |
| **exp-protegido-ms-ordenes-1** |4.65% | 3.66% | 3.13% | 3.08% | 4.29% | **3.76%** |
| **exp-protegido-ms-resenas-1** |3.12% | 3.41% | 3.85% | 3.00% | 4.18% | **3.51%** |
| **exp-protegido-ms-usuarios-1** |4.44% | 3.62% | 3.23% | 3.23% | 4.33% | **3.77%** |
| **exp-protegido-postgres-db-1** |5.42% | 4.36% | 4.64% | 5.03% | 4.33% | **4.76%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |96.52 MiB | 74.73 MiB | 72.94 MiB | 73.44 MiB | 74.85 MiB | **78.50 MiB** |
| **exp-protegido-mongo-db-1** |332.20 MiB | 327.00 MiB | 334.00 MiB | 342.50 MiB | 340.40 MiB | **335.22 MiB** |
| **exp-protegido-ms-catalogo-1** |46.85 MiB | 46.28 MiB | 45.52 MiB | 45.59 MiB | 45.64 MiB | **45.98 MiB** |
| **exp-protegido-ms-ordenes-1** |48.11 MiB | 46.41 MiB | 45.60 MiB | 45.75 MiB | 45.96 MiB | **46.37 MiB** |
| **exp-protegido-ms-resenas-1** |46.44 MiB | 47.44 MiB | 47.24 MiB | 45.41 MiB | 55.05 MiB | **48.32 MiB** |
| **exp-protegido-ms-usuarios-1** |45.86 MiB | 46.97 MiB | 45.13 MiB | 46.70 MiB | 47.32 MiB | **46.40 MiB** |
| **exp-protegido-postgres-db-1** |27.38 MiB | 27.43 MiB | 27.83 MiB | 27.38 MiB | 27.40 MiB | **27.48 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.07% | 1.57% | 1.64% | 1.60% | 1.57% | **1.69%** |
| **exp-protegido-mongo-db-1** |57.68% | 51.67% | 57.19% | 64.01% | 54.47% | **57.00%** |
| **exp-protegido-ms-catalogo-1** |4.59% | 3.30% | 3.32% | 3.81% | 4.72% | **3.95%** |
| **exp-protegido-ms-ordenes-1** |4.65% | 3.66% | 3.13% | 3.08% | 4.29% | **3.76%** |
| **exp-protegido-ms-resenas-1** |3.12% | 3.41% | 3.85% | 3.00% | 4.18% | **3.51%** |
| **exp-protegido-ms-usuarios-1** |4.44% | 3.62% | 3.23% | 3.23% | 4.33% | **3.77%** |
| **exp-protegido-postgres-db-1** |5.42% | 4.36% | 4.64% | 5.03% | 4.33% | **4.76%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |72.47 MiB | 69.65 MiB | 68.34 MiB | 68.62 MiB | 69.24 MiB | **69.66 MiB** |
| **exp-protegido-mongo-db-1** |332.20 MiB | 327.00 MiB | 334.00 MiB | 342.50 MiB | 340.40 MiB | **335.22 MiB** |
| **exp-protegido-ms-catalogo-1** |46.85 MiB | 46.28 MiB | 45.52 MiB | 45.59 MiB | 45.64 MiB | **45.98 MiB** |
| **exp-protegido-ms-ordenes-1** |48.11 MiB | 46.41 MiB | 45.60 MiB | 45.75 MiB | 45.96 MiB | **46.37 MiB** |
| **exp-protegido-ms-resenas-1** |46.44 MiB | 47.44 MiB | 47.24 MiB | 45.41 MiB | 55.05 MiB | **48.32 MiB** |
| **exp-protegido-ms-usuarios-1** |45.86 MiB | 46.97 MiB | 45.13 MiB | 46.70 MiB | 47.32 MiB | **46.40 MiB** |
| **exp-protegido-postgres-db-1** |27.38 MiB | 27.43 MiB | 27.83 MiB | 27.38 MiB | 27.40 MiB | **27.48 MiB** |
