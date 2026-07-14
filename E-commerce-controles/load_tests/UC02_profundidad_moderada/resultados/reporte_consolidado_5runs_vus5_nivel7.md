# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 11:13:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 300 | 6.390 ms | 0.00% | 100.00% |
| Run 2 | 300 | 7.130 ms | 0.00% | 100.00% |
| Run 3 | 300 | 7.430 ms | 0.00% | 100.00% |
| Run 4 | 300 | 7.040 ms | 0.00% | 100.00% |
| Run 5 | 300 | 7.110 ms | 0.00% | 100.00% |
| **PROMEDIO** | **300.0** | **7.020 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |8.16% | 4.64% | 5.57% | 8.35% | 12.00% | **7.74%** |
| **exp-protegido-mongo-db-1** |57.46% | 55.39% | 61.58% | 54.00% | 56.48% | **56.98%** |
| **exp-protegido-ms-catalogo-1** |4.04% | 3.87% | 4.09% | 4.75% | 3.78% | **4.11%** |
| **exp-protegido-ms-ordenes-1** |4.09% | 2.96% | 3.22% | 3.19% | 4.39% | **3.57%** |
| **exp-protegido-ms-resenas-1** |4.21% | 3.56% | 4.12% | 3.40% | 5.21% | **4.10%** |
| **exp-protegido-ms-usuarios-1** |3.19% | 2.85% | 3.27% | 3.81% | 4.21% | **3.47%** |
| **exp-protegido-postgres-db-1** |5.22% | 4.42% | 3.76% | 4.03% | 4.99% | **4.48%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |75.66 MiB | 74.58 MiB | 73.88 MiB | 75.33 MiB | 76.36 MiB | **75.16 MiB** |
| **exp-protegido-mongo-db-1** |341.90 MiB | 330.70 MiB | 342.80 MiB | 339.30 MiB | 339.80 MiB | **338.90 MiB** |
| **exp-protegido-ms-catalogo-1** |46.77 MiB | 46.00 MiB | 46.40 MiB | 47.33 MiB | 45.97 MiB | **46.49 MiB** |
| **exp-protegido-ms-ordenes-1** |46.13 MiB | 45.67 MiB | 46.77 MiB | 46.36 MiB | 47.94 MiB | **46.57 MiB** |
| **exp-protegido-ms-resenas-1** |45.75 MiB | 47.73 MiB | 45.64 MiB | 45.58 MiB | 46.74 MiB | **46.29 MiB** |
| **exp-protegido-ms-usuarios-1** |45.51 MiB | 46.05 MiB | 46.16 MiB | 45.32 MiB | 48.46 MiB | **46.30 MiB** |
| **exp-protegido-postgres-db-1** |29.14 MiB | 27.42 MiB | 28.10 MiB | 27.41 MiB | 27.56 MiB | **27.93 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.48% | 2.67% | 2.52% | 2.95% | 3.00% | **2.72%** |
| **exp-protegido-mongo-db-1** |57.46% | 55.39% | 61.58% | 54.00% | 56.48% | **56.98%** |
| **exp-protegido-ms-catalogo-1** |4.04% | 3.87% | 4.09% | 4.75% | 3.78% | **4.11%** |
| **exp-protegido-ms-ordenes-1** |4.09% | 2.96% | 3.22% | 3.19% | 4.39% | **3.57%** |
| **exp-protegido-ms-resenas-1** |4.21% | 3.56% | 4.12% | 3.40% | 5.21% | **4.10%** |
| **exp-protegido-ms-usuarios-1** |3.19% | 2.85% | 3.27% | 3.81% | 4.21% | **3.47%** |
| **exp-protegido-postgres-db-1** |5.22% | 4.42% | 3.76% | 4.03% | 4.99% | **4.48%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |71.50 MiB | 70.85 MiB | 69.75 MiB | 71.51 MiB | 71.56 MiB | **71.03 MiB** |
| **exp-protegido-mongo-db-1** |341.90 MiB | 330.70 MiB | 342.80 MiB | 339.30 MiB | 339.80 MiB | **338.90 MiB** |
| **exp-protegido-ms-catalogo-1** |46.77 MiB | 46.00 MiB | 46.40 MiB | 47.33 MiB | 45.97 MiB | **46.49 MiB** |
| **exp-protegido-ms-ordenes-1** |46.13 MiB | 45.67 MiB | 46.77 MiB | 46.36 MiB | 47.94 MiB | **46.57 MiB** |
| **exp-protegido-ms-resenas-1** |45.75 MiB | 47.73 MiB | 45.64 MiB | 45.58 MiB | 46.74 MiB | **46.29 MiB** |
| **exp-protegido-ms-usuarios-1** |45.51 MiB | 46.05 MiB | 46.16 MiB | 45.32 MiB | 48.46 MiB | **46.30 MiB** |
| **exp-protegido-postgres-db-1** |29.14 MiB | 27.42 MiB | 28.10 MiB | 27.41 MiB | 27.56 MiB | **27.93 MiB** |
