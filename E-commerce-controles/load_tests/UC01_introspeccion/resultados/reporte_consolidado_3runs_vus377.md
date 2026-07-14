# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=377)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 20:30:52

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 21951 | 38.359 ms | 0.68% |
| Run 2 | 21327 | 67.410 ms | 0.78% |
| Run 3 | 22198 | 26.424 ms | 0.63% |
| **PROMEDIO** | **21825.3** | **44.064 ms** | **0.70%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |108.71% | 112.76% | 116.66% | **112.71%** |
| **exp-protegido-mongo-db-1** |72.40% | 98.05% | 93.56% | **88.00%** |
| **exp-protegido-ms-catalogo-1** |5.24% | 4.11% | 4.64% | **4.66%** |
| **exp-protegido-ms-ordenes-1** |5.57% | 4.93% | 4.91% | **5.14%** |
| **exp-protegido-ms-resenas-1** |5.11% | 5.25% | 5.51% | **5.29%** |
| **exp-protegido-ms-usuarios-1** |5.14% | 9.84% | 4.89% | **6.62%** |
| **exp-protegido-postgres-db-1** |6.50% | 5.68% | 4.38% | **5.52%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |201.4MiB (201.40 MiB)  | 202.8MiB (202.80 MiB)  | 192MiB (192.00 MiB)  |
| **exp-protegido-mongo-db-1** |348.8MiB (348.80 MiB)  | 340.4MiB (340.40 MiB)  | 346.9MiB (346.90 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.41MiB (45.41 MiB)  | 46.16MiB (46.16 MiB)  | 47.46MiB (47.46 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.04MiB (46.04 MiB)  | 48.52MiB (48.52 MiB)  | 46.44MiB (46.44 MiB)  |
| **exp-protegido-ms-resenas-1** |46.84MiB (46.84 MiB)  | 45.59MiB (45.59 MiB)  | 46.41MiB (46.41 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.6MiB (46.60 MiB)  | 46.52MiB (46.52 MiB)  | 45.73MiB (45.73 MiB)  |
| **exp-protegido-postgres-db-1** |28MiB (28.00 MiB)  | 29.69MiB (29.69 MiB)  | 28.37MiB (28.37 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |75.80% | 79.46% | 80.96% | **78.74%** |
| **exp-protegido-mongo-db-1** |17.79% | 27.05% | 22.81% | **22.55%** |
| **exp-protegido-ms-catalogo-1** |1.37% | 0.88% | 1.16% | **1.14%** |
| **exp-protegido-ms-ordenes-1** |1.04% | 1.14% | 1.21% | **1.13%** |
| **exp-protegido-ms-resenas-1** |1.27% | 1.12% | 1.20% | **1.20%** |
| **exp-protegido-ms-usuarios-1** |1.13% | 1.48% | 1.22% | **1.28%** |
| **exp-protegido-postgres-db-1** |1.33% | 1.58% | 1.23% | **1.38%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |145.66 MiB | 134.57 MiB | 136.54 MiB | **138.92 MiB** |
| **exp-protegido-mongo-db-1** |209.32 MiB | 212.57 MiB | 206.04 MiB | **209.31 MiB** |
| **exp-protegido-ms-catalogo-1** |45.28 MiB | 46.06 MiB | 47.36 MiB | **46.23 MiB** |
| **exp-protegido-ms-ordenes-1** |45.92 MiB | 48.23 MiB | 46.34 MiB | **46.83 MiB** |
| **exp-protegido-ms-resenas-1** |45.27 MiB | 45.48 MiB | 46.32 MiB | **45.69 MiB** |
| **exp-protegido-ms-usuarios-1** |45.30 MiB | 46.21 MiB | 45.63 MiB | **45.71 MiB** |
| **exp-protegido-postgres-db-1** |27.85 MiB | 28.16 MiB | 27.99 MiB | **28.00 MiB** |