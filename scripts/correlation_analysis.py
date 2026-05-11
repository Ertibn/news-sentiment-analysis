import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import os

# Create reports/figures directory
os.makedirs('reports/figures', exist_ok=True)

# 1. Load Data
news_df = pd.read_csv('data/processed/news_sentiment.csv')
# Read stock data, handling potential MultiIndex header from yfinance
stock_df = pd.read_csv('data/processed/stock_with_indicators.csv', header=[0, 1, 2], index_col=0)
stock_df.columns = stock_df.columns.get_level_values(0) # Flatten MultiIndex columns
stock_df.index.name = 'Date'
stock_df = stock_df.reset_index()

# 2. Date Normalization
news_df['date'] = pd.to_datetime(news_df['date']).dt.date
stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date

# 3. Aggregate Sentiment by Date and Stock
daily_sentiment = news_df.groupby(['date', 'stock'])['sentiment_avg'].mean().reset_index()

# 4. Calculate Daily Returns
stock_df = stock_df.sort_values(['Date'])
price_col = 'Adj Close' if 'Adj Close' in stock_df.columns else 'Close'
stock_df['daily_return'] = stock_df[price_col].pct_change() * 100

# 5. Merge Datasets
# We need to map 'stock' in news to the ticker used in stock_df
# For now, we assume AAPL as used in technical_analysis.py
daily_sentiment_aapl = daily_sentiment[daily_sentiment['stock'] == 'AAPL']
merged_df = pd.merge(daily_sentiment_aapl, stock_df, left_on='date', right_on='Date')

# 6. Calculate Pearson Correlation
merged_df.dropna(subset=['sentiment_avg', 'daily_return'], inplace=True)
if len(merged_df) > 1:
    corr, p_value = pearsonr(merged_df['sentiment_avg'], merged_df['daily_return'])
    print(f"Pearson Correlation between Sentiment and Daily Return: {corr:.4f}")
    print(f"P-value: {p_value:.4f}")
else:
    print("Not enough overlapping data points for correlation analysis.")
    corr = 0

# 7. Visualization: Scatter Plot
plt.figure(figsize=(10, 6))
sns.regplot(x='sentiment_avg', y='daily_return', data=merged_df)
plt.title(f'Sentiment vs Daily Return (AAPL)\nCorrelation: {corr:.4f}')
plt.xlabel('Average Daily Sentiment Score')
plt.ylabel('Daily Stock Return (%)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('reports/figures/sentiment_return_correlation.png')
plt.close()

# 8. Visualization: Bar Chart by Sentiment Category
merged_df['sentiment_category'] = pd.cut(merged_df['sentiment_avg'], 
                                         bins=[-1, -0.1, 0.1, 1], 
                                         labels=['Negative', 'Neutral', 'Positive'])

plt.figure(figsize=(10, 6))
sns.barplot(x='sentiment_category', y='daily_return', data=merged_df, palette='viridis')
plt.title('Average Daily Return by Sentiment Category')
plt.xlabel('Sentiment Category')
plt.ylabel('Average Daily Return (%)')
plt.savefig('reports/figures/return_by_sentiment_category.png')
plt.close()

print("Correlation analysis completed. Figures saved in reports/figures/")
