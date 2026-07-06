# Laboratorio Experimental GraphQL (Apollo Federation v2)

Este repositorio contiene un ecosistema de microservicios basado en Node.js, GraphQL y Apollo Federation v2, diseñado como un laboratorio experimental para pruebas de ciberseguridad. El entorno es vulnerable por diseño para permitir pruebas de estrés como **Ataques de Profundidad Cíclica** y **Amplificación de Alias**.

## 🛠 Requisitos previos
- Docker Desktop
- Node.js (v18 o superior)

## 🚀 Instalación y Ejecución

Sigue estos pasos para desplegar el laboratorio completo en tu máquina:

1. **Clona este repositorio y entra a la carpeta:**
   ```bash
   git clone https://github.com/JostinQuilca/EntornoExperimentalGraphQL.git
   cd EntornoExperimentalGraphQL
   ```

2. **Levanta la infraestructura con Docker:**
   *(Esto descargará e iniciará PostgreSQL, MongoDB, los 4 microservicios y el API Gateway en segundo plano)*
   ```bash
   docker-compose up -d
   ```

3. **Puebla las bases de datos (Seeder masivo):**
   *(Instala las librerías locales y ejecuta el script que inyectará 180,000 registros de prueba)*
   ```bash
   npm install
   node seeder/seed.js
   ```

## 🌐 Acceso al Entorno

Una vez que los contenedores estén corriendo, el entorno principal (API Gateway) estará disponible en la siguiente URL:

👉 **http://localhost:4000/graphql** 👈

*(Puedes abrir esa URL directamente en tu navegador para acceder a la interfaz gráfica de Apollo Sandbox y realizar tus consultas)*.
