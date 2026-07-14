# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-10 23:06:15

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 39 | 570.817 ms | 0.00% | 0.00% |
| Run 2 | 39 | 568.437 ms | 0.00% | 0.00% |
| Run 3 | 39 | 567.207 ms | 0.00% | 0.00% |
| Run 4 | 39 | 570.334 ms | 0.00% | 0.00% |
| Run 5 | 39 | 572.555 ms | 0.00% | 0.00% |
| **PROMEDIO** | **39.0** | **569.870 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |3.98% | 3.95% | 4.02% | 4.46% | 1.11% | **3.50%** |
| **exp-protegido-mongo-db-1** |106.66% | 114.31% | 105.31% | 76.43% | 84.95% | **97.53%** |
| **exp-protegido-ms-catalogo-1** |5.18% | 4.73% | 5.17% | 4.39% | 4.31% | **4.76%** |
| **exp-protegido-ms-ordenes-1** |8.53% | 4.78% | 5.26% | 6.42% | 6.74% | **6.35%** |
| **exp-protegido-ms-resenas-1** |7.32% | 4.48% | 4.33% | 4.83% | 5.41% | **5.27%** |
| **exp-protegido-ms-usuarios-1** |4.89% | 10.31% | 4.41% | 5.00% | 4.81% | **5.88%** |
| **exp-protegido-postgres-db-1** |6.33% | 6.30% | 5.68% | 6.46% | 7.70% | **6.49%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.55MiB (65.55 MiB)  | 65.34MiB (65.34 MiB)  | 66.1MiB (66.10 MiB)  | 65.89MiB (65.89 MiB)  | 66.15MiB (66.15 MiB)  |
| **exp-protegido-mongo-db-1** |343.7MiB (343.70 MiB)  | 350.2MiB (350.20 MiB)  | 346.4MiB (346.40 MiB)  | 350.2MiB (350.20 MiB)  | 350.7MiB (350.70 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.88MiB (45.88 MiB)  | 47.73MiB (47.73 MiB)  | 47.39MiB (47.39 MiB)  | 46.14MiB (46.14 MiB)  | 48.83MiB (48.83 MiB)  |
| **exp-protegido-ms-ordenes-1** |51.12MiB (51.12 MiB)  | 49.85MiB (49.85 MiB)  | 48.58MiB (48.58 MiB)  | 48.92MiB (48.92 MiB)  | 50.07MiB (50.07 MiB)  |
| **exp-protegido-ms-resenas-1** |46.82MiB (46.82 MiB)  | 47.46MiB (47.46 MiB)  | 46.09MiB (46.09 MiB)  | 46.56MiB (46.56 MiB)  | 48.12MiB (48.12 MiB)  |
| **exp-protegido-ms-usuarios-1** |47.86MiB (47.86 MiB)  | 46.33MiB (46.33 MiB)  | 46.59MiB (46.59 MiB)  | 46.2MiB (46.20 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-protegido-postgres-db-1** |32.8MiB (32.80 MiB)  | 33MiB (33.00 MiB)  | 33.45MiB (33.45 MiB)  | 32.82MiB (32.82 MiB)  | 32.85MiB (32.85 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.72% | 0.66% | 0.70% | 0.63% | 0.52% | **0.65%** |
| **exp-protegido-mongo-db-1** |27.98% | 31.86% | 26.34% | 22.46% | 22.30% | **26.19%** |
| **exp-protegido-ms-catalogo-1** |1.13% | 1.31% | 1.19% | 1.04% | 1.15% | **1.16%** |
| **exp-protegido-ms-ordenes-1** |2.07% | 1.67% | 1.83% | 1.74% | 1.91% | **1.84%** |
| **exp-protegido-ms-resenas-1** |1.76% | 1.26% | 1.16% | 1.22% | 1.28% | **1.34%** |
| **exp-protegido-ms-usuarios-1** |1.29% | 1.61% | 1.27% | 1.23% | 1.14% | **1.31%** |
| **exp-protegido-postgres-db-1** |1.92% | 1.89% | 1.57% | 1.76% | 1.74% | **1.78%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |64.46 MiB | 64.39 MiB | 65.29 MiB | 65.01 MiB | 65.36 MiB | **64.90 MiB** |
| **exp-protegido-mongo-db-1** |206.95 MiB | 223.27 MiB | 205.55 MiB | 213.77 MiB | 222.65 MiB | **214.44 MiB** |
| **exp-protegido-ms-catalogo-1** |45.75 MiB | 46.28 MiB | 46.01 MiB | 46.04 MiB | 47.55 MiB | **46.33 MiB** |
| **exp-protegido-ms-ordenes-1** |50.45 MiB | 49.07 MiB | 47.92 MiB | 48.13 MiB | 49.37 MiB | **48.99 MiB** |
| **exp-protegido-ms-resenas-1** |46.71 MiB | 47.35 MiB | 45.99 MiB | 46.47 MiB | 48.03 MiB | **46.91 MiB** |
| **exp-protegido-ms-usuarios-1** |46.40 MiB | 46.22 MiB | 46.49 MiB | 45.85 MiB | 45.98 MiB | **46.19 MiB** |
| **exp-protegido-postgres-db-1** |32.40 MiB | 32.46 MiB | 32.45 MiB | 32.44 MiB | 32.42 MiB | **32.43 MiB** |