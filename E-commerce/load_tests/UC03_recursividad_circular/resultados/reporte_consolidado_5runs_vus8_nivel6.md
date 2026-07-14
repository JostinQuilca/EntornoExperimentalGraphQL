# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 21:52:17

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 9 | 55523.716 ms | 100.00% | 0.00% |
| Run 2 | 9 | 55000.474 ms | 100.00% | 0.00% |
| Run 3 | 9 | 55003.174 ms | 100.00% | 0.00% |
| Run 4 | 9 | 55000.154 ms | 100.00% | 0.00% |
| Run 5 | 9 | 55002.786 ms | 100.00% | 0.00% |
| **PROMEDIO** | **9.0** | **55106.061 ms** | **100.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |14.65% | 1.75% | 29.00% | 19.64% | 38.95% | **20.80%** |
| **exp-vulnerable-mongo-db-1** |122.71% | 123.96% | 123.84% | 132.55% | 116.40% | **123.89%** |
| **exp-vulnerable-ms-catalogo-1** |6.17% | 5.34% | 12.60% | 10.06% | 8.40% | **8.51%** |
| **exp-vulnerable-ms-ordenes-1** |10.04% | 5.66% | 7.25% | 8.40% | 7.49% | **7.77%** |
| **exp-vulnerable-ms-resenas-1** |238.40% | 276.92% | 263.34% | 274.44% | 227.14% | **256.05%** |
| **exp-vulnerable-ms-usuarios-1** |6.35% | 56.30% | 45.67% | 6.71% | 8.62% | **24.73%** |
| **exp-vulnerable-postgres-db-1** |12.91% | 7.79% | 7.63% | 14.42% | 61.11% | **20.77%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |73.41MiB (73.41 MiB)  | 70.96MiB (70.96 MiB)  | 73.82MiB (73.82 MiB)  | 73.14MiB (73.14 MiB)  | 96.44MiB (96.44 MiB)  |
| **exp-vulnerable-mongo-db-1** |354.4MiB (354.40 MiB)  | 343.3MiB (343.30 MiB)  | 350.1MiB (350.10 MiB)  | 351.4MiB (351.40 MiB)  | 350.8MiB (350.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.91MiB (45.91 MiB)  | 48.38MiB (48.38 MiB)  | 45.96MiB (45.96 MiB)  | 49.35MiB (49.35 MiB)  | 46.49MiB (46.49 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.03MiB (46.03 MiB)  | 46.96MiB (46.96 MiB)  | 46.98MiB (46.98 MiB)  | 47.61MiB (47.61 MiB)  | 53.82MiB (53.82 MiB)  |
| **exp-vulnerable-ms-resenas-1** |1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |73.13MiB (73.13 MiB)  | 69.79MiB (69.79 MiB)  | 69.3MiB (69.30 MiB)  | 67.77MiB (67.77 MiB)  | 73.76MiB (73.76 MiB)  |
| **exp-vulnerable-postgres-db-1** |70MiB (70.00 MiB)  | 74.98MiB (74.98 MiB)  | 75.96MiB (75.96 MiB)  | 69.6MiB (69.60 MiB)  | 68.22MiB (68.22 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.39% | 0.07% | 1.44% | 0.93% | 1.34% | **0.83%** |
| **exp-vulnerable-mongo-db-1** |43.78% | 40.62% | 38.44% | 37.95% | 38.30% | **39.82%** |
| **exp-vulnerable-ms-catalogo-1** |1.46% | 1.48% | 1.44% | 2.01% | 1.70% | **1.62%** |
| **exp-vulnerable-ms-ordenes-1** |1.64% | 1.49% | 1.51% | 1.76% | 1.79% | **1.64%** |
| **exp-vulnerable-ms-resenas-1** |76.02% | 95.04% | 81.33% | 87.65% | 95.65% | **87.14%** |
| **exp-vulnerable-ms-usuarios-1** |1.54% | 2.95% | 2.63% | 1.69% | 1.93% | **2.15%** |
| **exp-vulnerable-postgres-db-1** |2.17% | 2.06% | 2.01% | 2.64% | 3.89% | **2.55%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |71.21 MiB | 69.37 MiB | 66.09 MiB | 66.17 MiB | 67.50 MiB | **68.07 MiB** |
| **exp-vulnerable-mongo-db-1** |243.27 MiB | 208.93 MiB | 219.98 MiB | 228.90 MiB | 228.84 MiB | **225.98 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.70 MiB | 46.87 MiB | 45.81 MiB | 49.19 MiB | 46.34 MiB | **46.78 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.62 MiB | 46.81 MiB | 45.94 MiB | 46.07 MiB | 46.10 MiB | **46.11 MiB** |
| **exp-vulnerable-ms-resenas-1** |983.10 MiB | 952.07 MiB | 984.68 MiB | 980.84 MiB | 928.80 MiB | **965.90 MiB** |
| **exp-vulnerable-ms-usuarios-1** |71.14 MiB | 68.41 MiB | 68.95 MiB | 60.20 MiB | 72.91 MiB | **68.32 MiB** |
| **exp-vulnerable-postgres-db-1** |68.96 MiB | 72.43 MiB | 68.56 MiB | 66.28 MiB | 65.65 MiB | **68.38 MiB** |