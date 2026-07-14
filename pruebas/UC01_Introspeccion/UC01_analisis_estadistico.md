# UC-01 - Analisis estadistico inferencial
Fecha: 2026-07-07 20:38  
Alfa (nivel de significancia) = **0.05**, confianza = **95%**  
N replicas por escenario: **variable segun disponibilidad** (n=5 en niveles criticos re-corridos, n=3 en exploratorios; se filtran replicas invalidas con k6 colgado)

## 1. Prueba de Shapiro-Wilk (normalidad)
H0: la muestra proviene de una poblacion normal. Se rechaza si p < alfa.

| VUs | Entorno | Metrica | p (Shapiro) | Normal? |
| :---: | :--- | :--- | :---: | :---: |
| 1 | Vulnerable | Latencia (ms) | 0.3450 | Si |
| 1 | Vulnerable | Throughput (peticiones/60s) | 1.0000 | Si |
| 1 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 1 | Protegido | Latencia (ms) | 0.1812 | Si |
| 1 | Protegido | Throughput (peticiones/60s) | 1.0000 | Si |
| 1 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 2 | Vulnerable | Latencia (ms) | 0.9433 | Si |
| 2 | Vulnerable | Throughput (peticiones/60s) | 1.0000 | Si |
| 2 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 2 | Protegido | Latencia (ms) | 0.6604 | Si |
| 2 | Protegido | Throughput (peticiones/60s) | 1.0000 | Si |
| 2 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 3 | Vulnerable | Latencia (ms) | 0.6910 | Si |
| 3 | Vulnerable | Throughput (peticiones/60s) | 1.0000 | Si |
| 3 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 3 | Protegido | Latencia (ms) | 0.0181 | No |
| 3 | Protegido | Throughput (peticiones/60s) | 1.0000 | Si |
| 3 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 5 | Vulnerable | Latencia (ms) | 0.3323 | Si |
| 5 | Vulnerable | Throughput (peticiones/60s) | 1.0000 | Si |
| 5 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 5 | Protegido | Latencia (ms) | 0.2639 | Si |
| 5 | Protegido | Throughput (peticiones/60s) | 1.0000 | Si |
| 5 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 8 | Vulnerable | Latencia (ms) | 0.0010 | No |
| 8 | Vulnerable | Throughput (peticiones/60s) | 0.0001 | No |
| 8 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 8 | Protegido | Latencia (ms) | 0.2395 | Si |
| 8 | Protegido | Throughput (peticiones/60s) | 1.0000 | Si |
| 8 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 13 | Vulnerable | Latencia (ms) | 0.5994 | Si |
| 13 | Vulnerable | Throughput (peticiones/60s) | 1.0000 | Si |
| 13 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 13 | Protegido | Latencia (ms) | 0.1925 | Si |
| 13 | Protegido | Throughput (peticiones/60s) | 0.0001 | No |
| 13 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 21 | Vulnerable | Latencia (ms) | 0.4421 | Si |
| 21 | Vulnerable | Throughput (peticiones/60s) | 1.0000 | Si |
| 21 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 21 | Protegido | Latencia (ms) | 0.0002 | No |
| 21 | Protegido | Throughput (peticiones/60s) | 0.0001 | No |
| 21 | Protegido | Tasa de Fallos (%) | 0.0001 | No |
| 34 | Vulnerable | Latencia (ms) | 0.9044 | Si |
| 34 | Vulnerable | Throughput (peticiones/60s) | 0.0012 | No |
| 34 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 34 | Protegido | Latencia (ms) | 0.1979 | Si |
| 34 | Protegido | Throughput (peticiones/60s) | 1.0000 | Si |
| 34 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 55 | Vulnerable | Latencia (ms) | 0.0002 | No |
| 55 | Vulnerable | Throughput (peticiones/60s) | 0.0001 | No |
| 55 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 55 | Protegido | Latencia (ms) | 0.0213 | No |
| 55 | Protegido | Throughput (peticiones/60s) | 0.0001 | No |
| 55 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 89 | Vulnerable | Latencia (ms) | 0.0587 | Si |
| 89 | Vulnerable | Throughput (peticiones/60s) | 0.0001 | No |
| 89 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 89 | Protegido | Latencia (ms) | 0.1643 | Si |
| 89 | Protegido | Throughput (peticiones/60s) | 1.0000 | Si |
| 89 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 144 | Vulnerable | Latencia (ms) | 0.5388 | Si |
| 144 | Vulnerable | Throughput (peticiones/60s) | 0.0001 | No |
| 144 | Vulnerable | Tasa de Fallos (%) | 1.0000 | Si |
| 144 | Protegido | Latencia (ms) | 0.5017 | Si |
| 144 | Protegido | Throughput (peticiones/60s) | 0.3521 | Si |
| 144 | Protegido | Tasa de Fallos (%) | 1.0000 | Si |
| 233 | Vulnerable | Latencia (ms) | 0.1941 | Si |
| 233 | Vulnerable | Throughput (peticiones/60s) | 0.2466 | Si |
| 233 | Vulnerable | Tasa de Fallos (%) | 0.0846 | Si |
| 233 | Protegido | Latencia (ms) | 0.1724 | Si |
| 233 | Protegido | Throughput (peticiones/60s) | 0.3705 | Si |
| 233 | Protegido | Tasa de Fallos (%) | 0.9511 | Si |
| 377 | Vulnerable | Latencia (ms) | 0.6605 | Si |
| 377 | Vulnerable | Throughput (peticiones/60s) | 0.2674 | Si |
| 377 | Vulnerable | Tasa de Fallos (%) | 0.3027 | Si |
| 377 | Protegido | Latencia (ms) | 0.5981 | Si |
| 377 | Protegido | Throughput (peticiones/60s) | 0.6822 | Si |
| 377 | Protegido | Tasa de Fallos (%) | 0.0015 | No |

**Conclusion normalidad:** Existe evidencia de no normalidad -> se justifica el uso de Mann-Whitney U (no parametrica), acorde a la seccion 2.4.3 de la tesis.

## 2. Mann-Whitney U: Vulnerable vs Protegido
H0: no existe diferencia significativa entre los rangos de ambos grupos.
H1: existe diferencia significativa (bilateral). Se rechaza H0 si p < alfa.

| VUs | Metrica | U | p-valor | Conclusion |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Latencia (ms) | 2.00 | 0.0317 | Rechaza H0 (diferencia SIGNIFICATIVA) |
| 1 | Throughput (peticiones/60s) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 1 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 2 | Latencia (ms) | 3.00 | 0.0556 | No rechaza H0 (sin diferencia significativa) |
| 2 | Throughput (peticiones/60s) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 2 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 3 | Latencia (ms) | 9.00 | 0.5476 | No rechaza H0 (sin diferencia significativa) |
| 3 | Throughput (peticiones/60s) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 3 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 5 | Latencia (ms) | 1.00 | 0.0159 | Rechaza H0 (diferencia SIGNIFICATIVA) |
| 5 | Throughput (peticiones/60s) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 5 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 8 | Latencia (ms) | 5.00 | 0.1508 | No rechaza H0 (sin diferencia significativa) |
| 8 | Throughput (peticiones/60s) | 10.00 | 0.4237 | No rechaza H0 (sin diferencia significativa) |
| 8 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 13 | Latencia (ms) | 8.00 | 0.7302 | No rechaza H0 (sin diferencia significativa) |
| 13 | Throughput (peticiones/60s) | 12.00 | 0.5023 | No rechaza H0 (sin diferencia significativa) |
| 13 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 21 | Latencia (ms) | 1.00 | 0.0159 | Rechaza H0 (diferencia SIGNIFICATIVA) |
| 21 | Throughput (peticiones/60s) | 15.00 | 0.4237 | No rechaza H0 (sin diferencia significativa) |
| 21 | Tasa de Fallos (%) | 10.00 | 0.4237 | No rechaza H0 (sin diferencia significativa) |
| 34 | Latencia (ms) | 0.00 | 0.0159 | Rechaza H0 (diferencia SIGNIFICATIVA) |
| 34 | Throughput (peticiones/60s) | 7.50 | 0.3711 | No rechaza H0 (sin diferencia significativa) |
| 34 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 55 | Latencia (ms) | 8.00 | 0.4206 | No rechaza H0 (sin diferencia significativa) |
| 55 | Throughput (peticiones/60s) | 12.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 55 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 89 | Latencia (ms) | 7.00 | 0.3095 | No rechaza H0 (sin diferencia significativa) |
| 89 | Throughput (peticiones/60s) | 10.00 | 0.4237 | No rechaza H0 (sin diferencia significativa) |
| 89 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 144 | Latencia (ms) | 2.00 | 0.0317 | Rechaza H0 (diferencia SIGNIFICATIVA) |
| 144 | Throughput (peticiones/60s) | 19.00 | 0.1579 | No rechaza H0 (sin diferencia significativa) |
| 144 | Tasa de Fallos (%) | 0.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 233 | Latencia (ms) | 0.00 | 0.0159 | Rechaza H0 (diferencia SIGNIFICATIVA) |
| 233 | Throughput (peticiones/60s) | 20.00 | 0.0159 | Rechaza H0 (diferencia SIGNIFICATIVA) |
| 233 | Tasa de Fallos (%) | 10.00 | 1.0000 | No rechaza H0 (sin diferencia significativa) |
| 377 | Latencia (ms) | 0.00 | 0.0079 | Rechaza H0 (diferencia SIGNIFICATIVA) |
| 377 | Throughput (peticiones/60s) | 25.00 | 0.0079 | Rechaza H0 (diferencia SIGNIFICATIVA) |
| 377 | Tasa de Fallos (%) | 20.50 | 0.1105 | No rechaza H0 (sin diferencia significativa) |

## 3. Interpretacion frente a las hipotesis de la tesis
- **H_A2** (controles reducen latencia/fallos/consumo): se sustenta cuando p<alfa a favor del Protegido en las metricas de recursos/red bajo estres.
- Si el Vulnerable **no colapsa** en el rango probado, la ausencia de diferencia significativa en latencia y fallos es esperada y no contradice H_A2 -> se requiere ampliar la carga.