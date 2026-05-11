import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import os

# Create reports/figures directory if not exists
os.makedirs('reports/figures', exist_ok=True)

def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_macd(data, slow=26, fast=12, signal=9):
    exp1 = data.ewm(span=fast, adjust=False).mean()
    exp2 = data.ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

# Load stock data
ticker = 'AAPL'
print(f"Downloading data for {ticker}...")
stock_data = yf.download(ticker, start='2023-01-01', end='2023-05-01')

# 1. Moving Averages
stock_data['SMA_20'] = stock_data['Close'].rolling(window=20).mean()
stock_data['EMA_20'] = stock_data['Close'].ewm(span=20, adjust=False).mean()

# 2. RSI
stock_data['RSI_14'] = calculate_rsi(stock_data['Close'])

# 3. MACD
stock_data['MACD'], stock_data['MACD_Signal'] = calculate_macd(stock_data['Close'])

# Visualize Closing Prices and MAs
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(stock_data['Close'], label='Close Price', color='black')
plt.plot(stock_data['SMA_20'], label='SMA 20', color='blue', linestyle='--')
plt.plot(stock_data['EMA_20'], label='EMA 20', color='red', linestyle='--')
plt.title(f'{ticker} Price and Moving Averages')
plt.legend()

# Visualize RSI
plt.subplot(2, 1, 2)
plt.plot(stock_data['RSI_14'], label='RSI 14', color='purple')
plt.axhline(70, linestyle='--', color='red', alpha=0.5)
plt.axhline(30, linestyle='--', color='green', alpha=0.5)
plt.title('RSI')
plt.legend()

plt.tight_layout()
plt.savefig('reports/figures/stock_indicators.png')
plt.close()

# Save processed data
stock_data.to_csv('data/processed/stock_with_indicators.csv')
print("Technical analysis completed. Figures saved in reports/figures/")
