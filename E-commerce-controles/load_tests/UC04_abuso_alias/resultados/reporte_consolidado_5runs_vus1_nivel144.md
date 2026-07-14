# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 02:12:59

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 35 | 733.161 ms | 0.00% | 0.00% |
| Run 2 | 34 | 798.972 ms | 0.00% | 0.00% |
| Run 3 | 35 | 741.709 ms | 0.00% | 0.00% |
| Run 4 | 35 | 744.810 ms | 0.00% | 0.00% |
| Run 5 | 36 | 690.493 ms | 0.00% | 0.00% |
| **PROMEDIO** | **35.0** | **741.829 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |7.36% | 31.28% | 23.14% | 18.75% | 18.49% | **19.80%** |
| **exp-protegido-mongo-db-1** |87.10% | 113.62% | 113.12% | 131.12% | 90.80% | **107.15%** |
| **exp-protegido-ms-catalogo-1** |5.26% | 6.99% | 18.52% | 12.61% | 3.85% | **9.45%** |
| **exp-protegido-ms-ordenes-1** |28.17% | 34.27% | 19.16% | 33.60% | 14.00% | **25.84%** |
| **exp-protegido-ms-resenas-1** |5.85% | 10.28% | 5.34% | 4.88% | 4.01% | **6.07%** |
| **exp-protegido-ms-usuarios-1** |5.58% | 15.84% | 5.32% | 8.32% | 3.81% | **7.77%** |
| **exp-protegido-postgres-db-1** |53.07% | 138.81% | 54.03% | 129.05% | 38.43% | **82.68%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |70.01MiB (70.01 MiB)  | 70.75MiB (70.75 MiB)  | 70.76MiB (70.76 MiB)  | 70.1MiB (70.10 MiB)  | 70.81MiB (70.81 MiB)  |
| **exp-protegido-mongo-db-1** |334.7MiB (334.70 MiB)  | 350.5MiB (350.50 MiB)  | 345.6MiB (345.60 MiB)  | 349.6MiB (349.60 MiB)  | 349.7MiB (349.70 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.32MiB (46.32 MiB)  | 47.05MiB (47.05 MiB)  | 46.32MiB (46.32 MiB)  | 48.36MiB (48.36 MiB)  | 47.51MiB (47.51 MiB)  |
| **exp-protegido-ms-ordenes-1** |86.2MiB (86.20 MiB)  | 87.77MiB (87.77 MiB)  | 89.21MiB (89.21 MiB)  | 87.34MiB (87.34 MiB)  | 87.15MiB (87.15 MiB)  |
| **exp-protegido-ms-resenas-1** |46.62MiB (46.62 MiB)  | 49.42MiB (49.42 MiB)  | 45.79MiB (45.79 MiB)  | 46.61MiB (46.61 MiB)  | 45.9MiB (45.90 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.18MiB (46.18 MiB)  | 47MiB (47.00 MiB)  | 47.38MiB (47.38 MiB)  | 48.46MiB (48.46 MiB)  | 45.8MiB (45.80 MiB)  |
| **exp-protegido-postgres-db-1** |39.45MiB (39.45 MiB)  | 38MiB (38.00 MiB)  | 39.54MiB (39.54 MiB)  | 37.71MiB (37.71 MiB)  | 38.02MiB (38.02 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.69% | 3.30% | 2.48% | 2.10% | 1.65% | **2.24%** |
| **exp-protegido-mongo-db-1** |25.12% | 46.09% | 20.89% | 33.82% | 21.20% | **29.42%** |
| **exp-protegido-ms-catalogo-1** |1.28% | 1.45% | 1.63% | 1.67% | 1.00% | **1.41%** |
| **exp-protegido-ms-ordenes-1** |9.49% | 11.72% | 8.78% | 9.88% | 7.50% | **9.47%** |
| **exp-protegido-ms-resenas-1** |1.35% | 1.78% | 1.45% | 1.30% | 1.12% | **1.40%** |
| **exp-protegido-ms-usuarios-1** |1.64% | 1.89% | 1.42% | 1.57% | 1.06% | **1.52%** |
| **exp-protegido-postgres-db-1** |21.84% | 31.31% | 21.25% | 25.23% | 18.64% | **23.65%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.71 MiB | 68.46 MiB | 68.80 MiB | 68.18 MiB | 68.65 MiB | **68.36 MiB** |
| **exp-protegido-mongo-db-1** |210.45 MiB | 220.95 MiB | 213.64 MiB | 218.73 MiB | 216.53 MiB | **216.06 MiB** |
| **exp-protegido-ms-catalogo-1** |46.22 MiB | 46.95 MiB | 46.23 MiB | 47.94 MiB | 46.93 MiB | **46.85 MiB** |
| **exp-protegido-ms-ordenes-1** |73.51 MiB | 72.58 MiB | 75.25 MiB | 74.59 MiB | 74.46 MiB | **74.08 MiB** |
| **exp-protegido-ms-resenas-1** |46.49 MiB | 47.22 MiB | 45.68 MiB | 46.51 MiB | 45.81 MiB | **46.34 MiB** |
| **exp-protegido-ms-usuarios-1** |46.02 MiB | 46.75 MiB | 45.84 MiB | 46.10 MiB | 45.70 MiB | **46.08 MiB** |
| **exp-protegido-postgres-db-1** |37.37 MiB | 37.36 MiB | 37.41 MiB | 37.31 MiB | 37.35 MiB | **37.36 MiB** |