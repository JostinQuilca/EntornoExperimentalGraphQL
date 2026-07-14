# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=13)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 18:58:54

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 780 | 7.118 ms | 0.00% |
| Run 2 | 780 | 6.287 ms | 0.00% |
| Run 3 | 780 | 7.705 ms | 0.00% |
| **PROMEDIO** | **780.0** | **7.037 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |10.85% | 20.31% | 11.52% | **14.23%** |
| **exp-protegido-mongo-db-1** |60.49% | 57.00% | 56.01% | **57.83%** |
| **exp-protegido-ms-catalogo-1** |3.59% | 3.10% | 3.11% | **3.27%** |
| **exp-protegido-ms-ordenes-1** |5.84% | 4.02% | 2.84% | **4.23%** |
| **exp-protegido-ms-resenas-1** |5.33% | 3.39% | 3.10% | **3.94%** |
| **exp-protegido-ms-usuarios-1** |4.70% | 3.88% | 2.79% | **3.79%** |
| **exp-protegido-postgres-db-1** |5.01% | 4.73% | 4.36% | **4.70%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |84.08MiB (84.08 MiB)  | 83.36MiB (83.36 MiB)  | 84.22MiB (84.22 MiB)  |
| **exp-protegido-mongo-db-1** |348.2MiB (348.20 MiB)  | 340.2MiB (340.20 MiB)  | 342.4MiB (342.40 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.41MiB (46.41 MiB)  | 46.05MiB (46.05 MiB)  | 45.44MiB (45.44 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.82MiB (46.82 MiB)  | 47.08MiB (47.08 MiB)  | 45.58MiB (45.58 MiB)  |
| **exp-protegido-ms-resenas-1** |47.02MiB (47.02 MiB)  | 47.12MiB (47.12 MiB)  | 45.69MiB (45.69 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.75MiB (46.75 MiB)  | 46.13MiB (46.13 MiB)  | 45.89MiB (45.89 MiB)  |
| **exp-protegido-postgres-db-1** |27.94MiB (27.94 MiB)  | 28.1MiB (28.10 MiB)  | 28.01MiB (28.01 MiB)  |