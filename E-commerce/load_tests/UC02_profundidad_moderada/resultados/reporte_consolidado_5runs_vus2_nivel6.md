# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 22:06:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 45 | 1754.280 ms | 0.00% | 0.00% |
| Run 2 | 45 | 1964.270 ms | 0.00% | 0.00% |
| Run 3 | 46 | 1706.710 ms | 0.00% | 0.00% |
| Run 4 | 54 | 1472.660 ms | 0.00% | 0.00% |
| Run 5 | 48 | 1602.920 ms | 0.00% | 0.00% |
| **PROMEDIO** | **47.6** | **1700.168 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |8.93% | 4.13% | 13.94% | 2.41% | 8.25% | **7.53%** |
| **exp-vulnerable-mongo-db-1** |101.05% | 108.47% | 109.86% | 96.19% | 110.90% | **105.29%** |
| **exp-vulnerable-ms-catalogo-1** |5.39% | 7.20% | 6.17% | 5.44% | 4.96% | **5.83%** |
| **exp-vulnerable-ms-ordenes-1** |5.07% | 10.52% | 5.59% | 5.90% | 20.06% | **9.43%** |
| **exp-vulnerable-ms-resenas-1** |172.85% | 189.93% | 180.28% | 208.86% | 194.51% | **189.29%** |
| **exp-vulnerable-ms-usuarios-1** |4.87% | 9.60% | 6.26% | 6.05% | 9.40% | **7.24%** |
| **exp-vulnerable-postgres-db-1** |35.59% | 34.00% | 31.06% | 37.45% | 32.28% | **34.08%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.65 MiB | 66.23 MiB | 66.54 MiB | 68.22 MiB | 66.49 MiB | **72.83 MiB** |
| **exp-vulnerable-mongo-db-1** |349.20 MiB | 350.30 MiB | 351.80 MiB | 337.40 MiB | 350.60 MiB | **347.86 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.52 MiB | 48.76 MiB | 47.82 MiB | 46.32 MiB | 47.39 MiB | **47.36 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.18 MiB | 48.76 MiB | 46.15 MiB | 48.81 MiB | 46.62 MiB | **47.30 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | 255.90 MiB | **255.98 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.97 MiB | 47.02 MiB | 47.06 MiB | 46.57 MiB | 46.36 MiB | **46.60 MiB** |
| **exp-vulnerable-postgres-db-1** |59.51 MiB | 58.52 MiB | 61.27 MiB | 60.02 MiB | 58.51 MiB | **59.57 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.05% | 0.88% | 1.33% | 0.69% | 0.97% | **0.98%** |
| **exp-vulnerable-mongo-db-1** |101.05% | 108.47% | 109.86% | 96.19% | 110.90% | **105.29%** |
| **exp-vulnerable-ms-catalogo-1** |5.39% | 7.20% | 6.17% | 5.44% | 4.96% | **5.83%** |
| **exp-vulnerable-ms-ordenes-1** |5.07% | 10.52% | 5.59% | 5.90% | 20.06% | **9.43%** |
| **exp-vulnerable-ms-resenas-1** |172.85% | 189.93% | 180.28% | 208.86% | 194.51% | **189.29%** |
| **exp-vulnerable-ms-usuarios-1** |4.87% | 9.60% | 6.26% | 6.05% | 9.40% | **7.24%** |
| **exp-vulnerable-postgres-db-1** |35.59% | 34.00% | 31.06% | 37.45% | 32.28% | **34.08%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |68.76 MiB | 65.29 MiB | 65.34 MiB | 65.29 MiB | 65.24 MiB | **65.98 MiB** |
| **exp-vulnerable-mongo-db-1** |349.20 MiB | 350.30 MiB | 351.80 MiB | 337.40 MiB | 350.60 MiB | **347.86 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.52 MiB | 48.76 MiB | 47.82 MiB | 46.32 MiB | 47.39 MiB | **47.36 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.18 MiB | 48.76 MiB | 46.15 MiB | 48.81 MiB | 46.62 MiB | **47.30 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | 255.90 MiB | **255.98 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.97 MiB | 47.02 MiB | 47.06 MiB | 46.57 MiB | 46.36 MiB | **46.60 MiB** |
| **exp-vulnerable-postgres-db-1** |59.51 MiB | 58.52 MiB | 61.27 MiB | 60.02 MiB | 58.51 MiB | **59.57 MiB** |
