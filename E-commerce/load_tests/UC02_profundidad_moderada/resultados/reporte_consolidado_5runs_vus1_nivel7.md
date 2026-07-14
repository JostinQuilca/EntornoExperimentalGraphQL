# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 00:53:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 29 | 1088.380 ms | 0.00% | 0.00% |
| Run 2 | 27 | 1355.410 ms | 0.00% | 0.00% |
| Run 3 | 27 | 1459.560 ms | 0.00% | 0.00% |
| Run 4 | 25 | 1714.510 ms | 0.00% | 0.00% |
| Run 5 | 24 | 1526.550 ms | 0.00% | 0.00% |
| **PROMEDIO** | **26.4** | **1428.882 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |3.20% | 1.56% | 3.32% | 3.33% | 14.04% | **5.09%** |
| **exp-vulnerable-mongo-db-1** |109.18% | 98.65% | 94.33% | 85.64% | 83.50% | **94.26%** |
| **exp-vulnerable-ms-catalogo-1** |6.73% | 4.43% | 4.52% | 4.50% | 5.92% | **5.22%** |
| **exp-vulnerable-ms-ordenes-1** |4.32% | 5.13% | 4.30% | 4.09% | 10.95% | **5.76%** |
| **exp-vulnerable-ms-resenas-1** |185.77% | 203.48% | 200.13% | 210.57% | 198.10% | **199.61%** |
| **exp-vulnerable-ms-usuarios-1** |4.28% | 4.60% | 4.55% | 4.74% | 10.59% | **5.75%** |
| **exp-vulnerable-postgres-db-1** |15.25% | 17.42% | 15.49% | 19.18% | 49.37% | **23.34%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.54 MiB | 65.65 MiB | 65.62 MiB | 65.84 MiB | 65.54 MiB | **65.64 MiB** |
| **exp-vulnerable-mongo-db-1** |350.20 MiB | 343.20 MiB | 340.90 MiB | 335.50 MiB | 339.70 MiB | **341.90 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.78 MiB | 46.08 MiB | 45.14 MiB | 46.50 MiB | 45.52 MiB | **46.00 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.65 MiB | 46.22 MiB | 45.46 MiB | 45.46 MiB | 46.49 MiB | **45.86 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.54 MiB | 45.84 MiB | 47.13 MiB | 46.48 MiB | 47.63 MiB | **46.72 MiB** |
| **exp-vulnerable-postgres-db-1** |56.79 MiB | 56.78 MiB | 56.80 MiB | 57.18 MiB | 56.70 MiB | **56.85 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.52% | 0.43% | 0.44% | 0.39% | 0.83% | **0.52%** |
| **exp-vulnerable-mongo-db-1** |109.18% | 98.65% | 94.33% | 85.64% | 83.50% | **94.26%** |
| **exp-vulnerable-ms-catalogo-1** |6.73% | 4.43% | 4.52% | 4.50% | 5.92% | **5.22%** |
| **exp-vulnerable-ms-ordenes-1** |4.32% | 5.13% | 4.30% | 4.09% | 10.95% | **5.76%** |
| **exp-vulnerable-ms-resenas-1** |185.77% | 203.48% | 200.13% | 210.57% | 198.10% | **199.61%** |
| **exp-vulnerable-ms-usuarios-1** |4.28% | 4.60% | 4.55% | 4.74% | 10.59% | **5.75%** |
| **exp-vulnerable-postgres-db-1** |15.25% | 17.42% | 15.49% | 19.18% | 49.37% | **23.34%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |64.94 MiB | 64.87 MiB | 64.91 MiB | 65.15 MiB | 64.86 MiB | **64.95 MiB** |
| **exp-vulnerable-mongo-db-1** |350.20 MiB | 343.20 MiB | 340.90 MiB | 335.50 MiB | 339.70 MiB | **341.90 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.78 MiB | 46.08 MiB | 45.14 MiB | 46.50 MiB | 45.52 MiB | **46.00 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.65 MiB | 46.22 MiB | 45.46 MiB | 45.46 MiB | 46.49 MiB | **45.86 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | **255.94 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.54 MiB | 45.84 MiB | 47.13 MiB | 46.48 MiB | 47.63 MiB | **46.72 MiB** |
| **exp-vulnerable-postgres-db-1** |56.79 MiB | 56.78 MiB | 56.80 MiB | 57.18 MiB | 56.70 MiB | **56.85 MiB** |
