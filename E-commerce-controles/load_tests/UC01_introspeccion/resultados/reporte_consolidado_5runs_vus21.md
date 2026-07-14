# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=21)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-07 19:27:59

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 1260 | 6.164 ms | 0.00% |
| Run 2 | 1260 | 6.521 ms | 0.00% |
| Run 3 | 1260 | 7.020 ms | 0.00% |
| Run 4 | 867 | 236.601 ms | 0.46% |
| Run 5 | 1260 | 7.221 ms | 0.00% |
| **PROMEDIO** | **1181.4** | **52.706 ms** | **0.09%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |18.43% | 18.39% | 12.31% | 17.51% | 11.37% | **15.60%** |
| **exp-protegido-mongo-db-1** |64.83% | 66.80% | 65.41% | 61.65% | 70.69% | **65.88%** |
| **exp-protegido-ms-catalogo-1** |3.78% | 3.33% | 4.90% | 4.55% | 5.31% | **4.37%** |
| **exp-protegido-ms-ordenes-1** |3.45% | 3.43% | 7.05% | 3.74% | 3.38% | **4.21%** |
| **exp-protegido-ms-resenas-1** |3.54% | 3.60% | 5.79% | 3.48% | 3.41% | **3.96%** |
| **exp-protegido-ms-usuarios-1** |3.15% | 3.72% | 5.76% | 3.79% | 3.38% | **3.96%** |
| **exp-protegido-postgres-db-1** |4.28% | 5.05% | 4.29% | 3.78% | 8.33% | **5.15%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |97.92MiB (97.92 MiB)  | 87.33MiB (87.33 MiB)  | 85.85MiB (85.85 MiB)  | 85.24MiB (85.24 MiB)  | 87.14MiB (87.14 MiB)  |
| **exp-protegido-mongo-db-1** |340.7MiB (340.70 MiB)  | 340.8MiB (340.80 MiB)  | 332.8MiB (332.80 MiB)  | 332.5MiB (332.50 MiB)  | 343MiB (343.00 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.48MiB (46.48 MiB)  | 45.53MiB (45.53 MiB)  | 45.89MiB (45.89 MiB)  | 45.98MiB (45.98 MiB)  | 45.94MiB (45.94 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.21MiB (46.21 MiB)  | 45.88MiB (45.88 MiB)  | 53.81MiB (53.81 MiB)  | 46.64MiB (46.64 MiB)  | 47.54MiB (47.54 MiB)  |
| **exp-protegido-ms-resenas-1** |46.05MiB (46.05 MiB)  | 46.86MiB (46.86 MiB)  | 46.39MiB (46.39 MiB)  | 46.81MiB (46.81 MiB)  | 47.09MiB (47.09 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.38MiB (45.38 MiB)  | 46.23MiB (46.23 MiB)  | 46.09MiB (46.09 MiB)  | 46.34MiB (46.34 MiB)  | 47.93MiB (47.93 MiB)  |
| **exp-protegido-postgres-db-1** |27.4MiB (27.40 MiB)  | 29.04MiB (29.04 MiB)  | 27.39MiB (27.39 MiB)  | 27.41MiB (27.41 MiB)  | 27.36MiB (27.36 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |6.49% | 6.18% | 6.50% | 7.70% | 6.14% | **6.60%** |
| **exp-protegido-mongo-db-1** |17.33% | 18.85% | 17.81% | 18.34% | 18.88% | **18.24%** |
| **exp-protegido-ms-catalogo-1** |0.96% | 0.87% | 1.03% | 0.97% | 1.13% | **0.99%** |
| **exp-protegido-ms-ordenes-1** |0.85% | 0.92% | 1.25% | 1.05% | 0.91% | **1.00%** |
| **exp-protegido-ms-resenas-1** |0.74% | 0.97% | 1.04% | 0.95% | 0.86% | **0.91%** |
| **exp-protegido-ms-usuarios-1** |0.85% | 0.91% | 1.00% | 0.90% | 0.88% | **0.91%** |
| **exp-protegido-postgres-db-1** |1.21% | 1.27% | 1.16% | 1.08% | 1.14% | **1.17%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |84.72 MiB | 81.20 MiB | 79.97 MiB | 78.63 MiB | 81.11 MiB | **81.13 MiB** |
| **exp-protegido-mongo-db-1** |196.89 MiB | 202.47 MiB | 197.61 MiB | 202.03 MiB | 195.21 MiB | **198.84 MiB** |
| **exp-protegido-ms-catalogo-1** |45.99 MiB | 45.42 MiB | 45.79 MiB | 45.90 MiB | 45.84 MiB | **45.79 MiB** |
| **exp-protegido-ms-ordenes-1** |46.08 MiB | 45.77 MiB | 53.25 MiB | 46.43 MiB | 45.71 MiB | **47.45 MiB** |
| **exp-protegido-ms-resenas-1** |45.92 MiB | 46.75 MiB | 46.28 MiB | 46.60 MiB | 45.50 MiB | **46.21 MiB** |
| **exp-protegido-ms-usuarios-1** |45.26 MiB | 46.13 MiB | 45.99 MiB | 46.26 MiB | 46.43 MiB | **46.01 MiB** |
| **exp-protegido-postgres-db-1** |27.32 MiB | 27.52 MiB | 27.39 MiB | 27.41 MiB | 27.36 MiB | **27.40 MiB** |