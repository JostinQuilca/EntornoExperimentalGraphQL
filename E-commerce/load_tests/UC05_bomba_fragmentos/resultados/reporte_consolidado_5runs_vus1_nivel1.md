# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 03:02:24

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 47 | 284.862 ms | 0.00% | 0.00% |
| Run 2 | 42 | 432.705 ms | 0.00% | 0.00% |
| Run 3 | 47 | 291.093 ms | 0.00% | 0.00% |
| Run 4 | 47 | 276.144 ms | 0.00% | 0.00% |
| Run 5 | 46 | 309.196 ms | 0.00% | 0.00% |
| **PROMEDIO** | **45.8** | **318.800 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |27.62% | 34.43% | 26.98% | 39.49% | 26.04% | **30.91%** |
| **exp-vulnerable-mongo-db-1** |118.23% | 115.67% | 87.54% | 81.28% | 106.68% | **101.88%** |
| **exp-vulnerable-ms-catalogo-1** |6.42% | 5.40% | 4.06% | 4.46% | 4.91% | **5.05%** |
| **exp-vulnerable-ms-ordenes-1** |4.92% | 6.10% | 4.32% | 4.69% | 4.89% | **4.98%** |
| **exp-vulnerable-ms-resenas-1** |5.16% | 5.19% | 4.20% | 4.85% | 12.08% | **6.30%** |
| **exp-vulnerable-ms-usuarios-1** |39.98% | 56.20% | 50.41% | 42.15% | 82.52% | **54.25%** |
| **exp-vulnerable-postgres-db-1** |6.02% | 8.13% | 6.93% | 6.20% | 11.93% | **7.84%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |108.2MiB (108.20 MiB)  | 142.9MiB (142.90 MiB)  | 184.3MiB (184.30 MiB)  | 178.5MiB (178.50 MiB)  | 109.2MiB (109.20 MiB)  |
| **exp-vulnerable-mongo-db-1** |350.2MiB (350.20 MiB)  | 350.1MiB (350.10 MiB)  | 350.4MiB (350.40 MiB)  | 341.8MiB (341.80 MiB)  | 346.9MiB (346.90 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |53.9MiB (53.90 MiB)  | 45.73MiB (45.73 MiB)  | 47.91MiB (47.91 MiB)  | 45.66MiB (45.66 MiB)  | 46.66MiB (46.66 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |45.66MiB (45.66 MiB)  | 46.41MiB (46.41 MiB)  | 45.39MiB (45.39 MiB)  | 49.04MiB (49.04 MiB)  | 47.7MiB (47.70 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.07MiB (46.07 MiB)  | 46.84MiB (46.84 MiB)  | 45.54MiB (45.54 MiB)  | 48.39MiB (48.39 MiB)  | 46.86MiB (46.86 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |128.4MiB (128.40 MiB)  | 131.7MiB (131.70 MiB)  | 127.1MiB (127.10 MiB)  | 125.8MiB (125.80 MiB)  | 133.1MiB (133.10 MiB)  |
| **exp-vulnerable-postgres-db-1** |30.41MiB (30.41 MiB)  | 31.59MiB (31.59 MiB)  | 31.97MiB (31.97 MiB)  | 30.23MiB (30.23 MiB)  | 30.2MiB (30.20 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |12.42% | 13.32% | 9.25% | 10.28% | 13.45% | **11.74%** |
| **exp-vulnerable-mongo-db-1** |27.28% | 35.11% | 20.29% | 17.53% | 22.61% | **24.56%** |
| **exp-vulnerable-ms-catalogo-1** |1.34% | 1.16% | 1.11% | 1.17% | 1.37% | **1.23%** |
| **exp-vulnerable-ms-ordenes-1** |1.11% | 1.51% | 1.08% | 1.14% | 1.20% | **1.21%** |
| **exp-vulnerable-ms-resenas-1** |1.10% | 1.25% | 1.09% | 1.13% | 1.59% | **1.23%** |
| **exp-vulnerable-ms-usuarios-1** |19.11% | 22.24% | 19.60% | 18.39% | 20.57% | **19.98%** |
| **exp-vulnerable-postgres-db-1** |2.02% | 2.34% | 1.94% | 2.00% | 2.06% | **2.07%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |100.61 MiB | 115.34 MiB | 136.42 MiB | 117.83 MiB | 100.46 MiB | **114.13 MiB** |
| **exp-vulnerable-mongo-db-1** |225.39 MiB | 226.14 MiB | 210.84 MiB | 198.38 MiB | 211.26 MiB | **214.40 MiB** |
| **exp-vulnerable-ms-catalogo-1** |53.85 MiB | 45.63 MiB | 46.12 MiB | 45.51 MiB | 46.53 MiB | **47.53 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.55 MiB | 46.29 MiB | 45.28 MiB | 45.83 MiB | 46.05 MiB | **45.80 MiB** |
| **exp-vulnerable-ms-resenas-1** |45.94 MiB | 46.73 MiB | 45.42 MiB | 46.11 MiB | 45.40 MiB | **45.92 MiB** |
| **exp-vulnerable-ms-usuarios-1** |119.62 MiB | 119.71 MiB | 118.78 MiB | 118.56 MiB | 120.69 MiB | **119.47 MiB** |
| **exp-vulnerable-postgres-db-1** |30.08 MiB | 30.21 MiB | 30.30 MiB | 30.18 MiB | 30.19 MiB | **30.19 MiB** |