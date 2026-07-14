# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 15:55:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 104 | 1977.960 ms | 4.80% | 0.00% |
| Run 2 | 110 | 1765.010 ms | 4.54% | 0.00% |
| Run 3 | 97 | 2092.430 ms | 5.15% | 0.00% |
| Run 4 | 0 | 0.000 ms | 0.00% | 0.00% |
| Run 5 | 115 | 1641.390 ms | 0.00% | 0.00% |
| **PROMEDIO** | **85.2** | **1495.358 ms** | **2.90%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |9.94% | 25.69% | 7.27% | 17.47% | 6.35% | **13.34%** |
| **exp-vulnerable-mongo-db-1** |104.22% | 100.30% | 102.00% | 126.82% | 78.54% | **102.38%** |
| **exp-vulnerable-ms-catalogo-1** |11.17% | 5.97% | 5.57% | 3.37% | 5.17% | **6.25%** |
| **exp-vulnerable-ms-ordenes-1** |8.82% | 5.05% | 5.01% | 3.05% | 6.05% | **5.60%** |
| **exp-vulnerable-ms-resenas-1** |200.64% | 230.42% | 212.28% | 195.53% | 207.10% | **209.19%** |
| **exp-vulnerable-ms-usuarios-1** |6.42% | 4.60% | 4.37% | 4.22% | 4.99% | **4.92%** |
| **exp-vulnerable-postgres-db-1** |49.06% | 43.24% | 58.32% | 41.44% | 62.11% | **50.83%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |69.20 MiB | 70.30 MiB | 69.04 MiB | 68.95 MiB | 69.55 MiB | **69.41 MiB** |
| **exp-vulnerable-mongo-db-1** |355.00 MiB | 345.80 MiB | 336.90 MiB | 338.30 MiB | 339.30 MiB | **343.06 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.27 MiB | 47.80 MiB | 46.12 MiB | 47.12 MiB | 46.27 MiB | **46.72 MiB** |
| **exp-vulnerable-ms-ordenes-1** |49.73 MiB | 46.57 MiB | 46.07 MiB | 45.51 MiB | 47.12 MiB | **47.00 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.83 MiB | 46.08 MiB | 45.54 MiB | 46.04 MiB | 48.35 MiB | **46.57 MiB** |
| **exp-vulnerable-postgres-db-1** |75.19 MiB | 79.62 MiB | 70.01 MiB | 71.25 MiB | 68.58 MiB | **72.93 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.52% | 2.83% | 1.61% | 2.48% | 1.02% | **1.89%** |
| **exp-vulnerable-mongo-db-1** |104.22% | 100.30% | 102.00% | 126.82% | 78.54% | **102.38%** |
| **exp-vulnerable-ms-catalogo-1** |11.17% | 5.97% | 5.57% | 3.37% | 5.17% | **6.25%** |
| **exp-vulnerable-ms-ordenes-1** |8.82% | 5.05% | 5.01% | 3.05% | 6.05% | **5.60%** |
| **exp-vulnerable-ms-resenas-1** |200.64% | 230.42% | 212.28% | 195.53% | 207.10% | **209.19%** |
| **exp-vulnerable-ms-usuarios-1** |6.42% | 4.60% | 4.37% | 4.22% | 4.99% | **4.92%** |
| **exp-vulnerable-postgres-db-1** |49.06% | 43.24% | 58.32% | 41.44% | 62.11% | **50.83%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.35 MiB | 66.91 MiB | 66.70 MiB | 67.18 MiB | 67.16 MiB | **67.06 MiB** |
| **exp-vulnerable-mongo-db-1** |355.00 MiB | 345.80 MiB | 336.90 MiB | 338.30 MiB | 339.30 MiB | **343.06 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.27 MiB | 47.80 MiB | 46.12 MiB | 47.12 MiB | 46.27 MiB | **46.72 MiB** |
| **exp-vulnerable-ms-ordenes-1** |49.73 MiB | 46.57 MiB | 46.07 MiB | 45.51 MiB | 47.12 MiB | **47.00 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.83 MiB | 46.08 MiB | 45.54 MiB | 46.04 MiB | 48.35 MiB | **46.57 MiB** |
| **exp-vulnerable-postgres-db-1** |75.19 MiB | 79.62 MiB | 70.01 MiB | 71.25 MiB | 68.58 MiB | **72.93 MiB** |
