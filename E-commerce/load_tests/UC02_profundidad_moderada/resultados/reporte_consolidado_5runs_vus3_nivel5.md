# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 17:36:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 60 | 2332.190 ms | 5.00% | 0.00% |
| Run 2 | 66 | 1782.180 ms | 0.00% | 0.00% |
| Run 3 | 63 | 2578.490 ms | 4.76% | 0.00% |
| Run 4 | 63 | 1962.240 ms | 0.00% | 0.00% |
| Run 5 | 66 | 1767.090 ms | 0.00% | 0.00% |
| **PROMEDIO** | **63.6** | **2084.438 ms** | **1.95%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |4.41% | 2.26% | 2.56% | 14.63% | 16.48% | **8.07%** |
| **exp-vulnerable-mongo-db-1** |70.25% | 106.43% | 69.17% | 90.55% | 103.66% | **88.01%** |
| **exp-vulnerable-ms-catalogo-1** |4.05% | 5.79% | 3.14% | 6.07% | 5.13% | **4.84%** |
| **exp-vulnerable-ms-ordenes-1** |4.49% | 6.32% | 3.61% | 5.50% | 5.28% | **5.04%** |
| **exp-vulnerable-ms-resenas-1** |149.89% | 174.35% | 134.77% | 173.03% | 209.91% | **168.39%** |
| **exp-vulnerable-ms-usuarios-1** |3.91% | 6.26% | 3.76% | 4.98% | 11.00% | **5.98%** |
| **exp-vulnerable-postgres-db-1** |31.17% | 22.27% | 37.54% | 38.41% | 19.59% | **29.80%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |68.26 MiB | 69.04 MiB | 69.64 MiB | 67.24 MiB | 71.57 MiB | **69.15 MiB** |
| **exp-vulnerable-mongo-db-1** |354.60 MiB | 354.50 MiB | 339.10 MiB | 344.20 MiB | 349.80 MiB | **348.44 MiB** |
| **exp-vulnerable-ms-catalogo-1** |77.20 MiB | 49.69 MiB | 47.67 MiB | 48.34 MiB | 49.80 MiB | **54.54 MiB** |
| **exp-vulnerable-ms-ordenes-1** |53.99 MiB | 49.78 MiB | 53.45 MiB | 48.62 MiB | 53.55 MiB | **51.88 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |58.72 MiB | 47.30 MiB | 47.02 MiB | 47.19 MiB | 49.19 MiB | **49.88 MiB** |
| **exp-vulnerable-postgres-db-1** |71.23 MiB | 65.48 MiB | 62.62 MiB | 64.25 MiB | 63.50 MiB | **65.42 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.59% | 0.46% | 0.56% | 1.32% | 1.18% | **0.82%** |
| **exp-vulnerable-mongo-db-1** |70.25% | 106.43% | 69.17% | 90.55% | 103.66% | **88.01%** |
| **exp-vulnerable-ms-catalogo-1** |4.05% | 5.79% | 3.14% | 6.07% | 5.13% | **4.84%** |
| **exp-vulnerable-ms-ordenes-1** |4.49% | 6.32% | 3.61% | 5.50% | 5.28% | **5.04%** |
| **exp-vulnerable-ms-resenas-1** |149.89% | 174.35% | 134.77% | 173.03% | 209.91% | **168.39%** |
| **exp-vulnerable-ms-usuarios-1** |3.91% | 6.26% | 3.76% | 4.98% | 11.00% | **5.98%** |
| **exp-vulnerable-postgres-db-1** |31.17% | 22.27% | 37.54% | 38.41% | 19.59% | **29.80%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |66.61 MiB | 65.95 MiB | 68.49 MiB | 65.77 MiB | 67.99 MiB | **66.96 MiB** |
| **exp-vulnerable-mongo-db-1** |354.60 MiB | 354.50 MiB | 339.10 MiB | 344.20 MiB | 349.80 MiB | **348.44 MiB** |
| **exp-vulnerable-ms-catalogo-1** |77.20 MiB | 49.69 MiB | 47.67 MiB | 48.34 MiB | 49.80 MiB | **54.54 MiB** |
| **exp-vulnerable-ms-ordenes-1** |53.99 MiB | 49.78 MiB | 53.45 MiB | 48.62 MiB | 53.55 MiB | **51.88 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.80 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |58.72 MiB | 47.30 MiB | 47.02 MiB | 47.19 MiB | 49.19 MiB | **49.88 MiB** |
| **exp-vulnerable-postgres-db-1** |71.23 MiB | 65.48 MiB | 62.62 MiB | 64.25 MiB | 63.50 MiB | **65.42 MiB** |
