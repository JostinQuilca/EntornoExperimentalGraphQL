import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// =============================================================================
// FORMALIZACIÓN METROLOGÍA - NORMA ISO/IEC 25023 & METODOLOGÍA WOHLIN
// =============================================================================
export const LatenciaMedia = new Trend('iso_latencia_media');
export const TasaFallosRed = new Rate('iso_tasa_fallos_red');

// Nivel de profundidad inyectado por variable de entorno (1-7)
const LEVEL = __ENV.LEVEL ? parseInt(__ENV.LEVEL) : 5;

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
// QUERIES PREDETERMINADAS POR NIVEL DE PROFUNDIDAD
// Cada nivel añade un nivel de anidamiento sobre el grafo federado.
// Niveles 1-3: Consultas legítimas (uso normal)
// Niveles 4-5: Consultas en el límite OWASP (zona gris)
// Niveles 6-7: Ataque por profundidad excesiva
// ═══════════════════════════════════════════════════════════════

const QUERIES = {
  // Nivel 1: Consulta plana, sin anidamiento
  1: `query ProfundidadNivel1 {
    listarResenas {
      id
      comentario
    }
  }`,

  // Nivel 2: Un nivel de anidamiento (reseña → autor)
  2: `query ProfundidadNivel2 {
    listarResenas {
      id
      comentario
      autor {
        id
        nombre
        email
      }
    }
  }`,

  // Nivel 3: Dos niveles de anidamiento (reseña → autor → reseñas)
  3: `query ProfundidadNivel3 {
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

  // Nivel 4: Tres niveles (reseña → autor → reseñas → producto)
  4: `query ProfundidadNivel4 {
    listarResenas {
      id
      comentario
      autor {
        id
        nombre
        resenas {
          id
          comentario
          producto {
            id
            nombre
            precio
          }
        }
      }
    }
  }`,

  // Nivel 5: Profundidad 5 — Coincide con el depth limit configurado
  5: `query ProfundidadNivel5 {
    listarResenas {
      id
      comentario
      autor {
        id
        nombre
        email
        resenas {
          id
          comentario
          producto {
            id
            nombre
            precio
            resenas {
              id
              comentario
            }
          }
        }
      }
    }
  }`,

  // Nivel 6: Profundidad 6 — SUPERA el depth limit (ataque)
  6: `query ProfundidadNivel6 {
    listarResenas {
      id
      comentario
      autor {
        id
        nombre
        resenas {
          id
          comentario
          producto {
            id
            nombre
            resenas {
              id
              comentario
              autor {
                id
                nombre
              }
            }
          }
        }
      }
    }
  }`,

  // Nivel 7: Profundidad 7 — Ataque severo
  7: `query ProfundidadNivel7 {
    listarResenas {
      id
      comentario
      autor {
        id
        nombre
        resenas {
          id
          comentario
          producto {
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
};

const selectedQuery = QUERIES[LEVEL] || QUERIES[5];
const payload = JSON.stringify({ query: selectedQuery });

export default function () {
  const url = 'http://localhost:4000/graphql';
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'X-Attack-Vector': `UC-02-Profundidad-Nivel-${LEVEL}`,
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
