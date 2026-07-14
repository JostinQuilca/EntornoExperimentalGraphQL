# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-08 22:35:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 35 | 2882.280 ms | 0.00% | 0.00% |
| Run 2 | 28 | 3405.880 ms | 0.00% | 0.00% |
| Run 3 | 36 | 2467.750 ms | 0.00% | 0.00% |
| Run 4 | 36 | 2463.180 ms | 0.00% | 0.00% |
| Run 5 | 39 | 2193.610 ms | 0.00% | 0.00% |
| **PROMEDIO** | **34.8** | **2682.540 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |9.74% | 144.04% | 146.07% | 21.80% | 98.07% | **83.94%** |
| **exp-vulnerable-mongo-db-1** |104.79% | 109.99% | 96.13% | 74.76% | 107.66% | **98.67%** |
| **exp-vulnerable-ms-catalogo-1** |4.30% | 4.87% | 4.22% | 4.69% | 3.48% | **4.31%** |
| **exp-vulnerable-ms-ordenes-1** |6.50% | 5.07% | 4.02% | 4.59% | 7.84% | **5.60%** |
| **exp-vulnerable-ms-resenas-1** |166.86% | 185.36% | 149.65% | 166.24% | 183.38% | **170.30%** |
| **exp-vulnerable-ms-usuarios-1** |4.50% | 2.89% | 3.20% | 4.31% | 7.33% | **4.45%** |
| **exp-vulnerable-postgres-db-1** |24.96% | 16.30% | 26.23% | 17.88% | 17.44% | **20.56%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |139.70 MiB | 336.30 MiB | 335.60 MiB | 142.60 MiB | 192.20 MiB | **229.28 MiB** |
| **exp-vulnerable-mongo-db-1** |349.00 MiB | 341.00 MiB | 350.10 MiB | 342.60 MiB | 341.50 MiB | **344.84 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.70 MiB | 45.48 MiB | 47.88 MiB | 48.48 MiB | 47.55 MiB | **47.02 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.52 MiB | 47.42 MiB | 45.89 MiB | 45.95 MiB | 45.74 MiB | **46.10 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | **256.00 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.15 MiB | 45.72 MiB | 45.41 MiB | 48.05 MiB | 46.53 MiB | **46.17 MiB** |
| **exp-vulnerable-postgres-db-1** |60.59 MiB | 60.59 MiB | 61.52 MiB | 58.46 MiB | 59.47 MiB | **60.13 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.98% | 6.93% | 7.97% | 2.01% | 4.61% | **4.50%** |
| **exp-vulnerable-mongo-db-1** |104.79% | 109.99% | 96.13% | 74.76% | 107.66% | **98.67%** |
| **exp-vulnerable-ms-catalogo-1** |4.30% | 4.87% | 4.22% | 4.69% | 3.48% | **4.31%** |
| **exp-vulnerable-ms-ordenes-1** |6.50% | 5.07% | 4.02% | 4.59% | 7.84% | **5.60%** |
| **exp-vulnerable-ms-resenas-1** |166.86% | 185.36% | 149.65% | 166.24% | 183.38% | **170.30%** |
| **exp-vulnerable-ms-usuarios-1** |4.50% | 2.89% | 3.20% | 4.31% | 7.33% | **4.45%** |
| **exp-vulnerable-postgres-db-1** |24.96% | 16.30% | 26.23% | 17.88% | 17.44% | **20.56%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |93.11 MiB | 162.81 MiB | 140.97 MiB | 104.11 MiB | 98.56 MiB | **119.91 MiB** |
| **exp-vulnerable-mongo-db-1** |349.00 MiB | 341.00 MiB | 350.10 MiB | 342.60 MiB | 341.50 MiB | **344.84 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.70 MiB | 45.48 MiB | 47.88 MiB | 48.48 MiB | 47.55 MiB | **47.02 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.52 MiB | 47.42 MiB | 45.89 MiB | 45.95 MiB | 45.74 MiB | **46.10 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | **256.00 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.15 MiB | 45.72 MiB | 45.41 MiB | 48.05 MiB | 46.53 MiB | **46.17 MiB** |
| **exp-vulnerable-postgres-db-1** |60.59 MiB | 60.59 MiB | 61.52 MiB | 58.46 MiB | 59.47 MiB | **60.13 MiB** |
