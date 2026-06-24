# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=10)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-22 23:53:57

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 600 | 6.310 ms | 100.00% |
| Run 2 | 600 | 6.208 ms | 100.00% |
| Run 3 | 600 | 6.386 ms | 100.00% |
| **PROMEDIO** | **600.0** | **6.301 ms** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |14.94% | 14.59% | 15.63% | **15.05%** |
| **mongo-db** |61.56% | 64.83% | 50.42% | **58.94%** |
| **ms-catalogo** |6.28% | 3.77% | 3.52% | **4.52%** |
| **ms-ordenes** |4.29% | 3.93% | 4.80% | **4.34%** |
| **ms-resenas** |4.45% | 4.56% | 4.87% | **4.63%** |
| **ms-usuarios** |4.52% | 4.73% | 5.36% | **4.87%** |
| **postgres-db** |5.53% | 5.51% | 5.81% | **5.62%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |85.16MiB (85.16 MiB)  | 87.22MiB (87.22 MiB)  | 85.1MiB (85.10 MiB)  |
| **mongo-db** |333.3MiB (333.30 MiB)  | 340.3MiB (340.30 MiB)  | 325MiB (325.00 MiB)  |
| **ms-catalogo** |52.48MiB (52.48 MiB)  | 51.41MiB (51.41 MiB)  | 51.27MiB (51.27 MiB)  |
| **ms-ordenes** |48.74MiB (48.74 MiB)  | 48.79MiB (48.79 MiB)  | 48.92MiB (48.92 MiB)  |
| **ms-resenas** |49.69MiB (49.69 MiB)  | 49.75MiB (49.75 MiB)  | 49.48MiB (49.48 MiB)  |
| **ms-usuarios** |48.66MiB (48.66 MiB)  | 48.31MiB (48.31 MiB)  | 49.91MiB (49.91 MiB)  |
| **postgres-db** |46.5MiB (46.50 MiB)  | 46.87MiB (46.87 MiB)  | 47.49MiB (47.49 MiB)  |