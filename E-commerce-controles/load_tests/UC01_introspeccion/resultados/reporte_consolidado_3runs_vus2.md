# INFORME CONSOLIDADO DE 3 EJECUCIONES (VUS=2)
**Prueba:** uc01_stress_introspeccion
**Fecha de Consolidación:** 2026-07-06 18:03:31

## 1. RESUMEN DE MÉTRICAS K6
| Ejecución | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos |
| :---: | :---: | :---: | :---: |
| Run 1 | 120 | 7.078 ms | 0.00% |
| Run 2 | 120 | 5.975 ms | 0.00% |
| Run 3 | 120 | 6.492 ms | 0.00% |
| **PROMEDIO** | **120.0** | **6.515 ms** | **0.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |3.33% | 2.21% | 2.72% | **2.75%** |
| **exp-protegido-mongo-db-1** |56.52% | 65.01% | 60.06% | **60.53%** |
| **exp-protegido-ms-catalogo-1** |3.47% | 3.63% | 3.87% | **3.66%** |
| **exp-protegido-ms-ordenes-1** |4.01% | 4.52% | 3.15% | **3.89%** |
| **exp-protegido-ms-resenas-1** |4.01% | 4.96% | 2.91% | **3.96%** |
| **exp-protegido-ms-usuarios-1** |4.42% | 4.38% | 3.73% | **4.18%** |
| **exp-protegido-postgres-db-1** |3.95% | 5.12% | 4.04% | **4.37%** |

## 3. PICOS DE MEMORIA EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 |
| :--- |:---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |66.71MiB (66.71 MiB)  | 65MiB (65.00 MiB)  | 65.05MiB (65.05 MiB)  |
| **exp-protegido-mongo-db-1** |331.4MiB (331.40 MiB)  | 340.1MiB (340.10 MiB)  | 333.3MiB (333.30 MiB)  |
| **exp-protegido-ms-catalogo-1** |46.11MiB (46.11 MiB)  | 46.44MiB (46.44 MiB)  | 46.18MiB (46.18 MiB)  |
| **exp-protegido-ms-ordenes-1** |45.86MiB (45.86 MiB)  | 45.78MiB (45.78 MiB)  | 45.87MiB (45.87 MiB)  |
| **exp-protegido-ms-resenas-1** |46.94MiB (46.94 MiB)  | 46.65MiB (46.65 MiB)  | 46.1MiB (46.10 MiB)  |
| **exp-protegido-ms-usuarios-1** |45.93MiB (45.93 MiB)  | 46.97MiB (46.97 MiB)  | 45.91MiB (45.91 MiB)  |
| **exp-protegido-postgres-db-1** |28.14MiB (28.14 MiB)  | 27.97MiB (27.97 MiB)  | 28.22MiB (28.22 MiB)  |