# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=2)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 09:04:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 48 | 1782.750 ms | 0.00% | 0.00% |
| Run 2 | 48 | 1504.240 ms | 0.00% | 0.00% |
| Run 3 | 44 | 1742.380 ms | 0.00% | 0.00% |
| Run 4 | 50 | 1622.290 ms | 0.00% | 0.00% |
| Run 5 | 49 | 1426.880 ms | 0.00% | 0.00% |
| **PROMEDIO** | **47.8** | **1615.708 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |4.65% | 2.31% | 6.93% | 3.37% | 2.67% | **3.99%** |
| **exp-vulnerable-mongo-db-1** |72.64% | 88.24% | 111.33% | 115.32% | 99.36% | **97.38%** |
| **exp-vulnerable-ms-catalogo-1** |2.85% | 6.09% | 5.27% | 4.05% | 5.57% | **4.77%** |
| **exp-vulnerable-ms-ordenes-1** |3.78% | 4.36% | 4.50% | 4.72% | 5.67% | **4.61%** |
| **exp-vulnerable-ms-resenas-1** |170.93% | 187.66% | 194.36% | 200.88% | 186.68% | **188.10%** |
| **exp-vulnerable-ms-usuarios-1** |3.60% | 4.64% | 4.36% | 5.39% | 4.89% | **4.58%** |
| **exp-vulnerable-postgres-db-1** |32.48% | 22.63% | 27.70% | 22.24% | 29.40% | **26.89%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.92 MiB | 66.18 MiB | 65.56 MiB | 66.08 MiB | 66.26 MiB | **66.00 MiB** |
| **exp-vulnerable-mongo-db-1** |335.00 MiB | 348.60 MiB | 341.60 MiB | 349.70 MiB | 341.70 MiB | **343.32 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.08 MiB | 47.91 MiB | 48.09 MiB | 46.93 MiB | 45.67 MiB | **46.94 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.69 MiB | 46.59 MiB | 46.58 MiB | 45.97 MiB | 47.52 MiB | **46.47 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.98 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.94 MiB | 46.62 MiB | 55.70 MiB | 45.58 MiB | 45.87 MiB | **48.14 MiB** |
| **exp-vulnerable-postgres-db-1** |60.77 MiB | 58.46 MiB | 58.50 MiB | 58.46 MiB | 58.45 MiB | **58.93 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |0.50% | 0.42% | 0.73% | 0.71% | 0.44% | **0.56%** |
| **exp-vulnerable-mongo-db-1** |72.64% | 88.24% | 111.33% | 115.32% | 99.36% | **97.38%** |
| **exp-vulnerable-ms-catalogo-1** |2.85% | 6.09% | 5.27% | 4.05% | 5.57% | **4.77%** |
| **exp-vulnerable-ms-ordenes-1** |3.78% | 4.36% | 4.50% | 4.72% | 5.67% | **4.61%** |
| **exp-vulnerable-ms-resenas-1** |170.93% | 187.66% | 194.36% | 200.88% | 186.68% | **188.10%** |
| **exp-vulnerable-ms-usuarios-1** |3.60% | 4.64% | 4.36% | 5.39% | 4.89% | **4.58%** |
| **exp-vulnerable-postgres-db-1** |32.48% | 22.63% | 27.70% | 22.24% | 29.40% | **26.89%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |64.89 MiB | 65.01 MiB | 64.69 MiB | 65.03 MiB | 65.35 MiB | **64.99 MiB** |
| **exp-vulnerable-mongo-db-1** |335.00 MiB | 348.60 MiB | 341.60 MiB | 349.70 MiB | 341.70 MiB | **343.32 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.08 MiB | 47.91 MiB | 48.09 MiB | 46.93 MiB | 45.67 MiB | **46.94 MiB** |
| **exp-vulnerable-ms-ordenes-1** |45.69 MiB | 46.59 MiB | 46.58 MiB | 45.97 MiB | 47.52 MiB | **46.47 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 256.00 MiB | 255.90 MiB | 256.00 MiB | 256.00 MiB | **255.98 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.94 MiB | 46.62 MiB | 55.70 MiB | 45.58 MiB | 45.87 MiB | **48.14 MiB** |
| **exp-vulnerable-postgres-db-1** |60.77 MiB | 58.46 MiB | 58.50 MiB | 58.46 MiB | 58.45 MiB | **58.93 MiB** |
