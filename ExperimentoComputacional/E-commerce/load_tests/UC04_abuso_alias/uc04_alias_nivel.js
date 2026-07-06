import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// FORMALIZACIÓN METROLOGÍA - NORMA ISO/IEC 25023 & METODOLOGÍA WOHLIN
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');

// Nivel de intensidad inyectado por variable de entorno (1-9)
// Cada nivel corresponde a un número Fibonacci de aliases
const LEVEL = __ENV.LEVEL ? parseInt(__ENV.LEVEL) : 4;

// Secuencia Fibonacci: 1, 2, 3, 5, 8, 13, 21, 34, 55
const FIBONACCI_ALIASES = [1, 2, 3, 5, 8, 13, 21, 34, 55];
const NUM_ALIASES = FIBONACCI_ALIASES[Math.min(LEVEL - 1, FIBONACCI_ALIASES.length - 1)];

export const options = {
  vus: __ENV.VUS ? parseInt(__ENV.VUS) : 10,
  duration: '60s',
  thresholds: {
    // Circuit Breaker (Metodología SRE Google): aborta si el sistema ya colapsó
    'http_req_failed': [{ threshold: 'rate<0.50', abortOnFail: true, delayAbortEval: '10s' }],
    'http_req_duration': [{ threshold: 'p(95)<30000', abortOnFail: true, delayAbortEval: '10s' }],
  },
};

// ═══════════════════════════════════════════════════════════════
// GENERACIÓN DINÁMICA DE ALIASES (Fibonacci)
// Cada alias invoca obtenerReporteGeneral (resolver costoso
// con 500ms de latencia simulada + aggregation en BD).
// N aliases × 500ms = potencial bloqueo de N×500ms por petición.
//
// Niveles 1-3: Consultas legítimas (1-3 aliases)
// Niveles 4-5: Zona gris (5-8 aliases)
// Niveles 6-9: Ataque por abuso (13-55 aliases)
// ═══════════════════════════════════════════════════════════════

const aliases = [];
for (let i = 1; i <= NUM_ALIASES; i++) {
  aliases.push(`  reporte${i}: obtenerReporteGeneral { id totalVentas }`);
}

const payload = JSON.stringify({
  query: `
    query AtaqueAbusoAlias_Nivel${LEVEL}_x${NUM_ALIASES} {
${aliases.join('\n')}
    }
  `
});

export default function () {
  const url = 'http://localhost:4000/graphql';
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': `UC-04-Alias-Nivel-${LEVEL}-x${NUM_ALIASES}`,
    },
    timeout: '30s',
  };

  const res = http.post(url, payload, params);

  check(res, {
    'Respuesta exitosa (200 sin errores)': (r) => r.status === 200 && !r.body.includes('errors'),
    'Bloqueado por control (400/403)': (r) => r.status === 400 || r.status === 403 || (r.status === 200 && r.body.includes('errors')),
    'Servidor caido (500/502/504/timeout)': (r) => r.status >= 500 || r.error,
  });

  LatenciaMedia.add(res.timings.duration);
  const exito = res.status === 200 && !res.body.includes('errors');
  TasaFallosRed.add(!exito);

  sleep(0.1);
}
