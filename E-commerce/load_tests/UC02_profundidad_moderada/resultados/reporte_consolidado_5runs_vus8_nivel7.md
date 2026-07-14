# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 11:24:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 136 | 2850.940 ms | 11.76% | 0.00% |
| Run 2 | 160 | 2237.400 ms | 0.00% | 0.00% |
| Run 3 | 176 | 1740.090 ms | 0.00% | 0.00% |
| Run 4 | 160 | 2207.570 ms | 0.00% | 0.00% |
| Run 5 | 164 | 2369.360 ms | 0.00% | 0.00% |
| **PROMEDIO** | **159.2** | **2281.072 ms** | **2.35%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |21.38% | 13.23% | 8.55% | 12.97% | 7.77% | **12.78%** |
| **exp-vulnerable-mongo-db-1** |67.20% | 62.13% | 96.11% | 88.72% | 91.90% | **81.21%** |
| **exp-vulnerable-ms-catalogo-1** |5.02% | 4.14% | 4.41% | 5.42% | 5.01% | **4.80%** |
| **exp-vulnerable-ms-ordenes-1** |4.45% | 4.27% | 4.48% | 3.78% | 3.12% | **4.02%** |
| **exp-vulnerable-ms-resenas-1** |225.31% | 219.05% | 262.22% | 230.96% | 222.32% | **231.97%** |
| **exp-vulnerable-ms-usuarios-1** |4.47% | 3.77% | 4.24% | 3.43% | 4.39% | **4.06%** |
| **exp-vulnerable-postgres-db-1** |50.37% | 47.96% | 31.49% | 31.64% | 46.24% | **41.54%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |71.23 MiB | 73.76 MiB | 72.36 MiB | 70.54 MiB | 71.66 MiB | **71.91 MiB** |
| **exp-vulnerable-mongo-db-1** |350.50 MiB | 334.50 MiB | 331.50 MiB | 336.70 MiB | 350.10 MiB | **340.66 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.11 MiB | 45.05 MiB | 46.12 MiB | 45.69 MiB | 46.16 MiB | **45.63 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.21 MiB | 45.95 MiB | 45.78 MiB | 46.01 MiB | 46.40 MiB | **46.27 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.70 MiB | 255.80 MiB | 255.80 MiB | **255.80 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.35 MiB | 54.48 MiB | 45.89 MiB | 46.01 MiB | 46.06 MiB | **48.16 MiB** |
| **exp-vulnerable-postgres-db-1** |68.63 MiB | 71.00 MiB | 77.70 MiB | 76.41 MiB | 70.07 MiB | **72.76 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.80% | 2.06% | 1.61% | 1.82% | 1.28% | **1.71%** |
| **exp-vulnerable-mongo-db-1** |67.20% | 62.13% | 96.11% | 88.72% | 91.90% | **81.21%** |
| **exp-vulnerable-ms-catalogo-1** |5.02% | 4.14% | 4.41% | 5.42% | 5.01% | **4.80%** |
| **exp-vulnerable-ms-ordenes-1** |4.45% | 4.27% | 4.48% | 3.78% | 3.12% | **4.02%** |
| **exp-vulnerable-ms-resenas-1** |225.31% | 219.05% | 262.22% | 230.96% | 222.32% | **231.97%** |
| **exp-vulnerable-ms-usuarios-1** |4.47% | 3.77% | 4.24% | 3.43% | 4.39% | **4.06%** |
| **exp-vulnerable-postgres-db-1** |50.37% | 47.96% | 31.49% | 31.64% | 46.24% | **41.54%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |68.06 MiB | 69.81 MiB | 69.75 MiB | 67.98 MiB | 67.98 MiB | **68.72 MiB** |
| **exp-vulnerable-mongo-db-1** |350.50 MiB | 334.50 MiB | 331.50 MiB | 336.70 MiB | 350.10 MiB | **340.66 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.11 MiB | 45.05 MiB | 46.12 MiB | 45.69 MiB | 46.16 MiB | **45.63 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.21 MiB | 45.95 MiB | 45.78 MiB | 46.01 MiB | 46.40 MiB | **46.27 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.70 MiB | 255.80 MiB | 255.80 MiB | **255.80 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.35 MiB | 54.48 MiB | 45.89 MiB | 46.01 MiB | 46.06 MiB | **48.16 MiB** |
| **exp-vulnerable-postgres-db-1** |68.63 MiB | 71.00 MiB | 77.70 MiB | 76.41 MiB | 70.07 MiB | **72.76 MiB** |
