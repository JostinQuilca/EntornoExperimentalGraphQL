# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 11:24:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 63 | 2273.370 ms | 0.00% | 0.00% |
| Run 2 | 51 | 2700.370 ms | 5.88% | 0.00% |
| Run 3 | 76 | 1442.040 ms | 0.00% | 0.00% |
| Run 4 | 57 | 2195.200 ms | 0.00% | 0.00% |
| Run 5 | 45 | 3073.590 ms | 6.66% | 0.00% |
| **PROMEDIO** | **58.4** | **2336.914 ms** | **2.51%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |10.28% | 6.45% | 5.62% | 4.90% | 3.47% | **6.14%** |
| **exp-protegido-mongo-db-1** |76.54% | 107.83% | 85.70% | 84.27% | 105.46% | **91.96%** |
| **exp-protegido-ms-catalogo-1** |3.72% | 3.66% | 4.52% | 3.80% | 5.28% | **4.20%** |
| **exp-protegido-ms-ordenes-1** |5.06% | 3.60% | 2.77% | 5.90% | 4.53% | **4.37%** |
| **exp-protegido-ms-resenas-1** |216.42% | 170.82% | 188.62% | 147.01% | 234.12% | **191.40%** |
| **exp-protegido-ms-usuarios-1** |5.57% | 4.41% | 4.99% | 4.56% | 9.79% | **5.86%** |
| **exp-protegido-postgres-db-1** |31.91% | 31.34% | 23.38% | 30.53% | 31.60% | **29.75%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.07 MiB | 67.89 MiB | 67.40 MiB | 66.52 MiB | 66.31 MiB | **67.04 MiB** |
| **exp-protegido-mongo-db-1** |345.40 MiB | 341.00 MiB | 340.30 MiB | 354.80 MiB | 348.80 MiB | **346.06 MiB** |
| **exp-protegido-ms-catalogo-1** |46.39 MiB | 46.76 MiB | 47.71 MiB | 46.30 MiB | 45.46 MiB | **46.52 MiB** |
| **exp-protegido-ms-ordenes-1** |45.75 MiB | 46.05 MiB | 46.79 MiB | 46.99 MiB | 46.71 MiB | **46.46 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-protegido-ms-usuarios-1** |54.54 MiB | 46.14 MiB | 55.18 MiB | 45.91 MiB | 47.17 MiB | **49.79 MiB** |
| **exp-protegido-postgres-db-1** |63.20 MiB | 61.56 MiB | 60.29 MiB | 64.29 MiB | 66.18 MiB | **63.10 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.97% | 0.74% | 1.10% | 0.85% | 0.74% | **0.88%** |
| **exp-protegido-mongo-db-1** |76.54% | 107.83% | 85.70% | 84.27% | 105.46% | **91.96%** |
| **exp-protegido-ms-catalogo-1** |3.72% | 3.66% | 4.52% | 3.80% | 5.28% | **4.20%** |
| **exp-protegido-ms-ordenes-1** |5.06% | 3.60% | 2.77% | 5.90% | 4.53% | **4.37%** |
| **exp-protegido-ms-resenas-1** |216.42% | 170.82% | 188.62% | 147.01% | 234.12% | **191.40%** |
| **exp-protegido-ms-usuarios-1** |5.57% | 4.41% | 4.99% | 4.56% | 9.79% | **5.86%** |
| **exp-protegido-postgres-db-1** |31.91% | 31.34% | 23.38% | 30.53% | 31.60% | **29.75%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.72 MiB | 66.05 MiB | 66.19 MiB | 64.96 MiB | 65.15 MiB | **65.61 MiB** |
| **exp-protegido-mongo-db-1** |345.40 MiB | 341.00 MiB | 340.30 MiB | 354.80 MiB | 348.80 MiB | **346.06 MiB** |
| **exp-protegido-ms-catalogo-1** |46.39 MiB | 46.76 MiB | 47.71 MiB | 46.30 MiB | 45.46 MiB | **46.52 MiB** |
| **exp-protegido-ms-ordenes-1** |45.75 MiB | 46.05 MiB | 46.79 MiB | 46.99 MiB | 46.71 MiB | **46.46 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.80 MiB | 255.80 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-protegido-ms-usuarios-1** |54.54 MiB | 46.14 MiB | 55.18 MiB | 45.91 MiB | 47.17 MiB | **49.79 MiB** |
| **exp-protegido-postgres-db-1** |63.20 MiB | 61.56 MiB | 60.29 MiB | 64.29 MiB | 66.18 MiB | **63.10 MiB** |
