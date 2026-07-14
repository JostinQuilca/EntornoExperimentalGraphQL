# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=5)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 18:20:43

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 300 | 5.707 ms | 0.00% |
| Run 2 | 300 | 6.393 ms | 0.00% |
| Run 3 | 300 | 6.230 ms | 0.00% |
| **PROMEDIO** | **300.0** | **6.110 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |5.98% | 3.32% | 7.36% | **5.55%** |
| **exp-vulnerable-mongo-db-1** |60.74% | 91.01% | 65.53% | **72.43%** |
| **exp-vulnerable-ms-catalogo-1** |3.85% | 3.99% | 3.40% | **3.75%** |
| **exp-vulnerable-ms-ordenes-1** |3.10% | 4.13% | 3.65% | **3.63%** |
| **exp-vulnerable-ms-resenas-1** |3.20% | 4.41% | 3.15% | **3.59%** |
| **exp-vulnerable-ms-usuarios-1** |3.14% | 4.32% | 3.31% | **3.59%** |
| **exp-vulnerable-postgres-db-1** |5.45% | 4.75% | 3.83% | **4.68%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |73.04MiB (73.04 MiB)  | 70.95MiB (70.95 MiB)  | 71.3MiB (71.30 MiB)  |
| **exp-vulnerable-mongo-db-1** |333.7MiB (333.70 MiB)  | 340.1MiB (340.10 MiB)  | 330MiB (330.00 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.7MiB (45.70 MiB)  | 46MiB (46.00 MiB)  | 46.88MiB (46.88 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.02MiB (46.02 MiB)  | 46.18MiB (46.18 MiB)  | 46.5MiB (46.50 MiB)  |
| **exp-vulnerable-ms-resenas-1** |45.5MiB (45.50 MiB)  | 45.97MiB (45.97 MiB)  | 45.93MiB (45.93 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |47.79MiB (47.79 MiB)  | 46.48MiB (46.48 MiB)  | 45.91MiB (45.91 MiB)  |
| **exp-vulnerable-postgres-db-1** |28.96MiB (28.96 MiB)  | 27.45MiB (27.45 MiB)  | 27.57MiB (27.57 MiB)  |