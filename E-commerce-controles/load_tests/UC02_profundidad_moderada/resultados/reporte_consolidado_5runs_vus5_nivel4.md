# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 16:07:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 106 | 1836.570 ms | 0.00% | 0.00% |
| Run 2 | 100 | 2044.830 ms | 0.00% | 0.00% |
| Run 3 | 75 | 3290.110 ms | 13.33% | 0.00% |
| Run 4 | 100 | 2276.990 ms | 0.00% | 0.00% |
| Run 5 | 95 | 2713.980 ms | 10.52% | 0.00% |
| **PROMEDIO** | **95.2** | **2432.496 ms** | **4.77%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |8.53% | 6.94% | 6.61% | 13.24% | 8.67% | **8.80%** |
| **exp-protegido-mongo-db-1** |100.42% | 76.69% | 86.57% | 98.06% | 92.33% | **90.81%** |
| **exp-protegido-ms-catalogo-1** |4.24% | 4.46% | 5.71% | 4.20% | 3.87% | **4.50%** |
| **exp-protegido-ms-ordenes-1** |3.78% | 5.64% | 3.91% | 6.32% | 4.07% | **4.74%** |
| **exp-protegido-ms-resenas-1** |256.19% | 193.55% | 150.13% | 180.71% | 174.85% | **191.09%** |
| **exp-protegido-ms-usuarios-1** |4.13% | 5.63% | 3.21% | 6.39% | 4.76% | **4.82%** |
| **exp-protegido-postgres-db-1** |44.14% | 39.10% | 39.93% | 55.23% | 47.94% | **45.27%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |97.81 MiB | 69.59 MiB | 68.57 MiB | 68.38 MiB | 69.12 MiB | **74.69 MiB** |
| **exp-protegido-mongo-db-1** |347.90 MiB | 315.50 MiB | 275.30 MiB | 344.40 MiB | 344.10 MiB | **325.44 MiB** |
| **exp-protegido-ms-catalogo-1** |46.36 MiB | 45.77 MiB | 46.98 MiB | 45.85 MiB | 46.99 MiB | **46.39 MiB** |
| **exp-protegido-ms-ordenes-1** |47.48 MiB | 46.38 MiB | 48.12 MiB | 46.33 MiB | 45.92 MiB | **46.85 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | 255.90 MiB | **255.84 MiB** |
| **exp-protegido-ms-usuarios-1** |46.98 MiB | 46.62 MiB | 45.86 MiB | 45.22 MiB | 46.16 MiB | **46.17 MiB** |
| **exp-protegido-postgres-db-1** |70.55 MiB | 68.32 MiB | 63.66 MiB | 77.44 MiB | 76.18 MiB | **71.23 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.73% | 0.88% | 0.62% | 1.47% | 0.79% | **1.10%** |
| **exp-protegido-mongo-db-1** |100.42% | 76.69% | 86.57% | 98.06% | 92.33% | **90.81%** |
| **exp-protegido-ms-catalogo-1** |4.24% | 4.46% | 5.71% | 4.20% | 3.87% | **4.50%** |
| **exp-protegido-ms-ordenes-1** |3.78% | 5.64% | 3.91% | 6.32% | 4.07% | **4.74%** |
| **exp-protegido-ms-resenas-1** |256.19% | 193.55% | 150.13% | 180.71% | 174.85% | **191.09%** |
| **exp-protegido-ms-usuarios-1** |4.13% | 5.63% | 3.21% | 6.39% | 4.76% | **4.82%** |
| **exp-protegido-postgres-db-1** |44.14% | 39.10% | 39.93% | 55.23% | 47.94% | **45.27%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |70.40 MiB | 66.27 MiB | 66.64 MiB | 66.26 MiB | 67.35 MiB | **67.38 MiB** |
| **exp-protegido-mongo-db-1** |347.90 MiB | 315.50 MiB | 275.30 MiB | 344.40 MiB | 344.10 MiB | **325.44 MiB** |
| **exp-protegido-ms-catalogo-1** |46.36 MiB | 45.77 MiB | 46.98 MiB | 45.85 MiB | 46.99 MiB | **46.39 MiB** |
| **exp-protegido-ms-ordenes-1** |47.48 MiB | 46.38 MiB | 48.12 MiB | 46.33 MiB | 45.92 MiB | **46.85 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | 255.90 MiB | **255.84 MiB** |
| **exp-protegido-ms-usuarios-1** |46.98 MiB | 46.62 MiB | 45.86 MiB | 45.22 MiB | 46.16 MiB | **46.17 MiB** |
| **exp-protegido-postgres-db-1** |70.55 MiB | 68.32 MiB | 63.66 MiB | 77.44 MiB | 76.18 MiB | **71.23 MiB** |
