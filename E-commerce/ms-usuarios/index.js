const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { buildSubgraphSchema } = require('@apollo/subgraph');
const { PrismaClient } = require('@prisma/client');
const gql = require('graphql-tag');
const DataLoader = require('dataloader');

const prisma = new PrismaClient();

// DataLoader para batchear las resoluciones federadas (_entities) y eliminar N+1.
// Cada request GraphQL crea su propio loader (recomendado por Apollo).
const buildUsuarioLoader = () => new DataLoader(async (ids) => {
  const usuarios = await prisma.usuario.findMany({ where: { id: { in: [...ids] } } });
  const map = new Map(usuarios.map(u => [u.id, u]));
  return ids.map(id => map.get(id) || null);
});

const typeDefs = gql`
  extend schema @link(url: "https://specs.apollo.dev/federation/v2.0", import: ["@key", "@shareable"])
  
  type Perfil {
    id: ID!
    biografia: String
    telefono: String
  }

  type Usuario @key(fields: "id") {
    id: ID!
    nombre: String!
    email: String!
    perfil: Perfil
  }
  
  type Query {
    obtenerUsuario(id: ID!): Usuario
    listarUsuarios: [Usuario!]!
  }
  
  type Mutation {
    crearUsuario(nombre: String!, email: String!): Usuario!
  }
`;

const resolvers = {
  Query: {
    obtenerUsuario: (_, { id }) => prisma.usuario.findUnique({ where: { id } }),
    listarUsuarios: () => prisma.usuario.findMany(),
  },
  Mutation: {
    crearUsuario: (_, { nombre, email }) => prisma.usuario.create({
      data: { nombre, email }
    })
  },
  Usuario: {
    __resolveReference: (referencia, ctx) => ctx.usuarioLoader.load(referencia.id),
    perfil: (usuario) => prisma.perfil.findUnique({ where: { usuarioId: usuario.id } })
  }
};

const server = new ApolloServer({ schema: buildSubgraphSchema({ typeDefs, resolvers }) });
startStandaloneServer(server, {
  listen: { port: 4001 },
  context: async () => ({ usuarioLoader: buildUsuarioLoader() }),
}).then(({ url }) => console.log(`MS Usuarios en ${url}`));
