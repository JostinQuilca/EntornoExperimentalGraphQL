import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// FORMALIZACIÓN METROLOGÍA - NORMA ISO/IEC 25023 & METODOLOGÍA WOHLIN
// =============================================================================
// Definición de métricas personalizadas para la adquisición de datos crudos
export const LatenciaMedia = new Trend('iso_latencia_media'); // Ecuación (1) - Tiempo de respuesta promedio
export const TasaFallosRed = new Rate('iso_tasa_fallos_red'); // Ecuación (6) - Tasa de Fallos Estructurales (Ω)
export const TasaBloqueadas = new Rate('iso_tasa_bloqueadas'); // Bloqueo por control (4xx)

export const options = {
  // Captura dinámica del nivel de concurrencia inyectado por la variable de entorno
  vus: __ENV.VUS ? parseInt(__ENV.VUS) : 10, 
  // Ventana de observación estandarizada por escenario de estrés (Lawi et al. & Wohlin et al.)
  duration: '60s',
  // Configuración del agente de usuario para simular peticiones síncronas paralelas limpias
  userAgent: 'K6-GraphQL-Ofensive-Agent/1.0',
  thresholds: {
    // Métricas registradas sin aborto — necesitamos medir el punto de quiebre completo
    'http_req_failed': [{ threshold: 'rate<0.99', abortOnFail: false }],
    'http_req_duration': [{ threshold: 'p(95)<60000', abortOnFail: false }],
  },
};

// Endpoint perimetral federado (Apollo Gateway local en entorno de contenedores)
const GATEWAY_URL = 'http://localhost:4000/graphql';

export default function () {
  // Payload real de ataque por introspección estructural (Metacampos __schema y __type)
  // Este cuerpo extrae las consultas, mutaciones y tipos lógicos expuestos del grafo
  const queryIntrospeccion = JSON.stringify({
    query: `
      query AuditoriaIntrospeccionPasiva {
        __schema {
          queryType {
            name
            fields {
              name
              type {
                name
                kind
              }
            }
          }
          mutationType {
            name
            fields {
              name
              type {
                name
                kind
              }
            }
          }
        }
      }
    `
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': 'UC-01-Introspection-Baseline',
    },
    timeout: '10s', // Umbral límite para detectar Request Timeout físico en la red
  };

  // Ejecución de la solicitud HTTP POST de forma síncrona
  const response = http.post(GATEWAY_URL, queryIntrospeccion, params);

  // =============================================================================
  // VALIDACIÓN DE FALLOS LOGIC-AWARE (Aislamiento de falsos HTTP 200 OK)
  // =============================================================================
  // GraphQL suele encapsular errores dentro de un HTTP 200. Esta validación estricta
  // garantiza verificar si realmente se expuso la metadata sintáctica del esquema.
  check(response, {
    'HTTP Status es 200': (r) => r.status === 200,
    'Esquema no bloqueado (__schema presente)': (r) => r.body && r.body.includes('__schema'),
    'Sin mensajes de error internos': (r) => r.body && !r.body.includes('"errors":'),
  });

  // Almacenamiento de variables dependientes telemétricas
  LatenciaMedia.add(response.timings.duration);
  
  // Si la verificación falla (check devuelve false), se contabiliza como un fallo estructural (Ω)
  const bodyStr = response.body ? String(response.body) : '';
  const falloReal = response.status >= 500 || !!response.error; // fallo real = colapso (5xx/timeout); 4xx = bloqueo OK, no cuenta
  TasaFallosRed.add(falloReal);
  const bloqueado4xx = (response.status === 400 || response.status === 403);
  TasaBloqueadas.add(bloqueado4xx);

  // Pausa síncrona discreta para simular el comportamiento de concurrencia distribuida en red
  sleep(1);
}
