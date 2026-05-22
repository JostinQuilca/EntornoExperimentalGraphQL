const net = require('net');
const { execSync } = require('child_process');

const subgraphs = [
  { name: 'ms-usuarios', port: 4001 },
  { name: 'ms-catalogo', port: 4002 },
  { name: 'ms-resenas', port: 4003 },
  { name: 'ms-ordenes', port: 4004 }
];

function checkPort(port) {
  return new Promise((resolve) => {
    const socket = new net.Socket();
    const onError = () => {
      socket.destroy();
      resolve(false);
    };
    socket.setTimeout(1000);
    socket.once('error', onError);
    socket.once('timeout', onError);
    socket.connect(port, '127.0.0.1', () => {
      socket.end();
      resolve(true);
    });
  });
}

async function waitAll() {
  console.log("Esperando a que los microservicios estén listos en los puertos 4001-4004...");
  while (true) {
    const results = await Promise.all(subgraphs.map(s => checkPort(s.port)));
    if (results.every(status => status === true)) {
      console.log("\n¡Todos los subgrafos están en línea! Iniciando API Gateway...\n");
      break;
    }
    // Print status
    const statuses = subgraphs.map((s, idx) => `${s.name}: ${results[idx] ? 'ONLINE' : 'OFFLINE'}`).join(', ');
    process.stdout.write(`\rEstado: ${statuses}`);
    await new Promise(resolve => setTimeout(resolve, 1000));
  }
  
  try {
    execSync('npm run start --prefix api-gateway', { stdio: 'inherit' });
  } catch (err) {
    console.error("Error al iniciar el API Gateway:", err);
  }
}

waitAll();
