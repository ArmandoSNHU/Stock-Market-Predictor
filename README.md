# Stock Market Predictor

## Overview
This project analyzes historical stock market data and predicts future prices using the ARIMA model.

## Features
- Fetch historical stock data using Yahoo Finance API.
- Visualize trends in stock prices.
- Predict future prices using ARIMA.



## **How It Works**

1. Enter the stock ticker (e.g., `AAPL` for Apple).
2. Select the date range for the historical analysis.
3. Specify the number of days for forecasting (e.g., 30 days).
4. View a detailed stock price chart and ARIMA forecast.
5. Download the forecast results as a CSV for further analysis.

---

## **Requirements**

### **Python Libraries**
Ensure you have the following Python libraries installed:
- `yfinance`
- `pandas`
- `matplotlib`
- `statsmodels`
- `streamlit`

  
## Installation
1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
