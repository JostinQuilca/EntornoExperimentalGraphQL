# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 10:27:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 52 | 165.680 ms | 0.00% | 0.00% |
| Run 2 | 27 | 1236.420 ms | 0.00% | 0.00% |
| Run 3 | 25 | 1641.690 ms | 0.00% | 0.00% |
| Run 4 | 23 | 1877.300 ms | 0.00% | 0.00% |
| Run 5 | 32 | 888.970 ms | 0.00% | 0.00% |
| **PROMEDIO** | **31.8** | **1162.012 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |5.64% | 16.17% | 2.46% | 3.26% | 5.02% | **6.51%** |
| **exp-vulnerable-mongo-db-1** |71.83% | 93.09% | 101.95% | 110.96% | 115.94% | **98.75%** |
| **exp-vulnerable-ms-catalogo-1** |5.09% | 4.63% | 6.72% | 5.28% | 9.53% | **6.25%** |
| **exp-vulnerable-ms-ordenes-1** |5.97% | 5.91% | 3.44% | 5.16% | 8.03% | **5.70%** |
| **exp-vulnerable-ms-resenas-1** |186.02% | 207.53% | 210.07% | 197.79% | 224.78% | **205.24%** |
| **exp-vulnerable-ms-usuarios-1** |4.11% | 6.76% | 3.59% | 5.12% | 10.85% | **6.09%** |
| **exp-vulnerable-postgres-db-1** |11.01% | 16.94% | 20.05% | 12.86% | 25.49% | **17.27%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.39 MiB | 64.65 MiB | 64.87 MiB | 64.80 MiB | 65.41 MiB | **71.22 MiB** |
| **exp-vulnerable-mongo-db-1** |341.90 MiB | 348.50 MiB | 345.40 MiB | 353.30 MiB | 349.90 MiB | **347.80 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.68 MiB | 45.29 MiB | 46.00 MiB | 45.85 MiB | 46.14 MiB | **45.79 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.36 MiB | 46.26 MiB | 45.24 MiB | 46.09 MiB | 45.51 MiB | **46.09 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.24 MiB | 46.35 MiB | 46.06 MiB | 46.51 MiB | 47.02 MiB | **46.84 MiB** |
| **exp-vulnerable-postgres-db-1** |56.77 MiB | 59.00 MiB | 58.53 MiB | 58.32 MiB | 56.74 MiB | **57.87 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.95% | 1.11% | 0.52% | 0.45% | 0.90% | **0.79%** |
| **exp-vulnerable-mongo-db-1** |71.83% | 93.09% | 101.95% | 110.96% | 115.94% | **98.75%** |
| **exp-vulnerable-ms-catalogo-1** |5.09% | 4.63% | 6.72% | 5.28% | 9.53% | **6.25%** |
| **exp-vulnerable-ms-ordenes-1** |5.97% | 5.91% | 3.44% | 5.16% | 8.03% | **5.70%** |
| **exp-vulnerable-ms-resenas-1** |186.02% | 207.53% | 210.07% | 197.79% | 224.78% | **205.24%** |
| **exp-vulnerable-ms-usuarios-1** |4.11% | 6.76% | 3.59% | 5.12% | 10.85% | **6.09%** |
| **exp-vulnerable-postgres-db-1** |11.01% | 16.94% | 20.05% | 12.86% | 25.49% | **17.27%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.26 MiB | 64.03 MiB | 64.19 MiB | 64.01 MiB | 64.37 MiB | **64.77 MiB** |
| **exp-vulnerable-mongo-db-1** |341.90 MiB | 348.50 MiB | 345.40 MiB | 353.30 MiB | 349.90 MiB | **347.80 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.68 MiB | 45.29 MiB | 46.00 MiB | 45.85 MiB | 46.14 MiB | **45.79 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.36 MiB | 46.26 MiB | 45.24 MiB | 46.09 MiB | 45.51 MiB | **46.09 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.24 MiB | 46.35 MiB | 46.06 MiB | 46.51 MiB | 47.02 MiB | **46.84 MiB** |
| **exp-vulnerable-postgres-db-1** |56.77 MiB | 59.00 MiB | 58.53 MiB | 58.32 MiB | 56.74 MiB | **57.87 MiB** |
