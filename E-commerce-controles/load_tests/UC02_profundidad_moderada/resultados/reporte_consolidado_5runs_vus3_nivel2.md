# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=3)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidación:** 2026-07-10 14:48:23

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 7 | 26844.825 ms | 14.28% | 0.00% |
| Run 2 | 11 | 23399.929 ms | 18.18% | 0.00% |
| Run 3 | 11 | 22186.996 ms | 18.18% | 0.00% |
| Run 4 | 8 | 23627.291 ms | 25.00% | 0.00% |
| Run 5 | 11 | 20497.269 ms | 18.18% | 0.00% |
| **PROMEDIO** | **9.6** | **23311.262 ms** | **18.76%** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |175.35% | 152.19% | 169.22% | 163.18% | 166.67% | **165.32%** |
| **exp-protegido-mongo-db-1** |92.29% | 101.57% | 105.79% | 111.65% | 111.01% | **104.46%** |
| **exp-protegido-ms-catalogo-1** |5.94% | 4.24% | 6.27% | 7.94% | 5.84% | **6.05%** |
| **exp-protegido-ms-ordenes-1** |5.86% | 4.02% | 5.11% | 6.35% | 6.41% | **5.55%** |
| **exp-protegido-ms-resenas-1** |231.91% | 237.65% | 287.91% | 129.17% | 248.82% | **227.09%** |
| **exp-protegido-ms-usuarios-1** |213.66% | 277.93% | 241.84% | 227.78% | 240.72% | **240.39%** |
| **exp-protegido-postgres-db-1** |21.18% | 32.86% | 14.65% | 24.80% | 24.37% | **23.57%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
| :--- |:---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |1005MiB (1005.00 MiB)  | 1006MiB (1006.00 MiB)  | 1024MiB (1024.00 MiB)  | 1024MiB (1024.00 MiB)  | 1023MiB (1023.00 MiB)  |
| **exp-protegido-mongo-db-1** |339.2MiB (339.20 MiB)  | 349.8MiB (349.80 MiB)  | 356MiB (356.00 MiB)  | 349.3MiB (349.30 MiB)  | 350MiB (350.00 MiB)  |
| **exp-protegido-ms-catalogo-1** |45.89MiB (45.89 MiB)  | 46.71MiB (46.71 MiB)  | 47.33MiB (47.33 MiB)  | 46.55MiB (46.55 MiB)  | 46.5MiB (46.50 MiB)  |
| **exp-protegido-ms-ordenes-1** |46.1MiB (46.10 MiB)  | 46.32MiB (46.32 MiB)  | 54.55MiB (54.55 MiB)  | 47.21MiB (47.21 MiB)  | 46.47MiB (46.47 MiB)  |
| **exp-protegido-ms-resenas-1** |812.8MiB (812.80 MiB)  | 868.9MiB (868.90 MiB)  | 874.1MiB (874.10 MiB)  | 815MiB (815.00 MiB)  | 846.5MiB (846.50 MiB)  |
| **exp-protegido-ms-usuarios-1** |511.9MiB (511.90 MiB)  | 511.9MiB (511.90 MiB)  | 512MiB (512.00 MiB)  | 511.9MiB (511.90 MiB)  | 512MiB (512.00 MiB)  |
| **exp-protegido-postgres-db-1** |70.35MiB (70.35 MiB)  | 67.45MiB (67.45 MiB)  | 70.48MiB (70.48 MiB)  | 70.3MiB (70.30 MiB)  | 70.34MiB (70.34 MiB)  |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |57.90% | 47.93% | 46.35% | 60.60% | 49.53% | **52.46%** |
| **exp-protegido-mongo-db-1** |25.02% | 26.94% | 32.21% | 32.24% | 27.25% | **28.73%** |
| **exp-protegido-ms-catalogo-1** |1.59% | 1.09% | 1.06% | 1.56% | 1.18% | **1.30%** |
| **exp-protegido-ms-ordenes-1** |1.44% | 0.80% | 1.20% | 1.39% | 1.16% | **1.20%** |
| **exp-protegido-ms-resenas-1** |25.48% | 27.10% | 26.17% | 18.52% | 29.15% | **25.28%** |
| **exp-protegido-ms-usuarios-1** |33.32% | 30.46% | 35.24% | 34.27% | 34.00% | **33.46%** |
| **exp-protegido-postgres-db-1** |3.05% | 3.71% | 1.59% | 2.50% | 2.84% | **2.74%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |502.44 MiB | 505.93 MiB | 495.80 MiB | 511.53 MiB | 456.49 MiB | **494.44 MiB** |
| **exp-protegido-mongo-db-1** |213.43 MiB | 218.03 MiB | 219.68 MiB | 219.43 MiB | 219.62 MiB | **218.04 MiB** |
| **exp-protegido-ms-catalogo-1** |45.74 MiB | 46.56 MiB | 47.19 MiB | 45.04 MiB | 46.36 MiB | **46.18 MiB** |
| **exp-protegido-ms-ordenes-1** |45.90 MiB | 45.91 MiB | 49.60 MiB | 46.72 MiB | 46.34 MiB | **46.89 MiB** |
| **exp-protegido-ms-resenas-1** |591.02 MiB | 666.79 MiB | 667.27 MiB | 610.87 MiB | 624.61 MiB | **632.11 MiB** |
| **exp-protegido-ms-usuarios-1** |277.48 MiB | 324.47 MiB | 320.01 MiB | 268.31 MiB | 323.66 MiB | **302.79 MiB** |
| **exp-protegido-postgres-db-1** |65.55 MiB | 64.81 MiB | 65.42 MiB | 65.23 MiB | 65.55 MiB | **65.31 MiB** |