# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=5)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 18:27:00

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 300 | 6.295 ms | 0.00% |
| Run 2 | 300 | 7.484 ms | 0.00% |
| Run 3 | 300 | 6.304 ms | 0.00% |
| **PROMEDIO** | **300.0** | **6.694 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |4.80% | 5.03% | 9.46% | **6.43%** |
| **exp-protegido-mongo-db-1** |52.57% | 65.62% | 53.02% | **57.07%** |
| **exp-protegido-ms-catalogo-1** |3.07% | 3.84% | 3.74% | **3.55%** |
| **exp-protegido-ms-ordenes-1** |2.96% | 3.82% | 4.36% | **3.71%** |
| **exp-protegido-ms-resenas-1** |3.10% | 4.91% | 3.54% | **3.85%** |
| **exp-protegido-ms-usuarios-1** |3.30% | 4.80% | 3.92% | **4.01%** |
| **exp-protegido-postgres-db-1** |5.46% | 3.55% | 4.32% | **4.44%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |75.51MiB (75.51 MiB)  | 75.72MiB (75.72 MiB)  | 74.72MiB (74.72 MiB)  |
| **exp-protegido-mongo-db-1** |349.7MiB (349.70 MiB)  | 342.5MiB (342.50 MiB)  | 349.8MiB (349.80 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.84MiB (46.84 MiB)  | 45.38MiB (45.38 MiB)  | 45.57MiB (45.57 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.93MiB (45.93 MiB)  | 46.18MiB (46.18 MiB)  | 45.68MiB (45.68 MiB)  |
| **exp-protegido-ms-resenas-1** |45.78MiB (45.78 MiB)  | 46.41MiB (46.41 MiB)  | 46.2MiB (46.20 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.87MiB (46.87 MiB)  | 45.24MiB (45.24 MiB)  | 48.28MiB (48.28 MiB)  |
| **exp-protegido-postgres-db-1** |28MiB (28.00 MiB)  | 27.95MiB (27.95 MiB)  | 29.48MiB (29.48 MiB)  |