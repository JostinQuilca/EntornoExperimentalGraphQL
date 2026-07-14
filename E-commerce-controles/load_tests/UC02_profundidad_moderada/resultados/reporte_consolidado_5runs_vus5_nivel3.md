# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 11:46:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 111 | 1716.020 ms | 4.50% | 0.00% |
| Run 2 | 85 | 2698.410 ms | 0.00% | 0.00% |
| Run 3 | 110 | 1884.830 ms | 0.00% | 0.00% |
| Run 4 | 93 | 2243.570 ms | 5.37% | 0.00% |
| Run 5 | 105 | 2251.980 ms | 0.00% | 0.00% |
| **PROMEDIO** | **100.8** | **2158.962 ms** | **1.97%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |5.31% | 9.07% | 6.57% | 7.42% | 8.01% | **7.28%** |
| **exp-protegido-mongo-db-1** |113.27% | 104.06% | 92.22% | 116.22% | 82.53% | **101.66%** |
| **exp-protegido-ms-catalogo-1** |4.37% | 3.84% | 6.76% | 4.72% | 4.34% | **4.81%** |
| **exp-protegido-ms-ordenes-1** |7.34% | 3.69% | 4.98% | 6.95% | 6.87% | **5.97%** |
| **exp-protegido-ms-resenas-1** |227.98% | 230.10% | 222.00% | 184.17% | 242.02% | **221.25%** |
| **exp-protegido-ms-usuarios-1** |4.87% | 3.71% | 4.93% | 8.02% | 6.91% | **5.69%** |
| **exp-protegido-postgres-db-1** |61.06% | 50.05% | 46.28% | 43.15% | 56.88% | **51.48%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |69.48 MiB | 68.30 MiB | 68.66 MiB | 68.76 MiB | 69.36 MiB | **68.91 MiB** |
| **exp-protegido-mongo-db-1** |350.50 MiB | 348.30 MiB | 334.50 MiB | 348.00 MiB | 343.70 MiB | **345.00 MiB** |
| **exp-protegido-ms-catalogo-1** |45.90 MiB | 46.57 MiB | 46.65 MiB | 46.55 MiB | 46.37 MiB | **46.41 MiB** |
| **exp-protegido-ms-ordenes-1** |48.01 MiB | 45.57 MiB | 46.36 MiB | 47.31 MiB | 47.11 MiB | **46.87 MiB** |
| **exp-protegido-ms-resenas-1** |255.70 MiB | 255.90 MiB | 256.00 MiB | 255.80 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-protegido-ms-usuarios-1** |46.38 MiB | 45.60 MiB | 47.01 MiB | 45.77 MiB | 47.34 MiB | **46.42 MiB** |
| **exp-protegido-postgres-db-1** |70.91 MiB | 71.50 MiB | 67.11 MiB | 70.97 MiB | 72.05 MiB | **70.51 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.63% | 1.45% | 1.32% | 1.04% | 1.59% | **1.41%** |
| **exp-protegido-mongo-db-1** |113.27% | 104.06% | 92.22% | 116.22% | 82.53% | **101.66%** |
| **exp-protegido-ms-catalogo-1** |4.37% | 3.84% | 6.76% | 4.72% | 4.34% | **4.81%** |
| **exp-protegido-ms-ordenes-1** |7.34% | 3.69% | 4.98% | 6.95% | 6.87% | **5.97%** |
| **exp-protegido-ms-resenas-1** |227.98% | 230.10% | 222.00% | 184.17% | 242.02% | **221.25%** |
| **exp-protegido-ms-usuarios-1** |4.87% | 3.71% | 4.93% | 8.02% | 6.91% | **5.69%** |
| **exp-protegido-postgres-db-1** |61.06% | 50.05% | 46.28% | 43.15% | 56.88% | **51.48%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |67.14 MiB | 66.40 MiB | 66.23 MiB | 66.92 MiB | 66.81 MiB | **66.70 MiB** |
| **exp-protegido-mongo-db-1** |350.50 MiB | 348.30 MiB | 334.50 MiB | 348.00 MiB | 343.70 MiB | **345.00 MiB** |
| **exp-protegido-ms-catalogo-1** |45.90 MiB | 46.57 MiB | 46.65 MiB | 46.55 MiB | 46.37 MiB | **46.41 MiB** |
| **exp-protegido-ms-ordenes-1** |48.01 MiB | 45.57 MiB | 46.36 MiB | 47.31 MiB | 47.11 MiB | **46.87 MiB** |
| **exp-protegido-ms-resenas-1** |255.70 MiB | 255.90 MiB | 256.00 MiB | 255.80 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-protegido-ms-usuarios-1** |46.38 MiB | 45.60 MiB | 47.01 MiB | 45.77 MiB | 47.34 MiB | **46.42 MiB** |
| **exp-protegido-postgres-db-1** |70.91 MiB | 71.50 MiB | 67.11 MiB | 70.97 MiB | 72.05 MiB | **70.51 MiB** |
