# UC-01 — Evidencia del control de introspeccion

Misma query de introspeccion enviada a ambos entornos:

```graphql
query AtaqueIntrospeccion { __schema { queryType { name } types { name } } }
```

| Entorno | HTTP | Esquema expuesto | Veredicto |
| :--- | :---: | :---: | :--- |
| VULNERABLE | 200 | SI | Ataque exitoso |
| PROTEGIDO | 400 | NO | Ataque bloqueado (control efectivo) |

## Respuestas capturadas

### VULNERABLE (HTTP 200)
```json
{"data":{"__schema":{"queryType":{"name":"Query"},"types":[{"name":"Categoria"},{"name":"ID"},{"name":"String"},{"name":"ItemOrden"},{"name":"Int"},{"name":"Float"},{"name":"Mutation"},{"name":"Orden"},{"name":"Perfil"},{"name":"Producto"},{"name":"Query"},{"name":"ReporteFinanciero"},{"name":"Resena"},{"name":"Usuario"},{"name":"Boolean"},{"name":"__Schema"},{"name":"__Type"},{"name":"__TypeKind"},{"name":"__Field"},{"name":"__InputValue"},{"name":"__EnumValue"},{"name":"__Directive"},{"name":"__DirectiveLocation"}]}}}

```

### PROTEGIDO (HTTP 400)
```json
{"errors":[{"message":"GraphQL introspection is not allowed by Apollo Server, but the query contained __schema or __type. To enable introspection, pass introspection: true to ApolloServer in production","locations":[{"line":1,"column":29}],"extensions":{"validationErrorCode":"INTROSPECTION_DISABLED","code":"GRAPHQL_VALIDATION_FAILED","stacktrace":["GraphQLError: GraphQL introspection is not allowed by Apollo Server, but the query contained __schema or __type. To enable introspection, pass introspection: true to ApolloServer in production","    at Object.Field (/app/node_modules/@apollo/server/
```
