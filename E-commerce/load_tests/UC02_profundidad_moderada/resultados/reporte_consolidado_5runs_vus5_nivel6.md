# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 00:01:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 158 | 900.050 ms | 0.00% | 0.00% |
| Run 2 | 90 | 2374.260 ms | 0.00% | 0.00% |
| Run 3 | 55 | 979.210 ms | 0.00% | 0.00% |
| Run 4 | 111 | 1829.780 ms | 0.00% | 0.00% |
| Run 5 | 110 | 1922.020 ms | 0.00% | 0.00% |
| **PROMEDIO** | **104.8** | **1601.064 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |7.99% | 3.78% | 4.84% | 6.32% | 6.84% | **5.95%** |
| **exp-vulnerable-mongo-db-1** |88.61% | 103.74% | 67.22% | 76.42% | 105.33% | **88.26%** |
| **exp-vulnerable-ms-catalogo-1** |5.28% | 5.04% | 4.54% | 4.41% | 6.06% | **5.07%** |
| **exp-vulnerable-ms-ordenes-1** |4.82% | 4.27% | 4.44% | 5.55% | 4.83% | **4.78%** |
| **exp-vulnerable-ms-resenas-1** |261.79% | 239.07% | 196.02% | 234.06% | 230.57% | **232.30%** |
| **exp-vulnerable-ms-usuarios-1** |4.38% | 4.38% | 8.42% | 5.77% | 4.54% | **5.50%** |
| **exp-vulnerable-postgres-db-1** |60.33% | 60.91% | 65.55% | 32.06% | 57.72% | **55.31%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |107.70 MiB | 68.69 MiB | 67.08 MiB | 69.45 MiB | 69.68 MiB | **76.52 MiB** |
| **exp-vulnerable-mongo-db-1** |446.70 MiB | 334.70 MiB | 294.80 MiB | 342.80 MiB | 350.50 MiB | **353.90 MiB** |
| **exp-vulnerable-ms-catalogo-1** |93.02 MiB | 46.43 MiB | 46.16 MiB | 45.79 MiB | 45.63 MiB | **55.41 MiB** |
| **exp-vulnerable-ms-ordenes-1** |108.80 MiB | 46.52 MiB | 45.70 MiB | 46.30 MiB | 46.90 MiB | **58.84 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.70 MiB | 256.00 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |116.30 MiB | 48.32 MiB | 45.90 MiB | 45.91 MiB | 47.07 MiB | **60.70 MiB** |
| **exp-vulnerable-postgres-db-1** |84.25 MiB | 73.23 MiB | 74.62 MiB | 77.68 MiB | 68.68 MiB | **75.69 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.97% | 0.83% | 1.51% | 1.13% | 1.04% | **1.30%** |
| **exp-vulnerable-mongo-db-1** |88.61% | 103.74% | 67.22% | 76.42% | 105.33% | **88.26%** |
| **exp-vulnerable-ms-catalogo-1** |5.28% | 5.04% | 4.54% | 4.41% | 6.06% | **5.07%** |
| **exp-vulnerable-ms-ordenes-1** |4.82% | 4.27% | 4.44% | 5.55% | 4.83% | **4.78%** |
| **exp-vulnerable-ms-resenas-1** |261.79% | 239.07% | 196.02% | 234.06% | 230.57% | **232.30%** |
| **exp-vulnerable-ms-usuarios-1** |4.38% | 4.38% | 8.42% | 5.77% | 4.54% | **5.50%** |
| **exp-vulnerable-postgres-db-1** |60.33% | 60.91% | 65.55% | 32.06% | 57.72% | **55.31%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |84.82 MiB | 66.47 MiB | 66.04 MiB | 67.40 MiB | 66.84 MiB | **70.31 MiB** |
| **exp-vulnerable-mongo-db-1** |446.70 MiB | 334.70 MiB | 294.80 MiB | 342.80 MiB | 350.50 MiB | **353.90 MiB** |
| **exp-vulnerable-ms-catalogo-1** |93.02 MiB | 46.43 MiB | 46.16 MiB | 45.79 MiB | 45.63 MiB | **55.41 MiB** |
| **exp-vulnerable-ms-ordenes-1** |108.80 MiB | 46.52 MiB | 45.70 MiB | 46.30 MiB | 46.90 MiB | **58.84 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.70 MiB | 256.00 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |116.30 MiB | 48.32 MiB | 45.90 MiB | 45.91 MiB | 47.07 MiB | **60.70 MiB** |
| **exp-vulnerable-postgres-db-1** |84.25 MiB | 73.23 MiB | 74.62 MiB | 77.68 MiB | 68.68 MiB | **75.69 MiB** |
