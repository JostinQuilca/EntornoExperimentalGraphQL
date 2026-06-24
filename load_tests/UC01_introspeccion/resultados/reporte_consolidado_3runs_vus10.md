# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=10)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-06-22 08:56:53

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 600 | 9.990 ms | 0.00% |
| Run 2 | 600 | 5.981 ms | 0.00% |
| Run 3 | 600 | 5.431 ms | 0.00% |
| **PROMEDIO** | **600.0** | **7.134 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **api-gateway** |23.60% | 15.13% | 9.18% | **15.97%** |
| **minikube** |0.31% | 0.42% | 0.34% | **0.36%** |
| **mongo-db** |81.91% | 74.58% | 69.59% | **75.36%** |
| **ms-catalogo** |6.56% | 5.10% | 6.18% | **5.95%** |
| **ms-ordenes** |4.53% | 6.43% | 4.83% | **5.26%** |
| **ms-resenas** |7.67% | 4.12% | 6.69% | **6.16%** |
| **ms-usuarios** |4.93% | 6.88% | 5.80% | **5.87%** |
| **postgres-db** |6.69% | 5.83% | 6.76% | **6.43%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **api-gateway** |94.86MiB (94.86 MiB)  | 94.84MiB (94.84 MiB)  | 87.95MiB (87.95 MiB)  |
| **minikube** |117.1MiB (117.10 MiB)  | 116.8MiB (116.80 MiB)  | 116.8MiB (116.80 MiB)  |
| **mongo-db** |455.4MiB (455.40 MiB)  | 460.3MiB (460.30 MiB)  | 466.8MiB (466.80 MiB)  |
| **ms-catalogo** |108.6MiB (108.60 MiB)  | 110.6MiB (110.60 MiB)  | 109MiB (109.00 MiB)  |
| **ms-ordenes** |67.76MiB (67.76 MiB)  | 69.29MiB (69.29 MiB)  | 68.05MiB (68.05 MiB)  |
| **ms-resenas** |67.34MiB (67.34 MiB)  | 68.91MiB (68.91 MiB)  | 67.65MiB (67.65 MiB)  |
| **ms-usuarios** |68.01MiB (68.01 MiB)  | 69.45MiB (69.45 MiB)  | 68.34MiB (68.34 MiB)  |
| **postgres-db** |46.05MiB (46.05 MiB)  | 46.76MiB (46.76 MiB)  | 46.03MiB (46.03 MiB)  |