import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// FORMALIZACIÓN METROLOGÍA - NORMA ISO/IEC 25023 & METODOLOGÍA WOHLIN
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');

// Configuración base (se sobrescribe desde la terminal)
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
// Payload UC-03: Ataque Recursivo Circular
// Explota la relación circular bidireccional:
//   reseña → autor(Usuario) → reseñas → autor → reseñas → autor → reseñas
// Profundidad: 7 niveles con ciclo reseña↔autor
// A diferencia de UC-02 (profundidad lineal), este ataque
// fuerza el mismo ciclo repetitivo para amplificar las consultas
// a la base de datos de forma exponencial.
// ═══════════════════════════════════════════════════════════════
const payload = JSON.stringify({
  query: `
    query AtaqueRecursivoCircular {
      listarResenas {
        id
        comentario
        autor {
          id
          nombre
          resenas {
            id
            comentario
            autor {
              id
              nombre
              resenas {
                id
                comentario
                autor {
                  id
                  nombre
                  resenas {
                    id
                    comentario
                  }
                }
              }
            }
          }
        }
      }
    }
  `
});

export default function () {
  const url = 'http://localhost:4000/graphql';
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': 'UC-03-Recursividad-Circular',
    },
    timeout: '30s',
    thresholds: {
    // Circuit Breaker (Metodología SRE Google): aborta si el sistema ya colapsó
    'http_req_failed': [{ threshold: 'rate<0.50', abortOnFail: true, delayAbortEval: '10s' }],
    'http_req_duration': [{ threshold: 'p(95)<30000', abortOnFail: true, delayAbortEval: '10s' }],
  },
};
  const res = http.post(url, payload, params);

  // Verificaciones
  check(res, {
    'Respuesta exitosa (200 sin errores)': (r) => r.status === 200 && !r.body.includes('errors'),
    'Bloqueado por control (400/403)': (r) => r.status === 400 || r.status === 403 || (r.status === 200 && r.body.includes('errors')),
    'Servidor caido (500/502/504/timeout)': (r) => r.status >= 500 || r.error,
  });

  LatenciaMedia.add(res.timings.duration);
  const falloReal = res.status >= 500 || !!res.error; // fallo real = colapso (5xx/timeout); 4xx = bloqueo OK, no cuenta
  TasaFallosRed.add(falloReal);

  sleep(0.1);
}
