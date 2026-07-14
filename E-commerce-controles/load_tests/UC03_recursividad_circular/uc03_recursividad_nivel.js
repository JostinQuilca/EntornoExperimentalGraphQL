import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// UC-03 Ataque por Recursividad Circular
// Variable independiente: numero de ciclos recursivos (1..7)
// Concurrencia: fija en VUs=8 (variable independiente = ciclos, no carga)
// Ventana: 60 segundos por escenario
// Cada ciclo = resenas -> autor -> resenas -> autor (2 niveles de profundidad)
// Ciclo valido por el schema: Usuario.resenas: [Resena], Resena.autor: Usuario
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

// Genera la query de recursividad circular resenas->autor->resenas->autor...
// para un numero dado de ciclos, sobre UN usuario concreto. Cada ciclo son 2
// niveles de anidamiento. El alcance de un solo usuario permite medir el efecto
// de la recursividad sin la explosion de listar los 10K usuarios completos.
function buildQuery(cycles, userId) {
  let inner = 'id';
  for (let i = 0; i < cycles; i++) {
    inner = `resenas { autor { ${inner} } }`;
  }
  return `query AtaqueRecursivoCircular {
    obtenerUsuario(id: "${userId}") {
      ${inner}
    }
  }`;
}

const GATEWAY_URL = 'http://localhost:4000/graphql';

// setup() se ejecuta una sola vez antes del test y obtiene un ID de usuario valido
// de la base de datos sembrada. Asi la query no depende de un ID hardcodeado que
// podria no existir tras una resiembra.
export function setup() {
  const res = http.post(GATEWAY_URL, JSON.stringify({ query: '{ listarUsuarios { id } }' }),
    { headers: { 'Content-Type': 'application/json' }, timeout: '30s' });
  try {
    const usuarios = JSON.parse(res.body).data.listarUsuarios;
    return { userId: usuarios[0].id };
  } catch (e) {
    return { userId: '1' };
  }
}

export default function (data) {
  const payload = JSON.stringify({ query: buildQuery(LEVEL, data.userId) });
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': `UC-03-Recursion-Cycles-${LEVEL}`,
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
