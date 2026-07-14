# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc05_fragmentos_nivel
**Fecha de Consolidación:** 2026-07-11 03:53:39

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 43 | 406.862 ms | 0.00% | 0.00% |
| Run 2 | 47 | 281.612 ms | 0.00% | 0.00% |
| Run 3 | 47 | 291.662 ms | 0.00% | 0.00% |
| Run 4 | 47 | 275.130 ms | 0.00% | 0.00% |
| Run 5 | 47 | 297.651 ms | 0.00% | 0.00% |
| **PROMEDIO** | **46.2** | **310.584 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |39.08% | 27.98% | 23.89% | 18.41% | 27.40% | **27.35%** |
| **exp-protegido-mongo-db-1** |126.73% | 78.08% | 79.56% | 72.93% | 91.20% | **89.70%** |
| **exp-protegido-ms-catalogo-1** |5.84% | 4.39% | 4.02% | 12.14% | 5.52% | **6.38%** |
| **exp-protegido-ms-ordenes-1** |6.41% | 3.76% | 4.08% | 4.43% | 4.34% | **4.60%** |
| **exp-protegido-ms-resenas-1** |6.28% | 4.24% | 4.41% | 4.01% | 4.15% | **4.62%** |
| **exp-protegido-ms-usuarios-1** |47.75% | 44.56% | 43.43% | 44.50% | 37.57% | **43.56%** |
| **exp-protegido-postgres-db-1** |8.38% | 6.08% | 5.60% | 5.45% | 7.27% | **6.56%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |110.4MiB (110.40 MiB)  | 106.4MiB (106.40 MiB)  | 106.6MiB (106.60 MiB)  | 105.7MiB (105.70 MiB)  | 111.2MiB (111.20 MiB)  |
| **exp-protegido-mongo-db-1** |343.6MiB (343.60 MiB)  | 343.4MiB (343.40 MiB)  | 342.6MiB (342.60 MiB)  | 339.7MiB (339.70 MiB)  | 349.8MiB (349.80 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.45MiB (46.45 MiB)  | 48.44MiB (48.44 MiB)  | 47.34MiB (47.34 MiB)  | 47.15MiB (47.15 MiB)  | 47.26MiB (47.26 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.21MiB (46.21 MiB)  | 48.34MiB (48.34 MiB)  | 45.5MiB (45.50 MiB)  | 45.7MiB (45.70 MiB)  | 46.55MiB (46.55 MiB)  |
| **exp-protegido-ms-resenas-1** |45.83MiB (45.83 MiB)  | 46.19MiB (46.19 MiB)  | 46.36MiB (46.36 MiB)  | 46.4MiB (46.40 MiB)  | 45.63MiB (45.63 MiB)  |
| **exp-protegido-ms-usuarios-1** |129.7MiB (129.70 MiB)  | 131.6MiB (131.60 MiB)  | 137.8MiB (137.80 MiB)  | 128.4MiB (128.40 MiB)  | 125.6MiB (125.60 MiB)  |
| **exp-protegido-postgres-db-1** |30.2MiB (30.20 MiB)  | 32.14MiB (32.14 MiB)  | 31.7MiB (31.70 MiB)  | 30.24MiB (30.24 MiB)  | 30.48MiB (30.48 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |14.46% | 12.63% | 12.47% | 11.52% | 13.45% | **12.91%** |
| **exp-protegido-mongo-db-1** |26.84% | 21.69% | 22.16% | 17.88% | 23.49% | **22.41%** |
| **exp-protegido-ms-catalogo-1** |1.39% | 1.02% | 1.00% | 1.40% | 1.13% | **1.19%** |
| **exp-protegido-ms-ordenes-1** |1.44% | 1.16% | 1.18% | 1.23% | 1.07% | **1.22%** |
| **exp-protegido-ms-resenas-1** |1.58% | 1.20% | 1.12% | 1.16% | 1.08% | **1.23%** |
| **exp-protegido-ms-usuarios-1** |18.01% | 19.07% | 18.23% | 18.64% | 19.31% | **18.65%** |
| **exp-protegido-postgres-db-1** |2.58% | 1.96% | 1.95% | 1.90% | 2.00% | **2.08%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |101.99 MiB | 100.88 MiB | 100.83 MiB | 101.01 MiB | 101.27 MiB | **101.20 MiB** |
| **exp-protegido-mongo-db-1** |199.66 MiB | 215.60 MiB | 210.01 MiB | 202.35 MiB | 204.67 MiB | **206.46 MiB** |
| **exp-protegido-ms-catalogo-1** |46.32 MiB | 47.35 MiB | 46.59 MiB | 47.04 MiB | 45.90 MiB | **46.64 MiB** |
| **exp-protegido-ms-ordenes-1** |46.09 MiB | 46.43 MiB | 45.41 MiB | 45.58 MiB | 46.45 MiB | **45.99 MiB** |
| **exp-protegido-ms-resenas-1** |45.71 MiB | 46.10 MiB | 46.18 MiB | 46.30 MiB | 45.53 MiB | **45.96 MiB** |
| **exp-protegido-ms-usuarios-1** |120.81 MiB | 121.67 MiB | 126.75 MiB | 120.88 MiB | 117.56 MiB | **121.53 MiB** |
| **exp-protegido-postgres-db-1** |30.17 MiB | 30.19 MiB | 30.26 MiB | 30.18 MiB | 30.20 MiB | **30.20 MiB** |