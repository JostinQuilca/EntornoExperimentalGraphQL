# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 15:39:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 63 | 2326.070 ms | 0.00% | 0.00% |
| Run 2 | 69 | 1832.600 ms | 0.00% | 0.00% |
| Run 3 | 58 | 2096.020 ms | 0.00% | 0.00% |
| Run 4 | 0 | 0.000 ms | 0.00% | 0.00% |
| Run 5 | 67 | 1846.230 ms | 4.47% | 0.00% |
| **PROMEDIO** | **51.4** | **1620.184 ms** | **0.89%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |4.55% | 10.02% | 2.97% | 3.67% | 4.44% | **5.13%** |
| **exp-protegido-mongo-db-1** |110.32% | 97.23% | 80.82% | 62.73% | 91.29% | **88.48%** |
| **exp-protegido-ms-catalogo-1** |11.78% | 4.88% | 4.29% | 5.03% | 4.36% | **6.07%** |
| **exp-protegido-ms-ordenes-1** |4.90% | 6.56% | 29.96% | 4.68% | 3.67% | **9.95%** |
| **exp-protegido-ms-resenas-1** |207.75% | 204.89% | 240.72% | 202.40% | 217.92% | **214.74%** |
| **exp-protegido-ms-usuarios-1** |5.08% | 6.73% | 26.44% | 4.50% | 4.57% | **9.46%** |
| **exp-protegido-postgres-db-1** |36.40% | 41.37% | 62.59% | 21.96% | 25.24% | **37.51%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.44 MiB | 67.63 MiB | 67.08 MiB | 66.88 MiB | 67.48 MiB | **67.30 MiB** |
| **exp-protegido-mongo-db-1** |293.20 MiB | 349.60 MiB | 349.40 MiB | 340.90 MiB | 348.20 MiB | **336.26 MiB** |
| **exp-protegido-ms-catalogo-1** |45.48 MiB | 47.25 MiB | 46.83 MiB | 47.74 MiB | 45.03 MiB | **46.47 MiB** |
| **exp-protegido-ms-ordenes-1** |46.55 MiB | 47.40 MiB | 46.34 MiB | 47.93 MiB | 46.13 MiB | **46.87 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-protegido-ms-usuarios-1** |46.34 MiB | 47.27 MiB | 46.88 MiB | 46.35 MiB | 45.98 MiB | **46.56 MiB** |
| **exp-protegido-postgres-db-1** |60.16 MiB | 60.12 MiB | 60.20 MiB | 60.26 MiB | 62.53 MiB | **60.65 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.80% | 1.34% | 0.55% | 0.82% | 0.60% | **0.82%** |
| **exp-protegido-mongo-db-1** |110.32% | 97.23% | 80.82% | 62.73% | 91.29% | **88.48%** |
| **exp-protegido-ms-catalogo-1** |11.78% | 4.88% | 4.29% | 5.03% | 4.36% | **6.07%** |
| **exp-protegido-ms-ordenes-1** |4.90% | 6.56% | 29.96% | 4.68% | 3.67% | **9.95%** |
| **exp-protegido-ms-resenas-1** |207.75% | 204.89% | 240.72% | 202.40% | 217.92% | **214.74%** |
| **exp-protegido-ms-usuarios-1** |5.08% | 6.73% | 26.44% | 4.50% | 4.57% | **9.46%** |
| **exp-protegido-postgres-db-1** |36.40% | 41.37% | 62.59% | 21.96% | 25.24% | **37.51%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.95 MiB | 66.07 MiB | 65.95 MiB | 65.82 MiB | 66.16 MiB | **65.99 MiB** |
| **exp-protegido-mongo-db-1** |293.20 MiB | 349.60 MiB | 349.40 MiB | 340.90 MiB | 348.20 MiB | **336.26 MiB** |
| **exp-protegido-ms-catalogo-1** |45.48 MiB | 47.25 MiB | 46.83 MiB | 47.74 MiB | 45.03 MiB | **46.47 MiB** |
| **exp-protegido-ms-ordenes-1** |46.55 MiB | 47.40 MiB | 46.34 MiB | 47.93 MiB | 46.13 MiB | **46.87 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-protegido-ms-usuarios-1** |46.34 MiB | 47.27 MiB | 46.88 MiB | 46.35 MiB | 45.98 MiB | **46.56 MiB** |
| **exp-protegido-postgres-db-1** |60.16 MiB | 60.12 MiB | 60.20 MiB | 60.26 MiB | 62.53 MiB | **60.65 MiB** |
