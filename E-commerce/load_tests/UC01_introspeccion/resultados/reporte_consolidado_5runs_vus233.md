# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=233)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 21:08:25

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 13958 | 10.806 ms | 0.13% |
| Run 2 | 13945 | 12.099 ms | 0.12% |
| Run 3 | 13938 | 12.009 ms | 0.00% |
| Run 4 | 13980 | 10.985 ms | 0.17% |
| Run 5 | 13941 | 11.788 ms | 0.13% |
| **PROMEDIO** | **13952.4** | **11.537 ms** | **0.11%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |71.56% | 71.84% | 67.83% | 77.64% | 59.74% | **69.72%** |
| **exp-vulnerable-mongo-db-1** |75.03% | 58.28% | 57.23% | 68.92% | 66.29% | **65.15%** |
| **exp-vulnerable-ms-catalogo-1** |3.98% | 4.33% | 5.36% | 2.98% | 4.21% | **4.17%** |
| **exp-vulnerable-ms-ordenes-1** |2.66% | 3.15% | 3.58% | 3.64% | 3.97% | **3.40%** |
| **exp-vulnerable-ms-resenas-1** |3.41% | 3.46% | 3.94% | 3.35% | 4.44% | **3.72%** |
| **exp-vulnerable-ms-usuarios-1** |6.29% | 3.45% | 3.03% | 3.14% | 4.39% | **4.06%** |
| **exp-vulnerable-postgres-db-1** |3.95% | 3.97% | 4.34% | 3.91% | 3.90% | **4.01%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |183.6MiB (183.60 MiB)  | 137MiB (137.00 MiB)  | 146.1MiB (146.10 MiB)  | 183.2MiB (183.20 MiB)  | 129.6MiB (129.60 MiB)  |
| **exp-vulnerable-mongo-db-1** |349.2MiB (349.20 MiB)  | 342.7MiB (342.70 MiB)  | 334MiB (334.00 MiB)  | 345.1MiB (345.10 MiB)  | 333MiB (333.00 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |45.52MiB (45.52 MiB)  | 46.39MiB (46.39 MiB)  | 45.43MiB (45.43 MiB)  | 46.74MiB (46.74 MiB)  | 45.54MiB (45.54 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |47.13MiB (47.13 MiB)  | 46.64MiB (46.64 MiB)  | 46.14MiB (46.14 MiB)  | 46.44MiB (46.44 MiB)  | 45.71MiB (45.71 MiB)  |
| **exp-vulnerable-ms-resenas-1** |48.02MiB (48.02 MiB)  | 47MiB (47.00 MiB)  | 45.5MiB (45.50 MiB)  | 45.58MiB (45.58 MiB)  | 45.48MiB (45.48 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |54MiB (54.00 MiB)  | 46.48MiB (46.48 MiB)  | 46.21MiB (46.21 MiB)  | 45.98MiB (45.98 MiB)  | 46.16MiB (46.16 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.42MiB (27.42 MiB)  | 27.42MiB (27.42 MiB)  | 27.35MiB (27.35 MiB)  | 27.58MiB (27.58 MiB)  | 27.42MiB (27.42 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |38.20% | 36.62% | 39.96% | 37.22% | 39.79% | **38.36%** |
| **exp-vulnerable-mongo-db-1** |17.73% | 17.29% | 15.97% | 17.56% | 16.94% | **17.10%** |
| **exp-vulnerable-ms-catalogo-1** |1.04% | 0.94% | 0.86% | 0.81% | 0.88% | **0.91%** |
| **exp-vulnerable-ms-ordenes-1** |0.78% | 0.75% | 0.89% | 0.98% | 0.94% | **0.87%** |
| **exp-vulnerable-ms-resenas-1** |0.88% | 0.84% | 0.93% | 1.04% | 1.06% | **0.95%** |
| **exp-vulnerable-ms-usuarios-1** |1.01% | 0.81% | 0.84% | 1.01% | 0.93% | **0.92%** |
| **exp-vulnerable-postgres-db-1** |1.02% | 1.15% | 1.13% | 1.07% | 1.08% | **1.09%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |136.83 MiB | 113.30 MiB | 110.75 MiB | 122.98 MiB | 110.47 MiB | **118.87 MiB** |
| **exp-vulnerable-mongo-db-1** |202.10 MiB | 204.18 MiB | 204.54 MiB | 205.44 MiB | 201.06 MiB | **203.46 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.39 MiB | 46.27 MiB | 45.30 MiB | 46.59 MiB | 45.41 MiB | **45.79 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.44 MiB | 46.34 MiB | 46.02 MiB | 46.33 MiB | 45.59 MiB | **45.94 MiB** |
| **exp-vulnerable-ms-resenas-1** |46.04 MiB | 46.88 MiB | 45.39 MiB | 45.46 MiB | 45.37 MiB | **45.83 MiB** |
| **exp-vulnerable-ms-usuarios-1** |50.72 MiB | 46.31 MiB | 46.10 MiB | 45.86 MiB | 46.05 MiB | **47.01 MiB** |
| **exp-vulnerable-postgres-db-1** |27.36 MiB | 27.38 MiB | 27.30 MiB | 27.39 MiB | 27.37 MiB | **27.36 MiB** |