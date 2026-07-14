# Limitación técnica en la instrumentación de UC-02 (Profundidad Moderada)

## Descripción del hallazgo

Durante la ejecución del caso de uso UC-02 (Ataque por Profundidad Moderada), se identificó
un problema de instrumentación en el entorno experimental que afecta la interpretación de
las métricas para los niveles de profundidad 3 a 7. El problema se manifiesta en el
componente de resolución federada de Apollo Gateway v2 sobre los microservicios
`ms-usuarios` y `ms-resenas`, ambos con `@apollo/subgraph` 2.7.2 sobre `startStandaloneServer`
de `@apollo/server` 4.10.2.

## Causa raíz

El schema federado declara la relación `Resena.autor: Usuario` y `Usuario.resenas: [Resena]`,
lo que requiere que el gateway invoque el resolver `_entities` del subgrafo remoto por cada
referencia de tipo federado. En la implementación original, cada `__resolveReference` y cada
resolver de lista (por ejemplo, `Usuario.resenas`) ejecutaba una consulta Prisma independiente
por identificador, generando el patrón *N+1* clásico.

Bajo carga con VUs ≥ 1 y niveles de profundidad ≥ 2, la acumulación de peticiones a Postgres
excedía la capacidad de la conexión pooled de Prisma antes de que la ventana de 60 segundos
de k6 finalizara. El gateway, al no recibir respuesta del subgrafo dentro del timeout interno
del `HttpDataSource` de `@apollo/gateway`, respondía con status HTTP 200 conteniendo un
arreglo `errors` en el cuerpo. El script k6 en su instrumentación previa contabilizaba estas
respuestas como peticiones exitosas de baja latencia (5–10 ms) porque la métrica
`iso_tasa_bloqueadas` solo verificaba `status === 400 || status === 403`, no el contenido del
cuerpo.

Adicionalmente, cuando la presión sobre `ms-usuarios` excedía el `mem_limit` de 256 MiB
originalmente configurado, el proceso Node.js era terminado por el kernel de WSL 2 sin que
Docker marcara `OOMKilled=true` (comportamiento conocido en Docker Desktop for Windows con
back-end WSL 2). El proceso reiniciaba automáticamente por `restart: on-failure`, pero
durante la ventana de terminación las conexiones TCP entrantes se cerraban con `socket hang
up`, respuesta que el gateway propagaba también como 200 con `errors` en cuerpo.

## Impacto sobre los datos

Los reportes consolidados generados con anterioridad a la corrección presentan las siguientes
distorsiones sistemáticas para las combinaciones de VUs × Nivel donde la federación cruzaba
microservicios (todos los niveles ≥ 2 en el entorno Vulnerable, y niveles 2–5 en el entorno
Protegido):

- **Latencia media subestimada**: las peticiones que en realidad fueron abortadas por el
  gateway se registraron con la latencia del rebote (~1000–2500 ms) en lugar de la latencia
  real de resolución completa (que en las mediciones corregidas alcanza 5–42 segundos según
  la carga).
- **Throughput sobrestimado**: el número de peticiones por ventana refleja los rebotes
  rápidos y no las resoluciones completas.
- **Tasa de fallos infraestimada**: como las respuestas `errors` conservan HTTP 200, no
  fueron contabilizadas como fallos (`res.status >= 500`) por el script k6.
- **Tasa de bloqueo infraestimada**: la métrica `iso_tasa_bloqueadas` solo detectaba 4xx
  explícitos y no distinguía entre bloqueo por control de seguridad y colapso silencioso del
  microservicio.

## Corrección aplicada

Se introdujeron dos ajustes al entorno experimental:

1. **Batching mediante DataLoader**: se incorporó la librería `dataloader` (v2.2.2) en los
   microservicios `ms-usuarios` y `ms-resenas` para colapsar las N peticiones individuales
   de `_entities` en una única consulta batch por request GraphQL, siguiendo el patrón
   recomendado por la documentación oficial de Apollo Federation. Esto elimina el patrón
   *N+1* sin alterar la semántica del schema federado ni la superficie de ataque expuesta.
2. **Aumento de `mem_limit`**: se elevó el límite de memoria de `ms-resenas` de 256 MiB a
   1024 MiB y de `ms-usuarios` de 256 MiB a 512 MiB, con `api-gateway` a 1024 MiB, evitando
   la terminación silenciosa por el subsistema de memoria de WSL 2.
3. **Extensión del `timeout` de k6**: se incrementó el timeout por petición de 15 s a 55 s
   para acomodar las latencias reales de resolución federada sin abortar mediciones válidas.

## Alcance de la corrección

Debido a restricciones de tiempo del cronograma de la investigación, la matriz de UC-02 se
regeneró parcialmente:

- Las 5 combinaciones de VUs × Nivel donde la anomalía era más evidente (`vus{1,2,3,8}_nivel2`
  en Vulnerable, `vus{1,2,3,5,8}_nivel2` y `vus8_nivel5` en ambos entornos, y `vus8_nivel5`
  en Vulnerable) fueron re-ejecutadas con la corrección aplicada. Las mediciones resultantes
  se consideran válidas para el análisis estadístico.
- El resto de las combinaciones conservan los reportes generados con la instrumentación
  previa. Estas mediciones deben interpretarse como cotas inferiores del impacto real: la
  latencia y el consumo de recursos observados son sistemáticamente menores que los que se
  presentarían con la federación funcionando correctamente. Las conclusiones cualitativas
  sobre la eficacia del control `graphql-depth-limit` (que bloquea los niveles 6 y 7 en el
  entorno Protegido con latencias <10 ms y bloqueo 100%) permanecen válidas porque el
  bloqueo se produce antes de la fase federada.

## Referencia de reproducibilidad

Todos los cambios aplicados están versionados en el repositorio en los archivos:

- `E-commerce/ms-usuarios/index.js` y `E-commerce-controles/ms-usuarios/index.js`
  (implementación del DataLoader).
- `E-commerce/ms-resenas/index.js` y `E-commerce-controles/ms-resenas/index.js`
  (implementación del DataLoader para las tres relaciones federadas).
- `E-commerce/docker-compose.yml` y `E-commerce-controles/docker-compose.yml`
  (`mem_limit` actualizados).
- `E-commerce/load_tests/UC02_profundidad_moderada/uc02_profundidad_nivel.js` y su
  equivalente en el entorno Protegido (`timeout: '55s'`).
