const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { ApolloGateway, IntrospectAndCompose } = require('@apollo/gateway');
const { ApolloServerPluginLandingPageDisabled } = require('@apollo/server/plugin/disabled');
const depthLimit = require('graphql-depth-limit');
const { GraphQLError } = require('graphql'); // Importado para lanzar la excepción controlada

// ═══════════════════════════════════════════════════════════════
//  GATEWAY SEGURO — Controles de seguridad implementados:
//  1. Introspección deshabilitada globalmente (introspection: false)
//  2. LNT-SEC-01: Interceptor perimetral síncrono para Introspección
//  3. Límite de profundidad de queries (depth limit: 5)
//  4. Análisis de complejidad/costo de queries (max: 1000)
//  5. Prevención CSRF habilitada
//  6. Landing page (Sandbox/Explorer) deshabilitada
// ═══════════════════════════════════════════════════════════════

const gateway = new ApolloGateway({
  supergraphSdl: new IntrospectAndCompose({
    subgraphs: [
      { name: 'usuarios', url: process.env.USUARIOS_URL || 'http://localhost:4001/graphql' },
      { name: 'catalogo', url: process.env.CATALOGO_URL || 'http://localhost:4002/graphql' },
      { name: 'resenas',  url: process.env.RESENAS_URL  || 'http://localhost:4003/graphql' },
      { name: 'ordenes',  url: process.env.ORDENES_URL  || 'http://localhost:4004/graphql' }
    ],
  }),
});

// ── Ficha de Control LNT-SEC-01: Interceptor Perimetral Síncrono ──
const introspectionControlPlugin = {
  async requestDidStart() {
    return {
      // Regla de validación lógica sobre la fase didResolveOperation
      async didResolveOperation(requestContext) {
        const query = requestContext.request.query || '';
        
        // Inspeccionar estrictamente la cadena sintáctica buscando el metacampo __schema
        if (query.includes('__schema') || query.includes('__type')) {
          
          const isAdmin = requestContext.contextValue && requestContext.contextValue.esAdministrador;
          
          // Denegar el acceso si no cuenta con contexto de sesión administrativa
          if (!isAdmin) {
            console.warn("[LNT-SEC-01] Bloqueo perimetral ejecutado: Intento de reconocimiento pasivo.");
            // Abortar el hilo mediante el lanzamiento de una excepción controlada
            throw new GraphQLError(
              'Acceso denegado: Operación de reconocimiento estructural bloqueada por seguridad.',
              {
                extensions: { 
                  code: 'FORBIDDEN',
                  http: { status: 403 }
                }
              }
            );
          }
        }
      }
    };
  }
};

// ── Plugin personalizado: Análisis de complejidad de queries ──
const queryComplexityPlugin = {
  async requestDidStart() {
    return {
      async didResolveOperation(requestContext) {
        const { document } = requestContext;
        let totalFields = 0;
        const maxComplexity = 1000;

        function countSelections(selectionSet) {
          if (!selectionSet || !selectionSet.selections) return;
          for (const selection of selectionSet.selections) {
            totalFields++;
            if (selection.selectionSet) {
              countSelections(selection.selectionSet);
            }
          }
        }

        if (document && document.definitions) {
          for (const def of document.definitions) {
            if (def.selectionSet) {
              countSelections(def.selectionSet);
            }
          }
        }

        if (totalFields > maxComplexity) {
          throw new GraphQLError(
            `Query rechazada: complejidad ${totalFields} excede el máximo permitido (${maxComplexity}).`,
            { extensions: { code: 'BAD_REQUEST', http: { status: 400 } } }
          );
        }
      }
    };
  }
};

const server = new ApolloServer({
  gateway,
  // Control: Desactivar la característica nativa de introspección global
  introspection: false,                        
  csrfPrevention: true,                        
  validationRules: [depthLimit(5)],            
  plugins: [
    ApolloServerPluginLandingPageDisabled(),    
    queryComplexityPlugin,
    introspectionControlPlugin, // <--- Inyección del control perimetral LNT-SEC-01
  ],
});

async function iniciarGateway() {
  const { url } = await startStandaloneServer(server, { 
    listen: { port: 4000 },
    // Inyección de contexto administrativo simulado para validar el control LNT-SEC-01
    context: async ({ req }) => {
      const adminHeader = req.headers['x-admin-role'];
      const esAdministrador = adminHeader === 'true';
      return { esAdministrador };
    }
  });
  
  console.log(`══════════════════════════════════════════════════`);
  console.log(`  Apollo Gateway SEGURO operando en ${url}`);
  console.log(`  Controles activos:`);
  console.log(`    ✓ [LNT-SEC-01] Interceptor Introspección (Activo)`);
  console.log(`    ✓ [NATIVO] Introspection = false (Activo)`);
  console.log(`    ✓ Depth Limit: 5 niveles (Activo)`);
  console.log(`    ✓ Query Complexity: máx 1000 (Activo)`);
  console.log(`══════════════════════════════════════════════════`);
}
iniciarGateway();
