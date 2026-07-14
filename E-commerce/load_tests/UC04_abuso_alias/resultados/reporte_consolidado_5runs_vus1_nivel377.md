# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 02:42:22

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 31 | 940.027 ms | 0.00% | 0.00% |
| Run 2 | 32 | 886.138 ms | 0.00% | 0.00% |
| Run 3 | 33 | 843.214 ms | 0.00% | 0.00% |
| Run 4 | 32 | 900.083 ms | 0.00% | 0.00% |
| Run 5 | 33 | 856.525 ms | 0.00% | 0.00% |
| **PROMEDIO** | **32.2** | **885.197 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |58.65% | 5.56% | 49.13% | 11.43% | 40.58% | **33.07%** |
| **exp-vulnerable-mongo-db-1** |94.25% | 83.93% | 102.30% | 86.49% | 80.36% | **89.47%** |
| **exp-vulnerable-ms-catalogo-1** |4.88% | 4.12% | 4.65% | 3.91% | 4.17% | **4.35%** |
| **exp-vulnerable-ms-ordenes-1** |29.61% | 32.89% | 31.92% | 34.52% | 27.00% | **31.19%** |
| **exp-vulnerable-ms-resenas-1** |4.26% | 4.48% | 4.51% | 4.43% | 8.97% | **5.33%** |
| **exp-vulnerable-ms-usuarios-1** |4.00% | 4.60% | 4.67% | 4.56% | 5.07% | **4.58%** |
| **exp-vulnerable-postgres-db-1** |91.26% | 98.87% | 76.14% | 85.83% | 78.03% | **86.03%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |79.64MiB (79.64 MiB)  | 77.15MiB (77.15 MiB)  | 83.34MiB (83.34 MiB)  | 84.57MiB (84.57 MiB)  | 83.27MiB (83.27 MiB)  |
| **exp-vulnerable-mongo-db-1** |336.7MiB (336.70 MiB)  | 333.5MiB (333.50 MiB)  | 340.2MiB (340.20 MiB)  | 352.4MiB (352.40 MiB)  | 352.8MiB (352.80 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.57MiB (46.57 MiB)  | 46.19MiB (46.19 MiB)  | 47.44MiB (47.44 MiB)  | 45.94MiB (45.94 MiB)  | 47.19MiB (47.19 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |105.7MiB (105.70 MiB)  | 105.2MiB (105.20 MiB)  | 104.9MiB (104.90 MiB)  | 104.3MiB (104.30 MiB)  | 106.5MiB (106.50 MiB)  |
| **exp-vulnerable-ms-resenas-1** |55.79MiB (55.79 MiB)  | 55.21MiB (55.21 MiB)  | 46.95MiB (46.95 MiB)  | 46.01MiB (46.01 MiB)  | 55.37MiB (55.37 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |53.57MiB (53.57 MiB)  | 46.43MiB (46.43 MiB)  | 46.24MiB (46.24 MiB)  | 47.55MiB (47.55 MiB)  | 47.06MiB (47.06 MiB)  |
| **exp-vulnerable-postgres-db-1** |37.84MiB (37.84 MiB)  | 37.88MiB (37.88 MiB)  | 38.12MiB (38.12 MiB)  | 38.12MiB (38.12 MiB)  | 39.38MiB (39.38 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |4.10% | 1.43% | 3.28% | 1.47% | 2.85% | **2.63%** |
| **exp-vulnerable-mongo-db-1** |24.81% | 22.45% | 25.44% | 24.31% | 22.16% | **23.83%** |
| **exp-vulnerable-ms-catalogo-1** |1.15% | 1.05% | 1.10% | 0.97% | 1.02% | **1.06%** |
| **exp-vulnerable-ms-ordenes-1** |13.18% | 14.05% | 12.64% | 14.40% | 13.04% | **13.46%** |
| **exp-vulnerable-ms-resenas-1** |1.29% | 1.17% | 1.09% | 1.18% | 1.33% | **1.21%** |
| **exp-vulnerable-ms-usuarios-1** |1.35% | 1.18% | 1.05% | 1.05% | 1.12% | **1.15%** |
| **exp-vulnerable-postgres-db-1** |34.49% | 42.97% | 34.64% | 41.65% | 38.96% | **38.54%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |74.43 MiB | 73.04 MiB | 77.41 MiB | 76.72 MiB | 80.20 MiB | **76.36 MiB** |
| **exp-vulnerable-mongo-db-1** |214.00 MiB | 201.43 MiB | 206.90 MiB | 223.14 MiB | 208.73 MiB | **210.84 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.32 MiB | 46.06 MiB | 45.70 MiB | 45.82 MiB | 45.78 MiB | **45.94 MiB** |
| **exp-vulnerable-ms-ordenes-1** |96.64 MiB | 96.95 MiB | 96.07 MiB | 95.93 MiB | 96.77 MiB | **96.47 MiB** |
| **exp-vulnerable-ms-resenas-1** |52.61 MiB | 55.17 MiB | 46.51 MiB | 45.89 MiB | 51.79 MiB | **50.39 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.72 MiB | 46.31 MiB | 46.04 MiB | 46.98 MiB | 46.86 MiB | **46.98 MiB** |
| **exp-vulnerable-postgres-db-1** |37.21 MiB | 37.24 MiB | 37.27 MiB | 37.28 MiB | 37.49 MiB | **37.30 MiB** |