# Ejemplo de Dockerfile básico
FROM node:18-alpine

# Crear directorio de trabajo
WORKDIR /app

# Copiar package.json (si tienes una app Node.js)
# COPY package*.json ./

# Instalar dependencias
# RUN npm install

# Copiar código fuente
COPY . .

# Exponer puerto
EXPOSE 3000

# Comando por defecto
CMD ["echo", "Hello from Docker!"]