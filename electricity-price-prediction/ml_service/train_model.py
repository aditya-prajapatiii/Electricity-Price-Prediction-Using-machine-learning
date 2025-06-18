import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_historical_data():
    """Load historical electricity price data from CSV file"""
    try:
        # Path to historical data
        data_path = os.path.join('data', 'historical_electricity_data.csv')
        
        # Check if the file exists
        if os.path.exists(data_path):
            logger.info(f"Loading historical data from {data_path}")
            data = pd.read_csv(data_path)
            return data
        else:
            logger.warning(f"Historical data file not found at {data_path}. Will generate synthetic data instead.")
            return None
    except Exception as e:
        logger.error(f"Error loading historical data: {str(e)}")
        return None

def generate_synthetic_data(n_samples=1000):
    """Generate synthetic electricity price data for demonstration"""
    logger.info("Generating synthetic data as fallback...")
    np.random.seed(42)
    
    # Hours of the day (0-23)
    hours = np.random.randint(0, 24, n_samples)
    
    # Load in MW
    base_load = 15000 + 5000 * np.sin(np.pi * hours / 12)  # Daily pattern
    load = base_load + np.random.normal(0, 1000, n_samples)
    
    # Temperature in Celsius
    temp_base = 15 + 10 * np.sin(np.pi * hours / 12)  # Daily pattern
    temperature = temp_base + np.random.normal(0, 5, n_samples)
    
    # Weekend indicator
    is_weekend = np.random.choice([0, 1], n_samples, p=[0.714, 0.286])  # 2/7 days are weekends
    
    # Holiday indicator
    is_holiday = np.random.choice([0, 1], n_samples, p=[0.95, 0.05])  # 5% chance of holiday
    
    # Price calculation with some relationships
    base_price = 40 + 20 * np.sin(np.pi * hours / 12)  # Daily pattern
    load_effect = 0.001 * (load - base_load)  # Higher load -> higher price
    temp_effect = 0.5 * (temperature - 20)  # Higher temperature -> higher price (e.g., AC usage)
    weekend_effect = -5 * is_weekend  # Weekends have lower prices
    holiday_effect = -10 * is_holiday  # Holidays have lower prices
    
    # Add noise
    noise = np.random.normal(0, 5, n_samples)
    
    # Final price
    price = base_price + load_effect + temp_effect + weekend_effect + holiday_effect + noise
    price = np.maximum(10, price)  # Ensure minimum price
    
    # Create DataFrame
    df = pd.DataFrame({
        'hour': hours,
        'load': load,
        'temperature': temperature,
        'is_weekend': is_weekend,
        'is_holiday': is_holiday,
        'price': price
    })
    
    return df

def train_model():
    """Train a model to predict electricity prices using either historical or synthetic data"""
    try:
        # Try to load historical data first
        data = load_historical_data()
        
        # If historical data is not available, generate synthetic data
        if data is None:
            data = generate_synthetic_data(n_samples=10000)
        else:
            logger.info(f"Loaded historical data with {len(data)} records")
        
        # Split features and target
        X = data[['hour', 'load', 'temperature', 'is_weekend', 'is_holiday']]
        y = data['price']
        
        # Split into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        logger.info("Training model...")
        # Define model pipeline with preprocessing
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('regressor', RandomForestRegressor(random_state=42))
        ])
        
        # Define hyperparameters for grid search
        param_grid = {
            'regressor__n_estimators': [50, 100, 200],
            'regressor__max_depth': [None, 10, 20, 30]
        }
        
        # Perform grid search
        grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='neg_mean_squared_error')
        grid_search.fit(X_train, y_train)
        
        # Get best model
        best_model = grid_search.best_estimator_
        logger.info(f"Best parameters: {grid_search.best_params_}")
        
        # Evaluate model
        y_pred = best_model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        logger.info("Model evaluation metrics:")
        logger.info(f"RMSE: {rmse:.2f}")
        logger.info(f"MAE: {mae:.2f}")
        logger.info(f"R²: {r2:.4f}")
        
        # Save model
        model_dir = 'model'
        os.makedirs(model_dir, exist_ok=True)
        model_path = os.path.join(model_dir, 'electricity_price_model.pkl')
        joblib.dump(best_model, model_path)
        logger.info(f"Model successfully saved to {model_path}")
        
        # Save feature importance
        if hasattr(best_model['regressor'], 'feature_importances_'):
            importances = best_model['regressor'].feature_importances_
            feature_importance = pd.DataFrame({
                'Feature': X.columns,
                'Importance': importances
            }).sort_values('Importance', ascending=False)
            
            logger.info("Feature importance:")
            for i, row in feature_importance.iterrows():
                logger.info(f"  {row['Feature']}: {row['Importance']:.4f}")
        
        return best_model
        
    except Exception as e:
        logger.error(f"Error training model: {str(e)}")
        raise

if __name__ == "__main__":
    train_model() 