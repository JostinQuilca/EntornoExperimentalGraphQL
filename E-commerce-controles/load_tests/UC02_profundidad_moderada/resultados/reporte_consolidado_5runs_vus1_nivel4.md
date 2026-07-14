# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 12:14:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 29 | 1298.520 ms | 0.00% | 0.00% |
| Run 2 | 20 | 2134.580 ms | 5.00% | 0.00% |
| Run 3 | 23 | 1619.400 ms | 0.00% | 0.00% |
| Run 4 | 25 | 1509.230 ms | 0.00% | 0.00% |
| Run 5 | 21 | 1878.570 ms | 0.00% | 0.00% |
| **PROMEDIO** | **23.6** | **1688.060 ms** | **1.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |12.67% | 1.28% | 0.74% | 2.13% | 1.04% | **3.57%** |
| **exp-protegido-mongo-db-1** |96.10% | 74.41% | 62.32% | 82.21% | 77.07% | **78.42%** |
| **exp-protegido-ms-catalogo-1** |4.55% | 3.59% | 3.42% | 4.56% | 4.90% | **4.20%** |
| **exp-protegido-ms-ordenes-1** |3.99% | 5.28% | 4.43% | 3.62% | 3.96% | **4.26%** |
| **exp-protegido-ms-resenas-1** |198.82% | 203.91% | 183.93% | 194.23% | 190.85% | **194.35%** |
| **exp-protegido-ms-usuarios-1** |8.38% | 4.45% | 3.34% | 3.73% | 4.01% | **4.78%** |
| **exp-protegido-postgres-db-1** |19.40% | 15.09% | 13.61% | 16.42% | 10.92% | **15.09%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.72 MiB | 65.02 MiB | 65.91 MiB | 65.95 MiB | 65.32 MiB | **65.58 MiB** |
| **exp-protegido-mongo-db-1** |342.90 MiB | 339.30 MiB | 340.10 MiB | 349.10 MiB | 341.00 MiB | **342.48 MiB** |
| **exp-protegido-ms-catalogo-1** |47.48 MiB | 46.93 MiB | 46.28 MiB | 46.35 MiB | 45.98 MiB | **46.60 MiB** |
| **exp-protegido-ms-ordenes-1** |46.12 MiB | 46.23 MiB | 45.81 MiB | 45.68 MiB | 47.38 MiB | **46.24 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 256.00 MiB | 256.00 MiB | 255.80 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-protegido-ms-usuarios-1** |45.90 MiB | 45.91 MiB | 46.04 MiB | 47.11 MiB | 47.44 MiB | **46.48 MiB** |
| **exp-protegido-postgres-db-1** |56.80 MiB | 59.48 MiB | 59.22 MiB | 57.04 MiB | 56.76 MiB | **57.86 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.77% | 0.29% | 0.25% | 0.38% | 0.29% | **0.40%** |
| **exp-protegido-mongo-db-1** |96.10% | 74.41% | 62.32% | 82.21% | 77.07% | **78.42%** |
| **exp-protegido-ms-catalogo-1** |4.55% | 3.59% | 3.42% | 4.56% | 4.90% | **4.20%** |
| **exp-protegido-ms-ordenes-1** |3.99% | 5.28% | 4.43% | 3.62% | 3.96% | **4.26%** |
| **exp-protegido-ms-resenas-1** |198.82% | 203.91% | 183.93% | 194.23% | 190.85% | **194.35%** |
| **exp-protegido-ms-usuarios-1** |8.38% | 4.45% | 3.34% | 3.73% | 4.01% | **4.78%** |
| **exp-protegido-postgres-db-1** |19.40% | 15.09% | 13.61% | 16.42% | 10.92% | **15.09%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.02 MiB | 64.58 MiB | 65.22 MiB | 65.26 MiB | 64.74 MiB | **64.96 MiB** |
| **exp-protegido-mongo-db-1** |342.90 MiB | 339.30 MiB | 340.10 MiB | 349.10 MiB | 341.00 MiB | **342.48 MiB** |
| **exp-protegido-ms-catalogo-1** |47.48 MiB | 46.93 MiB | 46.28 MiB | 46.35 MiB | 45.98 MiB | **46.60 MiB** |
| **exp-protegido-ms-ordenes-1** |46.12 MiB | 46.23 MiB | 45.81 MiB | 45.68 MiB | 47.38 MiB | **46.24 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 256.00 MiB | 256.00 MiB | 255.80 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-protegido-ms-usuarios-1** |45.90 MiB | 45.91 MiB | 46.04 MiB | 47.11 MiB | 47.44 MiB | **46.48 MiB** |
| **exp-protegido-postgres-db-1** |56.80 MiB | 59.48 MiB | 59.22 MiB | 57.04 MiB | 56.76 MiB | **57.86 MiB** |
