# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 16:18:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 152 | 2244.960 ms | 10.52% | 0.00% |
| Run 2 | 168 | 1986.900 ms | 4.76% | 0.00% |
| Run 3 | 144 | 3063.620 ms | 5.55% | 0.00% |
| Run 4 | 166 | 2202.190 ms | 4.81% | 0.00% |
| Run 5 | 128 | 2938.580 ms | 6.25% | 0.00% |
| **PROMEDIO** | **151.6** | **2487.250 ms** | **6.38%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |14.99% | 20.49% | 9.76% | 13.19% | 22.08% | **16.10%** |
| **exp-vulnerable-mongo-db-1** |94.07% | 102.15% | 93.07% | 113.26% | 96.79% | **99.87%** |
| **exp-vulnerable-ms-catalogo-1** |7.24% | 6.85% | 3.89% | 7.34% | 7.20% | **6.50%** |
| **exp-vulnerable-ms-ordenes-1** |6.39% | 9.40% | 3.91% | 8.27% | 8.38% | **7.27%** |
| **exp-vulnerable-ms-resenas-1** |160.38% | 151.72% | 136.32% | 199.05% | 201.39% | **169.77%** |
| **exp-vulnerable-ms-usuarios-1** |5.52% | 6.86% | 3.30% | 6.96% | 6.68% | **5.86%** |
| **exp-vulnerable-postgres-db-1** |54.42% | 65.97% | 34.74% | 56.89% | 93.24% | **61.05%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |72.94 MiB | 72.80 MiB | 71.14 MiB | 71.64 MiB | 71.50 MiB | **72.00 MiB** |
| **exp-vulnerable-mongo-db-1** |346.30 MiB | 345.90 MiB | 336.40 MiB | 342.70 MiB | 336.00 MiB | **341.46 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.76 MiB | 46.17 MiB | 45.86 MiB | 46.02 MiB | 47.26 MiB | **46.21 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.80 MiB | 45.75 MiB | 46.02 MiB | 46.65 MiB | 46.61 MiB | **46.37 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.01 MiB | 45.40 MiB | 45.93 MiB | 46.01 MiB | 46.04 MiB | **46.08 MiB** |
| **exp-vulnerable-postgres-db-1** |78.60 MiB | 80.29 MiB | 76.47 MiB | 75.98 MiB | 79.09 MiB | **78.09 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |2.56% | 3.16% | 1.25% | 2.37% | 3.02% | **2.47%** |
| **exp-vulnerable-mongo-db-1** |94.07% | 102.15% | 93.07% | 113.26% | 96.79% | **99.87%** |
| **exp-vulnerable-ms-catalogo-1** |7.24% | 6.85% | 3.89% | 7.34% | 7.20% | **6.50%** |
| **exp-vulnerable-ms-ordenes-1** |6.39% | 9.40% | 3.91% | 8.27% | 8.38% | **7.27%** |
| **exp-vulnerable-ms-resenas-1** |160.38% | 151.72% | 136.32% | 199.05% | 201.39% | **169.77%** |
| **exp-vulnerable-ms-usuarios-1** |5.52% | 6.86% | 3.30% | 6.96% | 6.68% | **5.86%** |
| **exp-vulnerable-postgres-db-1** |54.42% | 65.97% | 34.74% | 56.89% | 93.24% | **61.05%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.81 MiB | 69.88 MiB | 68.89 MiB | 68.71 MiB | 68.04 MiB | **68.67 MiB** |
| **exp-vulnerable-mongo-db-1** |346.30 MiB | 345.90 MiB | 336.40 MiB | 342.70 MiB | 336.00 MiB | **341.46 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.76 MiB | 46.17 MiB | 45.86 MiB | 46.02 MiB | 47.26 MiB | **46.21 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.80 MiB | 45.75 MiB | 46.02 MiB | 46.65 MiB | 46.61 MiB | **46.37 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.01 MiB | 45.40 MiB | 45.93 MiB | 46.01 MiB | 46.04 MiB | **46.08 MiB** |
| **exp-vulnerable-postgres-db-1** |78.60 MiB | 80.29 MiB | 76.47 MiB | 75.98 MiB | 79.09 MiB | **78.09 MiB** |
