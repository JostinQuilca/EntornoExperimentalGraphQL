# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 22:20:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 120 | 11.310 ms | 0.00% | 100.00% |
| Run 2 | 120 | 10.100 ms | 0.00% | 100.00% |
| Run 3 | 120 | 8.760 ms | 0.00% | 100.00% |
| Run 4 | 120 | 9.230 ms | 0.00% | 100.00% |
| Run 5 | 120 | 8.220 ms | 0.00% | 100.00% |
| **PROMEDIO** | **120.0** | **9.524 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |11.74% | 3.36% | 7.73% | 1.79% | 5.27% | **5.98%** |
| **exp-protegido-mongo-db-1** |117.12% | 99.78% | 100.54% | 82.39% | 91.85% | **98.34%** |
| **exp-protegido-ms-catalogo-1** |5.34% | 3.93% | 5.19% | 4.98% | 4.86% | **4.86%** |
| **exp-protegido-ms-ordenes-1** |5.75% | 5.25% | 4.51% | 5.84% | 5.20% | **5.31%** |
| **exp-protegido-ms-resenas-1** |8.78% | 5.01% | 4.31% | 5.71% | 4.94% | **5.75%** |
| **exp-protegido-ms-usuarios-1** |10.38% | 4.81% | 4.43% | 4.77% | 6.59% | **6.20%** |
| **exp-protegido-postgres-db-1** |8.50% | 6.99% | 6.64% | 7.98% | 6.70% | **7.36%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |95.96 MiB | 66.00 MiB | 66.82 MiB | 66.14 MiB | 97.32 MiB | **78.45 MiB** |
| **exp-protegido-mongo-db-1** |348.20 MiB | 343.60 MiB | 350.60 MiB | 347.10 MiB | 341.40 MiB | **346.18 MiB** |
| **exp-protegido-ms-catalogo-1** |46.12 MiB | 47.09 MiB | 46.32 MiB | 47.94 MiB | 45.99 MiB | **46.69 MiB** |
| **exp-protegido-ms-ordenes-1** |46.26 MiB | 47.30 MiB | 45.56 MiB | 46.37 MiB | 46.09 MiB | **46.32 MiB** |
| **exp-protegido-ms-resenas-1** |49.28 MiB | 45.92 MiB | 46.76 MiB | 47.32 MiB | 46.57 MiB | **47.17 MiB** |
| **exp-protegido-ms-usuarios-1** |47.43 MiB | 45.92 MiB | 45.94 MiB | 47.78 MiB | 46.62 MiB | **46.74 MiB** |
| **exp-protegido-postgres-db-1** |27.56 MiB | 27.56 MiB | 27.48 MiB | 27.55 MiB | 27.39 MiB | **27.51 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1.89% | 1.18% | 1.51% | 1.06% | 1.28% | **1.38%** |
| **exp-protegido-mongo-db-1** |117.12% | 99.78% | 100.54% | 82.39% | 91.85% | **98.34%** |
| **exp-protegido-ms-catalogo-1** |5.34% | 3.93% | 5.19% | 4.98% | 4.86% | **4.86%** |
| **exp-protegido-ms-ordenes-1** |5.75% | 5.25% | 4.51% | 5.84% | 5.20% | **5.31%** |
| **exp-protegido-ms-resenas-1** |8.78% | 5.01% | 4.31% | 5.71% | 4.94% | **5.75%** |
| **exp-protegido-ms-usuarios-1** |10.38% | 4.81% | 4.43% | 4.77% | 6.59% | **6.20%** |
| **exp-protegido-postgres-db-1** |8.50% | 6.99% | 6.64% | 7.98% | 6.70% | **7.36%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |65.86 MiB | 64.83 MiB | 65.55 MiB | 64.84 MiB | 72.28 MiB | **66.67 MiB** |
| **exp-protegido-mongo-db-1** |348.20 MiB | 343.60 MiB | 350.60 MiB | 347.10 MiB | 341.40 MiB | **346.18 MiB** |
| **exp-protegido-ms-catalogo-1** |46.12 MiB | 47.09 MiB | 46.32 MiB | 47.94 MiB | 45.99 MiB | **46.69 MiB** |
| **exp-protegido-ms-ordenes-1** |46.26 MiB | 47.30 MiB | 45.56 MiB | 46.37 MiB | 46.09 MiB | **46.32 MiB** |
| **exp-protegido-ms-resenas-1** |49.28 MiB | 45.92 MiB | 46.76 MiB | 47.32 MiB | 46.57 MiB | **47.17 MiB** |
| **exp-protegido-ms-usuarios-1** |47.43 MiB | 45.92 MiB | 45.94 MiB | 47.78 MiB | 46.62 MiB | **46.74 MiB** |
| **exp-protegido-postgres-db-1** |27.56 MiB | 27.56 MiB | 27.48 MiB | 27.55 MiB | 27.39 MiB | **27.51 MiB** |
