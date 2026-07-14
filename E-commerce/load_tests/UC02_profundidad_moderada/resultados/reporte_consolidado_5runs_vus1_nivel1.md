# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-08 22:14:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 23 | 1586.480 ms | 0.00% | 0.00% |
| Run 2 | 24 | 1592.910 ms | 0.00% | 0.00% |
| Run 3 | 20 | 2031.620 ms | 0.00% | 0.00% |
| Run 4 | 22 | 1835.760 ms | 0.00% | 0.00% |
| Run 5 | 20 | 1919.960 ms | 0.00% | 0.00% |
| **PROMEDIO** | **21.8** | **1793.346 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |113.43% | 98.29% | 114.55% | 119.91% | 99.17% | **109.07%** |
| **exp-vulnerable-mongo-db-1** |117.83% | 109.96% | 104.97% | 81.34% | 112.76% | **105.37%** |
| **exp-vulnerable-ms-catalogo-1** |4.27% | 4.86% | 3.87% | 4.88% | 5.52% | **4.68%** |
| **exp-vulnerable-ms-ordenes-1** |5.10% | 4.84% | 3.37% | 4.54% | 10.17% | **5.60%** |
| **exp-vulnerable-ms-resenas-1** |137.14% | 155.44% | 162.78% | 141.20% | 147.94% | **148.90%** |
| **exp-vulnerable-ms-usuarios-1** |4.88% | 5.32% | 3.19% | 4.93% | 5.55% | **4.77%** |
| **exp-vulnerable-postgres-db-1** |16.22% | 12.64% | 10.45% | 13.17% | 11.49% | **12.79%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |233.90 MiB | 368.50 MiB | 368.10 MiB | 368.40 MiB | 221.30 MiB | **312.04 MiB** |
| **exp-vulnerable-mongo-db-1** |457.20 MiB | 357.70 MiB | 357.00 MiB | 349.50 MiB | 340.10 MiB | **372.30 MiB** |
| **exp-vulnerable-ms-catalogo-1** |93.58 MiB | 47.51 MiB | 47.11 MiB | 45.17 MiB | 46.19 MiB | **55.91 MiB** |
| **exp-vulnerable-ms-ordenes-1** |99.41 MiB | 51.82 MiB | 45.92 MiB | 47.25 MiB | 45.57 MiB | **57.99 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.60 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |104.10 MiB | 52.23 MiB | 46.81 MiB | 46.18 MiB | 46.72 MiB | **59.21 MiB** |
| **exp-vulnerable-postgres-db-1** |73.60 MiB | 56.78 MiB | 58.82 MiB | 59.54 MiB | 59.60 MiB | **61.67 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |8.92% | 12.33% | 13.77% | 13.94% | 8.45% | **11.48%** |
| **exp-vulnerable-mongo-db-1** |117.83% | 109.96% | 104.97% | 81.34% | 112.76% | **105.37%** |
| **exp-vulnerable-ms-catalogo-1** |4.27% | 4.86% | 3.87% | 4.88% | 5.52% | **4.68%** |
| **exp-vulnerable-ms-ordenes-1** |5.10% | 4.84% | 3.37% | 4.54% | 10.17% | **5.60%** |
| **exp-vulnerable-ms-resenas-1** |137.14% | 155.44% | 162.78% | 141.20% | 147.94% | **148.90%** |
| **exp-vulnerable-ms-usuarios-1** |4.88% | 5.32% | 3.19% | 4.93% | 5.55% | **4.77%** |
| **exp-vulnerable-postgres-db-1** |16.22% | 12.64% | 10.45% | 13.17% | 11.49% | **12.79%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |193.92 MiB | 210.32 MiB | 234.50 MiB | 212.61 MiB | 185.40 MiB | **207.35 MiB** |
| **exp-vulnerable-mongo-db-1** |457.20 MiB | 357.70 MiB | 357.00 MiB | 349.50 MiB | 340.10 MiB | **372.30 MiB** |
| **exp-vulnerable-ms-catalogo-1** |93.58 MiB | 47.51 MiB | 47.11 MiB | 45.17 MiB | 46.19 MiB | **55.91 MiB** |
| **exp-vulnerable-ms-ordenes-1** |99.41 MiB | 51.82 MiB | 45.92 MiB | 47.25 MiB | 45.57 MiB | **57.99 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.60 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 256.00 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |104.10 MiB | 52.23 MiB | 46.81 MiB | 46.18 MiB | 46.72 MiB | **59.21 MiB** |
| **exp-vulnerable-postgres-db-1** |73.60 MiB | 56.78 MiB | 58.82 MiB | 59.54 MiB | 59.60 MiB | **61.67 MiB** |
