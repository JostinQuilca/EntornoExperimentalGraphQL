const { PrismaClient: PrismaUsuarios } = require('../ms-usuarios/node_modules/@prisma/client');
const { PrismaClient: PrismaCatalogo } = require('../ms-catalogo/node_modules/@prisma/client');
const { PrismaClient: PrismaResenas } = require('../ms-resenas/node_modules/@prisma/client');
const { PrismaClient: PrismaOrdenes } = require('../ms-ordenes/node_modules/@prisma/client');
const { faker } = require('@faker-js/faker');
const crypto = require('crypto');

const usuariosPrisma = new PrismaUsuarios({
  datasources: { db: { url: process.env.USUARIOS_DATABASE_URL || "postgresql://postgres:password@localhost:55432/usuarios?schema=public" } }
});
const catalogoPrisma = new PrismaCatalogo({
  datasources: { db: { url: process.env.CATALOGO_DATABASE_URL || "mongodb://localhost:57017/catalogo?directConnection=true" } }
});
const resenasPrisma = new PrismaResenas({
  datasources: { db: { url: process.env.RESENAS_DATABASE_URL || "postgresql://postgres:password@localhost:55432/resenas?schema=public" } }
});
const ordenesPrisma = new PrismaOrdenes({
  datasources: { db: { url: process.env.ORDENES_DATABASE_URL || "postgresql://postgres:password@localhost:55432/ordenes?schema=public" } }
});

function generateObjectId() {
  const timestamp = Math.floor(new Date().getTime() / 1000).toString(16).padStart(8, '0');
  const random = Array.from({ length: 16 }, () => Math.floor(Math.random() * 16).toString(16)).join('');
  return timestamp + random;
}

async function main() {
  console.log("=== INICIANDO SEEDING MASIVO ===");
  console.time("Seeding Total");

  // 1. Limpieza de bases de datos
  console.log("\n1. Limpiando registros anteriores...");
  
  try {
    await resenasPrisma.resena.deleteMany();
    console.log("✔ Base de datos de Reseñas limpiada.");
  } catch (err) {
    console.log("⚠ Error al limpiar Reseñas:", err.message);
  }

  try {
    await ordenesPrisma.itemOrden.deleteMany();
    await ordenesPrisma.orden.deleteMany();
    await ordenesPrisma.reporteFinanciero.deleteMany();
    console.log("✔ Base de datos de Órdenes limpiada.");
  } catch (err) {
    console.log("⚠ Error al limpiar Órdenes:", err.message);
  }

  try {
    await usuariosPrisma.perfil.deleteMany();
    await usuariosPrisma.usuario.deleteMany();
    console.log("✔ Base de datos de Usuarios limpiada.");
  } catch (err) {
    console.log("⚠ Error al limpiar Usuarios:", err.message);
  }

  try {
    await catalogoPrisma.producto.deleteMany();
    await catalogoPrisma.categoria.deleteMany();
    console.log("✔ Base de datos de Catálogo limpiada.");
  } catch (err) {
    console.log("⚠ Error al limpiar Catálogo:", err.message);
  }

  // 2. Seeding Usuarios y Perfiles (10,000)
  console.log("\n2. Generando 10,000 Usuarios y Perfiles...");
  console.time("Usuarios");
  const userIds = [];
  const usersData = [];
  const profilesData = [];

  for (let i = 0; i < 10000; i++) {
    const userId = crypto.randomUUID();
    userIds.push(userId);
    
    usersData.push({
      id: userId,
      nombre: faker.person.fullName(),
      email: `user_${i}_${faker.string.alphanumeric(5)}@correo.com` // email único garantizado
    });
    
    profilesData.push({
      id: crypto.randomUUID(),
      biografia: faker.lorem.sentence(),
      telefono: faker.phone.number(),
      usuarioId: userId
    });
  }

  const userChunkSize = 2000;
  for (let i = 0; i < usersData.length; i += userChunkSize) {
    await usuariosPrisma.usuario.createMany({ data: usersData.slice(i, i + userChunkSize) });
    await usuariosPrisma.perfil.createMany({ data: profilesData.slice(i, i + userChunkSize) });
  }
  console.timeEnd("Usuarios");
  console.log("✔ Usuarios y Perfiles insertados.");

  // 3. Seeding Categorías y Productos (50,000)
  console.log("\n3. Generando 50,000 Productos...");
  console.time("Productos");
  const categoryNames = ['Electrónica', 'Ropa', 'Hogar', 'Deportes', 'Libros', 'Juguetes', 'Salud', 'Automotriz', 'Música', 'Videojuegos'];
  const categories = [];

  for (const name of categoryNames) {
    categories.push({
      id: generateObjectId(),
      nombre: name
    });
  }
  await catalogoPrisma.categoria.createMany({ data: categories });

  const productIds = [];
  const productsData = [];
  for (let i = 0; i < 50000; i++) {
    const prodId = generateObjectId();
    productIds.push(prodId);
    const category = categories[Math.floor(Math.random() * categories.length)];
    
    productsData.push({
      id: prodId,
      nombre: `${faker.commerce.productName()} #${i}`,
      precio: parseFloat(faker.commerce.price({ min: 10, max: 2000 })),
      categoriaId: category.id
    });
  }

  const prodChunkSize = 5000;
  for (let i = 0; i < productsData.length; i += prodChunkSize) {
    await catalogoPrisma.producto.createMany({ data: productsData.slice(i, i + prodChunkSize) });
  }
  console.timeEnd("Productos");
  console.log("✔ Productos insertados.");

  // 4. Seeding Reseñas (100,000)
  console.log("\n4. Generando 100,000 Reseñas...");
  console.time("Reseñas");
  const reviewsData = [];
  for (let i = 0; i < 100000; i++) {
    const randomUser = userIds[Math.floor(Math.random() * userIds.length)];
    const randomProduct = productIds[Math.floor(Math.random() * productIds.length)];
    
    reviewsData.push({
      id: crypto.randomUUID(),
      comentario: faker.lorem.paragraph(),
      usuarioId: randomUser,
      productoId: randomProduct
    });
  }

  const revChunkSize = 5000;
  for (let i = 0; i < reviewsData.length; i += revChunkSize) {
    await resenasPrisma.resena.createMany({ data: reviewsData.slice(i, i + revChunkSize) });
  }
  console.timeEnd("Reseñas");
  console.log("✔ Reseñas insertadas.");

  // 5. Seeding Órdenes (15,000)
  console.log("\n5. Generando 15,000 Órdenes de compra...");
  console.time("Órdenes");
  const ordersData = [];
  const orderItemsData = [];
  
  for (let i = 0; i < 15000; i++) {
    const orderId = crypto.randomUUID();
    const randomUser = userIds[Math.floor(Math.random() * userIds.length)];
    const date = faker.date.past();
    
    const itemCount = Math.floor(Math.random() * 4) + 1; // 1 a 4 items por orden
    let orderTotal = 0;
    
    for (let j = 0; j < itemCount; j++) {
      const randomProduct = productsData[Math.floor(Math.random() * productsData.length)];
      const qty = Math.floor(Math.random() * 3) + 1;
      const price = randomProduct.precio;
      orderTotal += price * qty;
      
      orderItemsData.push({
        id: crypto.randomUUID(),
        ordenId: orderId,
        productoId: randomProduct.id,
        cantidad: qty,
        precioUnitario: price
      });
    }
    
    ordersData.push({
      id: orderId,
      clienteId: randomUser,
      total: parseFloat(orderTotal.toFixed(2)),
      createdAt: date
    });
  }

  const orderChunkSize = 2000;
  for (let i = 0; i < ordersData.length; i += orderChunkSize) {
    await ordenesPrisma.orden.createMany({ data: ordersData.slice(i, i + orderChunkSize) });
  }

  const itemChunkSize = 5000;
  for (let i = 0; i < orderItemsData.length; i += itemChunkSize) {
    await ordenesPrisma.itemOrden.createMany({ data: orderItemsData.slice(i, i + itemChunkSize) });
  }

  console.log("\nGenerando 5,000 Reportes Financieros pesados...");
  const reportesData = [];
  for (let i = 0; i < 5000; i++) {
    reportesData.push({
      id: crypto.randomUUID(),
      totalVentas: parseFloat((Math.random() * 100000).toFixed(2)),
      createdAt: faker.date.past()
    });
  }
  const repChunkSize = 2500;
  for (let i = 0; i < reportesData.length; i += repChunkSize) {
    await ordenesPrisma.reporteFinanciero.createMany({ data: reportesData.slice(i, i + repChunkSize) });
  }

  console.timeEnd("Órdenes");
  console.log("✔ Órdenes, ítems y reportes insertados.");

  console.log("\n==================================");
  console.timeEnd("Seeding Total");
  console.log("==================================");
}

main()
  .catch((e) => {
    console.error("❌ Error durante el Seeding masivo:", e);
    process.exit(1);
  })
  .finally(async () => {
    await usuariosPrisma.$disconnect();
    await catalogoPrisma.$disconnect();
    await resenasPrisma.$disconnect();
    await ordenesPrisma.$disconnect();
  });
