# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-07 20:48:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 152 | 2208.280 ms | 5.26% | 0.00% |
| Run 2 | 173 | 1920.590 ms | 4.62% | 0.00% |
| Run 3 | 192 | 2135.700 ms | 8.33% | 0.00% |
| Run 4 | 176 | 1753.410 ms | 4.54% | 0.00% |
| Run 5 | 144 | 2465.270 ms | 5.55% | 0.00% |
| **PROMEDIO** | **167.4** | **2096.650 ms** | **5.66%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |15.75% | 5.24% | 16.17% | 10.42% | 30.07% | **15.53%** |
| **exp-vulnerable-mongo-db-1** |96.69% | 109.12% | 107.73% | 83.54% | 104.04% | **100.22%** |
| **exp-vulnerable-ms-catalogo-1** |3.84% | 4.46% | 5.74% | 4.17% | 5.17% | **4.68%** |
| **exp-vulnerable-ms-ordenes-1** |5.09% | 7.45% | 4.98% | 4.94% | 4.52% | **5.40%** |
| **exp-vulnerable-ms-resenas-1** |230.54% | 257.83% | 268.47% | 201.24% | 208.39% | **233.29%** |
| **exp-vulnerable-ms-usuarios-1** |4.81% | 7.56% | 5.84% | 3.06% | 4.80% | **5.21%** |
| **exp-vulnerable-postgres-db-1** |37.96% | 69.60% | 47.35% | 47.00% | 101.02% | **60.59%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |71.03 MiB | 71.63 MiB | 71.39 MiB | 71.34 MiB | 71.46 MiB | **71.37 MiB** |
| **exp-vulnerable-mongo-db-1** |344.80 MiB | 349.20 MiB | 334.80 MiB | 348.30 MiB | 352.50 MiB | **345.92 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.10 MiB | 46.05 MiB | 48.05 MiB | 47.25 MiB | 45.82 MiB | **46.65 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.41 MiB | 46.64 MiB | 47.20 MiB | 47.82 MiB | 45.15 MiB | **46.44 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.49 MiB | 47.09 MiB | 45.56 MiB | 45.44 MiB | 53.80 MiB | **47.68 MiB** |
| **exp-vulnerable-postgres-db-1** |69.62 MiB | 77.07 MiB | 70.52 MiB | 74.71 MiB | 69.64 MiB | **72.31 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.80% | 1.37% | 2.16% | 1.73% | 2.89% | **1.99%** |
| **exp-vulnerable-mongo-db-1** |96.69% | 109.12% | 107.73% | 83.54% | 104.04% | **100.22%** |
| **exp-vulnerable-ms-catalogo-1** |3.84% | 4.46% | 5.74% | 4.17% | 5.17% | **4.68%** |
| **exp-vulnerable-ms-ordenes-1** |5.09% | 7.45% | 4.98% | 4.94% | 4.52% | **5.40%** |
| **exp-vulnerable-ms-resenas-1** |230.54% | 257.83% | 268.47% | 201.24% | 208.39% | **233.29%** |
| **exp-vulnerable-ms-usuarios-1** |4.81% | 7.56% | 5.84% | 3.06% | 4.80% | **5.21%** |
| **exp-vulnerable-postgres-db-1** |37.96% | 69.60% | 47.35% | 47.00% | 101.02% | **60.59%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.31 MiB | 69.17 MiB | 69.51 MiB | 68.10 MiB | 67.78 MiB | **68.37 MiB** |
| **exp-vulnerable-mongo-db-1** |344.80 MiB | 349.20 MiB | 334.80 MiB | 348.30 MiB | 352.50 MiB | **345.92 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.10 MiB | 46.05 MiB | 48.05 MiB | 47.25 MiB | 45.82 MiB | **46.65 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.41 MiB | 46.64 MiB | 47.20 MiB | 47.82 MiB | 45.15 MiB | **46.44 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.49 MiB | 47.09 MiB | 45.56 MiB | 45.44 MiB | 53.80 MiB | **47.68 MiB** |
| **exp-vulnerable-postgres-db-1** |69.62 MiB | 77.07 MiB | 70.52 MiB | 74.71 MiB | 69.64 MiB | **72.31 MiB** |
