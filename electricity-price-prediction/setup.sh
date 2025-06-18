#!/bin/bash

# Make the script exit on error
set -e

echo "Setting up Electricity Price Prediction System..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker and Docker Compose before running this script."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose before running this script."
    exit 1
fi

echo "Creating required directories if they don't exist..."
mkdir -p ml_service/model
mkdir -p ml_service/data/analysis

echo "Ensuring all required files are executable..."
chmod +x ml_service/*.py

echo "Building and starting services with Docker Compose..."
docker-compose build
docker-compose up -d

echo "Waiting for services to start..."
sleep 10

echo "Checking service status..."
docker-compose ps

echo "Setup complete! The application is now running."
echo "- ML Service: http://localhost:5000"
echo "- Backend API: http://localhost:8080/api"
echo "- Frontend: http://localhost:3000"
echo ""
echo "You can view logs with: docker-compose logs -f"
echo "You can stop the application with: docker-compose down" 