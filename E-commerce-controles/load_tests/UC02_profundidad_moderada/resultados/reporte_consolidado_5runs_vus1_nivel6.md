# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 21:54:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 60 | 10.450 ms | 0.00% | 100.00% |
| Run 2 | 60 | 9.280 ms | 0.00% | 100.00% |
| Run 3 | 60 | 10.260 ms | 0.00% | 100.00% |
| Run 4 | 60 | 10.480 ms | 0.00% | 100.00% |
| Run 5 | 60 | 9.510 ms | 0.00% | 100.00% |
| **PROMEDIO** | **60.0** | **9.996 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.97% | 3.50% | 3.02% | 3.64% | 3.08% | **3.24%** |
| **exp-protegido-mongo-db-1** |95.83% | 109.47% | 90.08% | 121.39% | 87.56% | **100.87%** |
| **exp-protegido-ms-catalogo-1** |4.67% | 5.76% | 5.46% | 5.51% | 5.04% | **5.29%** |
| **exp-protegido-ms-ordenes-1** |9.81% | 6.47% | 7.04% | 5.04% | 5.66% | **6.80%** |
| **exp-protegido-ms-resenas-1** |5.90% | 6.17% | 7.31% | 5.28% | 4.75% | **5.88%** |
| **exp-protegido-ms-usuarios-1** |7.04% | 6.08% | 4.27% | 5.09% | 4.21% | **5.34%** |
| **exp-protegido-postgres-db-1** |7.70% | 7.21% | 5.15% | 6.17% | 5.93% | **6.43%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |64.41 MiB | 65.68 MiB | 65.22 MiB | 64.89 MiB | 65.35 MiB | **65.11 MiB** |
| **exp-protegido-mongo-db-1** |349.70 MiB | 344.90 MiB | 348.60 MiB | 349.90 MiB | 342.30 MiB | **347.08 MiB** |
| **exp-protegido-ms-catalogo-1** |54.52 MiB | 47.66 MiB | 47.07 MiB | 46.73 MiB | 48.12 MiB | **48.82 MiB** |
| **exp-protegido-ms-ordenes-1** |46.30 MiB | 47.36 MiB | 46.77 MiB | 45.65 MiB | 46.87 MiB | **46.59 MiB** |
| **exp-protegido-ms-resenas-1** |49.02 MiB | 46.19 MiB | 46.68 MiB | 49.17 MiB | 47.86 MiB | **47.78 MiB** |
| **exp-protegido-ms-usuarios-1** |45.23 MiB | 47.60 MiB | 46.70 MiB | 46.64 MiB | 46.70 MiB | **46.57 MiB** |
| **exp-protegido-postgres-db-1** |28.38 MiB | 27.39 MiB | 27.44 MiB | 27.45 MiB | 28.97 MiB | **27.93 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |0.78% | 0.76% | 0.92% | 0.86% | 0.75% | **0.81%** |
| **exp-protegido-mongo-db-1** |95.83% | 109.47% | 90.08% | 121.39% | 87.56% | **100.87%** |
| **exp-protegido-ms-catalogo-1** |4.67% | 5.76% | 5.46% | 5.51% | 5.04% | **5.29%** |
| **exp-protegido-ms-ordenes-1** |9.81% | 6.47% | 7.04% | 5.04% | 5.66% | **6.80%** |
| **exp-protegido-ms-resenas-1** |5.90% | 6.17% | 7.31% | 5.28% | 4.75% | **5.88%** |
| **exp-protegido-ms-usuarios-1** |7.04% | 6.08% | 4.27% | 5.09% | 4.21% | **5.34%** |
| **exp-protegido-postgres-db-1** |7.70% | 7.21% | 5.15% | 6.17% | 5.93% | **6.43%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |63.65 MiB | 64.91 MiB | 64.67 MiB | 63.90 MiB | 64.44 MiB | **64.31 MiB** |
| **exp-protegido-mongo-db-1** |349.70 MiB | 344.90 MiB | 348.60 MiB | 349.90 MiB | 342.30 MiB | **347.08 MiB** |
| **exp-protegido-ms-catalogo-1** |54.52 MiB | 47.66 MiB | 47.07 MiB | 46.73 MiB | 48.12 MiB | **48.82 MiB** |
| **exp-protegido-ms-ordenes-1** |46.30 MiB | 47.36 MiB | 46.77 MiB | 45.65 MiB | 46.87 MiB | **46.59 MiB** |
| **exp-protegido-ms-resenas-1** |49.02 MiB | 46.19 MiB | 46.68 MiB | 49.17 MiB | 47.86 MiB | **47.78 MiB** |
| **exp-protegido-ms-usuarios-1** |45.23 MiB | 47.60 MiB | 46.70 MiB | 46.64 MiB | 46.70 MiB | **46.57 MiB** |
| **exp-protegido-postgres-db-1** |28.38 MiB | 27.39 MiB | 27.44 MiB | 27.45 MiB | 28.97 MiB | **27.93 MiB** |
