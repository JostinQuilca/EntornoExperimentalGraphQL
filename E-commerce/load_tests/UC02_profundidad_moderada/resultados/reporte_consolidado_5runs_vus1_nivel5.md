# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 16:42:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 26 | 1343.240 ms | 0.00% | 0.00% |
| Run 2 | 24 | 1539.280 ms | 0.00% | 0.00% |
| Run 3 | 21 | 1941.910 ms | 0.00% | 0.00% |
| Run 4 | 28 | 1406.280 ms | 0.00% | 0.00% |
| Run 5 | 24 | 1579.550 ms | 0.00% | 0.00% |
| **PROMEDIO** | **24.6** | **1562.052 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |9.10% | 1.50% | 6.85% | 2.44% | 15.23% | **7.02%** |
| **exp-vulnerable-mongo-db-1** |93.54% | 120.58% | 94.10% | 91.96% | 75.15% | **95.07%** |
| **exp-vulnerable-ms-catalogo-1** |6.33% | 12.21% | 5.01% | 6.50% | 5.39% | **7.09%** |
| **exp-vulnerable-ms-ordenes-1** |4.32% | 8.28% | 5.29% | 6.20% | 4.33% | **5.68%** |
| **exp-vulnerable-ms-resenas-1** |197.80% | 227.18% | 187.99% | 177.49% | 185.65% | **195.22%** |
| **exp-vulnerable-ms-usuarios-1** |6.66% | 7.86% | 4.06% | 5.35% | 4.42% | **5.67%** |
| **exp-vulnerable-postgres-db-1** |13.62% | 10.25% | 9.74% | 15.98% | 10.35% | **11.99%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.34 MiB | 66.27 MiB | 65.08 MiB | 66.41 MiB | 65.52 MiB | **65.72 MiB** |
| **exp-vulnerable-mongo-db-1** |350.00 MiB | 350.50 MiB | 338.20 MiB | 344.70 MiB | 352.20 MiB | **347.12 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.65 MiB | 50.96 MiB | 48.41 MiB | 47.66 MiB | 51.16 MiB | **48.97 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.66 MiB | 48.58 MiB | 54.98 MiB | 47.45 MiB | 50.39 MiB | **49.81 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.59 MiB | 49.24 MiB | 48.21 MiB | 47.90 MiB | 52.21 MiB | **48.83 MiB** |
| **exp-vulnerable-postgres-db-1** |57.06 MiB | 58.65 MiB | 56.85 MiB | 58.52 MiB | 58.62 MiB | **57.94 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.71% | 0.27% | 0.45% | 0.36% | 0.78% | **0.51%** |
| **exp-vulnerable-mongo-db-1** |93.54% | 120.58% | 94.10% | 91.96% | 75.15% | **95.07%** |
| **exp-vulnerable-ms-catalogo-1** |6.33% | 12.21% | 5.01% | 6.50% | 5.39% | **7.09%** |
| **exp-vulnerable-ms-ordenes-1** |4.32% | 8.28% | 5.29% | 6.20% | 4.33% | **5.68%** |
| **exp-vulnerable-ms-resenas-1** |197.80% | 227.18% | 187.99% | 177.49% | 185.65% | **195.22%** |
| **exp-vulnerable-ms-usuarios-1** |6.66% | 7.86% | 4.06% | 5.35% | 4.42% | **5.67%** |
| **exp-vulnerable-postgres-db-1** |13.62% | 10.25% | 9.74% | 15.98% | 10.35% | **11.99%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |64.74 MiB | 65.32 MiB | 64.45 MiB | 65.68 MiB | 64.85 MiB | **65.01 MiB** |
| **exp-vulnerable-mongo-db-1** |350.00 MiB | 350.50 MiB | 338.20 MiB | 344.70 MiB | 352.20 MiB | **347.12 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.65 MiB | 50.96 MiB | 48.41 MiB | 47.66 MiB | 51.16 MiB | **48.97 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.66 MiB | 48.58 MiB | 54.98 MiB | 47.45 MiB | 50.39 MiB | **49.81 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.59 MiB | 49.24 MiB | 48.21 MiB | 47.90 MiB | 52.21 MiB | **48.83 MiB** |
| **exp-vulnerable-postgres-db-1** |57.06 MiB | 58.65 MiB | 56.85 MiB | 58.52 MiB | 58.62 MiB | **57.94 MiB** |
