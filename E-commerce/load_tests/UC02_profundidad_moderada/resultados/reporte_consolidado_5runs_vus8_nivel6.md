# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 00:27:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 185 | 1908.110 ms | 0.00% | 0.00% |
| Run 2 | 203 | 1486.290 ms | 0.00% | 0.00% |
| Run 3 | 207 | 1445.950 ms | 0.00% | 0.00% |
| Run 4 | 160 | 2315.210 ms | 5.00% | 0.00% |
| Run 5 | 192 | 1509.140 ms | 4.16% | 0.00% |
| **PROMEDIO** | **189.4** | **1732.940 ms** | **1.83%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |29.90% | 16.38% | 11.30% | 33.58% | 35.59% | **25.35%** |
| **exp-vulnerable-mongo-db-1** |111.93% | 115.08% | 98.18% | 98.47% | 112.97% | **107.33%** |
| **exp-vulnerable-ms-catalogo-1** |6.02% | 7.73% | 7.50% | 5.62% | 5.76% | **6.53%** |
| **exp-vulnerable-ms-ordenes-1** |8.36% | 7.13% | 8.20% | 5.53% | 5.87% | **7.02%** |
| **exp-vulnerable-ms-resenas-1** |222.49% | 220.82% | 220.77% | 265.14% | 226.72% | **231.19%** |
| **exp-vulnerable-ms-usuarios-1** |8.41% | 6.79% | 5.23% | 5.35% | 5.99% | **6.35%** |
| **exp-vulnerable-postgres-db-1** |100.49% | 76.42% | 111.63% | 59.79% | 64.89% | **82.64%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |97.56 MiB | 73.21 MiB | 72.68 MiB | 72.29 MiB | 71.22 MiB | **77.39 MiB** |
| **exp-vulnerable-mongo-db-1** |349.30 MiB | 350.20 MiB | 340.00 MiB | 340.60 MiB | 351.60 MiB | **346.34 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.85 MiB | 46.87 MiB | 46.73 MiB | 46.36 MiB | 47.61 MiB | **46.68 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.52 MiB | 46.31 MiB | 48.11 MiB | 46.77 MiB | 47.26 MiB | **46.99 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | 255.80 MiB | **255.84 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.20 MiB | 45.63 MiB | 46.89 MiB | 45.74 MiB | 46.94 MiB | **46.28 MiB** |
| **exp-vulnerable-postgres-db-1** |78.58 MiB | 71.54 MiB | 67.62 MiB | 75.59 MiB | 79.92 MiB | **74.65 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |3.50% | 2.82% | 3.78% | 3.34% | 3.97% | **3.48%** |
| **exp-vulnerable-mongo-db-1** |111.93% | 115.08% | 98.18% | 98.47% | 112.97% | **107.33%** |
| **exp-vulnerable-ms-catalogo-1** |6.02% | 7.73% | 7.50% | 5.62% | 5.76% | **6.53%** |
| **exp-vulnerable-ms-ordenes-1** |8.36% | 7.13% | 8.20% | 5.53% | 5.87% | **7.02%** |
| **exp-vulnerable-ms-resenas-1** |222.49% | 220.82% | 220.77% | 265.14% | 226.72% | **231.19%** |
| **exp-vulnerable-ms-usuarios-1** |8.41% | 6.79% | 5.23% | 5.35% | 5.99% | **6.35%** |
| **exp-vulnerable-postgres-db-1** |100.49% | 76.42% | 111.63% | 59.79% | 64.89% | **82.64%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |72.83 MiB | 70.10 MiB | 69.60 MiB | 70.38 MiB | 69.12 MiB | **70.41 MiB** |
| **exp-vulnerable-mongo-db-1** |349.30 MiB | 350.20 MiB | 340.00 MiB | 340.60 MiB | 351.60 MiB | **346.34 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.85 MiB | 46.87 MiB | 46.73 MiB | 46.36 MiB | 47.61 MiB | **46.68 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.52 MiB | 46.31 MiB | 48.11 MiB | 46.77 MiB | 47.26 MiB | **46.99 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | 255.80 MiB | **255.84 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.20 MiB | 45.63 MiB | 46.89 MiB | 45.74 MiB | 46.94 MiB | **46.28 MiB** |
| **exp-vulnerable-postgres-db-1** |78.58 MiB | 71.54 MiB | 67.62 MiB | 75.59 MiB | 79.92 MiB | **74.65 MiB** |
