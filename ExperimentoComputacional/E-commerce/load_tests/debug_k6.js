import http from 'k6/http';
import { check } from 'k6';

export const options = {
  vus: 1,
  duration: '10s',
};

const GATEWAY_URL = 'http://localhost:4000/graphql';

export default function () {
  const query = JSON.stringify({
    query: `query { __schema { queryType { name } } }`
  });

  const params = {
    headers: { 'Content-Type': 'application/json' },
    timeout: '10s',
  };

  const response = http.post(GATEWAY_URL, query, params);
  
  const bodyStr = response.body ? String(response.body) : '';
  const hasErrors = bodyStr.includes('errors');
  const hasSchema = bodyStr.includes('__schema');
  
  console.log(`STATUS=${response.status} hasErrors=${hasErrors} hasSchema=${hasSchema} body=${bodyStr.substring(0, 100)}`);
  
  check(response, {
    'status is 200': (r) => r.status === 200,
    'no errors in body': (r) => r.body && !r.body.includes('"errors":'),
    'schema present': (r) => r.body && r.body.includes('__schema'),
  });
}
