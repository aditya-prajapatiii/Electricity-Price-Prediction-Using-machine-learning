import os
import sys
import subprocess

# Add the ml_service directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'ml_service'))

# Change to the ml_service directory
os.chdir(os.path.join(os.path.dirname(__file__), 'ml_service'))

# Install required dependencies
print("Installing required packages...")
subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Generate the model if it doesn't exist
if not os.path.exists(os.path.join('model', 'electricity_price_model.pkl')):
    print("Generating model from historical data...")
    try:
        import generate_model
    except Exception as e:
        print(f"Error generating model: {str(e)}")

# Start the Flask app
print("Starting Flask application...")
try:
    import app
    app.app.run(host='0.0.0.0', port=5000, debug=True)
except Exception as e:
    print(f"Error starting Flask app: {str(e)}")
    print("Please ensure all dependencies are installed: pip install -r ml_service/requirements.txt") 