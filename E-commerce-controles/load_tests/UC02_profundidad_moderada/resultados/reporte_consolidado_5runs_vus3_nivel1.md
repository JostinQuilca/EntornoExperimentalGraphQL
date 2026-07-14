# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-08 23:07:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 52 | 2462.920 ms | 0.00% | 0.00% |
| Run 2 | 53 | 2533.700 ms | 0.00% | 0.00% |
| Run 3 | 49 | 3052.740 ms | 0.00% | 0.00% |
| Run 4 | 55 | 2472.120 ms | 5.45% | 0.00% |
| Run 5 | 59 | 2060.680 ms | 0.00% | 0.00% |
| **PROMEDIO** | **53.6** | **2516.432 ms** | **1.09%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |143.67% | 91.59% | 120.74% | 84.70% | 113.55% | **110.85%** |
| **exp-protegido-mongo-db-1** |110.21% | 102.92% | 63.18% | 98.31% | 89.59% | **92.84%** |
| **exp-protegido-ms-catalogo-1** |5.70% | 4.65% | 4.11% | 6.11% | 3.69% | **4.85%** |
| **exp-protegido-ms-ordenes-1** |5.18% | 4.27% | 4.76% | 3.35% | 4.32% | **4.38%** |
| **exp-protegido-ms-resenas-1** |160.74% | 204.55% | 214.85% | 188.17% | 177.47% | **189.16%** |
| **exp-protegido-ms-usuarios-1** |4.97% | 4.15% | 4.94% | 3.60% | 4.35% | **4.40%** |
| **exp-protegido-postgres-db-1** |27.40% | 30.36% | 39.52% | 31.27% | 31.22% | **31.95%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |370.50 MiB | 250.60 MiB | 228.80 MiB | 235.50 MiB | 252.90 MiB | **267.66 MiB** |
| **exp-protegido-mongo-db-1** |333.60 MiB | 332.10 MiB | 333.90 MiB | 343.30 MiB | 348.60 MiB | **338.30 MiB** |
| **exp-protegido-ms-catalogo-1** |45.95 MiB | 45.43 MiB | 46.51 MiB | 45.91 MiB | 46.88 MiB | **46.14 MiB** |
| **exp-protegido-ms-ordenes-1** |46.66 MiB | 45.82 MiB | 45.94 MiB | 47.76 MiB | 46.30 MiB | **46.50 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-protegido-ms-usuarios-1** |45.48 MiB | 46.09 MiB | 46.05 MiB | 47.13 MiB | 45.84 MiB | **46.12 MiB** |
| **exp-protegido-postgres-db-1** |61.29 MiB | 60.20 MiB | 60.16 MiB | 60.23 MiB | 60.18 MiB | **60.41 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |10.59% | 7.59% | 5.50% | 5.06% | 10.39% | **7.83%** |
| **exp-protegido-mongo-db-1** |110.21% | 102.92% | 63.18% | 98.31% | 89.59% | **92.84%** |
| **exp-protegido-ms-catalogo-1** |5.70% | 4.65% | 4.11% | 6.11% | 3.69% | **4.85%** |
| **exp-protegido-ms-ordenes-1** |5.18% | 4.27% | 4.76% | 3.35% | 4.32% | **4.38%** |
| **exp-protegido-ms-resenas-1** |160.74% | 204.55% | 214.85% | 188.17% | 177.47% | **189.16%** |
| **exp-protegido-ms-usuarios-1** |4.97% | 4.15% | 4.94% | 3.60% | 4.35% | **4.40%** |
| **exp-protegido-postgres-db-1** |27.40% | 30.36% | 39.52% | 31.27% | 31.22% | **31.95%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |210.60 MiB | 155.46 MiB | 106.01 MiB | 93.48 MiB | 173.31 MiB | **147.77 MiB** |
| **exp-protegido-mongo-db-1** |333.60 MiB | 332.10 MiB | 333.90 MiB | 343.30 MiB | 348.60 MiB | **338.30 MiB** |
| **exp-protegido-ms-catalogo-1** |45.95 MiB | 45.43 MiB | 46.51 MiB | 45.91 MiB | 46.88 MiB | **46.14 MiB** |
| **exp-protegido-ms-ordenes-1** |46.66 MiB | 45.82 MiB | 45.94 MiB | 47.76 MiB | 46.30 MiB | **46.50 MiB** |
| **exp-protegido-ms-resenas-1** |255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.90 MiB** |
| **exp-protegido-ms-usuarios-1** |45.48 MiB | 46.09 MiB | 46.05 MiB | 47.13 MiB | 45.84 MiB | **46.12 MiB** |
| **exp-protegido-postgres-db-1** |61.29 MiB | 60.20 MiB | 60.16 MiB | 60.23 MiB | 60.18 MiB | **60.41 MiB** |
