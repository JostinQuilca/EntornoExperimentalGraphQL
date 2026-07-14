# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-08 23:29:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 95 | 2444.710 ms | 0.00% | 0.00% |
| Run 2 | 115 | 2188.700 ms | 0.00% | 0.00% |
| Run 3 | 112 | 2034.990 ms | 0.00% | 0.00% |
| Run 4 | 75 | 3139.340 ms | 0.00% | 0.00% |
| Run 5 | 110 | 2139.560 ms | 4.54% | 0.00% |
| **PROMEDIO** | **101.4** | **2389.460 ms** | **0.91%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |3.95% | 3.58% | 3.86% | 5.22% | 8.70% | **5.06%** |
| **exp-protegido-mongo-db-1** |115.07% | 105.53% | 83.05% | 69.84% | 88.16% | **92.33%** |
| **exp-protegido-ms-catalogo-1** |4.59% | 5.21% | 4.86% | 4.57% | 6.11% | **5.07%** |
| **exp-protegido-ms-ordenes-1** |4.61% | 3.06% | 3.88% | 4.92% | 5.10% | **4.31%** |
| **exp-protegido-ms-resenas-1** |194.12% | 244.65% | 210.36% | 273.52% | 241.10% | **232.75%** |
| **exp-protegido-ms-usuarios-1** |4.32% | 3.75% | 4.66% | 4.27% | 5.15% | **4.43%** |
| **exp-protegido-postgres-db-1** |50.12% | 43.09% | 39.54% | 45.81% | 76.07% | **50.93%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |68.47 MiB | 69.17 MiB | 69.54 MiB | 67.48 MiB | 69.11 MiB | **68.75 MiB** |
| **exp-protegido-mongo-db-1** |354.70 MiB | 334.10 MiB | 348.70 MiB | 347.60 MiB | 334.30 MiB | **343.88 MiB** |
| **exp-protegido-ms-catalogo-1** |46.79 MiB | 46.77 MiB | 46.52 MiB | 46.02 MiB | 48.16 MiB | **46.85 MiB** |
| **exp-protegido-ms-ordenes-1** |46.33 MiB | 45.32 MiB | 46.55 MiB | 46.93 MiB | 46.25 MiB | **46.28 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | **255.90 MiB** |
| **exp-protegido-ms-usuarios-1** |46.90 MiB | 46.90 MiB | 46.94 MiB | 46.07 MiB | 45.55 MiB | **46.47 MiB** |
| **exp-protegido-postgres-db-1** |70.84 MiB | 66.82 MiB | 67.98 MiB | 70.21 MiB | 66.35 MiB | **68.44 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.80% | 0.68% | 0.87% | 0.80% | 1.23% | **0.88%** |
| **exp-protegido-mongo-db-1** |115.07% | 105.53% | 83.05% | 69.84% | 88.16% | **92.33%** |
| **exp-protegido-ms-catalogo-1** |4.59% | 5.21% | 4.86% | 4.57% | 6.11% | **5.07%** |
| **exp-protegido-ms-ordenes-1** |4.61% | 3.06% | 3.88% | 4.92% | 5.10% | **4.31%** |
| **exp-protegido-ms-resenas-1** |194.12% | 244.65% | 210.36% | 273.52% | 241.10% | **232.75%** |
| **exp-protegido-ms-usuarios-1** |4.32% | 3.75% | 4.66% | 4.27% | 5.15% | **4.43%** |
| **exp-protegido-postgres-db-1** |50.12% | 43.09% | 39.54% | 45.81% | 76.07% | **50.93%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |66.27 MiB | 67.54 MiB | 67.69 MiB | 65.93 MiB | 67.40 MiB | **66.97 MiB** |
| **exp-protegido-mongo-db-1** |354.70 MiB | 334.10 MiB | 348.70 MiB | 347.60 MiB | 334.30 MiB | **343.88 MiB** |
| **exp-protegido-ms-catalogo-1** |46.79 MiB | 46.77 MiB | 46.52 MiB | 46.02 MiB | 48.16 MiB | **46.85 MiB** |
| **exp-protegido-ms-ordenes-1** |46.33 MiB | 45.32 MiB | 46.55 MiB | 46.93 MiB | 46.25 MiB | **46.28 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | **255.90 MiB** |
| **exp-protegido-ms-usuarios-1** |46.90 MiB | 46.90 MiB | 46.94 MiB | 46.07 MiB | 45.55 MiB | **46.47 MiB** |
| **exp-protegido-postgres-db-1** |70.84 MiB | 66.82 MiB | 67.98 MiB | 70.21 MiB | 66.35 MiB | **68.44 MiB** |
