import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Ensure the directory exists
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Step 1: Data Acquisition
def fetch_stock_data(ticker, start, end, file_path):
    print(f"Fetching data for {ticker}...")
    
    # Check and delete old file if it exists
    if os.path.exists(file_path):
        print(f"Deleting old file: {file_path}")
        os.remove(file_path)
    
    try:
        # Fetch data and ensure the index is reset
        data = yf.download(ticker, start=start, end=end)
        data.reset_index(inplace=True)  # Ensure 'Date' becomes a column
        data.to_csv(file_path, index=False)  # Save without including the index
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error fetching data: {e}")

# Step 2: Load, Plot, and Save Chart
def plot_stock_data(file_path, chart_file_path):
    try:
        # Ensure the directory for the chart exists
        ensure_directory_exists(os.path.dirname(chart_file_path))
        
        # Load data
        data = pd.read_csv(file_path)
        print(f"Data Columns: {list(data.columns)}")  # Debugging output

        # Ensure 'Date' exists and is correctly formatted
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'])
            data.set_index('Date', inplace=True)
        else:
            raise ValueError("The file does not contain a 'Date' column.")

        # Convert 'Close' column to numeric and handle errors
        data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

        # Drop rows with missing or invalid 'Close' values
        data = data.dropna(subset=['Close'])

        # Plot the data
        plt.figure(figsize=(10, 6))
        data['Close'].plot()
        plt.title('Stock Closing Prices')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.grid()

        # Save the chart
        plt.savefig(chart_file_path)
        print(f"Chart saved to {chart_file_path}")

        # Show the chart
        plt.show()
    except Exception as e:
        print(f"Error processing data for plotting: {e}")

# Step 3: ARIMA Model and Forecasting
def arima_forecast(file_path):
    try:
        # Load data
        data = pd.read_csv(file_path, index_col='Date', parse_dates=True)

        # Convert 'Close' column to numeric and handle errors
        data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

        # Drop rows with missing or invalid 'Close' values
        data = data.dropna(subset=['Close'])

        # Fit ARIMA model
        model = ARIMA(data['Close'], order=(5, 1, 0))
        model_fit = model.fit()

        # Forecast next 30 days
        forecast = model_fit.forecast(steps=30)
        print("30-Day Forecast:")
        print(forecast)
    except Exception as e:
        print(f"Error during ARIMA forecasting: {e}")

# Main Function
if __name__ == "__main__":
    TICKER = "AAPL"
    START_DATE = "2010-01-01"
    END_DATE = "2023-12-31"
    FILE_PATH = "/Users/mando/Stock-Market-Predictor/data/aapl_stock_data.csv"
    CHART_FILE_PATH = "/Users/mando/Stock-Market-Predictor/data/stock_prices_chart.png"

    # Fetch and save data
    fetch_stock_data(TICKER, START_DATE, END_DATE, FILE_PATH)

    # Plot the data and save the chart
    plot_stock_data(FILE_PATH, CHART_FILE_PATH)

    # Perform ARIMA forecasting
    arima_forecast(FILE_PATH)
