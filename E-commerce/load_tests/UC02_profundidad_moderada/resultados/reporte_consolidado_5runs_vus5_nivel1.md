# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-08 23:17:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 96 | 2283.240 ms | 0.00% | 0.00% |
| Run 2 | 95 | 2554.630 ms | 0.00% | 0.00% |
| Run 3 | 135 | 1366.390 ms | 0.00% | 0.00% |
| Run 4 | 120 | 1506.920 ms | 0.00% | 0.00% |
| Run 5 | 113 | 1995.240 ms | 4.42% | 0.00% |
| **PROMEDIO** | **111.8** | **1941.284 ms** | **0.88%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |8.74% | 8.39% | 6.95% | 126.02% | 3.28% | **30.68%** |
| **exp-vulnerable-mongo-db-1** |104.23% | 102.49% | 90.11% | 91.48% | 63.49% | **90.36%** |
| **exp-vulnerable-ms-catalogo-1** |4.73% | 5.21% | 4.16% | 5.77% | 8.01% | **5.58%** |
| **exp-vulnerable-ms-ordenes-1** |4.43% | 5.42% | 3.40% | 6.04% | 5.16% | **4.89%** |
| **exp-vulnerable-ms-resenas-1** |217.19% | 220.95% | 233.90% | 217.49% | 270.66% | **232.04%** |
| **exp-vulnerable-ms-usuarios-1** |4.71% | 5.43% | 3.44% | 6.39% | 5.63% | **5.12%** |
| **exp-vulnerable-postgres-db-1** |48.08% | 55.43% | 37.47% | 42.95% | 47.35% | **46.26%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |97.86 MiB | 68.43 MiB | 69.74 MiB | 247.40 MiB | 68.57 MiB | **110.40 MiB** |
| **exp-vulnerable-mongo-db-1** |346.70 MiB | 349.30 MiB | 334.70 MiB | 346.00 MiB | 334.70 MiB | **342.28 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.51 MiB | 47.82 MiB | 45.47 MiB | 45.62 MiB | 46.18 MiB | **46.12 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.68 MiB | 46.11 MiB | 45.58 MiB | 45.77 MiB | 47.11 MiB | **46.05 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.80 MiB | 256.00 MiB | 255.80 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.70 MiB | 46.58 MiB | 45.95 MiB | 45.62 MiB | 48.78 MiB | **46.53 MiB** |
| **exp-vulnerable-postgres-db-1** |77.35 MiB | 71.18 MiB | 75.68 MiB | 67.07 MiB | 69.29 MiB | **72.11 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.38% | 0.93% | 1.22% | 6.06% | 0.84% | **2.09%** |
| **exp-vulnerable-mongo-db-1** |104.23% | 102.49% | 90.11% | 91.48% | 63.49% | **90.36%** |
| **exp-vulnerable-ms-catalogo-1** |4.73% | 5.21% | 4.16% | 5.77% | 8.01% | **5.58%** |
| **exp-vulnerable-ms-ordenes-1** |4.43% | 5.42% | 3.40% | 6.04% | 5.16% | **4.89%** |
| **exp-vulnerable-ms-resenas-1** |217.19% | 220.95% | 233.90% | 217.49% | 270.66% | **232.04%** |
| **exp-vulnerable-ms-usuarios-1** |4.71% | 5.43% | 3.44% | 6.39% | 5.63% | **5.12%** |
| **exp-vulnerable-postgres-db-1** |48.08% | 55.43% | 37.47% | 42.95% | 47.35% | **46.26%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |82.47 MiB | 66.09 MiB | 67.18 MiB | 163.88 MiB | 66.78 MiB | **89.28 MiB** |
| **exp-vulnerable-mongo-db-1** |346.70 MiB | 349.30 MiB | 334.70 MiB | 346.00 MiB | 334.70 MiB | **342.28 MiB** |
| **exp-vulnerable-ms-catalogo-1** |45.51 MiB | 47.82 MiB | 45.47 MiB | 45.62 MiB | 46.18 MiB | **46.12 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.68 MiB | 46.11 MiB | 45.58 MiB | 45.77 MiB | 47.11 MiB | **46.05 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.80 MiB | 256.00 MiB | 255.80 MiB | 255.90 MiB | **255.88 MiB** |
| **exp-vulnerable-ms-usuarios-1** |45.70 MiB | 46.58 MiB | 45.95 MiB | 45.62 MiB | 48.78 MiB | **46.53 MiB** |
| **exp-vulnerable-postgres-db-1** |77.35 MiB | 71.18 MiB | 75.68 MiB | 67.07 MiB | 69.29 MiB | **72.11 MiB** |
