# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=8)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 18:38:34

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 480 | 6.479 ms | 0.00% |
| Run 2 | 480 | 5.803 ms | 0.00% |
| Run 3 | 480 | 6.303 ms | 0.00% |
| **PROMEDIO** | **480.0** | **6.195 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |21.15% | 6.36% | 4.93% | **10.81%** |
| **exp-protegido-mongo-db-1** |52.52% | 46.73% | 50.44% | **49.90%** |
| **exp-protegido-ms-catalogo-1** |3.29% | 3.58% | 3.35% | **3.41%** |
| **exp-protegido-ms-ordenes-1** |3.03% | 3.70% | 2.82% | **3.18%** |
| **exp-protegido-ms-resenas-1** |2.58% | 3.41% | 3.54% | **3.18%** |
| **exp-protegido-ms-usuarios-1** |2.56% | 3.15% | 3.44% | **3.05%** |
| **exp-protegido-postgres-db-1** |4.08% | 5.09% | 4.67% | **4.61%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |98.46MiB (98.46 MiB)  | 75.39MiB (75.39 MiB)  | 76.3MiB (76.30 MiB)  |
| **exp-protegido-mongo-db-1** |340.7MiB (340.70 MiB)  | 344.6MiB (344.60 MiB)  | 342.4MiB (342.40 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.4MiB (46.40 MiB)  | 47.23MiB (47.23 MiB)  | 45.53MiB (45.53 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.98MiB (45.98 MiB)  | 46.89MiB (46.89 MiB)  | 46.26MiB (46.26 MiB)  |
| **exp-protegido-ms-resenas-1** |46.73MiB (46.73 MiB)  | 47.53MiB (47.53 MiB)  | 46.64MiB (46.64 MiB)  |
| **exp-protegido-ms-usuarios-1** |46.14MiB (46.14 MiB)  | 45.8MiB (45.80 MiB)  | 44.93MiB (44.93 MiB)  |
| **exp-protegido-postgres-db-1** |28MiB (28.00 MiB)  | 27.98MiB (27.98 MiB)  | 30.15MiB (30.15 MiB)  |