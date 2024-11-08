import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch historical data
tickers = ['BND', 'SPY']
data = yf.download(tickers, start='2015-01-01', end='2024-10-31')

# Clean the data
data = data.dropna()

# Loop through each ticker to analyze volatility
for ticker in tickers:
    # Select the adjusted close price for the ticker
    adjusted_close = data['Adj Close'][ticker]
    
    # Calculate daily returns
    daily_returns = adjusted_close.pct_change() * 100  # Convert to percentage
    
    # Calculate rolling mean and standard deviation
    rolling_mean = daily_returns.rolling(window=20).mean()  # 20-day rolling mean
    rolling_std = daily_returns.rolling(window=20).std()    # 20-day rolling standard deviation
    
    # Plotting the results
    plt.figure(figsize=(14, 7))
    plt.plot(daily_returns, label='Daily Returns', color='blue', alpha=0.5)
    plt.plot(rolling_mean, label='20-Day Rolling Mean', color='green', linestyle='--')
    plt.plot(rolling_std, label='20-Day Rolling Std Dev', color='red', linestyle='--')
    
    plt.title(f'Volatility Analysis of {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Daily Returns (%)')
    plt.legend()
    plt.grid()
    plt.show()