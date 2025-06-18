import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def analyze_historical_data():
    """Analyze and visualize historical electricity price data"""
    try:
        # Path to historical data
        data_path = os.path.join('data', 'historical_electricity_data.csv')
        
        # Check if the file exists
        if not os.path.exists(data_path):
            logger.error(f"Historical data file not found at {data_path}")
            return
        
        # Load the data
        logger.info(f"Loading data from {data_path}")
        data = pd.read_csv(data_path)
        
        # Convert timestamp to datetime
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        
        # Display basic information
        logger.info(f"Dataset shape: {data.shape}")
        logger.info("\nData summary:")
        logger.info(f"\n{data.describe()}")
        
        # Create output directory for plots
        plots_dir = os.path.join('data', 'analysis')
        os.makedirs(plots_dir, exist_ok=True)
        
        # Time series plot of electricity prices
        plt.figure(figsize=(12, 6))
        plt.plot(data['timestamp'], data['price'], marker='o', linestyle='-', alpha=0.7)
        plt.title('Electricity Price Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price ($/MWh)')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, 'price_time_series.png'))
        
        # Price distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(data['price'], kde=True, bins=20)
        plt.title('Distribution of Electricity Prices')
        plt.xlabel('Price ($/MWh)')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, 'price_distribution.png'))
        
        # Price by hour of day
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='hour', y='price', data=data)
        plt.title('Electricity Price by Hour of Day')
        plt.xlabel('Hour')
        plt.ylabel('Price ($/MWh)')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, 'price_by_hour.png'))
        
        # Price by weekend/weekday
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='is_weekend', y='price', data=data)
        plt.title('Electricity Price: Weekend vs Weekday')
        plt.xlabel('Weekend (1) vs Weekday (0)')
        plt.ylabel('Price ($/MWh)')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, 'price_weekend_weekday.png'))
        
        # Price by holiday/non-holiday
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='is_holiday', y='price', data=data)
        plt.title('Electricity Price: Holiday vs Non-Holiday')
        plt.xlabel('Holiday (1) vs Non-Holiday (0)')
        plt.ylabel('Price ($/MWh)')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, 'price_holiday_nonholiday.png'))
        
        # Correlation heatmap
        plt.figure(figsize=(10, 8))
        correlation = data[['hour', 'load', 'temperature', 'is_weekend', 'is_holiday', 'price']].corr()
        sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, 'correlation_heatmap.png'))
        
        # Price vs Load scatter plot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='load', y='price', hue='hour', data=data, palette='viridis', alpha=0.7)
        plt.title('Electricity Price vs Load')
        plt.xlabel('Load (MW)')
        plt.ylabel('Price ($/MWh)')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, 'price_vs_load.png'))
        
        # Price vs Temperature scatter plot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='temperature', y='price', hue='hour', data=data, palette='viridis', alpha=0.7)
        plt.title('Electricity Price vs Temperature')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Price ($/MWh)')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, 'price_vs_temperature.png'))
        
        # Generate summary statistics file
        summary_path = os.path.join(plots_dir, 'data_summary.txt')
        with open(summary_path, 'w') as f:
            f.write("Electricity Price Prediction - Data Summary\n")
            f.write("===========================================\n\n")
            f.write(f"Dataset shape: {data.shape}\n\n")
            f.write("Descriptive Statistics:\n")
            f.write(f"{data.describe().to_string()}\n\n")
            f.write("Correlation Matrix:\n")
            f.write(f"{correlation.to_string()}\n\n")
            
            # Additional statistics
            f.write("Average price by hour:\n")
            f.write(f"{data.groupby('hour')['price'].mean().to_string()}\n\n")
            
            f.write("Average price by weekend/weekday:\n")
            f.write(f"{data.groupby('is_weekend')['price'].mean().to_string()}\n\n")
            
            f.write("Average price by holiday/non-holiday:\n")
            f.write(f"{data.groupby('is_holiday')['price'].mean().to_string()}\n\n")
        
        logger.info(f"Analysis completed. Plots and summary saved to {plots_dir}")
        
        # Return data for further analysis if needed
        return data
        
    except Exception as e:
        logger.error(f"Error analyzing historical data: {str(e)}")
        
if __name__ == "__main__":
    analyze_historical_data() 