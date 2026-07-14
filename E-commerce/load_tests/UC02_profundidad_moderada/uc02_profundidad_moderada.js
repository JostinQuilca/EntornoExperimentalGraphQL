import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// FORMALIZACIÓN METROLOGÍA - NORMA ISO/IEC 25023 & METODOLOGÍA WOHLIN
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');

// Configuración base (se sobrescribe desde la terminal al lanzar el ataque)
export const options = {
  vus: __ENV.VUS ? parseInt(__ENV.VUS) : 10,
  duration: '60s',
  timeout: '30s' // Tolerancia para registrar los fallos reales cuando Node.js se congele
  thresholds: {
    // Circuit Breaker (Metodología SRE Google): aborta si el sistema ya colapsó
    'http_req_failed': [{ threshold: 'rate<0.50', abortOnFail: true, delayAbortEval: '10s' }],
    'http_req_duration': [{ threshold: 'p(95)<30000', abortOnFail: true, delayAbortEval: '10s' }],
  },
};
// Payload del UC-02: Profundidad Moderada (Exactamente 5 Niveles)
const payload = JSON.stringify({
  query: `
    query AtaqueProfundidadModerada {
      listarResenas {                # Nivel 1
        id
        comentario
        autor {                      # Nivel 2
          id
          nombre
          email
          resenas {                  # Nivel 3
            id
            comentario
            producto {               # Nivel 4
              id
              nombre
              precio
              resenas {              # Nivel 5
                id
                comentario
              }
            }
          }
        }
      }
    }
  `
});

export default function () {
  const url = 'http://localhost:4000/graphql'; // Endpoint del Apollo Gateway
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': 'UC-02-Profundidad-Moderada',
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
    'Gateway Vulnerable (200 OK - Petición procesada)': (r) => r.status === 200 && !r.body.includes('errors'),
    'Gateway Protegido (400 Error - Bloqueo por Límite de Profundidad)': (r) => r.status === 400 || (r.status === 200 && r.body.includes('errors')),
    'Gateway Caído / Timeout (500/502/504)': (r) => r.status >= 500 || r.error,
  });

  LatenciaMedia.add(res.timings.duration);
  const falloReal = res.status >= 500 || !!res.error; // fallo real = colapso (5xx/timeout); 4xx = bloqueo OK, no cuenta
  TasaFallosRed.add(falloReal);

  // Pequeño respiro para no saturar los puertos de tu propia máquina anfitriona
  sleep(0.1); 
}
