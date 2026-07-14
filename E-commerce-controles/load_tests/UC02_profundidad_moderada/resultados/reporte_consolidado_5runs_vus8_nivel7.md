# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=8)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 11:38:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 480 | 7.350 ms | 0.00% | 100.00% |
| Run 2 | 480 | 6.770 ms | 0.00% | 100.00% |
| Run 3 | 480 | 7.350 ms | 0.00% | 100.00% |
| Run 4 | 480 | 7.340 ms | 0.00% | 100.00% |
| Run 5 | 480 | 7.040 ms | 0.00% | 100.00% |
| **PROMEDIO** | **480.0** | **7.170 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |9.68% | 11.23% | 6.80% | 12.28% | 7.21% | **9.44%** |
| **exp-protegido-mongo-db-1** |60.91% | 52.22% | 60.18% | 57.70% | 48.02% | **55.81%** |
| **exp-protegido-ms-catalogo-1** |4.54% | 4.08% | 3.57% | 3.53% | 3.16% | **3.78%** |
| **exp-protegido-ms-ordenes-1** |3.17% | 3.01% | 3.68% | 4.30% | 3.36% | **3.50%** |
| **exp-protegido-ms-resenas-1** |3.61% | 3.20% | 3.11% | 3.72% | 3.25% | **3.38%** |
| **exp-protegido-ms-usuarios-1** |3.32% | 3.33% | 3.39% | 4.91% | 3.53% | **3.70%** |
| **exp-protegido-postgres-db-1** |3.95% | 4.34% | 4.53% | 5.15% | 4.73% | **4.54%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |81.51 MiB | 97.19 MiB | 76.32 MiB | 82.38 MiB | 75.73 MiB | **82.63 MiB** |
| **exp-protegido-mongo-db-1** |334.70 MiB | 314.10 MiB | 343.00 MiB | 344.00 MiB | 334.00 MiB | **333.96 MiB** |
| **exp-protegido-ms-catalogo-1** |45.96 MiB | 46.62 MiB | 46.93 MiB | 46.27 MiB | 46.16 MiB | **46.39 MiB** |
| **exp-protegido-ms-ordenes-1** |47.49 MiB | 46.08 MiB | 48.06 MiB | 46.49 MiB | 46.89 MiB | **47.00 MiB** |
| **exp-protegido-ms-resenas-1** |46.79 MiB | 46.46 MiB | 47.68 MiB | 47.05 MiB | 54.24 MiB | **48.44 MiB** |
| **exp-protegido-ms-usuarios-1** |47.34 MiB | 45.68 MiB | 45.56 MiB | 46.05 MiB | 47.39 MiB | **46.40 MiB** |
| **exp-protegido-postgres-db-1** |27.35 MiB | 27.36 MiB | 27.43 MiB | 27.38 MiB | 27.95 MiB | **27.49 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |3.73% | 4.20% | 3.43% | 3.63% | 3.52% | **3.70%** |
| **exp-protegido-mongo-db-1** |60.91% | 52.22% | 60.18% | 57.70% | 48.02% | **55.81%** |
| **exp-protegido-ms-catalogo-1** |4.54% | 4.08% | 3.57% | 3.53% | 3.16% | **3.78%** |
| **exp-protegido-ms-ordenes-1** |3.17% | 3.01% | 3.68% | 4.30% | 3.36% | **3.50%** |
| **exp-protegido-ms-resenas-1** |3.61% | 3.20% | 3.11% | 3.72% | 3.25% | **3.38%** |
| **exp-protegido-ms-usuarios-1** |3.32% | 3.33% | 3.39% | 4.91% | 3.53% | **3.70%** |
| **exp-protegido-postgres-db-1** |3.95% | 4.34% | 4.53% | 5.15% | 4.73% | **4.54%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |74.42 MiB | 75.68 MiB | 73.24 MiB | 75.12 MiB | 72.43 MiB | **74.18 MiB** |
| **exp-protegido-mongo-db-1** |334.70 MiB | 314.10 MiB | 343.00 MiB | 344.00 MiB | 334.00 MiB | **333.96 MiB** |
| **exp-protegido-ms-catalogo-1** |45.96 MiB | 46.62 MiB | 46.93 MiB | 46.27 MiB | 46.16 MiB | **46.39 MiB** |
| **exp-protegido-ms-ordenes-1** |47.49 MiB | 46.08 MiB | 48.06 MiB | 46.49 MiB | 46.89 MiB | **47.00 MiB** |
| **exp-protegido-ms-resenas-1** |46.79 MiB | 46.46 MiB | 47.68 MiB | 47.05 MiB | 54.24 MiB | **48.44 MiB** |
| **exp-protegido-ms-usuarios-1** |47.34 MiB | 45.68 MiB | 45.56 MiB | 46.05 MiB | 47.39 MiB | **46.40 MiB** |
| **exp-protegido-postgres-db-1** |27.35 MiB | 27.36 MiB | 27.43 MiB | 27.38 MiB | 27.95 MiB | **27.49 MiB** |
