# Use an official Node runtime as a parent image
FROM node:18-alpine

# Set work directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project files
COPY . .

# Set environment variables
ARG VITE_API_BASE_URL=http://127.0.0.1:8000/api
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL

# Expose port 5173
EXPOSE 5173

# Command to run the application in dev mode
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
