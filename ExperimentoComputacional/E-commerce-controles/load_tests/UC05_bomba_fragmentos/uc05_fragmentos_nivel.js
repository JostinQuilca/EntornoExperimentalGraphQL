import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// FORMALIZACIÓN METROLOGÍA - NORMA ISO/IEC 25023 & METODOLOGÍA WOHLIN
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');

// Nivel de intensidad inyectado por variable de entorno (1-5)
const LEVEL = __ENV.LEVEL ? parseInt(__ENV.LEVEL) : 3;

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
// QUERIES PREDETERMINADAS POR NIVEL DE BOMBA DE FRAGMENTOS
// Explota la evaluación exponencial de fragmentos anidados.
// Cada nivel incrementa el factor de expansión (spreads × niveles).
//
// Nivel 1: 1 spread × 1 nivel = 1 resolución (normal)
// Nivel 2: 2 spreads × 2 niveles = 4 resoluciones (normal)
// Nivel 3: 3 spreads × 3 niveles = 27 resoluciones (moderado)
// Nivel 4: 5 spreads × 3 niveles = 125 resoluciones (ataque)
// Nivel 5: 5 spreads × 4 niveles = 625 resoluciones (ataque severo)
// ═══════════════════════════════════════════════════════════════

const QUERIES = {
  // Nivel 1: Sin fragmentos, consulta directa (1 resolución)
  1: `query FragmentosNivel1 {
    listarUsuarios {
      id
      nombre
      email
    }
  }`,

  // Nivel 2: 2 spreads × 2 niveles = 4 resoluciones
  2: `query FragmentosNivel2 {
    listarUsuarios {
      ...F1
      ...F1
    }
  }

  fragment F1 on Usuario {
    ...F2
    ...F2
  }

  fragment F2 on Usuario {
    id
    nombre
    email
  }`,

  // Nivel 3: 3 spreads × 3 niveles = 27 resoluciones
  3: `query FragmentosNivel3 {
    listarUsuarios {
      ...F1
      ...F1
      ...F1
    }
  }

  fragment F1 on Usuario {
    ...F2
    ...F2
    ...F2
  }

  fragment F2 on Usuario {
    ...F3
    ...F3
    ...F3
  }

  fragment F3 on Usuario {
    id
    nombre
    email
  }`,

  // Nivel 4: 5 spreads × 3 niveles = 125 resoluciones
  4: `query FragmentosNivel4 {
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
    id
    nombre
    email
  }`,

  // Nivel 5: 5 spreads × 4 niveles = 625 resoluciones (el actual)
  5: `query FragmentosNivel5 {
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
  }`,
};

const selectedQuery = QUERIES[LEVEL] || QUERIES[3];
const payload = JSON.stringify({ query: selectedQuery });

export default function () {
  const url = 'http://localhost:4000/graphql';
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': `UC-05-Fragmentos-Nivel-${LEVEL}`,
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
