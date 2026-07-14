# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 17:59:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 63 | 1895.160 ms | 4.76% | 0.00% |
| Run 2 | 69 | 1655.160 ms | 0.00% | 0.00% |
| Run 3 | 69 | 1619.420 ms | 0.00% | 0.00% |
| Run 4 | 65 | 1809.230 ms | 4.61% | 0.00% |
| Run 5 | 69 | 1812.910 ms | 0.00% | 0.00% |
| **PROMEDIO** | **67.0** | **1758.376 ms** | **1.87%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |5.76% | 4.14% | 5.97% | 2.67% | 8.09% | **5.33%** |
| **exp-protegido-mongo-db-1** |101.68% | 91.04% | 104.32% | 104.61% | 91.76% | **98.68%** |
| **exp-protegido-ms-catalogo-1** |6.57% | 3.92% | 4.72% | 6.26% | 3.64% | **5.02%** |
| **exp-protegido-ms-ordenes-1** |11.18% | 4.87% | 4.52% | 4.58% | 4.23% | **5.88%** |
| **exp-protegido-ms-resenas-1** |191.38% | 183.72% | 166.24% | 245.22% | 170.62% | **191.44%** |
| **exp-protegido-ms-usuarios-1** |15.55% | 4.44% | 4.26% | 4.89% | 3.62% | **6.55%** |
| **exp-protegido-postgres-db-1** |31.06% | 41.98% | 23.77% | 26.95% | 36.08% | **31.97%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.53 MiB | 75.30 MiB | 67.15 MiB | 67.54 MiB | 68.59 MiB | **69.22 MiB** |
| **exp-protegido-mongo-db-1** |359.40 MiB | 359.20 MiB | 349.80 MiB | 343.60 MiB | 344.80 MiB | **351.36 MiB** |
| **exp-protegido-ms-catalogo-1** |56.79 MiB | 46.79 MiB | 48.72 MiB | 45.81 MiB | 48.06 MiB | **49.23 MiB** |
| **exp-protegido-ms-ordenes-1** |56.43 MiB | 48.02 MiB | 48.28 MiB | 46.07 MiB | 47.11 MiB | **49.18 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-protegido-ms-usuarios-1** |57.37 MiB | 48.39 MiB | 47.42 MiB | 47.19 MiB | 48.78 MiB | **49.83 MiB** |
| **exp-protegido-postgres-db-1** |70.41 MiB | 67.36 MiB | 60.74 MiB | 60.43 MiB | 60.79 MiB | **63.95 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.25% | 0.93% | 0.83% | 0.49% | 0.67% | **0.83%** |
| **exp-protegido-mongo-db-1** |101.68% | 91.04% | 104.32% | 104.61% | 91.76% | **98.68%** |
| **exp-protegido-ms-catalogo-1** |6.57% | 3.92% | 4.72% | 6.26% | 3.64% | **5.02%** |
| **exp-protegido-ms-ordenes-1** |11.18% | 4.87% | 4.52% | 4.58% | 4.23% | **5.88%** |
| **exp-protegido-ms-resenas-1** |191.38% | 183.72% | 166.24% | 245.22% | 170.62% | **191.44%** |
| **exp-protegido-ms-usuarios-1** |15.55% | 4.44% | 4.26% | 4.89% | 3.62% | **6.55%** |
| **exp-protegido-postgres-db-1** |31.06% | 41.98% | 23.77% | 26.95% | 36.08% | **31.97%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.63 MiB | 73.99 MiB | 65.68 MiB | 66.04 MiB | 66.75 MiB | **67.62 MiB** |
| **exp-protegido-mongo-db-1** |359.40 MiB | 359.20 MiB | 349.80 MiB | 343.60 MiB | 344.80 MiB | **351.36 MiB** |
| **exp-protegido-ms-catalogo-1** |56.79 MiB | 46.79 MiB | 48.72 MiB | 45.81 MiB | 48.06 MiB | **49.23 MiB** |
| **exp-protegido-ms-ordenes-1** |56.43 MiB | 48.02 MiB | 48.28 MiB | 46.07 MiB | 47.11 MiB | **49.18 MiB** |
| **exp-protegido-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-protegido-ms-usuarios-1** |57.37 MiB | 48.39 MiB | 47.42 MiB | 47.19 MiB | 48.78 MiB | **49.83 MiB** |
| **exp-protegido-postgres-db-1** |70.41 MiB | 67.36 MiB | 60.74 MiB | 60.43 MiB | 60.79 MiB | **63.95 MiB** |
