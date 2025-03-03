# Stage 1: Install dependencies (development)
FROM node:20-alpine AS development-dependencies-env
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# Stage 2: Install dependencies (production)
FROM node:20-alpine AS production-dependencies-env
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

# Stage 3: Build the React app
FROM node:20-alpine AS build-env
WORKDIR /app
COPY --from=development-dependencies-env /app/node_modules /app/node_modules
COPY . .
RUN npm run build

# Stage 4: Create the final container
FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json ./
COPY --from=production-dependencies-env /app/node_modules /app/node_modules
COPY --from=build-env /app/build /app/build
CMD ["npm", "run", "start"]
