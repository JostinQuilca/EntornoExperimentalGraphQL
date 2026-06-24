const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { buildSubgraphSchema } = require('@apollo/subgraph');
const { PrismaClient } = require('@prisma/client');
const gql = require('graphql-tag');

const prisma = new PrismaClient();

const typeDefs = gql`
  extend schema @link(url: "https://specs.apollo.dev/federation/v2.0", import: ["@key", "@external", "@extends"])
  
  type Resena @key(fields: "id") {
    id: ID!
    comentario: String!
    autor: Usuario!
    producto: Producto!
  }
  
  type Usuario @key(fields: "id") @extends {
    id: ID! @external
    resenas: [Resena!]!
  }
  
  type Producto @key(fields: "id") @extends {
    id: ID! @external
    resenas: [Resena!]!
  }
  
  type Query {
    obtenerResena(id: ID!): Resena
    listarResenas: [Resena!]!
  }
  
  type Mutation {
    crearResena(comentario: String!, usuarioId: String!, productoId: String!): Resena!
  }
`;

const resolvers = {
  Query: {
    obtenerResena: (_, { id }) => prisma.resena.findUnique({ where: { id } }),
    listarResenas: () => prisma.resena.findMany()
  },
  Mutation: {
    crearResena: (_, { comentario, usuarioId, productoId }) => prisma.resena.create({
      data: { comentario, usuarioId, productoId }
    })
  },
  Resena: {
    __resolveReference: (ref) => prisma.resena.findUnique({ where: { id: ref.id } }),
    autor: (resena) => ({ id: resena.usuarioId }),
    producto: (resena) => ({ id: resena.productoId })
  },
  Usuario: {
    __resolveReference: (ref) => ({ id: ref.id }),
    resenas: (usuario) => prisma.resena.findMany({ where: { usuarioId: usuario.id } })
  },
  Producto: {
    __resolveReference: (ref) => ({ id: ref.id }),
    resenas: (producto) => prisma.resena.findMany({ where: { productoId: producto.id } })
  }
};

const server = new ApolloServer({ schema: buildSubgraphSchema({ typeDefs, resolvers }) });
startStandaloneServer(server, { listen: { port: 4003 } }).then(({ url }) => console.log(`MS Reseñas en ${url}`));
