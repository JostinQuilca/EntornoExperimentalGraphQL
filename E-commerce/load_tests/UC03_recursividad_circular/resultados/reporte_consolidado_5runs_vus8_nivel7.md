# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc03_recursividad_nivel
**Fecha de Consolidación:** 2026-07-10 22:14:12

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 17 | 39655.210 ms | 50.00% | 0.00% |
| Run 2 | 17 | 34154.599 ms | 50.00% | 0.00% |
| Run 3 | 17 | 33026.110 ms | 50.00% | 0.00% |
| Run 4 | 17 | 34723.390 ms | 50.00% | 0.00% |
| Run 5 | 17 | 33960.726 ms | 50.00% | 0.00% |
| **PROMEDIO** | **17.0** | **35104.007 ms** | **50.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |25.55% | 57.77% | 26.77% | 16.43% | 13.84% | **28.07%** |
| **exp-vulnerable-mongo-db-1** |109.62% | 116.71% | 114.12% | 117.97% | 121.22% | **115.93%** |
| **exp-vulnerable-ms-catalogo-1** |7.66% | 13.65% | 8.94% | 6.12% | 4.81% | **8.24%** |
| **exp-vulnerable-ms-ordenes-1** |8.57% | 6.16% | 6.43% | 7.63% | 5.17% | **6.79%** |
| **exp-vulnerable-ms-resenas-1** |288.93% | 272.50% | 295.99% | 228.85% | 245.63% | **266.38%** |
| **exp-vulnerable-ms-usuarios-1** |46.20% | 98.22% | 47.81% | 8.13% | 15.08% | **43.09%** |
| **exp-vulnerable-postgres-db-1** |11.65% | 8.93% | 9.20% | 35.26% | 6.36% | **14.28%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |100.1MiB (100.10 MiB)  | 73.59MiB (73.59 MiB)  | 100.3MiB (100.30 MiB)  | 96.37MiB (96.37 MiB)  | 96.4MiB (96.40 MiB)  |
| **exp-vulnerable-mongo-db-1** |346.4MiB (346.40 MiB)  | 350.8MiB (350.80 MiB)  | 346.7MiB (346.70 MiB)  | 350.2MiB (350.20 MiB)  | 351.6MiB (351.60 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.39MiB (45.39 MiB)  | 47.23MiB (47.23 MiB)  | 46.09MiB (46.09 MiB)  | 47.49MiB (47.49 MiB)  | 46.86MiB (46.86 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |55.25MiB (55.25 MiB)  | 46.59MiB (46.59 MiB)  | 45.14MiB (45.14 MiB)  | 45.95MiB (45.95 MiB)  | 47.76MiB (47.76 MiB)  |
| **exp-vulnerable-ms-resenas-1** |1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |72.82MiB (72.82 MiB)  | 69.57MiB (69.57 MiB)  | 71.7MiB (71.70 MiB)  | 67.79MiB (67.79 MiB)  | 71.2MiB (71.20 MiB)  |
| **exp-vulnerable-postgres-db-1** |69.13MiB (69.13 MiB)  | 69.9MiB (69.90 MiB)  | 73.33MiB (73.33 MiB)  | 70.31MiB (70.31 MiB)  | 70.25MiB (70.25 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.51% | 1.93% | 1.28% | 1.02% | 0.78% | **1.30%** |
| **exp-vulnerable-mongo-db-1** |31.92% | 31.98% | 32.61% | 30.59% | 20.58% | **29.54%** |
| **exp-vulnerable-ms-catalogo-1** |2.56% | 1.85% | 1.78% | 1.90% | 1.36% | **1.89%** |
| **exp-vulnerable-ms-ordenes-1** |1.87% | 1.53% | 1.75% | 1.91% | 1.36% | **1.68%** |
| **exp-vulnerable-ms-resenas-1** |127.01% | 110.98% | 120.37% | 125.33% | 106.85% | **118.11%** |
| **exp-vulnerable-ms-usuarios-1** |3.76% | 4.64% | 3.10% | 2.04% | 1.92% | **3.09%** |
| **exp-vulnerable-postgres-db-1** |3.53% | 2.31% | 2.57% | 3.67% | 1.74% | **2.76%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |71.33 MiB | 70.34 MiB | 73.85 MiB | 67.61 MiB | 67.14 MiB | **70.05 MiB** |
| **exp-vulnerable-mongo-db-1** |214.56 MiB | 233.24 MiB | 222.86 MiB | 239.65 MiB | 236.38 MiB | **229.34 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.22 MiB | 47.10 MiB | 45.96 MiB | 46.35 MiB | 45.53 MiB | **46.03 MiB** |
| **exp-vulnerable-ms-ordenes-1** |53.74 MiB | 46.45 MiB | 45.00 MiB | 45.33 MiB | 46.45 MiB | **47.39 MiB** |
| **exp-vulnerable-ms-resenas-1** |928.54 MiB | 938.53 MiB | 936.50 MiB | 925.67 MiB | 938.55 MiB | **933.56 MiB** |
| **exp-vulnerable-ms-usuarios-1** |72.58 MiB | 68.99 MiB | 71.31 MiB | 65.07 MiB | 61.54 MiB | **67.90 MiB** |
| **exp-vulnerable-postgres-db-1** |65.75 MiB | 65.73 MiB | 66.24 MiB | 66.60 MiB | 66.81 MiB | **66.23 MiB** |