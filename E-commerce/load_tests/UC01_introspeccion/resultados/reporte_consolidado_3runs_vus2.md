# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=2)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 17:57:12

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 120 | 5.881 ms | 0.00% |
| Run 2 | 0 | 0.000 ms | 0.00% |
| Run 3 | 120 | 5.696 ms | 0.00% |
| **PROMEDIO** | **80.0** | **3.859 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |16.97% | 1.20% | 10.62% | **9.60%** |
| **exp-vulnerable-mongo-db-1** |73.07% | 52.57% | 80.68% | **68.77%** |
| **exp-vulnerable-ms-catalogo-1** |5.36% | 6.51% | 3.48% | **5.12%** |
| **exp-vulnerable-ms-ordenes-1** |3.31% | 0.00% | 3.18% | **2.16%** |
| **exp-vulnerable-ms-resenas-1** |4.25% | 0.00% | 2.81% | **2.35%** |
| **exp-vulnerable-ms-usuarios-1** |3.26% | 0.00% | 2.91% | **2.06%** |
| **exp-vulnerable-postgres-db-1** |5.63% | 0.05% | 4.67% | **3.45%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |97.05MiB (97.05 MiB)  | 63.75MiB (63.75 MiB)  | 65.85MiB (65.85 MiB)  |
| **exp-vulnerable-mongo-db-1** |344.2MiB (344.20 MiB)  | 187MiB (187.00 MiB)  | 349MiB (349.00 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.16MiB (45.16 MiB)  | 45.66MiB (45.66 MiB)  | 46.14MiB (46.14 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |46.27MiB (46.27 MiB)  | 44.69MiB (44.69 MiB)  | 45.68MiB (45.68 MiB)  |
| **exp-vulnerable-ms-resenas-1** |46.2MiB (46.20 MiB)  | 46.35MiB (46.35 MiB)  | 46.28MiB (46.28 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |46.85MiB (46.85 MiB)  | 46.1MiB (46.10 MiB)  | 45.45MiB (45.45 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.55MiB (27.55 MiB)  | 27.21MiB (27.21 MiB)  | 28.89MiB (28.89 MiB)  |