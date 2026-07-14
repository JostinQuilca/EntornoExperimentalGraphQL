const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { buildSubgraphSchema } = require('@apollo/subgraph');
const { PrismaClient } = require('@prisma/client');
const gql = require('graphql-tag');

const prisma = new PrismaClient();

const typeDefs = gql`
  extend schema @link(url: "https://specs.apollo.dev/federation/v2.0", import: ["@key", "@external", "@extends"])
  
  type ReporteFinanciero {
    id: ID!
    totalVentas: Float!
  }

  type ItemOrden {
    id: ID!
    productoId: String!
    cantidad: Int!
    precioUnitario: Float!
  }

  type Orden {
    id: ID!
    clienteId: String!
    total: Float!
    items: [ItemOrden!]!
  }
  
  type Query {
    obtenerReporteGeneral: ReporteFinanciero!
    listarOrdenes: [Orden!]!
    listarReportes: [ReporteFinanciero!]!
  }

  type Mutation {
    crearOrden(clienteId: String!, total: Float!): Orden!
  }
`;

const resolvers = {
  Query: {
    obtenerReporteGeneral: async () => {
      // Simulación de carga pesada en base de datos real para el ataque de Alias
      await new Promise(resolve => setTimeout(resolve, 500)); 
      
      const aggregate = await prisma.orden.aggregate({
        _sum: {
          total: true
        }
      });
      
      return { 
        id: "REP-GENERAL", 
        totalVentas: aggregate._sum.total || 0.0 
      };
    },
    listarOrdenes: () => prisma.orden.findMany(),
    listarReportes: () => prisma.reporteFinanciero.findMany()
  },
  Mutation: {
    crearOrden: (_, { clienteId, total }) => prisma.orden.create({
      data: { clienteId, total }
    })
  },
  Orden: {
    items: (orden) => prisma.itemOrden.findMany({ where: { ordenId: orden.id } })
  }
};

const server = new ApolloServer({ schema: buildSubgraphSchema({ typeDefs, resolvers }) });
startStandaloneServer(server, { listen: { port: 4004 } }).then(({ url }) => console.log(`MS Órdenes en ${url}`));
