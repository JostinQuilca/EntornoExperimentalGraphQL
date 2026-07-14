# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 10:49:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 52 | 1321.650 ms | 0.00% | 0.00% |
| Run 2 | 40 | 2003.310 ms | 0.00% | 0.00% |
| Run 3 | 51 | 1485.850 ms | 0.00% | 0.00% |
| Run 4 | 42 | 2238.070 ms | 0.00% | 0.00% |
| Run 5 | 50 | 1430.270 ms | 0.00% | 0.00% |
| **PROMEDIO** | **47.0** | **1695.830 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |4.78% | 2.03% | 1.94% | 7.53% | 7.47% | **4.75%** |
| **exp-vulnerable-mongo-db-1** |103.16% | 109.51% | 118.09% | 117.86% | 113.42% | **112.41%** |
| **exp-vulnerable-ms-catalogo-1** |4.38% | 3.82% | 5.33% | 7.46% | 6.45% | **5.49%** |
| **exp-vulnerable-ms-ordenes-1** |5.35% | 4.68% | 5.72% | 6.16% | 7.22% | **5.83%** |
| **exp-vulnerable-ms-resenas-1** |226.00% | 201.06% | 191.85% | 210.54% | 201.19% | **206.13%** |
| **exp-vulnerable-ms-usuarios-1** |4.51% | 4.58% | 6.57% | 6.45% | 7.37% | **5.90%** |
| **exp-vulnerable-postgres-db-1** |32.63% | 21.81% | 24.19% | 41.43% | 49.81% | **33.97%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.81 MiB | 66.25 MiB | 66.11 MiB | 66.15 MiB | 96.11 MiB | **72.09 MiB** |
| **exp-vulnerable-mongo-db-1** |350.10 MiB | 348.20 MiB | 345.40 MiB | 345.00 MiB | 341.50 MiB | **346.04 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.68 MiB | 46.55 MiB | 46.86 MiB | 46.82 MiB | 47.46 MiB | **46.67 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.43 MiB | 46.24 MiB | 46.70 MiB | 46.85 MiB | 45.45 MiB | **46.33 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.34 MiB | 53.76 MiB | 46.11 MiB | 47.48 MiB | 46.09 MiB | **47.76 MiB** |
| **exp-vulnerable-postgres-db-1** |58.43 MiB | 58.70 MiB | 60.38 MiB | 60.00 MiB | 60.29 MiB | **59.56 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.73% | 0.43% | 0.56% | 0.91% | 0.84% | **0.69%** |
| **exp-vulnerable-mongo-db-1** |103.16% | 109.51% | 118.09% | 117.86% | 113.42% | **112.41%** |
| **exp-vulnerable-ms-catalogo-1** |4.38% | 3.82% | 5.33% | 7.46% | 6.45% | **5.49%** |
| **exp-vulnerable-ms-ordenes-1** |5.35% | 4.68% | 5.72% | 6.16% | 7.22% | **5.83%** |
| **exp-vulnerable-ms-resenas-1** |226.00% | 201.06% | 191.85% | 210.54% | 201.19% | **206.13%** |
| **exp-vulnerable-ms-usuarios-1** |4.51% | 4.58% | 6.57% | 6.45% | 7.37% | **5.90%** |
| **exp-vulnerable-postgres-db-1** |32.63% | 21.81% | 24.19% | 41.43% | 49.81% | **33.97%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |64.51 MiB | 65.04 MiB | 64.96 MiB | 65.05 MiB | 66.08 MiB | **65.13 MiB** |
| **exp-vulnerable-mongo-db-1** |350.10 MiB | 348.20 MiB | 345.40 MiB | 345.00 MiB | 341.50 MiB | **346.04 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.68 MiB | 46.55 MiB | 46.86 MiB | 46.82 MiB | 47.46 MiB | **46.67 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.43 MiB | 46.24 MiB | 46.70 MiB | 46.85 MiB | 45.45 MiB | **46.33 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | **255.96 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.34 MiB | 53.76 MiB | 46.11 MiB | 47.48 MiB | 46.09 MiB | **47.76 MiB** |
| **exp-vulnerable-postgres-db-1** |58.43 MiB | 58.70 MiB | 60.38 MiB | 60.00 MiB | 60.29 MiB | **59.56 MiB** |
