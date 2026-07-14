# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=1)
**Prueba:** uc04_alias_nivel
**Fecha de Consolidación:** 2026-07-11 01:01:26

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 38 | 604.231 ms | 0.00% | 0.00% |
| Run 2 | 38 | 595.660 ms | 0.00% | 0.00% |
| Run 3 | 38 | 592.401 ms | 0.00% | 0.00% |
| Run 4 | 38 | 593.407 ms | 0.00% | 0.00% |
| Run 5 | 38 | 593.435 ms | 0.00% | 0.00% |
| **PROMEDIO** | **38.0** | **595.827 ms** | **0.00%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |3.82% | 3.03% | 18.07% | 10.15% | 3.59% | **7.73%** |
| **exp-vulnerable-mongo-db-1** |74.14% | 78.54% | 83.67% | 74.76% | 99.97% | **82.22%** |
| **exp-vulnerable-ms-catalogo-1** |4.21% | 4.72% | 4.17% | 8.78% | 4.95% | **5.37%** |
| **exp-vulnerable-ms-ordenes-1** |11.80% | 7.45% | 9.12% | 16.12% | 7.18% | **10.33%** |
| **exp-vulnerable-ms-resenas-1** |6.46% | 4.91% | 4.29% | 10.72% | 4.66% | **6.21%** |
| **exp-vulnerable-ms-usuarios-1** |4.45% | 4.94% | 4.28% | 8.98% | 5.43% | **5.62%** |
| **exp-vulnerable-postgres-db-1** |16.68% | 11.08% | 11.52% | 14.19% | 14.28% | **13.55%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |66.39MiB (66.39 MiB)  | 66.44MiB (66.44 MiB)  | 98.33MiB (98.33 MiB)  | 66.48MiB (66.48 MiB)  | 96.48MiB (96.48 MiB)  |
| **exp-vulnerable-mongo-db-1** |339.6MiB (339.60 MiB)  | 345.6MiB (345.60 MiB)  | 351.5MiB (351.50 MiB)  | 343MiB (343.00 MiB)  | 351.2MiB (351.20 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |46.54MiB (46.54 MiB)  | 47.43MiB (47.43 MiB)  | 49.01MiB (49.01 MiB)  | 45.99MiB (45.99 MiB)  | 47.57MiB (47.57 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |60.72MiB (60.72 MiB)  | 53.53MiB (53.53 MiB)  | 53.39MiB (53.39 MiB)  | 54.86MiB (54.86 MiB)  | 53.79MiB (53.79 MiB)  |
| **exp-vulnerable-ms-resenas-1** |54.23MiB (54.23 MiB)  | 46.73MiB (46.73 MiB)  | 46.21MiB (46.21 MiB)  | 45.98MiB (45.98 MiB)  | 47.18MiB (47.18 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |47.14MiB (47.14 MiB)  | 45.27MiB (45.27 MiB)  | 45.71MiB (45.71 MiB)  | 46.02MiB (46.02 MiB)  | 54.32MiB (54.32 MiB)  |
| **exp-vulnerable-postgres-db-1** |37.73MiB (37.73 MiB)  | 37.95MiB (37.95 MiB)  | 37.63MiB (37.63 MiB)  | 37.98MiB (37.98 MiB)  | 37.69MiB (37.69 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |1.12% | 0.84% | 1.46% | 1.12% | 1.02% | **1.11%** |
| **exp-vulnerable-mongo-db-1** |18.27% | 18.61% | 19.82% | 20.50% | 23.68% | **20.18%** |
| **exp-vulnerable-ms-catalogo-1** |1.06% | 0.94% | 1.01% | 1.35% | 1.18% | **1.11%** |
| **exp-vulnerable-ms-ordenes-1** |3.63% | 2.69% | 2.86% | 3.58% | 3.14% | **3.18%** |
| **exp-vulnerable-ms-resenas-1** |1.30% | 1.15% | 0.95% | 1.36% | 1.16% | **1.18%** |
| **exp-vulnerable-ms-usuarios-1** |1.22% | 1.15% | 1.03% | 1.29% | 1.12% | **1.16%** |
| **exp-vulnerable-postgres-db-1** |6.58% | 4.61% | 5.15% | 6.34% | 6.00% | **5.74%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-vulnerable-api-gateway-1** |65.32 MiB | 65.38 MiB | 81.04 MiB | 65.27 MiB | 66.62 MiB | **68.73 MiB** |
| **exp-vulnerable-mongo-db-1** |208.97 MiB | 206.25 MiB | 199.38 MiB | 204.35 MiB | 205.57 MiB | **204.90 MiB** |
| **exp-vulnerable-ms-catalogo-1** |46.41 MiB | 47.31 MiB | 47.57 MiB | 45.88 MiB | 46.18 MiB | **46.67 MiB** |
| **exp-vulnerable-ms-ordenes-1** |52.92 MiB | 50.97 MiB | 51.33 MiB | 52.00 MiB | 51.37 MiB | **51.72 MiB** |
| **exp-vulnerable-ms-resenas-1** |54.11 MiB | 46.61 MiB | 46.09 MiB | 45.87 MiB | 45.79 MiB | **47.69 MiB** |
| **exp-vulnerable-ms-usuarios-1** |46.85 MiB | 45.15 MiB | 45.60 MiB | 45.90 MiB | 46.95 MiB | **46.09 MiB** |
| **exp-vulnerable-postgres-db-1** |37.30 MiB | 37.34 MiB | 37.23 MiB | 37.33 MiB | 37.29 MiB | **37.30 MiB** |