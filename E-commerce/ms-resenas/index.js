const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { buildSubgraphSchema } = require('@apollo/subgraph');
const { PrismaClient } = require('@prisma/client');
const gql = require('graphql-tag');
const DataLoader = require('dataloader');

const prisma = new PrismaClient();

// DataLoaders para eliminar N+1 en resoluciones federadas y listas por FK.
const buildLoaders = () => ({
  resenaLoader: new DataLoader(async (ids) => {
    const resenas = await prisma.resena.findMany({ where: { id: { in: [...ids] } } });
    const map = new Map(resenas.map(r => [r.id, r]));
    return ids.map(id => map.get(id) || null);
  }),
  resenasByUsuario: new DataLoader(async (usuarioIds) => {
    const resenas = await prisma.resena.findMany({ where: { usuarioId: { in: [...usuarioIds] } } });
    const map = new Map();
    for (const r of resenas) {
      if (!map.has(r.usuarioId)) map.set(r.usuarioId, []);
      map.get(r.usuarioId).push(r);
    }
    return usuarioIds.map(id => map.get(id) || []);
  }),
  resenasByProducto: new DataLoader(async (productoIds) => {
    const resenas = await prisma.resena.findMany({ where: { productoId: { in: [...productoIds] } } });
    const map = new Map();
    for (const r of resenas) {
      if (!map.has(r.productoId)) map.set(r.productoId, []);
      map.get(r.productoId).push(r);
    }
    return productoIds.map(id => map.get(id) || []);
  }),
});

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
    __resolveReference: (ref, ctx) => ctx.resenaLoader.load(ref.id),
    autor: (resena) => ({ id: resena.usuarioId }),
    producto: (resena) => ({ id: resena.productoId })
  },
  Usuario: {
    __resolveReference: (ref) => ({ id: ref.id }),
    resenas: (usuario, _, ctx) => ctx.resenasByUsuario.load(usuario.id)
  },
  Producto: {
    __resolveReference: (ref) => ({ id: ref.id }),
    resenas: (producto, _, ctx) => ctx.resenasByProducto.load(producto.id)
  }
};

const server = new ApolloServer({ schema: buildSubgraphSchema({ typeDefs, resolvers }) });
startStandaloneServer(server, {
  listen: { port: 4003 },
  context: async () => buildLoaders(),
}).then(({ url }) => console.log(`MS Reseñas en ${url}`));
