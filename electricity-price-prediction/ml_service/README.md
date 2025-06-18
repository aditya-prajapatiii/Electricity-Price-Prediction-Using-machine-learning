# Electricity Price Prediction - ML Service

This directory contains the machine learning service for the Electricity Price Prediction system.

## Components

- `app.py`: Flask application that serves the prediction API
- `train_model.py`: Script to train the prediction model using historical data
- `data_analysis.py`: Script to analyze historical data and generate visualizations
- `generate_model.py`: Simple script to generate a model without extensive hyperparameter tuning
- `data/`: Directory containing historical electricity price data
- `model/`: Directory where trained models are stored

## Model

The pre-trained model uses a Random Forest Regressor to predict electricity prices based on:

- Hour of day
- Electricity load
- Temperature
- Weekend indicator
- Holiday indicator

### Generating the Model

To generate the model with the provided historical data:

```bash
# Navigate to the ml_service directory
cd electricity-price-prediction/ml_service

# Install dependencies
pip install -r requirements.txt

# Generate the model
python generate_model.py
```

This will create a model file at `model/electricity_price_model.pkl`.

For more extensive training with hyperparameter tuning:

```bash
python train_model.py
```

### Data Analysis

To analyze the historical data and generate visualizations:

```bash
python data_analysis.py
```

This will create visualizations in the `data/analysis` directory.

## API Endpoints

The Flask application provides the following API endpoints:

- `POST /predict`: Get a price prediction based on input parameters

  ```json
  {
    "hour": 12,
    "load": 15000,
    "temperature": 25,
    "is_weekend": false,
    "is_holiday": false
  }
  ```

- `GET /health`: Check the health of the ML service
- `GET /model-info`: Get information about the trained model

## Model Performance

The model achieved the following metrics on test data:

- RMSE: 1.17
- MAE: 0.82
- R²: 0.9923

Feature importance:

- load: 36.5%
- hour: 31.2%
- temperature: 24.8%
- is_weekend: 5.3%
- is_holiday: 2.2%
