# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-08 22:56:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 46 | 3321.250 ms | 6.52% | 0.00% |
| Run 2 | 51 | 2555.380 ms | 5.88% | 0.00% |
| Run 3 | 65 | 2074.330 ms | 0.00% | 0.00% |
| Run 4 | 54 | 2390.730 ms | 0.00% | 0.00% |
| Run 5 | 56 | 2970.220 ms | 5.35% | 0.00% |
| **PROMEDIO** | **54.4** | **2662.382 ms** | **3.55%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |9.67% | 52.27% | 72.08% | 124.89% | 61.84% | **64.15%** |
| **exp-vulnerable-mongo-db-1** |77.05% | 112.10% | 110.87% | 100.41% | 102.84% | **100.65%** |
| **exp-vulnerable-ms-catalogo-1** |4.30% | 5.25% | 3.44% | 5.98% | 4.60% | **4.71%** |
| **exp-vulnerable-ms-ordenes-1** |6.25% | 5.40% | 5.63% | 4.92% | 3.59% | **5.16%** |
| **exp-vulnerable-ms-resenas-1** |183.85% | 206.63% | 192.61% | 180.79% | 228.47% | **198.47%** |
| **exp-vulnerable-ms-usuarios-1** |4.18% | 4.81% | 4.72% | 4.74% | 3.84% | **4.46%** |
| **exp-vulnerable-postgres-db-1** |27.26% | 34.42% | 31.01% | 30.40% | 42.32% | **33.08%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |141.20 MiB | 227.70 MiB | 172.10 MiB | 227.90 MiB | 372.80 MiB | **228.34 MiB** |
| **exp-vulnerable-mongo-db-1** |354.40 MiB | 271.30 MiB | 333.30 MiB | 350.40 MiB | 350.60 MiB | **332.00 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.54 MiB | 46.24 MiB | 45.50 MiB | 47.58 MiB | 48.27 MiB | **46.83 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.38 MiB | 46.97 MiB | 45.91 MiB | 46.31 MiB | 47.11 MiB | **46.54 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | **255.92 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.27 MiB | 45.46 MiB | 46.33 MiB | 45.73 MiB | 45.96 MiB | **45.95 MiB** |
| **exp-vulnerable-postgres-db-1** |60.20 MiB | 60.19 MiB | 60.49 MiB | 61.73 MiB | 60.21 MiB | **60.56 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.71% | 2.90% | 4.82% | 5.52% | 5.70% | **3.93%** |
| **exp-vulnerable-mongo-db-1** |77.05% | 112.10% | 110.87% | 100.41% | 102.84% | **100.65%** |
| **exp-vulnerable-ms-catalogo-1** |4.30% | 5.25% | 3.44% | 5.98% | 4.60% | **4.71%** |
| **exp-vulnerable-ms-ordenes-1** |6.25% | 5.40% | 5.63% | 4.92% | 3.59% | **5.16%** |
| **exp-vulnerable-ms-resenas-1** |183.85% | 206.63% | 192.61% | 180.79% | 228.47% | **198.47%** |
| **exp-vulnerable-ms-usuarios-1** |4.18% | 4.81% | 4.72% | 4.74% | 3.84% | **4.46%** |
| **exp-vulnerable-postgres-db-1** |27.26% | 34.42% | 31.01% | 30.40% | 42.32% | **33.08%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |81.10 MiB | 94.41 MiB | 98.18 MiB | 102.38 MiB | 191.41 MiB | **113.50 MiB** |
| **exp-vulnerable-mongo-db-1** |354.40 MiB | 271.30 MiB | 333.30 MiB | 350.40 MiB | 350.60 MiB | **332.00 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.54 MiB | 46.24 MiB | 45.50 MiB | 47.58 MiB | 48.27 MiB | **46.83 MiB** |
| **exp-vulnerable-ms-ordenes-1** |46.38 MiB | 46.97 MiB | 45.91 MiB | 46.31 MiB | 47.11 MiB | **46.54 MiB** |
| **exp-vulnerable-ms-resenas-1** |255.90 MiB | 255.90 MiB | 256.00 MiB | 255.90 MiB | 255.90 MiB | **255.92 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.27 MiB | 45.46 MiB | 46.33 MiB | 45.73 MiB | 45.96 MiB | **45.95 MiB** |
| **exp-vulnerable-postgres-db-1** |60.20 MiB | 60.19 MiB | 60.49 MiB | 61.73 MiB | 60.21 MiB | **60.56 MiB** |
