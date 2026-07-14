# INFORME CONSOLIDADO DE 5 EJECUCIONES (VUS=5)
**Prueba:** uc02_profundidad_nivel
**Fecha de Consolidacion:** 2026-07-10 00:15:00

## 1. RESUMEN DE METRICAS K6
| Ejecucion | Peticiones Totales | Latencia Media (ms) | Tasa de Fallos | Tasa de Bloqueo |
| :---: | :---: | :---: | :---: | :---: |
| Run 1 | 300 | 6.940 ms | 0.00% | 100.00% |
| Run 2 | 300 | 6.730 ms | 0.00% | 100.00% |
| Run 3 | 300 | 12.260 ms | 0.00% | 100.00% |
| Run 4 | 295 | 16.710 ms | 0.00% | 100.00% |
| Run 5 | 300 | 8.520 ms | 0.00% | 100.00% |
| **PROMEDIO** | **299.0** | **10.232 ms** | **0.00%** | **100.00%** |

## 2. PICOS DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |5.36% | 6.58% | 13.27% | 19.01% | 6.66% | **10.18%** |
| **exp-protegido-mongo-db-1** |86.66% | 72.75% | 138.99% | 98.30% | 80.03% | **95.35%** |
| **exp-protegido-ms-catalogo-1** |3.56% | 4.88% | 8.28% | 4.89% | 4.99% | **5.32%** |
| **exp-protegido-ms-ordenes-1** |3.95% | 4.15% | 9.14% | 4.51% | 4.33% | **5.22%** |
| **exp-protegido-ms-resenas-1** |3.88% | 4.69% | 18.29% | 4.88% | 3.63% | **7.07%** |
| **exp-protegido-ms-usuarios-1** |3.98% | 4.28% | 16.97% | 7.23% | 4.94% | **7.48%** |
| **exp-protegido-postgres-db-1** |5.58% | 5.59% | 9.25% | 5.99% | 6.41% | **6.56%** |

## 3. PICOS DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |82.00 MiB | 75.94 MiB | 75.04 MiB | 97.14 MiB | 71.45 MiB | **80.31 MiB** |
| **exp-protegido-mongo-db-1** |333.20 MiB | 330.20 MiB | 349.10 MiB | 340.90 MiB | 350.10 MiB | **340.70 MiB** |
| **exp-protegido-ms-catalogo-1** |90.75 MiB | 46.49 MiB | 45.97 MiB | 46.41 MiB | 47.73 MiB | **55.47 MiB** |
| **exp-protegido-ms-ordenes-1** |93.14 MiB | 46.97 MiB | 45.07 MiB | 55.02 MiB | 47.05 MiB | **57.45 MiB** |
| **exp-protegido-ms-resenas-1** |92.96 MiB | 46.95 MiB | 45.72 MiB | 46.39 MiB | 47.99 MiB | **56.00 MiB** |
| **exp-protegido-ms-usuarios-1** |92.79 MiB | 47.43 MiB | 45.75 MiB | 45.78 MiB | 48.39 MiB | **56.03 MiB** |
| **exp-protegido-postgres-db-1** |27.57 MiB | 30.04 MiB | 27.79 MiB | 28.88 MiB | 27.68 MiB | **28.39 MiB** |

## 4. PROMEDIO DE CPU (%) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |2.36% | 1.90% | 3.60% | 3.99% | 2.52% | **2.87%** |
| **exp-protegido-mongo-db-1** |86.66% | 72.75% | 138.99% | 98.30% | 80.03% | **95.35%** |
| **exp-protegido-ms-catalogo-1** |3.56% | 4.88% | 8.28% | 4.89% | 4.99% | **5.32%** |
| **exp-protegido-ms-ordenes-1** |3.95% | 4.15% | 9.14% | 4.51% | 4.33% | **5.22%** |
| **exp-protegido-ms-resenas-1** |3.88% | 4.69% | 18.29% | 4.88% | 3.63% | **7.07%** |
| **exp-protegido-ms-usuarios-1** |3.98% | 4.28% | 16.97% | 7.23% | 4.94% | **7.48%** |
| **exp-protegido-postgres-db-1** |5.58% | 5.59% | 9.25% | 5.99% | 6.41% | **6.56%** |

## 5. PROMEDIO DE MEMORIA (MiB) EN CONTENEDORES
| Contenedor |Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Promedio Pico |
| :--- |:---: | :---: | :---: | :---: | :---: | :---: |
| **exp-protegido-api-gateway-1** |77.86 MiB | 70.41 MiB | 69.89 MiB | 73.57 MiB | 69.14 MiB | **72.17 MiB** |
| **exp-protegido-mongo-db-1** |333.20 MiB | 330.20 MiB | 349.10 MiB | 340.90 MiB | 350.10 MiB | **340.70 MiB** |
| **exp-protegido-ms-catalogo-1** |90.75 MiB | 46.49 MiB | 45.97 MiB | 46.41 MiB | 47.73 MiB | **55.47 MiB** |
| **exp-protegido-ms-ordenes-1** |93.14 MiB | 46.97 MiB | 45.07 MiB | 55.02 MiB | 47.05 MiB | **57.45 MiB** |
| **exp-protegido-ms-resenas-1** |92.96 MiB | 46.95 MiB | 45.72 MiB | 46.39 MiB | 47.99 MiB | **56.00 MiB** |
| **exp-protegido-ms-usuarios-1** |92.79 MiB | 47.43 MiB | 45.75 MiB | 45.78 MiB | 48.39 MiB | **56.03 MiB** |
| **exp-protegido-postgres-db-1** |27.57 MiB | 30.04 MiB | 27.79 MiB | 28.88 MiB | 27.68 MiB | **28.39 MiB** |
