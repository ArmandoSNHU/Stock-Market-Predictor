import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Step 1: Data Acquisition
def fetch_stock_data(ticker, start, end, file_path):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, start=start, end=end)
    data.to_csv(file_path)
    print(f"Data saved to {file_path}")

# Step 2: Load and Plot Data
def plot_stock_data(file_path):
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    data['Close'].plot(figsize=(10, 6))
    plt.title('Stock Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.show()

# Step 3: ARIMA Model and Forecasting
def arima_forecast(file_path):
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    model = ARIMA(data['Close'], order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=30)
    print("30-Day Forecast:")
    print(forecast)

# Main Function
if __name__ == "__main__":
    TICKER = "AAPL"
    START_DATE = "2010-01-01"
    END_DATE = "2023-12-31"
    FILE_PATH = "data/aapl_stock_data.csv"

    # Fetch and save data
    fetch_stock_data(TICKER, START_DATE, END_DATE, FILE_PATH)

    # Plot the data
    plot_stock_data(FILE_PATH)

    # Perform ARIMA forecasting
    arima_forecast(FILE_PATH)
