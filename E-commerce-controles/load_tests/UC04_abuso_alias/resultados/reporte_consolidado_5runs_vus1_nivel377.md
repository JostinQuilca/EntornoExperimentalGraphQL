# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 02:53:17

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 60 | 8.006 ms | 0.00% | 100.00% |
| Run 2 | 60 | 6.850 ms | 0.00% | 100.00% |
| Run 3 | 60 | 7.336 ms | 0.00% | 100.00% |
| Run 4 | 60 | 7.249 ms | 0.00% | 100.00% |
| Run 5 | 60 | 6.671 ms | 0.00% | 100.00% |
| **PROMEDIO** | **60.0** | **7.223 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |16.36% | 14.54% | 13.88% | 0.61% | 0.74% | **9.23%** |
| **exp-protegido-mongo-db-1** |75.12% | 74.96% | 74.77% | 78.07% | 73.02% | **75.19%** |
| **exp-protegido-ms-catalogo-1** |5.60% | 4.08% | 3.81% | 3.62% | 4.12% | **4.25%** |
| **exp-protegido-ms-ordenes-1** |7.42% | 4.74% | 4.38% | 4.23% | 4.85% | **5.12%** |
| **exp-protegido-ms-resenas-1** |4.85% | 4.37% | 5.12% | 4.44% | 4.84% | **4.72%** |
| **exp-protegido-ms-usuarios-1** |5.12% | 4.53% | 5.09% | 4.21% | 4.69% | **4.73%** |
| **exp-protegido-postgres-db-1** |5.30% | 5.17% | 5.16% | 4.85% | 4.61% | **5.02%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |96.22MiB (96.22 MiB)  | 65.71MiB (65.71 MiB)  | 65.91MiB (65.91 MiB)  | 65.6MiB (65.60 MiB)  | 66.16MiB (66.16 MiB)  |
| **exp-protegido-mongo-db-1** |344.4MiB (344.40 MiB)  | 347MiB (347.00 MiB)  | 334.1MiB (334.10 MiB)  | 339.5MiB (339.50 MiB)  | 336.5MiB (336.50 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.71MiB (46.71 MiB)  | 47.16MiB (47.16 MiB)  | 47.87MiB (47.87 MiB)  | 46.13MiB (46.13 MiB)  | 45.93MiB (45.93 MiB)  |
| **exp-protegido-ms-ordenes-1** |48.46MiB (48.46 MiB)  | 47.63MiB (47.63 MiB)  | 47.49MiB (47.49 MiB)  | 45.71MiB (45.71 MiB)  | 47.51MiB (47.51 MiB)  |
| **exp-protegido-ms-resenas-1** |54.62MiB (54.62 MiB)  | 47.52MiB (47.52 MiB)  | 47.27MiB (47.27 MiB)  | 47.11MiB (47.11 MiB)  | 47.08MiB (47.08 MiB)  |
| **exp-protegido-ms-usuarios-1** |47.5MiB (47.50 MiB)  | 47.7MiB (47.70 MiB)  | 47.7MiB (47.70 MiB)  | 45.98MiB (45.98 MiB)  | 46.34MiB (46.34 MiB)  |
| **exp-protegido-postgres-db-1** |27.55MiB (27.55 MiB)  | 27.36MiB (27.36 MiB)  | 27.32MiB (27.32 MiB)  | 27.4MiB (27.40 MiB)  | 27.43MiB (27.43 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.99% | 0.89% | 0.81% | 0.33% | 0.29% | **0.66%** |
| **exp-protegido-mongo-db-1** |21.49% | 19.68% | 18.97% | 20.62% | 20.26% | **20.20%** |
| **exp-protegido-ms-catalogo-1** |1.18% | 1.01% | 1.01% | 1.05% | 1.01% | **1.05%** |
| **exp-protegido-ms-ordenes-1** |1.46% | 1.32% | 1.29% | 1.03% | 1.09% | **1.24%** |
| **exp-protegido-ms-resenas-1** |1.33% | 1.25% | 1.24% | 1.01% | 1.07% | **1.18%** |
| **exp-protegido-ms-usuarios-1** |1.14% | 1.25% | 1.29% | 1.05% | 1.11% | **1.17%** |
| **exp-protegido-postgres-db-1** |1.70% | 1.43% | 1.46% | 1.29% | 1.37% | **1.45%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |66.84 MiB | 64.97 MiB | 65.19 MiB | 64.97 MiB | 65.00 MiB | **65.39 MiB** |
| **exp-protegido-mongo-db-1** |211.26 MiB | 207.74 MiB | 201.16 MiB | 201.47 MiB | 206.37 MiB | **205.60 MiB** |
| **exp-protegido-ms-catalogo-1** |45.76 MiB | 45.69 MiB | 46.02 MiB | 45.93 MiB | 45.83 MiB | **45.85 MiB** |
| **exp-protegido-ms-ordenes-1** |45.62 MiB | 46.12 MiB | 45.95 MiB | 45.61 MiB | 46.50 MiB | **45.96 MiB** |
| **exp-protegido-ms-resenas-1** |46.45 MiB | 46.22 MiB | 45.97 MiB | 47.01 MiB | 46.77 MiB | **46.48 MiB** |
| **exp-protegido-ms-usuarios-1** |47.32 MiB | 46.75 MiB | 47.41 MiB | 45.89 MiB | 46.00 MiB | **46.67 MiB** |
| **exp-protegido-postgres-db-1** |27.40 MiB | 27.34 MiB | 27.31 MiB | 27.39 MiB | 27.39 MiB | **27.37 MiB** |