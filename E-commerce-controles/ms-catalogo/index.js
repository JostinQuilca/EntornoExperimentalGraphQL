const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { buildSubgraphSchema } = require('@apollo/subgraph');
const { PrismaClient } = require('@prisma/client');
const gql = require('graphql-tag');

const prisma = new PrismaClient();

const typeDefs = gql`
  extend schema @link(url: "https://specs.apollo.dev/federation/v2.0", import: ["@key"])
  
  type Categoria {
    id: ID!
    nombre: String!
    productos: [Producto!]!
  }

  type Producto @key(fields: "id") {
    id: ID!
    nombre: String!
    precio: Float!
    categoria: Categoria
  }
  
  type Query {
    obtenerProducto(id: ID!): Producto
    listarProductos: [Producto!]!
    listarCategorias: [Categoria!]!
  }

  type Mutation {
    crearProducto(nombre: String!, precio: Float!, categoriaId: String): Producto!
  }
`;

const resolvers = {
  Query: {
    obtenerProducto: (_, { id }) => prisma.producto.findUnique({ where: { id } }),
    listarProductos: () => prisma.producto.findMany(),
    listarCategorias: () => prisma.categoria.findMany()
  },
  Mutation: {
    crearProducto: (_, { nombre, precio, categoriaId }) => prisma.producto.create({
      data: { nombre, precio, categoriaId }
    })
  },
  Producto: {
    __resolveReference: (ref) => prisma.producto.findUnique({ where: { id: ref.id } }),
    categoria: (producto) => {
      if (!producto.categoriaId) return null;
      return prisma.categoria.findUnique({ where: { id: producto.categoriaId } });
    }
  },
  Categoria: {
    productos: (categoria) => prisma.producto.findMany({ where: { categoriaId: categoria.id } })
  }
};

const server = new ApolloServer({ schema: buildSubgraphSchema({ typeDefs, resolvers }) });
startStandaloneServer(server, { listen: { port: 4002 } }).then(({ url }) => console.log(`MS Catalogo en ${url}`));
