# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 21:40:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 30 | 1050.260 ms | 0.00% | 0.00% |
| Run 2 | 28 | 1184.880 ms | 0.00% | 0.00% |
| Run 3 | 24 | 1503.130 ms | 0.00% | 0.00% |
| Run 4 | 33 | 948.480 ms | 0.00% | 0.00% |
| Run 5 | 28 | 1172.220 ms | 0.00% | 0.00% |
| **PROMEDIO** | **28.6** | **1171.794 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |20.04% | 6.82% | 2.06% | 10.41% | 22.84% | **12.43%** |
| **exp-vulnerable-mongo-db-1** |126.21% | 113.58% | 95.80% | 114.17% | 88.12% | **107.58%** |
| **exp-vulnerable-ms-catalogo-1** |6.85% | 5.70% | 5.05% | 6.03% | 6.48% | **6.02%** |
| **exp-vulnerable-ms-ordenes-1** |5.26% | 6.47% | 5.39% | 6.63% | 7.54% | **6.26%** |
| **exp-vulnerable-ms-resenas-1** |191.53% | 211.24% | 187.84% | 192.04% | 184.10% | **193.35%** |
| **exp-vulnerable-ms-usuarios-1** |4.50% | 11.04% | 4.94% | 9.21% | 6.00% | **7.14%** |
| **exp-vulnerable-postgres-db-1** |23.81% | 31.03% | 18.25% | 24.33% | 23.48% | **24.18%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.59 MiB | 66.00 MiB | 65.20 MiB | 96.75 MiB | 65.01 MiB | **77.91 MiB** |
| **exp-vulnerable-mongo-db-1** |339.80 MiB | 348.90 MiB | 336.90 MiB | 350.10 MiB | 343.20 MiB | **343.78 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.23 MiB | 46.12 MiB | 46.37 MiB | 47.86 MiB | 45.79 MiB | **46.47 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.31 MiB | 45.70 MiB | 46.33 MiB | 47.70 MiB | 45.57 MiB | **46.52 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.17 MiB | 45.77 MiB | 53.82 MiB | 45.46 MiB | 45.68 MiB | **47.38 MiB** |
| **exp-vulnerable-postgres-db-1** |56.71 MiB | 57.62 MiB | 56.80 MiB | 56.76 MiB | 56.75 MiB | **56.93 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.57% | 0.83% | 0.41% | 0.97% | 1.22% | **1.00%** |
| **exp-vulnerable-mongo-db-1** |126.21% | 113.58% | 95.80% | 114.17% | 88.12% | **107.58%** |
| **exp-vulnerable-ms-catalogo-1** |6.85% | 5.70% | 5.05% | 6.03% | 6.48% | **6.02%** |
| **exp-vulnerable-ms-ordenes-1** |5.26% | 6.47% | 5.39% | 6.63% | 7.54% | **6.26%** |
| **exp-vulnerable-ms-resenas-1** |191.53% | 211.24% | 187.84% | 192.04% | 184.10% | **193.35%** |
| **exp-vulnerable-ms-usuarios-1** |4.50% | 11.04% | 4.94% | 9.21% | 6.00% | **7.14%** |
| **exp-vulnerable-postgres-db-1** |23.81% | 31.03% | 18.25% | 24.33% | 23.48% | **24.18%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |66.47 MiB | 65.11 MiB | 64.45 MiB | 69.85 MiB | 64.16 MiB | **66.01 MiB** |
| **exp-vulnerable-mongo-db-1** |339.80 MiB | 348.90 MiB | 336.90 MiB | 350.10 MiB | 343.20 MiB | **343.78 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.23 MiB | 46.12 MiB | 46.37 MiB | 47.86 MiB | 45.79 MiB | **46.47 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.31 MiB | 45.70 MiB | 46.33 MiB | 47.70 MiB | 45.57 MiB | **46.52 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.17 MiB | 45.77 MiB | 53.82 MiB | 45.46 MiB | 45.68 MiB | **47.38 MiB** |
| **exp-vulnerable-postgres-db-1** |56.71 MiB | 57.62 MiB | 56.80 MiB | 56.76 MiB | 56.75 MiB | **56.93 MiB** |
