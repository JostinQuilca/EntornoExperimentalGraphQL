import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// UC-02 Ataque por Profundidad Moderada
// Variable independiente: profundidad de anidamiento (progresion Fibonacci 1, 2, 3, 5, 8)
// Concurrencia: fija en VUs=8
// Ventana: 60 segundos por escenario
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');
export const TasaBloqueadas = new Rate('iso_tasa_bloqueadas'); // Bloqueo por control (4xx)

const LEVEL = __ENV.LEVEL ? parseInt(__ENV.LEVEL) : 1;

export const options = {
  vus: __ENV.VUS ? parseInt(__ENV.VUS) : 8,
  duration: '60s',
  userAgent: 'K6-GraphQL-Ofensive-Agent/1.0',
  thresholds: {
    'http_req_failed':   [{ threshold: 'rate<0.99', abortOnFail: false }],
    'http_req_duration': [{ threshold: 'p(95)<60000', abortOnFail: false }],
  },
};

// Construye una query de profundidad N anidando ciclicamente y respetando el
// esquema federado. El ciclo alterna entre tipos:
//   Resena (raiz) -> Usuario (autor) -> Resena -> Producto -> Resena -> Usuario -> ...
// Cada nodo consulta solo escalares validos para su tipo.
function buildQuery(level) {
  // cycle[i] describe el nodo del nivel (i+2). Los escalares evitan campos
  // que no existan en el tipo (p. ej. "comentario" no existe en Usuario).
  const cycle = [
    { field: 'autor',    scalar: 'id nombre' },       // Resena -> Usuario
    { field: 'resenas',  scalar: 'id comentario' },   // Usuario -> [Resena]
    { field: 'producto', scalar: 'id nombre precio' },// Resena -> Producto
    { field: 'resenas',  scalar: 'id comentario' },   // Producto -> [Resena]
  ];
  const rootScalar = 'id comentario';

  if (level <= 1) {
    return `query AtaqueProfundidadNivel${level} {
  listarResenas {
    ${rootScalar}
  }
}`;
  }

  // Construye desde el mas profundo (nivel = level) hacia el nivel 2.
  let inner = '';
  for (let i = level - 1; i >= 1; i--) {
    const c = cycle[(i - 1) % cycle.length];
    if (i === level - 1) {
      inner = `${c.field} { ${c.scalar} }`;
    } else {
      inner = `${c.field} { ${c.scalar} ${inner} }`;
    }
  }
  return `query AtaqueProfundidadNivel${level} {
  listarResenas {
    ${rootScalar}
    ${inner}
  }
}`;
}

const GATEWAY_URL = 'http://localhost:4000/graphql';
const QUERY = buildQuery(LEVEL);

export default function () {
  const payload = JSON.stringify({ query: QUERY });
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': `UC-02-Depth-Level-${LEVEL}`,
    },
    timeout: '55s',
  };

  const res = http.post(GATEWAY_URL, payload, params);

  check(res, {
    'Respuesta exitosa (200 sin errores)':      (r) => r.status === 200 && !r.body.includes('errors'),
    'Bloqueado por control (400/403)':          (r) => r.status === 400 || r.status === 403 || (r.status === 200 && r.body.includes('errors')),
    'Servidor caido (500/502/504/timeout)':     (r) => r.status >= 500 || r.error,
  });

  LatenciaMedia.add(res.timings.duration);
  const falloReal = res.status >= 500 || !!res.error;
  TasaFallosRed.add(falloReal);
  const bloqueado4xx = (res.status === 400 || res.status === 403);
  TasaBloqueadas.add(bloqueado4xx);

  sleep(1);
}
