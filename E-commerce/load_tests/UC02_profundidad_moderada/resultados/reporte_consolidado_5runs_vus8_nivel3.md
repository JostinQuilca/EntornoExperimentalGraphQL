# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-07 21:29:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 152 | 2278.550 ms | 0.00% | 0.00% |
| Run 2 | 219 | 1222.400 ms | 0.00% | 0.00% |
| Run 3 | 176 | 1799.500 ms | 0.00% | 0.00% |
| Run 4 | 168 | 2112.320 ms | 4.76% | 0.00% |
| Run 5 | 184 | 1798.940 ms | 4.34% | 0.00% |
| **PROMEDIO** | **179.8** | **1842.342 ms** | **1.82%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |8.67% | 10.27% | 10.25% | 14.22% | 20.34% | **12.75%** |
| **exp-vulnerable-mongo-db-1** |97.97% | 110.58% | 89.80% | 113.41% | 104.87% | **103.33%** |
| **exp-vulnerable-ms-catalogo-1** |4.46% | 6.90% | 5.28% | 4.94% | 4.48% | **5.21%** |
| **exp-vulnerable-ms-ordenes-1** |4.20% | 5.65% | 4.67% | 3.39% | 4.54% | **4.49%** |
| **exp-vulnerable-ms-resenas-1** |231.99% | 271.14% | 233.40% | 224.12% | 201.28% | **232.39%** |
| **exp-vulnerable-ms-usuarios-1** |4.89% | 6.23% | 4.69% | 4.35% | 5.46% | **5.12%** |
| **exp-vulnerable-postgres-db-1** |65.25% | 55.31% | 66.98% | 76.67% | 57.94% | **64.43%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |71.24 MiB | 72.62 MiB | 71.95 MiB | 69.93 MiB | 74.02 MiB | **71.95 MiB** |
| **exp-vulnerable-mongo-db-1** |350.00 MiB | 349.70 MiB | 340.00 MiB | 339.50 MiB | 351.00 MiB | **346.04 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.17 MiB | 45.33 MiB | 46.52 MiB | 45.95 MiB | 45.24 MiB | **45.84 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.32 MiB | 46.00 MiB | 45.76 MiB | 45.47 MiB | 55.23 MiB | **47.76 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |54.68 MiB | 46.41 MiB | 45.97 MiB | 45.98 MiB | 47.05 MiB | **48.02 MiB** |
| **exp-vulnerable-postgres-db-1** |70.90 MiB | 76.14 MiB | 75.84 MiB | 70.90 MiB | 72.03 MiB | **73.16 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.43% | 2.84% | 2.14% | 2.23% | 2.94% | **2.32%** |
| **exp-vulnerable-mongo-db-1** |97.97% | 110.58% | 89.80% | 113.41% | 104.87% | **103.33%** |
| **exp-vulnerable-ms-catalogo-1** |4.46% | 6.90% | 5.28% | 4.94% | 4.48% | **5.21%** |
| **exp-vulnerable-ms-ordenes-1** |4.20% | 5.65% | 4.67% | 3.39% | 4.54% | **4.49%** |
| **exp-vulnerable-ms-resenas-1** |231.99% | 271.14% | 233.40% | 224.12% | 201.28% | **232.39%** |
| **exp-vulnerable-ms-usuarios-1** |4.89% | 6.23% | 4.69% | 4.35% | 5.46% | **5.12%** |
| **exp-vulnerable-postgres-db-1** |65.25% | 55.31% | 66.98% | 76.67% | 57.94% | **64.43%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |69.45 MiB | 69.01 MiB | 69.59 MiB | 67.85 MiB | 69.45 MiB | **69.07 MiB** |
| **exp-vulnerable-mongo-db-1** |350.00 MiB | 349.70 MiB | 340.00 MiB | 339.50 MiB | 351.00 MiB | **346.04 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.17 MiB | 45.33 MiB | 46.52 MiB | 45.95 MiB | 45.24 MiB | **45.84 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.32 MiB | 46.00 MiB | 45.76 MiB | 45.47 MiB | 55.23 MiB | **47.76 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |54.68 MiB | 46.41 MiB | 45.97 MiB | 45.98 MiB | 47.05 MiB | **48.02 MiB** |
| **exp-vulnerable-postgres-db-1** |70.90 MiB | 76.14 MiB | 75.84 MiB | 70.90 MiB | 72.03 MiB | **73.16 MiB** |
