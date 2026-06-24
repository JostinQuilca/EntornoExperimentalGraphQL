const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { buildSubgraphSchema } = require('@apollo/subgraph');
const { PrismaClient } = require('@prisma/client');
const gql = require('graphql-tag');

const prisma = new PrismaClient();

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
    __resolveReference: (referencia) => prisma.usuario.findUnique({ where: { id: referencia.id } }),
    perfil: (usuario) => prisma.perfil.findUnique({ where: { usuarioId: usuario.id } })
  }
};

const server = new ApolloServer({ schema: buildSubgraphSchema({ typeDefs, resolvers }) });
startStandaloneServer(server, { listen: { port: 4001 } }).then(({ url }) => console.log(`MS Usuarios en ${url}`));
