import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// FORMALIZACIÓN METROLOGÍA - NORMA ISO/IEC 25023 & METODOLOGÍA WOHLIN
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');

// Nivel de recursión inyectado por variable de entorno (1-5)
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
// QUERIES PREDETERMINADAS POR NIVEL DE RECURSIÓN CIRCULAR
// Explota la relación circular bidireccional:
//   reseña → autor(Usuario) → reseñas → autor → reseñas → ...
// Cada nivel añade un ciclo completo (autor → reseñas → autor).
// Niveles 1-2: Consultas legítimas (uso normal)
// Nivel 3: Zona gris (moderado)
// Niveles 4-5: Ataque recursivo severo
// ═══════════════════════════════════════════════════════════════

const QUERIES = {
  // Nivel 1: Un solo paso (reseña → autor), sin recursión
  1: `query RecursividadNivel1 {
    listarResenas {
      id
      comentario
      autor {
        id
        nombre
      }
    }
  }`,

  // Nivel 2: Un ciclo completo (reseña → autor → reseñas)
  2: `query RecursividadNivel2 {
    listarResenas {
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
  }`,

  // Nivel 3: Dos ciclos (reseña → autor → reseñas → autor → reseñas)
  3: `query RecursividadNivel3 {
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
            }
          }
        }
      }
    }
  }`,

  // Nivel 4: Tres ciclos (ataque moderado-severo)
  4: `query RecursividadNivel4 {
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
  }`,

  // Nivel 5: Cuatro ciclos (ataque severo - máximo recursivo)
  5: `query RecursividadNivel5 {
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
    }
  }`,
};

const selectedQuery = QUERIES[LEVEL] || QUERIES[3];
const payload = JSON.stringify({ query: selectedQuery });

export default function () {
  const url = 'http://localhost:4000/graphql';
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': `UC-03-Recursividad-Nivel-${LEVEL}`,
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
