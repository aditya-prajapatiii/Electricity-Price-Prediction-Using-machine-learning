FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create model directory
RUN mkdir -p model

# Ensure data directory exists
RUN mkdir -p data

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port for Flask
EXPOSE 5000

# Generate model and run Flask app
CMD ["python", "app.py"] 