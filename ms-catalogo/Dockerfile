FROM node:18-slim
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN apt-get update && apt-get install -y netcat-openbsd openssl
COPY . .
RUN npx prisma generate
EXPOSE 4002
CMD ["sh", "-c", "npx prisma db push && npm start"]
