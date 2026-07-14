# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 11:34:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 100 | 2147.950 ms | 5.00% | 0.00% |
| Run 2 | 120 | 2112.750 ms | 8.33% | 0.00% |
| Run 3 | 89 | 2489.280 ms | 5.61% | 0.00% |
| Run 4 | 87 | 2559.010 ms | 0.00% | 0.00% |
| Run 5 | 134 | 1778.470 ms | 3.73% | 0.00% |
| **PROMEDIO** | **106.0** | **2217.492 ms** | **4.53%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |12.43% | 16.91% | 3.40% | 3.86% | 6.34% | **8.59%** |
| **exp-vulnerable-mongo-db-1** |89.75% | 104.01% | 105.40% | 102.99% | 123.20% | **105.07%** |
| **exp-vulnerable-ms-catalogo-1** |4.80% | 5.32% | 7.91% | 6.08% | 4.35% | **5.69%** |
| **exp-vulnerable-ms-ordenes-1** |6.63% | 4.99% | 6.87% | 4.46% | 6.81% | **5.95%** |
| **exp-vulnerable-ms-resenas-1** |225.01% | 219.99% | 240.37% | 216.15% | 224.20% | **225.14%** |
| **exp-vulnerable-ms-usuarios-1** |6.59% | 5.35% | 7.75% | 7.89% | 6.40% | **6.80%** |
| **exp-vulnerable-postgres-db-1** |48.19% | 70.77% | 49.10% | 34.42% | 46.47% | **49.79%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |97.68 MiB | 69.93 MiB | 68.41 MiB | 68.16 MiB | 69.84 MiB | **74.80 MiB** |
| **exp-vulnerable-mongo-db-1** |333.90 MiB | 350.60 MiB | 344.30 MiB | 338.80 MiB | 349.20 MiB | **343.36 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.13 MiB | 46.34 MiB | 47.52 MiB | 46.33 MiB | 45.61 MiB | **46.39 MiB** |
| **exp-vulnerable-ms-ordenes-1** |49.52 MiB | 45.79 MiB | 48.82 MiB | 46.11 MiB | 47.18 MiB | **47.48 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.66 MiB | 47.43 MiB | 54.99 MiB | 46.36 MiB | 46.07 MiB | **48.70 MiB** |
| **exp-vulnerable-postgres-db-1** |75.98 MiB | 71.23 MiB | 76.43 MiB | 70.39 MiB | 74.75 MiB | **73.76 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.66% | 1.56% | 0.82% | 0.88% | 1.29% | **1.24%** |
| **exp-vulnerable-mongo-db-1** |89.75% | 104.01% | 105.40% | 102.99% | 123.20% | **105.07%** |
| **exp-vulnerable-ms-catalogo-1** |4.80% | 5.32% | 7.91% | 6.08% | 4.35% | **5.69%** |
| **exp-vulnerable-ms-ordenes-1** |6.63% | 4.99% | 6.87% | 4.46% | 6.81% | **5.95%** |
| **exp-vulnerable-ms-resenas-1** |225.01% | 219.99% | 240.37% | 216.15% | 224.20% | **225.14%** |
| **exp-vulnerable-ms-usuarios-1** |6.59% | 5.35% | 7.75% | 7.89% | 6.40% | **6.80%** |
| **exp-vulnerable-postgres-db-1** |48.19% | 70.77% | 49.10% | 34.42% | 46.47% | **49.79%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |70.13 MiB | 67.97 MiB | 65.82 MiB | 66.21 MiB | 67.77 MiB | **67.58 MiB** |
| **exp-vulnerable-mongo-db-1** |333.90 MiB | 350.60 MiB | 344.30 MiB | 338.80 MiB | 349.20 MiB | **343.36 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.13 MiB | 46.34 MiB | 47.52 MiB | 46.33 MiB | 45.61 MiB | **46.39 MiB** |
| **exp-vulnerable-ms-ordenes-1** |49.52 MiB | 45.79 MiB | 48.82 MiB | 46.11 MiB | 47.18 MiB | **47.48 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.66 MiB | 47.43 MiB | 54.99 MiB | 46.36 MiB | 46.07 MiB | **48.70 MiB** |
| **exp-vulnerable-postgres-db-1** |75.98 MiB | 71.23 MiB | 76.43 MiB | 70.39 MiB | 74.75 MiB | **73.76 MiB** |
