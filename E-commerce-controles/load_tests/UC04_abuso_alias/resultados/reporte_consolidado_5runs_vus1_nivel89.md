# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 01:52:41

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 37 | 656.593 ms | 0.00% | 0.00% |
| Run 2 | 37 | 655.782 ms | 0.00% | 0.00% |
| Run 3 | 37 | 656.750 ms | 0.00% | 0.00% |
| Run 4 | 36 | 673.659 ms | 0.00% | 0.00% |
| Run 5 | 36 | 676.220 ms | 0.00% | 0.00% |
| **PROMEDIO** | **36.6** | **663.801 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |14.25% | 4.70% | 8.08% | 7.31% | 14.82% | **9.83%** |
| **exp-protegido-mongo-db-1** |73.83% | 71.56% | 99.77% | 119.58% | 111.91% | **95.33%** |
| **exp-protegido-ms-catalogo-1** |11.41% | 4.53% | 4.61% | 10.00% | 9.15% | **7.94%** |
| **exp-protegido-ms-ordenes-1** |40.60% | 12.35% | 22.73% | 36.32% | 18.28% | **26.06%** |
| **exp-protegido-ms-resenas-1** |7.37% | 4.95% | 5.62% | 18.55% | 5.96% | **8.49%** |
| **exp-protegido-ms-usuarios-1** |4.27% | 8.99% | 5.05% | 7.13% | 5.98% | **6.28%** |
| **exp-protegido-postgres-db-1** |80.44% | 28.80% | 37.23% | 64.97% | 37.67% | **49.82%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |68.69MiB (68.69 MiB)  | 68.18MiB (68.18 MiB)  | 67.54MiB (67.54 MiB)  | 67.66MiB (67.66 MiB)  | 68.16MiB (68.16 MiB)  |
| **exp-protegido-mongo-db-1** |334.7MiB (334.70 MiB)  | 345MiB (345.00 MiB)  | 345.9MiB (345.90 MiB)  | 349.2MiB (349.20 MiB)  | 351.2MiB (351.20 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.55MiB (46.55 MiB)  | 45.33MiB (45.33 MiB)  | 46.39MiB (46.39 MiB)  | 47.12MiB (47.12 MiB)  | 47.61MiB (47.61 MiB)  |
| **exp-protegido-ms-ordenes-1** |72.61MiB (72.61 MiB)  | 72.51MiB (72.51 MiB)  | 72.51MiB (72.51 MiB)  | 72.17MiB (72.17 MiB)  | 70.7MiB (70.70 MiB)  |
| **exp-protegido-ms-resenas-1** |46.45MiB (46.45 MiB)  | 46.43MiB (46.43 MiB)  | 45.96MiB (45.96 MiB)  | 45.64MiB (45.64 MiB)  | 45.74MiB (45.74 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.52MiB (45.52 MiB)  | 47.09MiB (47.09 MiB)  | 47.23MiB (47.23 MiB)  | 46.65MiB (46.65 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-protegido-postgres-db-1** |38.58MiB (38.58 MiB)  | 39.15MiB (39.15 MiB)  | 37.92MiB (37.92 MiB)  | 39.87MiB (39.87 MiB)  | 38.18MiB (38.18 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.46% | 1.08% | 1.35% | 1.29% | 2.02% | **1.44%** |
| **exp-protegido-mongo-db-1** |19.97% | 16.57% | 18.15% | 31.62% | 28.55% | **22.97%** |
| **exp-protegido-ms-catalogo-1** |1.33% | 1.15% | 1.17% | 1.44% | 1.83% | **1.38%** |
| **exp-protegido-ms-ordenes-1** |7.36% | 5.98% | 6.83% | 7.40% | 6.23% | **6.76%** |
| **exp-protegido-ms-resenas-1** |1.32% | 1.32% | 1.26% | 1.93% | 1.18% | **1.40%** |
| **exp-protegido-ms-usuarios-1** |1.34% | 1.51% | 1.20% | 1.41% | 1.16% | **1.32%** |
| **exp-protegido-postgres-db-1** |16.33% | 13.20% | 14.25% | 16.47% | 13.40% | **14.73%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |66.68 MiB | 66.54 MiB | 65.85 MiB | 65.91 MiB | 66.68 MiB | **66.33 MiB** |
| **exp-protegido-mongo-db-1** |198.43 MiB | 207.60 MiB | 214.88 MiB | 200.81 MiB | 205.28 MiB | **205.40 MiB** |
| **exp-protegido-ms-catalogo-1** |46.42 MiB | 45.22 MiB | 46.29 MiB | 47.02 MiB | 46.74 MiB | **46.34 MiB** |
| **exp-protegido-ms-ordenes-1** |65.84 MiB | 65.76 MiB | 64.93 MiB | 65.53 MiB | 64.91 MiB | **65.39 MiB** |
| **exp-protegido-ms-resenas-1** |46.28 MiB | 46.26 MiB | 45.86 MiB | 45.50 MiB | 45.65 MiB | **45.91 MiB** |
| **exp-protegido-ms-usuarios-1** |45.39 MiB | 45.87 MiB | 47.14 MiB | 46.38 MiB | 45.98 MiB | **46.15 MiB** |
| **exp-protegido-postgres-db-1** |37.29 MiB | 37.39 MiB | 37.32 MiB | 37.44 MiB | 37.31 MiB | **37.35 MiB** |