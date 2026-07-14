# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 10:35:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 66 | 1937.280 ms | 0.00% | 0.00% |
| Run 2 | 57 | 2274.130 ms | 0.00% | 0.00% |
| Run 3 | 57 | 2570.280 ms | 5.26% | 0.00% |
| Run 4 | 66 | 2091.170 ms | 0.00% | 0.00% |
| Run 5 | 60 | 2282.940 ms | 0.00% | 0.00% |
| **PROMEDIO** | **61.2** | **2231.160 ms** | **1.05%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |5.05% | 5.07% | 2.51% | 15.67% | 6.79% | **7.02%** |
| **exp-vulnerable-mongo-db-1** |81.55% | 89.01% | 79.50% | 74.21% | 99.63% | **84.78%** |
| **exp-vulnerable-ms-catalogo-1** |5.11% | 3.48% | 4.11% | 3.48% | 4.02% | **4.04%** |
| **exp-vulnerable-ms-ordenes-1** |5.10% | 4.35% | 5.35% | 3.77% | 3.24% | **4.36%** |
| **exp-vulnerable-ms-resenas-1** |197.84% | 161.29% | 182.34% | 222.81% | 244.24% | **201.70%** |
| **exp-vulnerable-ms-usuarios-1** |4.59% | 4.83% | 5.82% | 3.67% | 4.12% | **4.61%** |
| **exp-vulnerable-postgres-db-1** |31.36% | 21.87% | 19.17% | 24.78% | 36.76% | **26.79%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.77 MiB | 66.44 MiB | 66.71 MiB | 67.73 MiB | 68.29 MiB | **67.39 MiB** |
| **exp-vulnerable-mongo-db-1** |352.20 MiB | 346.50 MiB | 335.50 MiB | 342.10 MiB | 340.90 MiB | **343.44 MiB** |
| **exp-vulnerable-ms-catalogo-1** |53.64 MiB | 46.11 MiB | 45.89 MiB | 47.69 MiB | 46.95 MiB | **48.06 MiB** |
| **exp-vulnerable-ms-ordenes-1** |48.76 MiB | 46.89 MiB | 46.12 MiB | 46.00 MiB | 47.38 MiB | **47.03 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.33 MiB | 46.02 MiB | 46.01 MiB | 48.43 MiB | 47.15 MiB | **47.19 MiB** |
| **exp-vulnerable-postgres-db-1** |60.26 MiB | 60.16 MiB | 60.16 MiB | 60.21 MiB | 60.23 MiB | **60.20 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.76% | 0.67% | 0.48% | 1.27% | 0.81% | **0.80%** |
| **exp-vulnerable-mongo-db-1** |81.55% | 89.01% | 79.50% | 74.21% | 99.63% | **84.78%** |
| **exp-vulnerable-ms-catalogo-1** |5.11% | 3.48% | 4.11% | 3.48% | 4.02% | **4.04%** |
| **exp-vulnerable-ms-ordenes-1** |5.10% | 4.35% | 5.35% | 3.77% | 3.24% | **4.36%** |
| **exp-vulnerable-ms-resenas-1** |197.84% | 161.29% | 182.34% | 222.81% | 244.24% | **201.70%** |
| **exp-vulnerable-ms-usuarios-1** |4.59% | 4.83% | 5.82% | 3.67% | 4.12% | **4.61%** |
| **exp-vulnerable-postgres-db-1** |31.36% | 21.87% | 19.17% | 24.78% | 36.76% | **26.79%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.56 MiB | 65.02 MiB | 65.56 MiB | 65.36 MiB | 65.73 MiB | **65.45 MiB** |
| **exp-vulnerable-mongo-db-1** |352.20 MiB | 346.50 MiB | 335.50 MiB | 342.10 MiB | 340.90 MiB | **343.44 MiB** |
| **exp-vulnerable-ms-catalogo-1** |53.64 MiB | 46.11 MiB | 45.89 MiB | 47.69 MiB | 46.95 MiB | **48.06 MiB** |
| **exp-vulnerable-ms-ordenes-1** |48.76 MiB | 46.89 MiB | 46.12 MiB | 46.00 MiB | 47.38 MiB | **47.03 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.80 MiB | 255.90 MiB | 255.90 MiB | 255.80 MiB | 255.90 MiB | **255.86 MiB** |
| **exp-vulnerable-ms-usuarios-1** |48.33 MiB | 46.02 MiB | 46.01 MiB | 48.43 MiB | 47.15 MiB | **47.19 MiB** |
| **exp-vulnerable-postgres-db-1** |60.26 MiB | 60.16 MiB | 60.16 MiB | 60.21 MiB | 60.23 MiB | **60.20 MiB** |
