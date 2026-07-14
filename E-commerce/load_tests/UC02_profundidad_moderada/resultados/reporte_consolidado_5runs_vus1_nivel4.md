# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-09 11:56:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 22 | 1847.280 ms | 0.00% | 0.00% |
| Run 2 | 24 | 1572.340 ms | 0.00% | 0.00% |
| Run 3 | 29 | 1138.870 ms | 0.00% | 0.00% |
| Run 4 | 23 | 1729.110 ms | 0.00% | 0.00% |
| Run 5 | 23 | 1685.190 ms | 0.00% | 0.00% |
| **PROMEDIO** | **24.2** | **1594.558 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |17.52% | 1.91% | 8.45% | 2.19% | 4.17% | **6.85%** |
| **exp-vulnerable-mongo-db-1** |91.76% | 72.07% | 96.10% | 80.06% | 87.46% | **85.49%** |
| **exp-vulnerable-ms-catalogo-1** |3.76% | 3.33% | 5.47% | 4.09% | 3.18% | **3.97%** |
| **exp-vulnerable-ms-ordenes-1** |6.39% | 7.15% | 6.03% | 4.78% | 2.72% | **5.41%** |
| **exp-vulnerable-ms-resenas-1** |209.45% | 213.49% | 195.30% | 211.08% | 212.75% | **208.41%** |
| **exp-vulnerable-ms-usuarios-1** |6.16% | 6.79% | 4.70% | 5.63% | 3.49% | **5.35%** |
| **exp-vulnerable-postgres-db-1** |28.87% | 14.57% | 21.96% | 8.79% | 11.50% | **17.14%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |96.84 MiB | 64.89 MiB | 65.48 MiB | 64.92 MiB | 65.34 MiB | **71.49 MiB** |
| **exp-vulnerable-mongo-db-1** |189.10 MiB | 334.50 MiB | 318.60 MiB | 340.00 MiB | 348.60 MiB | **306.16 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.17 MiB | 45.51 MiB | 45.77 MiB | 45.55 MiB | 45.61 MiB | **45.72 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.43 MiB | 47.22 MiB | 46.29 MiB | 45.94 MiB | 46.14 MiB | **46.60 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.92 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.39 MiB | 55.70 MiB | 45.62 MiB | 46.23 MiB | 47.19 MiB | **48.43 MiB** |
| **exp-vulnerable-postgres-db-1** |56.77 MiB | 57.16 MiB | 56.80 MiB | 56.79 MiB | 57.16 MiB | **56.94 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.00% | 0.40% | 0.78% | 0.27% | 0.49% | **0.59%** |
| **exp-vulnerable-mongo-db-1** |91.76% | 72.07% | 96.10% | 80.06% | 87.46% | **85.49%** |
| **exp-vulnerable-ms-catalogo-1** |3.76% | 3.33% | 5.47% | 4.09% | 3.18% | **3.97%** |
| **exp-vulnerable-ms-ordenes-1** |6.39% | 7.15% | 6.03% | 4.78% | 2.72% | **5.41%** |
| **exp-vulnerable-ms-resenas-1** |209.45% | 213.49% | 195.30% | 211.08% | 212.75% | **208.41%** |
| **exp-vulnerable-ms-usuarios-1** |6.16% | 6.79% | 4.70% | 5.63% | 3.49% | **5.35%** |
| **exp-vulnerable-postgres-db-1** |28.87% | 14.57% | 21.96% | 8.79% | 11.50% | **17.14%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |67.98 MiB | 64.12 MiB | 64.64 MiB | 64.33 MiB | 64.43 MiB | **65.10 MiB** |
| **exp-vulnerable-mongo-db-1** |189.10 MiB | 334.50 MiB | 318.60 MiB | 340.00 MiB | 348.60 MiB | **306.16 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.17 MiB | 45.51 MiB | 45.77 MiB | 45.55 MiB | 45.61 MiB | **45.72 MiB** |
| **exp-vulnerable-ms-ordenes-1** |47.43 MiB | 47.22 MiB | 46.29 MiB | 45.94 MiB | 46.14 MiB | **46.60 MiB** |
| **exp-vulnerable-ms-resenas-1** |256.00 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | 255.90 MiB | **255.92 MiB** |
| **exp-vulnerable-ms-usuarios-1** |47.39 MiB | 55.70 MiB | 45.62 MiB | 46.23 MiB | 47.19 MiB | **48.43 MiB** |
| **exp-vulnerable-postgres-db-1** |56.77 MiB | 57.16 MiB | 56.80 MiB | 56.79 MiB | 57.16 MiB | **56.94 MiB** |
