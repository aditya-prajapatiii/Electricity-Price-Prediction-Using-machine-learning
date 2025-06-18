-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS electricity_price_prediction;

-- Use the database
USE electricity_price_prediction;

-- Create prediction_records table
CREATE TABLE IF NOT EXISTS prediction_records (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    hour INT NOT NULL,
    load DOUBLE NOT NULL,
    temperature DOUBLE NOT NULL,
    weekend BOOLEAN NOT NULL,
    holiday BOOLEAN NOT NULL,
    predicted_price DOUBLE NOT NULL,
    created_at DATETIME NOT NULL
); 