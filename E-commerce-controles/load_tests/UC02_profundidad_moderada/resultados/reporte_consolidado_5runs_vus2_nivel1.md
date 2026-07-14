# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-08 22:46:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 29 | 3211.130 ms | 0.00% | 0.00% |
| Run 2 | 35 | 2454.390 ms | 0.00% | 0.00% |
| Run 3 | 38 | 2292.620 ms | 0.00% | 0.00% |
| Run 4 | 36 | 2302.350 ms | 0.00% | 0.00% |
| Run 5 | 34 | 2558.300 ms | 0.00% | 0.00% |
| **PROMEDIO** | **34.4** | **2563.758 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |136.69% | 133.46% | 117.81% | 62.76% | 132.71% | **116.69%** |
| **exp-protegido-mongo-db-1** |86.87% | 78.33% | 92.02% | 95.74% | 110.12% | **92.62%** |
| **exp-protegido-ms-catalogo-1** |6.31% | 4.85% | 3.66% | 3.72% | 5.11% | **4.73%** |
| **exp-protegido-ms-ordenes-1** |4.35% | 5.91% | 5.50% | 5.90% | 4.15% | **5.16%** |
| **exp-protegido-ms-resenas-1** |150.17% | 163.28% | 164.39% | 147.70% | 161.64% | **157.44%** |
| **exp-protegido-ms-usuarios-1** |4.08% | 5.51% | 4.84% | 5.59% | 5.00% | **5.00%** |
| **exp-protegido-postgres-db-1** |10.88% | 31.00% | 27.25% | 20.96% | 20.47% | **22.11%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |347.60 MiB | 307.20 MiB | 247.90 MiB | 193.20 MiB | 323.90 MiB | **283.96 MiB** |
| **exp-protegido-mongo-db-1** |338.40 MiB | 334.60 MiB | 340.30 MiB | 334.20 MiB | 346.40 MiB | **338.78 MiB** |
| **exp-protegido-ms-catalogo-1** |46.25 MiB | 46.36 MiB | 47.23 MiB | 47.68 MiB | 45.89 MiB | **46.68 MiB** |
| **exp-protegido-ms-ordenes-1** |47.59 MiB | 46.34 MiB | 45.99 MiB | 46.09 MiB | 46.60 MiB | **46.52 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | 255.90 MiB | **255.98 MiB** |
| **exp-protegido-ms-usuarios-1** |54.45 MiB | 46.61 MiB | 45.75 MiB | 46.02 MiB | 47.33 MiB | **48.03 MiB** |
| **exp-protegido-postgres-db-1** |59.70 MiB | 60.86 MiB | 61.38 MiB | 61.46 MiB | 62.69 MiB | **61.22 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |9.05% | 13.21% | 11.92% | 5.75% | 8.31% | **9.65%** |
| **exp-protegido-mongo-db-1** |86.87% | 78.33% | 92.02% | 95.74% | 110.12% | **92.62%** |
| **exp-protegido-ms-catalogo-1** |6.31% | 4.85% | 3.66% | 3.72% | 5.11% | **4.73%** |
| **exp-protegido-ms-ordenes-1** |4.35% | 5.91% | 5.50% | 5.90% | 4.15% | **5.16%** |
| **exp-protegido-ms-resenas-1** |150.17% | 163.28% | 164.39% | 147.70% | 161.64% | **157.44%** |
| **exp-protegido-ms-usuarios-1** |4.08% | 5.51% | 4.84% | 5.59% | 5.00% | **5.00%** |
| **exp-protegido-postgres-db-1** |10.88% | 31.00% | 27.25% | 20.96% | 20.47% | **22.11%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |105.40 MiB | 167.10 MiB | 144.78 MiB | 130.50 MiB | 180.05 MiB | **145.57 MiB** |
| **exp-protegido-mongo-db-1** |338.40 MiB | 334.60 MiB | 340.30 MiB | 334.20 MiB | 346.40 MiB | **338.78 MiB** |
| **exp-protegido-ms-catalogo-1** |46.25 MiB | 46.36 MiB | 47.23 MiB | 47.68 MiB | 45.89 MiB | **46.68 MiB** |
| **exp-protegido-ms-ordenes-1** |47.59 MiB | 46.34 MiB | 45.99 MiB | 46.09 MiB | 46.60 MiB | **46.52 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 256.00 MiB | 256.00 MiB | 256.00 MiB | 255.90 MiB | **255.98 MiB** |
| **exp-protegido-ms-usuarios-1** |54.45 MiB | 46.61 MiB | 45.75 MiB | 46.02 MiB | 47.33 MiB | **48.03 MiB** |
| **exp-protegido-postgres-db-1** |59.70 MiB | 60.86 MiB | 61.38 MiB | 61.46 MiB | 62.69 MiB | **61.22 MiB** |
