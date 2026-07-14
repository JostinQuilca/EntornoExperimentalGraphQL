# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 15:19:13

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 16 | 40292.910 ms | 0.00% | 0.00% |
| Run 2 | 9 | 45588.104 ms | 0.00% | 0.00% |
| Run 3 | 16 | 41912.036 ms | 0.00% | 0.00% |
| Run 4 | 8 | 43366.543 ms | 0.00% | 0.00% |
| Run 5 | 16 | 41086.160 ms | 0.00% | 0.00% |
| **PROMEDIO** | **13.0** | **42449.150 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |170.37% | 207.21% | 181.83% | 195.37% | 192.47% | **189.45%** |
| **exp-vulnerable-mongo-db-1** |113.97% | 118.84% | 98.84% | 104.12% | 106.93% | **108.54%** |
| **exp-vulnerable-ms-catalogo-1** |5.96% | 6.07% | 5.28% | 5.24% | 4.85% | **5.48%** |
| **exp-vulnerable-ms-ordenes-1** |5.13% | 5.70% | 5.10% | 6.26% | 5.25% | **5.49%** |
| **exp-vulnerable-ms-resenas-1** |317.57% | 339.51% | 360.49% | 308.76% | 381.32% | **341.53%** |
| **exp-vulnerable-ms-usuarios-1** |309.67% | 221.44% | 269.51% | 333.45% | 253.26% | **277.47%** |
| **exp-vulnerable-postgres-db-1** |29.92% | 35.50% | 37.67% | 34.60% | 24.84% | **32.51%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  |
| **exp-vulnerable-mongo-db-1** |351.3MiB (351.30 MiB)  | 353.6MiB (353.60 MiB)  | 355.8MiB (355.80 MiB)  | 345.6MiB (345.60 MiB)  | 357.4MiB (357.40 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |48.02MiB (48.02 MiB)  | 61.75MiB (61.75 MiB)  | 78MiB (78.00 MiB)  | 49.04MiB (49.04 MiB)  | 59.37MiB (59.37 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |47.62MiB (47.62 MiB)  | 58.91MiB (58.91 MiB)  | 81.95MiB (81.95 MiB)  | 48.07MiB (48.07 MiB)  | 72.07MiB (72.07 MiB)  |
| **exp-vulnerable-ms-resenas-1** |1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |1.464GiB (1499.14 MiB)  | 1.635GiB (1674.24 MiB)  | 1.486GiB (1521.66 MiB)  | 1.637GiB (1676.29 MiB)  | 1.591GiB (1629.18 MiB)  |
| **exp-vulnerable-postgres-db-1** |76.79MiB (76.79 MiB)  | 97.4MiB (97.40 MiB)  | 97.92MiB (97.92 MiB)  | 86.38MiB (86.38 MiB)  | 83.45MiB (83.45 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |51.35% | 56.10% | 56.13% | 47.89% | 49.30% | **52.15%** |
| **exp-vulnerable-mongo-db-1** |32.35% | 36.52% | 21.16% | 29.27% | 28.65% | **29.59%** |
| **exp-vulnerable-ms-catalogo-1** |1.27% | 1.10% | 1.09% | 1.25% | 0.91% | **1.12%** |
| **exp-vulnerable-ms-ordenes-1** |1.39% | 1.15% | 1.11% | 1.22% | 1.14% | **1.20%** |
| **exp-vulnerable-ms-resenas-1** |55.94% | 43.72% | 44.95% | 53.23% | 48.23% | **49.21%** |
| **exp-vulnerable-ms-usuarios-1** |44.40% | 39.68% | 40.43% | 42.53% | 34.76% | **40.36%** |
| **exp-vulnerable-postgres-db-1** |3.27% | 4.18% | 3.94% | 5.28% | 2.67% | **3.87%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |552.63 MiB | 605.67 MiB | 652.73 MiB | 647.10 MiB | 691.10 MiB | **629.85 MiB** |
| **exp-vulnerable-mongo-db-1** |216.74 MiB | 239.48 MiB | 208.13 MiB | 212.35 MiB | 226.22 MiB | **220.58 MiB** |
| **exp-vulnerable-ms-catalogo-1** |47.56 MiB | 60.17 MiB | 77.84 MiB | 47.18 MiB | 59.21 MiB | **58.39 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.98 MiB | 58.06 MiB | 81.59 MiB | 46.75 MiB | 71.23 MiB | **60.92 MiB** |
| **exp-vulnerable-ms-resenas-1** |736.67 MiB | 668.96 MiB | 690.52 MiB | 730.27 MiB | 643.76 MiB | **694.04 MiB** |
| **exp-vulnerable-ms-usuarios-1** |780.00 MiB | 1149.97 MiB | 767.76 MiB | 1171.31 MiB | 707.47 MiB | **915.30 MiB** |
| **exp-vulnerable-postgres-db-1** |72.39 MiB | 84.43 MiB | 87.82 MiB | 77.80 MiB | 77.99 MiB | **80.09 MiB** |