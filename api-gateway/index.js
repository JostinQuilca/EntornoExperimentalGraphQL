const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { ApolloGateway, IntrospectAndCompose } = require('@apollo/gateway');

const gateway = new ApolloGateway({
  supergraphSdl: new IntrospectAndCompose({
    subgraphs: [
      { name: 'usuarios', url: process.env.USUARIOS_URL || 'http://localhost:4001/graphql' },
      { name: 'catalogo', url: process.env.CATALOGO_URL || 'http://localhost:4002/graphql' },
      { name: 'resenas', url: process.env.RESENAS_URL || 'http://localhost:4003/graphql' },
      { name: 'ordenes', url: process.env.ORDENES_URL || 'http://localhost:4004/graphql' }
    ],
  }),
});

const server = new ApolloServer({ gateway });

async function iniciarGateway() {
  const { url } = await startStandaloneServer(server, { listen: { port: 4000 } });
  console.log(`Apollo Gateway unificado operando en ${url}`);
}
iniciarGateway();
