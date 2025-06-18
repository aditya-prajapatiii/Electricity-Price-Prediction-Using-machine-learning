"""
Simple script to run the ML service locally
"""
import os
import sys
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    # Install dependencies
    logger.info("Checking required packages...")
    import pandas
    import numpy
    import sklearn
    import flask
    import joblib
    logger.info("All required packages are installed.")
except ImportError as e:
    logger.error(f"Missing dependency: {e}")
    logger.info("Installing required packages...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    logger.info("Dependencies installed successfully.")

# Create required directories
os.makedirs('model', exist_ok=True)
os.makedirs(os.path.join('data', 'analysis'), exist_ok=True)

# Check for model file
model_path = os.path.join('model', 'electricity_price_model.pkl')
if not os.path.exists(model_path):
    logger.info("Model not found. Generating a model using training data...")
    try:
        from train_model import train_model
        train_model()
        logger.info("Model generated successfully.")
    except Exception as e:
        logger.error(f"Error generating model: {str(e)}")
        logger.info("Will use synthetic data if needed.")

# Run the Flask app
logger.info("Starting the ML service...")
try:
    from app import app
    app.run(host='0.0.0.0', port=5000, debug=True)
except Exception as e:
    logger.error(f"Error starting the ML service: {str(e)}")
    sys.exit(1) 