# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=144)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 20:05:19

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 8513 | 19.942 ms | 0.00% |
| Run 2 | 8526 | 18.443 ms | 0.00% |
| Run 3 | 8380 | 38.734 ms | 0.00% |
| **PROMEDIO** | **8473.0** | **25.706 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **--** |0.00% | 0.00% | 0.00% | **0.00%** |
| **exp-protegido-api-gateway-1** |0.00% | 77.40% | 68.86% | **48.75%** |
| **exp-protegido-mongo-db-1** |0.00% | 68.79% | 72.13% | **46.97%** |
| **exp-protegido-ms-catalogo-1** |0.00% | 2.67% | 5.24% | **2.64%** |
| **exp-protegido-ms-ordenes-1** |0.00% | 3.15% | 6.27% | **3.14%** |
| **exp-protegido-ms-resenas-1** |0.00% | 3.36% | 5.11% | **2.82%** |
| **exp-protegido-ms-usuarios-1** |0.00% | 3.61% | 5.23% | **2.95%** |
| **exp-protegido-postgres-db-1** |0.00% | 6.08% | 6.73% | **4.27%** |
| **exp-vulnerable-mongo-db-1** |0.00% | 0.00% | 78.77% | **26.26%** |
| **exp-vulnerable-mongo-init-1** |0.00% | 0.00% | 45.64% | **15.21%** |
| **exp-vulnerable-ms-catalogo-1** |0.00% | 0.00% | 136.84% | **45.61%** |
| **exp-vulnerable-ms-ordenes-1** |0.00% | 0.00% | 108.75% | **36.25%** |
| **exp-vulnerable-ms-resenas-1** |0.00% | 0.00% | 106.91% | **35.64%** |
| **exp-vulnerable-ms-usuarios-1** |0.00% | 0.00% | 97.69% | **32.56%** |
| **exp-vulnerable-postgres-db-1** |0.00% | 0.00% | 32.20% | **10.73%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **--** |N/A | N/A | (0.00 MiB)  |
| **exp-protegido-api-gateway-1** |N/A | 148.5MiB (148.50 MiB)  | 127.4MiB (127.40 MiB)  |
| **exp-protegido-mongo-db-1** |N/A | 341.5MiB (341.50 MiB)  | 337.9MiB (337.90 MiB)  |
| **exp-protegido-ms-catalogo-1** |N/A | 46.2MiB (46.20 MiB)  | 47.35MiB (47.35 MiB)  |
| **exp-protegido-ms-ordenes-1** |N/A | 46.98MiB (46.98 MiB)  | 46.07MiB (46.07 MiB)  |
| **exp-protegido-ms-resenas-1** |N/A | 45.93MiB (45.93 MiB)  | 46.96MiB (46.96 MiB)  |
| **exp-protegido-ms-usuarios-1** |N/A | 45.88MiB (45.88 MiB)  | 45.74MiB (45.74 MiB)  |
| **exp-protegido-postgres-db-1** |N/A | 27.98MiB (27.98 MiB)  | 28.01MiB (28.01 MiB)  |
| **exp-vulnerable-mongo-db-1** |N/A | N/A | 349.4MiB (349.40 MiB)  |
| **exp-vulnerable-mongo-init-1** |N/A | N/A | 157.4MiB (157.40 MiB)  |
| **exp-vulnerable-ms-catalogo-1** |N/A | N/A | 64.07MiB (64.07 MiB)  |
| **exp-vulnerable-ms-ordenes-1** |N/A | N/A | 126MiB (126.00 MiB)  |
| **exp-vulnerable-ms-resenas-1** |N/A | N/A | 121.6MiB (121.60 MiB)  |
| **exp-vulnerable-ms-usuarios-1** |N/A | N/A | 140.4MiB (140.40 MiB)  |
| **exp-vulnerable-postgres-db-1** |N/A | N/A | 27.01MiB (27.01 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **--** |0.00% | 0.00% | 0.00% | **0.00%** |
| **exp-protegido-api-gateway-1** |0.00% | 57.85% | 44.40% | **34.08%** |
| **exp-protegido-mongo-db-1** |0.00% | 19.44% | 20.61% | **13.35%** |
| **exp-protegido-ms-catalogo-1** |0.00% | 0.77% | 1.27% | **0.68%** |
| **exp-protegido-ms-ordenes-1** |0.00% | 0.70% | 1.06% | **0.59%** |
| **exp-protegido-ms-resenas-1** |0.00% | 0.95% | 1.17% | **0.71%** |
| **exp-protegido-ms-usuarios-1** |0.00% | 0.99% | 1.11% | **0.70%** |
| **exp-protegido-postgres-db-1** |0.00% | 1.12% | 1.07% | **0.73%** |
| **exp-vulnerable-mongo-db-1** |0.00% | 0.00% | 26.96% | **8.99%** |
| **exp-vulnerable-mongo-init-1** |0.00% | 0.00% | 15.20% | **5.07%** |
| **exp-vulnerable-ms-catalogo-1** |0.00% | 0.00% | 52.83% | **17.61%** |
| **exp-vulnerable-ms-ordenes-1** |0.00% | 0.00% | 41.75% | **13.92%** |
| **exp-vulnerable-ms-resenas-1** |0.00% | 0.00% | 39.57% | **13.19%** |
| **exp-vulnerable-ms-usuarios-1** |0.00% | 0.00% | 37.73% | **12.58%** |
| **exp-vulnerable-postgres-db-1** |0.00% | 0.00% | 5.08% | **1.69%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **--** |0.00 MiB | 0.00 MiB | 0.00 MiB | **0.00 MiB** |
| **exp-protegido-api-gateway-1** |0.00 MiB | 118.86 MiB | 106.51 MiB | **75.12 MiB** |
| **exp-protegido-mongo-db-1** |0.00 MiB | 204.72 MiB | 210.36 MiB | **138.36 MiB** |
| **exp-protegido-ms-catalogo-1** |0.00 MiB | 46.06 MiB | 45.80 MiB | **30.62 MiB** |
| **exp-protegido-ms-ordenes-1** |0.00 MiB | 46.89 MiB | 45.97 MiB | **30.95 MiB** |
| **exp-protegido-ms-resenas-1** |0.00 MiB | 45.83 MiB | 46.88 MiB | **30.90 MiB** |
| **exp-protegido-ms-usuarios-1** |0.00 MiB | 45.78 MiB | 45.64 MiB | **30.47 MiB** |
| **exp-protegido-postgres-db-1** |0.00 MiB | 27.97 MiB | 28.00 MiB | **18.66 MiB** |
| **exp-vulnerable-mongo-db-1** |0.00 MiB | 0.00 MiB | 227.73 MiB | **75.91 MiB** |
| **exp-vulnerable-mongo-init-1** |0.00 MiB | 0.00 MiB | 56.04 MiB | **18.68 MiB** |
| **exp-vulnerable-ms-catalogo-1** |0.00 MiB | 0.00 MiB | 59.85 MiB | **19.95 MiB** |
| **exp-vulnerable-ms-ordenes-1** |0.00 MiB | 0.00 MiB | 65.39 MiB | **21.80 MiB** |
| **exp-vulnerable-ms-resenas-1** |0.00 MiB | 0.00 MiB | 65.83 MiB | **21.94 MiB** |
| **exp-vulnerable-ms-usuarios-1** |0.00 MiB | 0.00 MiB | 77.12 MiB | **25.71 MiB** |
| **exp-vulnerable-postgres-db-1** |0.00 MiB | 0.00 MiB | 22.72 MiB | **7.57 MiB** |