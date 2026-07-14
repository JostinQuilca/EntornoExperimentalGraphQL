import http from 'k6/http';
import { check } from 'k6';

export const options = {
  scenarios: {
    'EXP_01': {
      executor: 'constant-vus',
      vus: 10,
      duration: '60s',
      startTime: '0s',
    },
    'EXP_02': {
      executor: 'constant-vus',
      vus: 20,
      duration: '60s',
      startTime: '60s',
    },
    'EXP_03': {
      executor: 'constant-vus',
      vus: 50,
      duration: '60s',
      startTime: '120s',
    },
    'EXP_04': {
      executor: 'constant-vus',
      vus: 100,
      duration: '60s',
      startTime: '180s',
    },
    'EXP_05': {
      executor: 'constant-vus',
      vus: 250,
      duration: '60s',
      startTime: '240s',
    },
  },
};

const URL = 'http://localhost:4000/graphql';

const payload = JSON.stringify({
  query: 'query { listarResenas { id comentario autor { id nombre resenas { id producto { id nombre } } } } }'
});

const params = {
  headers: {
    'Content-Type': 'application/json',
  },
};

export default function () {
  const res = http.post(URL, payload, params);

  check(res, {
    'status is 200': (r) => r.status === 200,
  });
}
