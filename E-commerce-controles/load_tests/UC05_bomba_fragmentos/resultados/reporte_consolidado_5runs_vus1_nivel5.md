# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 04:13:36

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 46 | 314.164 ms | 0.00% | 0.00% |
| Run 2 | 47 | 286.545 ms | 0.00% | 0.00% |
| Run 3 | 47 | 287.827 ms | 0.00% | 0.00% |
| Run 4 | 47 | 281.882 ms | 0.00% | 0.00% |
| Run 5 | 47 | 293.745 ms | 0.00% | 0.00% |
| **PROMEDIO** | **46.8** | **292.833 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |29.68% | 39.65% | 24.71% | 25.42% | 31.60% | **30.21%** |
| **exp-protegido-mongo-db-1** |110.85% | 74.23% | 87.12% | 77.76% | 85.07% | **87.01%** |
| **exp-protegido-ms-catalogo-1** |13.83% | 4.18% | 9.56% | 3.37% | 4.28% | **7.04%** |
| **exp-protegido-ms-ordenes-1** |4.78% | 3.68% | 4.51% | 4.43% | 3.47% | **4.17%** |
| **exp-protegido-ms-resenas-1** |5.29% | 3.65% | 4.52% | 4.27% | 4.51% | **4.45%** |
| **exp-protegido-ms-usuarios-1** |45.96% | 43.28% | 32.68% | 40.33% | 50.50% | **42.55%** |
| **exp-protegido-postgres-db-1** |6.22% | 4.75% | 5.05% | 5.57% | 5.61% | **5.44%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |184.9MiB (184.90 MiB)  | 111.4MiB (111.40 MiB)  | 110.9MiB (110.90 MiB)  | 106.4MiB (106.40 MiB)  | 106.8MiB (106.80 MiB)  |
| **exp-protegido-mongo-db-1** |350MiB (350.00 MiB)  | 339.7MiB (339.70 MiB)  | 349.5MiB (349.50 MiB)  | 336MiB (336.00 MiB)  | 349.7MiB (349.70 MiB)  |
| **exp-protegido-ms-catalogo-1** |55.29MiB (55.29 MiB)  | 45.67MiB (45.67 MiB)  | 47.42MiB (47.42 MiB)  | 45.84MiB (45.84 MiB)  | 46.39MiB (46.39 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.84MiB (46.84 MiB)  | 46.5MiB (46.50 MiB)  | 48.17MiB (48.17 MiB)  | 46.6MiB (46.60 MiB)  | 47.68MiB (47.68 MiB)  |
| **exp-protegido-ms-resenas-1** |45.85MiB (45.85 MiB)  | 46.14MiB (46.14 MiB)  | 49.27MiB (49.27 MiB)  | 47.99MiB (47.99 MiB)  | 47.04MiB (47.04 MiB)  |
| **exp-protegido-ms-usuarios-1** |138MiB (138.00 MiB)  | 131.6MiB (131.60 MiB)  | 133.2MiB (133.20 MiB)  | 128.1MiB (128.10 MiB)  | 130.4MiB (130.40 MiB)  |
| **exp-protegido-postgres-db-1** |30.17MiB (30.17 MiB)  | 30.18MiB (30.18 MiB)  | 30.19MiB (30.19 MiB)  | 30.12MiB (30.12 MiB)  | 30.27MiB (30.27 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |10.23% | 12.36% | 12.49% | 10.91% | 14.52% | **12.10%** |
| **exp-protegido-mongo-db-1** |31.85% | 19.34% | 21.13% | 21.70% | 21.90% | **23.18%** |
| **exp-protegido-ms-catalogo-1** |1.57% | 1.04% | 1.30% | 0.92% | 1.04% | **1.17%** |
| **exp-protegido-ms-ordenes-1** |1.47% | 1.08% | 1.07% | 1.19% | 1.19% | **1.20%** |
| **exp-protegido-ms-resenas-1** |1.49% | 0.98% | 1.18% | 0.99% | 1.40% | **1.21%** |
| **exp-protegido-ms-usuarios-1** |18.47% | 19.45% | 18.04% | 18.79% | 19.42% | **18.83%** |
| **exp-protegido-postgres-db-1** |2.23% | 1.69% | 1.62% | 1.84% | 1.97% | **1.87%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |130.58 MiB | 102.96 MiB | 101.18 MiB | 100.69 MiB | 101.56 MiB | **107.39 MiB** |
| **exp-protegido-mongo-db-1** |215.02 MiB | 205.94 MiB | 207.77 MiB | 205.05 MiB | 207.66 MiB | **208.29 MiB** |
| **exp-protegido-ms-catalogo-1** |46.94 MiB | 45.48 MiB | 46.05 MiB | 45.74 MiB | 46.29 MiB | **46.10 MiB** |
| **exp-protegido-ms-ordenes-1** |46.71 MiB | 46.34 MiB | 47.00 MiB | 45.14 MiB | 46.28 MiB | **46.29 MiB** |
| **exp-protegido-ms-resenas-1** |45.71 MiB | 46.04 MiB | 47.52 MiB | 45.80 MiB | 45.78 MiB | **46.17 MiB** |
| **exp-protegido-ms-usuarios-1** |123.96 MiB | 123.24 MiB | 119.37 MiB | 118.63 MiB | 121.17 MiB | **121.27 MiB** |
| **exp-protegido-postgres-db-1** |30.02 MiB | 30.17 MiB | 30.09 MiB | 30.11 MiB | 30.25 MiB | **30.13 MiB** |