# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 03:42:42

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 43 | 419.863 ms | 0.00% | 0.00% |
| Run 2 | 46 | 320.211 ms | 0.00% | 0.00% |
| Run 3 | 45 | 347.373 ms | 0.00% | 0.00% |
| Run 4 | 45 | 343.241 ms | 0.00% | 0.00% |
| Run 5 | 46 | 314.128 ms | 0.00% | 0.00% |
| **PROMEDIO** | **45.0** | **348.963 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |48.20% | 27.37% | 22.99% | 23.88% | 42.97% | **33.08%** |
| **exp-vulnerable-mongo-db-1** |101.00% | 94.02% | 98.79% | 97.12% | 85.49% | **95.28%** |
| **exp-vulnerable-ms-catalogo-1** |9.25% | 5.60% | 4.61% | 5.09% | 4.56% | **5.82%** |
| **exp-vulnerable-ms-ordenes-1** |7.08% | 5.09% | 4.82% | 5.47% | 4.09% | **5.31%** |
| **exp-vulnerable-ms-resenas-1** |6.05% | 4.88% | 5.54% | 4.63% | 5.26% | **5.27%** |
| **exp-vulnerable-ms-usuarios-1** |131.07% | 36.61% | 61.06% | 37.79% | 40.11% | **61.33%** |
| **exp-vulnerable-postgres-db-1** |8.79% | 8.84% | 7.84% | 5.64% | 6.59% | **7.54%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |105.6MiB (105.60 MiB)  | 195.9MiB (195.90 MiB)  | 170.7MiB (170.70 MiB)  | 182.2MiB (182.20 MiB)  | 178.9MiB (178.90 MiB)  |
| **exp-vulnerable-mongo-db-1** |341.1MiB (341.10 MiB)  | 346.3MiB (346.30 MiB)  | 343.1MiB (343.10 MiB)  | 350.3MiB (350.30 MiB)  | 350.7MiB (350.70 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.55MiB (46.55 MiB)  | 46.36MiB (46.36 MiB)  | 46.1MiB (46.10 MiB)  | 45.48MiB (45.48 MiB)  | 47.02MiB (47.02 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.87MiB (46.87 MiB)  | 45.57MiB (45.57 MiB)  | 46.93MiB (46.93 MiB)  | 47.16MiB (47.16 MiB)  | 46.91MiB (46.91 MiB)  |
| **exp-vulnerable-ms-resenas-1** |47.1MiB (47.10 MiB)  | 48.01MiB (48.01 MiB)  | 46.19MiB (46.19 MiB)  | 47.08MiB (47.08 MiB)  | 48.19MiB (48.19 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |135.3MiB (135.30 MiB)  | 136.1MiB (136.10 MiB)  | 134.8MiB (134.80 MiB)  | 124.1MiB (124.10 MiB)  | 123.9MiB (123.90 MiB)  |
| **exp-vulnerable-postgres-db-1** |31.07MiB (31.07 MiB)  | 30.95MiB (30.95 MiB)  | 30.22MiB (30.22 MiB)  | 31.46MiB (31.46 MiB)  | 30.21MiB (30.21 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |17.58% | 9.95% | 9.71% | 10.45% | 12.92% | **12.12%** |
| **exp-vulnerable-mongo-db-1** |25.20% | 26.77% | 24.27% | 25.54% | 19.76% | **24.31%** |
| **exp-vulnerable-ms-catalogo-1** |1.76% | 1.11% | 1.27% | 1.24% | 1.19% | **1.31%** |
| **exp-vulnerable-ms-ordenes-1** |1.81% | 1.24% | 1.25% | 1.46% | 1.08% | **1.37%** |
| **exp-vulnerable-ms-resenas-1** |1.43% | 1.26% | 1.30% | 1.26% | 1.16% | **1.28%** |
| **exp-vulnerable-ms-usuarios-1** |22.75% | 18.86% | 20.17% | 18.84% | 17.21% | **19.57%** |
| **exp-vulnerable-postgres-db-1** |2.72% | 2.15% | 2.41% | 1.74% | 2.09% | **2.22%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |99.63 MiB | 136.25 MiB | 119.64 MiB | 116.56 MiB | 116.17 MiB | **117.65 MiB** |
| **exp-vulnerable-mongo-db-1** |203.37 MiB | 209.35 MiB | 214.62 MiB | 205.65 MiB | 211.98 MiB | **208.99 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.41 MiB | 46.24 MiB | 45.98 MiB | 45.29 MiB | 46.20 MiB | **46.02 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.66 MiB | 45.45 MiB | 45.20 MiB | 47.04 MiB | 46.80 MiB | **46.03 MiB** |
| **exp-vulnerable-ms-resenas-1** |45.87 MiB | 47.90 MiB | 46.09 MiB | 45.72 MiB | 46.42 MiB | **46.40 MiB** |
| **exp-vulnerable-ms-usuarios-1** |119.70 MiB | 124.18 MiB | 124.86 MiB | 116.51 MiB | 116.92 MiB | **120.43 MiB** |
| **exp-vulnerable-postgres-db-1** |30.21 MiB | 30.22 MiB | 30.10 MiB | 30.14 MiB | 30.18 MiB | **30.17 MiB** |