# Experimento Computacional — Seguridad en GraphQL sobre Microservicios

Laboratorio reproducible que **demuestra empíricamente** las debilidades de
seguridad de GraphQL en una arquitectura de microservicios *sin controles*
(**Entorno Vulnerable**) y las compara contra un ecosistema *robustecido*
(**Entorno Protegido**: bloqueo de introspección, límite de profundidad,
análisis de complejidad, timeouts).

Ambos entornos se someten a **pruebas de estrés idénticas** y se mide el
**punto de quiebre** del servidor mediante:

- **Tasa de errores** (HTTP 500 / timeouts)
- **Latencia** (tiempo de respuesta)
- **Consumo de CPU y RAM** por contenedor

> ⚠️ **Esta carpeta es autocontenida y está aislada del proyecto original.**
> Es una copia limpia de `../E-commerce` y `../E-commerce-controles` con la
> orquestación corregida (rutas relativas) y con **Docker aislado** para no
> tocar los contenedores, redes ni volúmenes del proyecto original.
> Ver la sección [Aislamiento](#aislamiento-respecto-al-proyecto-original).

---

## 1. Arquitectura

Plataforma de E-commerce con **Apollo Federation v2**.

| Componente | Rol | Puerto interno |
| :--- | :--- | :---: |
| `api-gateway` | Único punto de entrada. Federa y ensambla la respuesta. | 4000 (publicado en `localhost:4000`) |
| `ms-usuarios` | Subgrafo de clientes (PostgreSQL) | 4001 |
| `ms-catalogo` | Subgrafo de productos (MongoDB, replica set `rs0`) | 4002 |
| `ms-resenas` | Subgrafo de valoraciones (PostgreSQL) | 4003 |
| `ms-ordenes` | Subgrafo de historial de compras (PostgreSQL) | 4004 |
| `postgres-db` | Base relacional (usuarios, órdenes, reseñas) | 5432 |
| `mongo-db` | Base NoSQL con replica set (transacciones Prisma) | 27017 |

Todo corre bajo **Docker Compose**, encapsulando red y volúmenes.

### Diferencia de entornos

| | `E-commerce/` (Vulnerable) | `E-commerce-controles/` (Protegido) |
| :--- | :--- | :--- |
| Introspección | `introspection: true` | `introspection: false` (bloqueada) |
| Profundidad | sin límite | `graphql-depth-limit(5)` |
| Complejidad | sin análisis | plugin de costo/complejidad (máx. 1000) |
| Landing page | habilitada | `ApolloServerPluginLandingPageDisabled` |
| Respuesta a query maliciosa | la procesa (impacto real) | la rechaza (`400`/`403`) antes de llegar a los microservicios |

---

## 2. Casos de Uso (vulnerabilidades atacadas)

| UC | Ataque | Script K6 (dentro de `load_tests/`) | Impacto esperado en Vulnerable |
| :--- | :--- | :--- | :--- |
| **UC-01** | Introspección | `UC01_introspeccion/uc01_stress_introspeccion.js` | Alta latencia y picos de memoria en el Gateway |
| **UC-02** | Profundidad moderada (N+1) | `UC02_profundidad_moderada/uc02_profundidad_nivel.js` | Explosión de peticiones a BD |
| **UC-03** | Recursividad circular | `UC03_recursividad_circular/uc03_recursividad_nivel.js` | Exhaustión de memoria (OOM) |
| **UC-04** | Abuso de alias | `UC04_abuso_alias/uc04_alias_nivel.js` | Bypass de rate-limit, sobrecarga de CPU |
| **UC-05** | Bomba de fragmentos / paginación masiva | `UC05_bomba_fragmentos/uc05_fragmentos_nivel.js` | Cuellos de botella en BD |

---

## 3. Requisitos previos

- **Docker Desktop** (con Docker Compose v2). Verificado con Compose `v5.1.0`.
- **[k6](https://k6.io/docs/get-started/installation/)** en el `PATH` (inyector de carga).
- **Python 3.10+** con las dependencias:
  ```powershell
  pip install -r requirements.txt
  ```
- Docker debe estar **corriendo** antes de lanzar cualquier prueba.

---

## 4. Cómo ejecutar

Desde esta carpeta (`ExperimentoComputacional/`):

### Paso 1 — (Recomendado) Sembrar datos de prueba
Los ataques de profundidad (UC-02+) necesitan datos reales; si no, GraphQL
devuelve arreglos vacíos y da falsos positivos de rendimiento. El seeder inyecta
**10.000 usuarios, 50.000 productos, 100.000 reseñas y 15.000 órdenes**.
```powershell
python prepare_mock_data.py
```

### Paso 2 — Ejecutar las pruebas

**Opción A — Panel de control gráfico (recomendado, cubre los 5 UC):**
```powershell
python panel_control.py
```

**Opción B — Runners headless por consola:**
```powershell
python uc01_runner.py     # UC-01 con escalado Fibonacci hasta el punto de quiebre
python uc02_runner.py     # UC-02 por niveles de profundidad (1-7)
python night_runner.py    # Ejecuta los 5 UC de corrido y genera reportes al final
```

### Paso 3 — Gráficos comparativos
```powershell
python generar_todos_graficos.py
```

Los reportes Excel/CSV se generan automáticamente durante los runners
(módulo `generate_reports.py`).

---

## 5. Metodología

- **Escalado por serie de Fibonacci** (`1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377` VUs)
  para trazar la curva de degradación y hallar el punto de quiebre exacto.
- **3 réplicas por nivel** (promedio matemático real), 60 s de carga por réplica.
- **Aislamiento y autosanación**: cada nivel destruye los contenedores y arranca
  desde cero (sin caché que contamine la prueba); si Docker en Windows falla por
  red ocupada, purga y reintenta hasta 3 veces.
- **Punto de quiebre**: se declara cuando la tasa de fallos del Vulnerable
  supera el 50 %.

---

## 6. Estructura

```
ExperimentoComputacional/
├── E-commerce/               # Entorno VULNERABLE (Docker: proyecto "exp-vulnerable")
│   ├── docker-compose.yml
│   ├── .env                  # COMPOSE_PROJECT_NAME=exp-vulnerable (aislamiento)
│   ├── api-gateway/ ms-*/ seeder/
│   └── load_tests/           # scripts K6, monitor y orquestador por-entorno
├── E-commerce-controles/     # Entorno PROTEGIDO (Docker: proyecto "exp-protegido")
│   └── .env                  # COMPOSE_PROJECT_NAME=exp-protegido
├── panel_control.py          # Orquestador gráfico (los 5 UC)
├── uc01_runner.py            # Runner CLI UC-01 (Fibonacci / punto de quiebre)
├── uc02_runner.py            # Runner CLI UC-02 (por niveles)
├── night_runner.py           # Batch de los 5 UC
├── prepare_mock_data.py      # Siembra de datos (10k/50k/100k/15k)
├── generate_reports.py       # Módulo de reportes Excel
├── generar_todos_graficos.py # Gráficos comparativos maestros
├── requirements.txt
├── pruebas/                  # salida: Excel + gráficos por UC
└── graficos/                 # salida: gráficos maestros / resumen ejecutivo
```

Cada prueba deja sus `.md` consolidados en
`E-commerce*/load_tests/UCxx.../resultados/`.

---

## Aislamiento respecto al proyecto original

Docker Compose deriva el nombre de proyecto del nombre de carpeta, así que una
copia en `.../E-commerce` reutilizaría por defecto el proyecto `e-commerce`, la
red `ecommerce-net` y los contenedores `e-commerce-*` del proyecto **original**.

Para evitar cualquier colisión, cada entorno de esta carpeta fija su propio
proyecto Docker mediante `COMPOSE_PROJECT_NAME` en su `.env`:

- `E-commerce/.env` → `exp-vulnerable`  → contenedores `exp-vulnerable-*`, red `exp-vulnerable_ecommerce-net`
- `E-commerce-controles/.env` → `exp-protegido` → contenedores `exp-protegido-*`, red `exp-protegido_ecommerce-net`

Así, esta copia tiene **contenedores, redes y volúmenes propios**, separados del
proyecto original.

> **Único recurso compartido:** el puerto host `4000`. Solo un gateway puede
> escuchar en `localhost:4000` a la vez, por lo que **no ejecutes esta copia y el
> proyecto original simultáneamente**. Los runners levantan un entorno a la vez,
> así que dentro de esta carpeta no hay conflicto.

---

## Nota ética

Este laboratorio está diseñado **exclusivamente** para investigación de seguridad
defensiva en un entorno local controlado. Los ataques solo deben ejecutarse
contra los servicios incluidos en esta carpeta.
