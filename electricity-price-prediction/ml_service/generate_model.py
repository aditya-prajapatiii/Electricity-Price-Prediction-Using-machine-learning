"""
Script to generate a pre-trained model for electricity price prediction
using the provided historical data.
"""
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# Ensure model directory exists
os.makedirs('model', exist_ok=True)

# Path to historical data
data_path = os.path.join('data', 'historical_electricity_data.csv')

# Check if the file exists
if not os.path.exists(data_path):
    print(f"Error: Historical data file not found at {data_path}")
    exit(1)

# Load the data
print(f"Loading data from {data_path}")
data = pd.read_csv(data_path)

# Display basic information
print(f"Dataset shape: {data.shape}")
print("\nData summary:")
print(data.describe())

# Split features and target
X = data[['hour', 'load', 'temperature', 'is_weekend', 'is_holiday']]
y = data['price']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training model...")
# Define model pipeline with preprocessing
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', RandomForestRegressor(n_estimators=100, max_depth=20, random_state=42))
])

# Train the model
pipeline.fit(X_train, y_train)

# Save model
model_path = os.path.join('model', 'electricity_price_model.pkl')
joblib.dump(pipeline, model_path)
print(f"Model successfully saved to {model_path}")

# Feature importance
if hasattr(pipeline['regressor'], 'feature_importances_'):
    importances = pipeline['regressor'].feature_importances_
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': importances
    }).sort_values('Importance', ascending=False)
    
    print("\nFeature importance:")
    for i, row in feature_importance.iterrows():
        print(f"  {row['Feature']}: {row['Importance']:.4f}")

print("\nPre-trained model has been successfully generated.") 