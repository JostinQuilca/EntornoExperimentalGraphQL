# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 10:59:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 105 | 1914.310 ms | 0.00% | 0.00% |
| Run 2 | 100 | 2295.880 ms | 0.00% | 0.00% |
| Run 3 | 95 | 2375.210 ms | 10.52% | 0.00% |
| Run 4 | 115 | 1637.160 ms | 0.00% | 0.00% |
| Run 5 | 95 | 2192.830 ms | 0.00% | 0.00% |
| **PROMEDIO** | **102.0** | **2083.078 ms** | **2.10%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |7.10% | 8.08% | 7.07% | 7.86% | 5.15% | **7.05%** |
| **exp-vulnerable-mongo-db-1** |98.55% | 97.56% | 98.87% | 103.68% | 72.78% | **94.29%** |
| **exp-vulnerable-ms-catalogo-1** |3.26% | 5.25% | 5.45% | 4.12% | 4.26% | **4.47%** |
| **exp-vulnerable-ms-ordenes-1** |4.23% | 5.09% | 4.03% | 5.22% | 3.08% | **4.33%** |
| **exp-vulnerable-ms-resenas-1** |211.93% | 261.24% | 238.88% | 262.47% | 196.19% | **234.14%** |
| **exp-vulnerable-ms-usuarios-1** |4.24% | 5.82% | 4.40% | 4.90% | 3.45% | **4.56%** |
| **exp-vulnerable-postgres-db-1** |40.94% | 35.24% | 44.61% | 40.36% | 42.62% | **40.75%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |68.75 MiB | 68.44 MiB | 69.09 MiB | 69.39 MiB | 69.12 MiB | **68.96 MiB** |
| **exp-vulnerable-mongo-db-1** |341.60 MiB | 351.00 MiB | 348.40 MiB | 346.00 MiB | 332.30 MiB | **343.86 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.58 MiB | 46.22 MiB | 45.49 MiB | 47.03 MiB | 45.81 MiB | **46.03 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.27 MiB | 46.56 MiB | 47.71 MiB | 54.13 MiB | 48.60 MiB | **48.65 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | **255.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.39 MiB | 54.38 MiB | 46.02 MiB | 54.03 MiB | 47.38 MiB | **49.64 MiB** |
| **exp-vulnerable-postgres-db-1** |73.91 MiB | 72.52 MiB | 74.23 MiB | 71.14 MiB | 63.61 MiB | **71.08 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.13% | 1.12% | 1.04% | 1.37% | 1.15% | **1.16%** |
| **exp-vulnerable-mongo-db-1** |98.55% | 97.56% | 98.87% | 103.68% | 72.78% | **94.29%** |
| **exp-vulnerable-ms-catalogo-1** |3.26% | 5.25% | 5.45% | 4.12% | 4.26% | **4.47%** |
| **exp-vulnerable-ms-ordenes-1** |4.23% | 5.09% | 4.03% | 5.22% | 3.08% | **4.33%** |
| **exp-vulnerable-ms-resenas-1** |211.93% | 261.24% | 238.88% | 262.47% | 196.19% | **234.14%** |
| **exp-vulnerable-ms-usuarios-1** |4.24% | 5.82% | 4.40% | 4.90% | 3.45% | **4.56%** |
| **exp-vulnerable-postgres-db-1** |40.94% | 35.24% | 44.61% | 40.36% | 42.62% | **40.75%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |66.69 MiB | 65.51 MiB | 67.11 MiB | 67.41 MiB | 67.23 MiB | **66.79 MiB** |
| **exp-vulnerable-mongo-db-1** |341.60 MiB | 351.00 MiB | 348.40 MiB | 346.00 MiB | 332.30 MiB | **343.86 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.58 MiB | 46.22 MiB | 45.49 MiB | 47.03 MiB | 45.81 MiB | **46.03 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.27 MiB | 46.56 MiB | 47.71 MiB | 54.13 MiB | 48.60 MiB | **48.65 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | **255.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.39 MiB | 54.38 MiB | 46.02 MiB | 54.03 MiB | 47.38 MiB | **49.64 MiB** |
| **exp-vulnerable-postgres-db-1** |73.91 MiB | 72.52 MiB | 74.23 MiB | 71.14 MiB | 63.61 MiB | **71.08 MiB** |
