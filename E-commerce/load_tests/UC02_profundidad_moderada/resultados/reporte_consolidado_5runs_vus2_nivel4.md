# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 12:32:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 52 | 1368.400 ms | 0.00% | 0.00% |
| Run 2 | 50 | 1417.960 ms | 0.00% | 0.00% |
| Run 3 | 38 | 2194.700 ms | 0.00% | 0.00% |
| Run 4 | 0 | 0.000 ms | 0.00% | 0.00% |
| Run 5 | 40 | 2023.110 ms | 0.00% | 0.00% |
| **PROMEDIO** | **36.0** | **1400.834 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |4.29% | 2.98% | 2.53% | 4.09% | 4.06% | **3.59%** |
| **exp-vulnerable-mongo-db-1** |84.74% | 89.34% | 78.03% | 118.71% | 74.32% | **89.03%** |
| **exp-vulnerable-ms-catalogo-1** |4.92% | 4.80% | 4.04% | 3.10% | 5.76% | **4.52%** |
| **exp-vulnerable-ms-ordenes-1** |4.20% | 5.08% | 4.20% | 3.47% | 6.03% | **4.60%** |
| **exp-vulnerable-ms-resenas-1** |178.29% | 192.38% | 172.81% | 199.95% | 195.00% | **187.69%** |
| **exp-vulnerable-ms-usuarios-1** |5.25% | 5.83% | 4.33% | 2.76% | 6.73% | **4.98%** |
| **exp-vulnerable-postgres-db-1** |23.47% | 16.47% | 15.96% | 24.42% | 23.82% | **20.83%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |66.56 MiB | 65.73 MiB | 65.59 MiB | 65.59 MiB | 65.57 MiB | **65.81 MiB** |
| **exp-vulnerable-mongo-db-1** |349.00 MiB | 333.40 MiB | 335.10 MiB | 335.40 MiB | 338.30 MiB | **338.24 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.15 MiB | 46.69 MiB | 45.77 MiB | 46.71 MiB | 48.56 MiB | **46.78 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.54 MiB | 46.63 MiB | 45.91 MiB | 46.82 MiB | 45.77 MiB | **46.13 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.44 MiB | 45.42 MiB | 45.91 MiB | 44.90 MiB | 45.84 MiB | **45.50 MiB** |
| **exp-vulnerable-postgres-db-1** |59.40 MiB | 59.88 MiB | 58.59 MiB | 58.50 MiB | 58.51 MiB | **58.98 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.74% | 0.75% | 0.52% | 0.73% | 0.67% | **0.68%** |
| **exp-vulnerable-mongo-db-1** |84.74% | 89.34% | 78.03% | 118.71% | 74.32% | **89.03%** |
| **exp-vulnerable-ms-catalogo-1** |4.92% | 4.80% | 4.04% | 3.10% | 5.76% | **4.52%** |
| **exp-vulnerable-ms-ordenes-1** |4.20% | 5.08% | 4.20% | 3.47% | 6.03% | **4.60%** |
| **exp-vulnerable-ms-resenas-1** |178.29% | 192.38% | 172.81% | 199.95% | 195.00% | **187.69%** |
| **exp-vulnerable-ms-usuarios-1** |5.25% | 5.83% | 4.33% | 2.76% | 6.73% | **4.98%** |
| **exp-vulnerable-postgres-db-1** |23.47% | 16.47% | 15.96% | 24.42% | 23.82% | **20.83%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.27 MiB | 64.73 MiB | 64.68 MiB | 64.64 MiB | 64.76 MiB | **64.82 MiB** |
| **exp-vulnerable-mongo-db-1** |349.00 MiB | 333.40 MiB | 335.10 MiB | 335.40 MiB | 338.30 MiB | **338.24 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.15 MiB | 46.69 MiB | 45.77 MiB | 46.71 MiB | 48.56 MiB | **46.78 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.54 MiB | 46.63 MiB | 45.91 MiB | 46.82 MiB | 45.77 MiB | **46.13 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.44 MiB | 45.42 MiB | 45.91 MiB | 44.90 MiB | 45.84 MiB | **45.50 MiB** |
| **exp-vulnerable-postgres-db-1** |59.40 MiB | 59.88 MiB | 58.59 MiB | 58.50 MiB | 58.51 MiB | **58.98 MiB** |
