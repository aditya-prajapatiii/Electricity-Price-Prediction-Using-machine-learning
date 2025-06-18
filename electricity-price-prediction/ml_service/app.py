import os
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Path to the trained model
MODEL_PATH = os.path.join('model', 'electricity_price_model.pkl')

def load_model():
    """Load the trained model"""
    try:
        if os.path.exists(MODEL_PATH):
            logger.info(f"Loading model from {MODEL_PATH}")
            return joblib.load(MODEL_PATH)
        else:
            logger.warning(f"Model file not found at {MODEL_PATH}")
            # Attempt to train a model since one doesn't exist
            from train_model import train_model
            logger.info("Attempting to train a new model...")
            model = train_model()
            return model
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        return None

# Load the model at startup
model = load_model()

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint to check the health of the service"""
    status = "healthy" if model is not None else "unhealthy"
    return jsonify({
        "status": status,
        "message": "ML service is running",
        "model_loaded": model is not None
    })

@app.route('/model-info', methods=['GET'])
def model_info():
    """Endpoint to get information about the model"""
    if model is None:
        return jsonify({
            "status": "error",
            "message": "No model is loaded"
        }), 500
    
    # Extract model information
    info = {
        "model_type": "Random Forest Regressor",
        "features": ["hour", "load", "temperature", "is_weekend", "is_holiday"],
        "preprocessing": "StandardScaler",
    }
    
    # Add feature importances if available
    if hasattr(model['regressor'], 'feature_importances_'):
        importances = model['regressor'].feature_importances_
        feature_importance = {}
        for i, feature in enumerate(info["features"]):
            feature_importance[feature] = float(importances[i])
        info["feature_importance"] = feature_importance
    
    # Add hyperparameters if available
    if hasattr(model['regressor'], 'get_params'):
        params = model['regressor'].get_params()
        info["hyperparameters"] = params
    
    return jsonify({
        "status": "success",
        "model_info": info
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint to make price predictions based on input parameters"""
    if model is None:
        return jsonify({
            "status": "error",
            "message": "No model is loaded"
        }), 500
    
    try:
        # Get data from request
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['hour', 'load', 'temperature', 'is_weekend', 'is_holiday']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "status": "error",
                    "message": f"Missing required field: {field}"
                }), 400
        
        # Create input DataFrame
        input_df = pd.DataFrame({
            'hour': [data['hour']],
            'load': [data['load']],
            'temperature': [data['temperature']],
            'is_weekend': [1 if data['is_weekend'] else 0],
            'is_holiday': [1 if data['is_holiday'] else 0]
        })
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        
        # Return prediction
        return jsonify({
            "status": "success",
            "prediction": float(prediction),
            "input": data
        })
        
    except Exception as e:
        logger.error(f"Error making prediction: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Error making prediction: {str(e)}"
        }), 500

# Add this main block for direct execution
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) 