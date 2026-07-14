# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 16:54:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 26 | 1527.150 ms | 0.00% | 0.00% |
| Run 2 | 20 | 2142.760 ms | 0.00% | 0.00% |
| Run 3 | 24 | 1513.760 ms | 0.00% | 0.00% |
| Run 4 | 25 | 1456.620 ms | 0.00% | 0.00% |
| Run 5 | 26 | 1407.410 ms | 0.00% | 0.00% |
| **PROMEDIO** | **24.2** | **1609.540 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.35% | 2.58% | 1.30% | 1.01% | 2.90% | **2.03%** |
| **exp-protegido-mongo-db-1** |72.12% | 75.49% | 70.95% | 86.06% | 111.23% | **83.17%** |
| **exp-protegido-ms-catalogo-1** |4.93% | 3.98% | 3.05% | 3.66% | 5.51% | **4.23%** |
| **exp-protegido-ms-ordenes-1** |4.54% | 3.78% | 4.30% | 5.02% | 6.60% | **4.85%** |
| **exp-protegido-ms-resenas-1** |204.34% | 178.05% | 175.91% | 187.21% | 177.05% | **184.51%** |
| **exp-protegido-ms-usuarios-1** |4.27% | 3.68% | 3.79% | 5.35% | 7.05% | **4.83%** |
| **exp-protegido-postgres-db-1** |13.90% | 8.30% | 9.49% | 10.25% | 12.92% | **10.97%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |66.96 MiB | 66.74 MiB | 68.31 MiB | 68.75 MiB | 69.07 MiB | **67.97 MiB** |
| **exp-protegido-mongo-db-1** |192.50 MiB | 351.60 MiB | 324.80 MiB | 301.10 MiB | 354.00 MiB | **304.80 MiB** |
| **exp-protegido-ms-catalogo-1** |52.80 MiB | 49.66 MiB | 50.62 MiB | 49.81 MiB | 53.97 MiB | **51.37 MiB** |
| **exp-protegido-ms-ordenes-1** |51.45 MiB | 49.21 MiB | 51.75 MiB | 50.56 MiB | 58.83 MiB | **52.36 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | **255.98 MiB** |
| **exp-protegido-ms-usuarios-1** |52.36 MiB | 48.15 MiB | 50.73 MiB | 50.43 MiB | 51.79 MiB | **50.69 MiB** |
| **exp-protegido-postgres-db-1** |61.18 MiB | 58.85 MiB | 62.07 MiB | 62.18 MiB | 64.91 MiB | **61.84 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.38% | 0.34% | 0.27% | 0.26% | 0.42% | **0.33%** |
| **exp-protegido-mongo-db-1** |72.12% | 75.49% | 70.95% | 86.06% | 111.23% | **83.17%** |
| **exp-protegido-ms-catalogo-1** |4.93% | 3.98% | 3.05% | 3.66% | 5.51% | **4.23%** |
| **exp-protegido-ms-ordenes-1** |4.54% | 3.78% | 4.30% | 5.02% | 6.60% | **4.85%** |
| **exp-protegido-ms-resenas-1** |204.34% | 178.05% | 175.91% | 187.21% | 177.05% | **184.51%** |
| **exp-protegido-ms-usuarios-1** |4.27% | 3.68% | 3.79% | 5.35% | 7.05% | **4.83%** |
| **exp-protegido-postgres-db-1** |13.90% | 8.30% | 9.49% | 10.25% | 12.92% | **10.97%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |66.33 MiB | 66.21 MiB | 67.62 MiB | 68.03 MiB | 68.32 MiB | **67.30 MiB** |
| **exp-protegido-mongo-db-1** |192.50 MiB | 351.60 MiB | 324.80 MiB | 301.10 MiB | 354.00 MiB | **304.80 MiB** |
| **exp-protegido-ms-catalogo-1** |52.80 MiB | 49.66 MiB | 50.62 MiB | 49.81 MiB | 53.97 MiB | **51.37 MiB** |
| **exp-protegido-ms-ordenes-1** |51.45 MiB | 49.21 MiB | 51.75 MiB | 50.56 MiB | 58.83 MiB | **52.36 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | **255.98 MiB** |
| **exp-protegido-ms-usuarios-1** |52.36 MiB | 48.15 MiB | 50.73 MiB | 50.43 MiB | 51.79 MiB | **50.69 MiB** |
| **exp-protegido-postgres-db-1** |61.18 MiB | 58.85 MiB | 62.07 MiB | 62.18 MiB | 64.91 MiB | **61.84 MiB** |
