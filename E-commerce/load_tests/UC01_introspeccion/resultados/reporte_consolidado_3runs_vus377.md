# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=377)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 20:24:35

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 22489 | 13.270 ms | 0.71% |
| Run 2 | 22308 | 20.414 ms | 0.53% |
| Run 3 | 22253 | 23.713 ms | 0.72% |
| **PROMEDIO** | **22350.0** | **19.132 ms** | **0.65%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |83.22% | 110.98% | 98.08% | **97.43%** |
| **exp-vulnerable-mongo-db-1** |79.77% | 79.22% | 82.84% | **80.61%** |
| **exp-vulnerable-ms-catalogo-1** |2.46% | 4.76% | 5.54% | **4.25%** |
| **exp-vulnerable-ms-ordenes-1** |3.42% | 4.76% | 4.40% | **4.19%** |
| **exp-vulnerable-ms-resenas-1** |3.18% | 4.39% | 4.72% | **4.10%** |
| **exp-vulnerable-ms-usuarios-1** |3.18% | 3.95% | 4.69% | **3.94%** |
| **exp-vulnerable-postgres-db-1** |3.69% | 4.36% | 7.19% | **5.08%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |203.2MiB (203.20 MiB)  | 194.1MiB (194.10 MiB)  | 203.4MiB (203.40 MiB)  |
| **exp-vulnerable-mongo-db-1** |339.2MiB (339.20 MiB)  | 348.1MiB (348.10 MiB)  | 334.1MiB (334.10 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.7MiB (46.70 MiB)  | 46.21MiB (46.21 MiB)  | 46.02MiB (46.02 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |48MiB (48.00 MiB)  | 46.4MiB (46.40 MiB)  | 45.54MiB (45.54 MiB)  |
| **exp-vulnerable-ms-resenas-1** |45.96MiB (45.96 MiB)  | 46.47MiB (46.47 MiB)  | 46.41MiB (46.41 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |46.55MiB (46.55 MiB)  | 45.57MiB (45.57 MiB)  | 46.38MiB (46.38 MiB)  |
| **exp-vulnerable-postgres-db-1** |27.35MiB (27.35 MiB)  | 27.41MiB (27.41 MiB)  | 27.35MiB (27.35 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |49.08% | 58.76% | 67.18% | **58.34%** |
| **exp-vulnerable-mongo-db-1** |18.27% | 20.20% | 18.02% | **18.83%** |
| **exp-vulnerable-ms-catalogo-1** |0.84% | 1.00% | 1.03% | **0.96%** |
| **exp-vulnerable-ms-ordenes-1** |0.93% | 1.09% | 0.94% | **0.99%** |
| **exp-vulnerable-ms-resenas-1** |0.92% | 0.99% | 0.88% | **0.93%** |
| **exp-vulnerable-ms-usuarios-1** |0.92% | 1.11% | 1.02% | **1.02%** |
| **exp-vulnerable-postgres-db-1** |0.93% | 1.14% | 1.36% | **1.14%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |138.42 MiB | 149.89 MiB | 144.78 MiB | **144.36 MiB** |
| **exp-vulnerable-mongo-db-1** |201.47 MiB | 203.00 MiB | 202.58 MiB | **202.35 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.57 MiB | 46.06 MiB | 45.89 MiB | **46.17 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.83 MiB | 46.26 MiB | 45.43 MiB | **46.51 MiB** |
| **exp-vulnerable-ms-resenas-1** |45.83 MiB | 46.35 MiB | 46.30 MiB | **46.16 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.43 MiB | 45.30 MiB | 44.83 MiB | **45.52 MiB** |
| **exp-vulnerable-postgres-db-1** |27.29 MiB | 27.37 MiB | 27.31 MiB | **27.32 MiB** |