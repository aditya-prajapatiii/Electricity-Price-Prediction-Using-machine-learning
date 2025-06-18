# Electricity Price Prediction System

A full-stack web application that predicts electricity prices using machine learning based on various input parameters such as hour of the day, load, temperature, and special day indicators.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Quick Start with Docker](#quick-start-with-docker)
  - [Manual Setup](#manual-setup)
  - [Troubleshooting](#troubleshooting)
- [Data and Model](#data-and-model)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Overview

This project implements a complete electricity price prediction system with a Java Spring Boot backend, Python Flask machine learning microservice, and React frontend. The system allows users to input parameters and receive real-time electricity price predictions based on a trained machine learning model.

## Features

- Real-time electricity price prediction
- Historical data-driven machine learning model
- Input form for prediction parameters
- History tracking of predictions
- Visualization of prediction history and model insights
- RESTful API for integration
- Responsive web design

## Tech Stack

### Backend

- Java 11
- Spring Boot 2.7.8
- Spring Data JPA
- Maven

### ML Service

- Python 3.9+
- Flask
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- joblib

### Frontend

- React 18
- React Bootstrap
- Chart.js
- axios

### Database

- MySQL 8

## Project Structure

```
electricity-price-prediction/
├── backend/                  # Java Spring Boot backend
│   ├── src/                  # Source code
│   └── pom.xml               # Maven dependencies
├── frontend/                 # React frontend
│   ├── public/               # Static files
│   ├── src/                  # React source code
│   └── package.json          # NPM dependencies
├── ml_service/               # Python Flask ML service
│   ├── model/                # ML model storage
│   ├── data/                 # Training data and analysis
│   │   ├── historical_electricity_data.csv  # Historical data
│   │   └── analysis/        # Data visualizations and statistics
│   ├── app.py                # Flask application
│   ├── train_model.py        # Model training script
│   └── data_analysis.py      # Data analysis script
├── db/                       # Database scripts
│   └── schema.sql            # Database schema
└── README.md                 # Project documentation
```

## Setup Instructions

### Prerequisites

- Docker and Docker Compose (recommended)
- Alternatively:
  - Java 11
  - Node.js and npm
  - Python 3.9+
  - MySQL 8

### Quick Start with Docker

The easiest way to run the application is with Docker:

1. Make sure Docker and Docker Compose are installed
2. Clone the repository
3. Run the setup script:
   - Windows: `setup.bat`
   - Linux/Mac: `./setup.sh`
4. Access the application at http://localhost:3000

The setup script will:

- Create necessary directories
- Build all Docker images
- Start all services
- Ensure the ML model is generated

### Manual Setup

#### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd electricity-price-prediction/backend
   ```

2. Build the project:

   ```bash
   mvn clean install
   ```

3. Run the application:
   ```bash
   mvn spring-boot:run
   ```

The backend will start on port 8080.

#### ML Service Setup

1. Navigate to the ML service directory:

   ```bash
   cd electricity-price-prediction/ml_service
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Analyze the historical data (optional):

   ```bash
   python data_analysis.py
   ```

5. Train the model using historical data:

   ```bash
   python train_model.py
   ```

6. Run the Flask app:
   ```bash
   python app.py
   ```

The ML service will start on port 5000.

#### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd electricity-price-prediction/frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm start
   ```

The frontend will start on port 3000.

#### Database Setup

1. Start MySQL server
2. Create the database and tables:
   ```bash
   mysql -u root -p < electricity-price-prediction/db/schema.sql
   ```

### Troubleshooting

#### Import Errors with scikit-learn

If you encounter import errors with scikit-learn, ensure all dependencies are installed:

```bash
pip install scikit-learn pandas numpy joblib matplotlib seaborn flask flask-cors
```

#### Maven Build Errors

If you encounter Maven build errors, make sure you have the correct version of Java installed (Java 11) and that the JAVA_HOME environment variable is set correctly.

#### Docker Connection Issues

If Docker containers cannot communicate with each other, make sure that Docker Compose is creating the correct network and that the service names match what's specified in the configuration.

## Data and Model

### Historical Data

The system uses historical electricity price data that includes:

- Timestamp
- Hour of day (0-23)
- Electricity load (MW)
- Temperature (°C)
- Weekend indicator (0/1)
- Holiday indicator (0/1)
- Electricity price ($/MWh)

The historical data helps the model learn patterns and relationships between various factors and electricity prices.

### Machine Learning Model

The prediction model is a Random Forest Regressor, which:

- Learns from historical electricity price data
- Identifies patterns in price variations based on time, load, temperature, etc.
- Provides feature importance to understand key price drivers
- Delivers accurate predictions for new input data

For more insights, run the data analysis script to generate visualizations and statistics:

```bash
cd electricity-price-prediction/ml_service
python data_analysis.py
```

This will create visualizations in the `ml_service/data/analysis` directory.

## Usage

1. Open a web browser and navigate to `http://localhost:3000`
2. Use the "Predict" page to make electricity price predictions
3. View your prediction history on the "History" page
4. Learn about the system and model insights on the "About" page

## API Endpoints

### Backend API

- `POST /api/predictions` - Make a new price prediction
- `GET /api/predictions/recent` - Get recent prediction history

### ML Service API

- `POST /predict` - Get a price prediction based on input parameters
- `GET /health` - Check the health of the ML service
- `GET /model-info` - Get information about the trained model
