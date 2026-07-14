# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 01:32:29

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 37 | 636.366 ms | 0.00% | 0.00% |
| Run 2 | 38 | 615.837 ms | 0.00% | 0.00% |
| Run 3 | 38 | 616.164 ms | 0.00% | 0.00% |
| Run 4 | 38 | 617.804 ms | 0.00% | 0.00% |
| Run 5 | 38 | 616.005 ms | 0.00% | 0.00% |
| **PROMEDIO** | **37.8** | **620.435 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |17.59% | 4.27% | 2.67% | 11.52% | 11.13% | **9.44%** |
| **exp-protegido-mongo-db-1** |117.03% | 88.30% | 77.94% | 111.23% | 80.99% | **95.10%** |
| **exp-protegido-ms-catalogo-1** |4.68% | 4.55% | 4.27% | 7.24% | 5.34% | **5.22%** |
| **exp-protegido-ms-ordenes-1** |12.58% | 8.87% | 9.02% | 11.79% | 7.48% | **9.95%** |
| **exp-protegido-ms-resenas-1** |4.91% | 5.55% | 4.57% | 4.69% | 4.21% | **4.79%** |
| **exp-protegido-ms-usuarios-1** |4.64% | 3.88% | 4.81% | 4.89% | 4.06% | **4.46%** |
| **exp-protegido-postgres-db-1** |20.71% | 18.47% | 17.00% | 34.77% | 17.52% | **21.69%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |97.59MiB (97.59 MiB)  | 67.62MiB (67.62 MiB)  | 67.42MiB (67.42 MiB)  | 67.07MiB (67.07 MiB)  | 66.81MiB (66.81 MiB)  |
| **exp-protegido-mongo-db-1** |341.3MiB (341.30 MiB)  | 349MiB (349.00 MiB)  | 350.2MiB (350.20 MiB)  | 351.5MiB (351.50 MiB)  | 346.4MiB (346.40 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.45MiB (46.45 MiB)  | 48.36MiB (48.36 MiB)  | 46.78MiB (46.78 MiB)  | 47.3MiB (47.30 MiB)  | 47.42MiB (47.42 MiB)  |
| **exp-protegido-ms-ordenes-1** |62MiB (62.00 MiB)  | 62.29MiB (62.29 MiB)  | 63.44MiB (63.44 MiB)  | 62.64MiB (62.64 MiB)  | 58.45MiB (58.45 MiB)  |
| **exp-protegido-ms-resenas-1** |46.38MiB (46.38 MiB)  | 48.63MiB (48.63 MiB)  | 54.64MiB (54.64 MiB)  | 47.38MiB (47.38 MiB)  | 48.52MiB (48.52 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.35MiB (46.35 MiB)  | 47.8MiB (47.80 MiB)  | 46.27MiB (46.27 MiB)  | 46.58MiB (46.58 MiB)  | 46.87MiB (46.87 MiB)  |
| **exp-protegido-postgres-db-1** |37.84MiB (37.84 MiB)  | 37.97MiB (37.97 MiB)  | 38MiB (38.00 MiB)  | 39.15MiB (39.15 MiB)  | 38.21MiB (38.21 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.19% | 1.08% | 0.86% | 1.22% | 1.29% | **1.33%** |
| **exp-protegido-mongo-db-1** |27.26% | 21.66% | 22.07% | 22.35% | 23.77% | **23.42%** |
| **exp-protegido-ms-catalogo-1** |1.19% | 0.99% | 1.02% | 1.16% | 1.22% | **1.12%** |
| **exp-protegido-ms-ordenes-1** |4.99% | 4.38% | 4.54% | 4.66% | 4.20% | **4.55%** |
| **exp-protegido-ms-resenas-1** |1.18% | 1.39% | 1.29% | 1.15% | 1.08% | **1.22%** |
| **exp-protegido-ms-usuarios-1** |1.09% | 1.16% | 1.33% | 1.16% | 1.09% | **1.17%** |
| **exp-protegido-postgres-db-1** |9.61% | 8.65% | 9.15% | 9.53% | 8.40% | **9.07%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |69.27 MiB | 66.09 MiB | 65.89 MiB | 66.01 MiB | 65.44 MiB | **66.54 MiB** |
| **exp-protegido-mongo-db-1** |198.14 MiB | 205.65 MiB | 214.60 MiB | 217.03 MiB | 216.57 MiB | **210.40 MiB** |
| **exp-protegido-ms-catalogo-1** |46.32 MiB | 47.04 MiB | 45.97 MiB | 47.15 MiB | 46.03 MiB | **46.50 MiB** |
| **exp-protegido-ms-ordenes-1** |56.17 MiB | 56.57 MiB | 56.93 MiB | 56.62 MiB | 55.28 MiB | **56.31 MiB** |
| **exp-protegido-ms-resenas-1** |46.26 MiB | 48.34 MiB | 53.45 MiB | 46.04 MiB | 47.09 MiB | **48.24 MiB** |
| **exp-protegido-ms-usuarios-1** |46.23 MiB | 46.42 MiB | 45.92 MiB | 45.78 MiB | 46.78 MiB | **46.23 MiB** |
| **exp-protegido-postgres-db-1** |37.19 MiB | 37.36 MiB | 37.39 MiB | 37.38 MiB | 37.37 MiB | **37.34 MiB** |