@echo off
echo Setting up Electricity Price Prediction System...

REM Check if Docker is installed
where docker >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Docker is not installed. Please install Docker and Docker Compose before running this script.
    exit /b 1
)

REM Check if Docker Compose is installed
where docker-compose >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Docker Compose is not installed. Please install Docker Compose before running this script.
    exit /b 1
)

echo Creating required directories if they don't exist...
if not exist ml_service\model mkdir ml_service\model
if not exist ml_service\data\analysis mkdir ml_service\data\analysis

echo Building and starting services with Docker Compose...
docker-compose build
docker-compose up -d

echo Waiting for services to start...
timeout /t 10 /nobreak >nul

echo Checking service status...
docker-compose ps

echo.
echo Setup complete! The application is now running.
echo - ML Service: http://localhost:5000
echo - Backend API: http://localhost:8080/api
echo - Frontend: http://localhost:3000
echo.
echo You can view logs with: docker-compose logs -f
echo You can stop the application with: docker-compose down

pause 