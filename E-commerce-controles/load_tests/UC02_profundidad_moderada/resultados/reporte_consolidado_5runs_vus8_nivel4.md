# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 16:32:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 207 | 1337.900 ms | 0.00% | 0.00% |
| Run 2 | 208 | 1911.990 ms | 3.84% | 0.00% |
| Run 3 | 204 | 1425.720 ms | 0.00% | 0.00% |
| Run 4 | 135 | 2600.340 ms | 5.92% | 0.00% |
| Run 5 | 139 | 2892.980 ms | 5.75% | 0.00% |
| **PROMEDIO** | **178.6** | **2033.786 ms** | **3.10%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |23.93% | 16.60% | 17.58% | 18.41% | 14.42% | **18.19%** |
| **exp-protegido-mongo-db-1** |109.86% | 107.86% | 100.46% | 113.70% | 88.89% | **104.15%** |
| **exp-protegido-ms-catalogo-1** |7.73% | 10.91% | 7.84% | 13.46% | 4.16% | **8.82%** |
| **exp-protegido-ms-ordenes-1** |9.75% | 8.29% | 7.13% | 7.88% | 5.64% | **7.74%** |
| **exp-protegido-ms-resenas-1** |244.95% | 186.40% | 240.86% | 232.87% | 199.74% | **220.96%** |
| **exp-protegido-ms-usuarios-1** |7.86% | 6.06% | 6.49% | 7.30% | 6.08% | **6.76%** |
| **exp-protegido-postgres-db-1** |75.82% | 99.50% | 78.42% | 87.01% | 51.36% | **78.42%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |97.10 MiB | 72.24 MiB | 72.11 MiB | 70.04 MiB | 71.31 MiB | **76.56 MiB** |
| **exp-protegido-mongo-db-1** |347.60 MiB | 347.90 MiB | 344.60 MiB | 350.60 MiB | 337.70 MiB | **345.68 MiB** |
| **exp-protegido-ms-catalogo-1** |46.74 MiB | 46.67 MiB | 46.59 MiB | 46.07 MiB | 46.30 MiB | **46.47 MiB** |
| **exp-protegido-ms-ordenes-1** |45.93 MiB | 46.10 MiB | 47.14 MiB | 46.67 MiB | 48.18 MiB | **46.80 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.92 MiB** |
| **exp-protegido-ms-usuarios-1** |46.55 MiB | 45.38 MiB | 45.94 MiB | 46.39 MiB | 47.64 MiB | **46.38 MiB** |
| **exp-protegido-postgres-db-1** |78.55 MiB | 72.17 MiB | 73.68 MiB | 76.68 MiB | 69.38 MiB | **74.09 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |3.91% | 3.29% | 3.55% | 2.76% | 1.55% | **3.01%** |
| **exp-protegido-mongo-db-1** |109.86% | 107.86% | 100.46% | 113.70% | 88.89% | **104.15%** |
| **exp-protegido-ms-catalogo-1** |7.73% | 10.91% | 7.84% | 13.46% | 4.16% | **8.82%** |
| **exp-protegido-ms-ordenes-1** |9.75% | 8.29% | 7.13% | 7.88% | 5.64% | **7.74%** |
| **exp-protegido-ms-resenas-1** |244.95% | 186.40% | 240.86% | 232.87% | 199.74% | **220.96%** |
| **exp-protegido-ms-usuarios-1** |7.86% | 6.06% | 6.49% | 7.30% | 6.08% | **6.76%** |
| **exp-protegido-postgres-db-1** |75.82% | 99.50% | 78.42% | 87.01% | 51.36% | **78.42%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |72.66 MiB | 69.92 MiB | 69.46 MiB | 67.00 MiB | 69.17 MiB | **69.64 MiB** |
| **exp-protegido-mongo-db-1** |347.60 MiB | 347.90 MiB | 344.60 MiB | 350.60 MiB | 337.70 MiB | **345.68 MiB** |
| **exp-protegido-ms-catalogo-1** |46.74 MiB | 46.67 MiB | 46.59 MiB | 46.07 MiB | 46.30 MiB | **46.47 MiB** |
| **exp-protegido-ms-ordenes-1** |45.93 MiB | 46.10 MiB | 47.14 MiB | 46.67 MiB | 48.18 MiB | **46.80 MiB** |
| **exp-protegido-ms-resenas-1** |256.00 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.92 MiB** |
| **exp-protegido-ms-usuarios-1** |46.55 MiB | 45.38 MiB | 45.94 MiB | 46.39 MiB | 47.64 MiB | **46.38 MiB** |
| **exp-protegido-postgres-db-1** |78.55 MiB | 72.17 MiB | 73.68 MiB | 76.68 MiB | 69.38 MiB | **74.09 MiB** |
