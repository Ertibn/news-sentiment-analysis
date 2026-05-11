import pandas as pd
<<<<<<< HEAD
=======
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
>>>>>>> 909a87140493563d1072b172ce438b2d0325d2f6
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import os

<<<<<<< HEAD
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
=======
# Create figures directory
os.makedirs('reports/figures', exist_ok=True)

# 1. Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    return analyzer.polarity_scores(text)['compound']

# 2. Load Datasets
news_df = pd.read_csv('data/raw/raw_analyst_ratings.csv')
stock_df = pd.read_csv('data/processed/stock_with_indicators.csv', index_col=0, header=[0, 1])

# Flatten multi-index columns if they exist
if isinstance(stock_df.columns, pd.MultiIndex):
    stock_df.columns = stock_df.columns.get_level_values(0)

stock_df.index = pd.to_datetime(stock_df.index)
news_df['date'] = pd.to_datetime(news_df['date']).dt.date

# 3. Sentiment Analysis
print("Calculating sentiment scores...")
news_df['sentiment'] = news_df['headline'].apply(get_sentiment)

# 4. Stock Returns
print("Calculating daily returns...")
stock_df['Daily_Return'] = stock_df['Close'].pct_change() * 100

# 5. Date Alignment
# Function to align news to the next trading day
trading_days = stock_df.index.date
def align_to_trading_day(news_date):
    if news_date in trading_days:
        return news_date
    else:
        # Find the next available trading day
        future_days = [d for d in trading_days if d > news_date]
        return min(future_days) if future_days else None

print("Aligning dates...")
news_df['trading_date'] = news_df['date'].apply(align_to_trading_day)
news_df = news_df.dropna(subset=['trading_date'])

# 6. Aggregate Sentiment by Day and Stock
daily_sentiment = news_df.groupby(['trading_date', 'stock'])['sentiment'].mean().reset_index()

# 7. Merge with Stock Returns
# Note: Since our mock news has multiple stocks, we'll merge on both date and stock if possible.
# For simplicity in this script, we'll assume we are looking at the overall relationship if stock matches.
stock_returns = stock_df[['Daily_Return']].reset_index()
stock_returns['Date'] = stock_returns['Date'].dt.date

# Merging
merged_df = pd.merge(daily_sentiment, stock_returns, left_on='trading_date', right_on='Date')

# 8. Correlation Calculation
# Drop NaNs which might occur in Daily_Return (e.g. first row)
merged_df = merged_df.dropna(subset=['Daily_Return', 'sentiment'])

corr, p_value = pearsonr(merged_df['sentiment'], merged_df['Daily_Return'])
print(f"Pearson Correlation: {corr:.4f} (p-value: {p_value:.4f})")

# 9. Visualization
# Scatter Plot
plt.figure(figsize=(10, 6))
sns.regplot(x='sentiment', y='Daily_Return', data=merged_df, scatter_kws={'alpha':0.5})
plt.title(f'Correlation between News Sentiment and Daily Returns\nPearson Corr: {corr:.4f}')
plt.xlabel('Average Daily Sentiment Score')
plt.ylabel('Daily Stock Return (%)')
plt.savefig('reports/figures/sentiment_return_correlation.png')
plt.close()

# Bar Chart by Sentiment Category
def categorize_sentiment(score):
    if score > 0.05: return 'Positive'
    elif score < -0.05: return 'Negative'
    else: return 'Neutral'

merged_df['sentiment_class'] = merged_df['sentiment'].apply(categorize_sentiment)
avg_return_by_cat = merged_df.groupby('sentiment_class')['Daily_Return'].mean()

plt.figure(figsize=(10, 6))
avg_return_by_cat.plot(kind='bar', color=['red', 'gray', 'green'])
plt.title('Average Daily Return per Sentiment Category')
plt.xlabel('Sentiment Class')
>>>>>>> 909a87140493563d1072b172ce438b2d0325d2f6
plt.ylabel('Average Daily Return (%)')
plt.savefig('reports/figures/return_by_sentiment_category.png')
plt.close()

<<<<<<< HEAD
=======
# Save final merged data
merged_df.to_csv('data/processed/sentiment_correlation_results.csv', index=False)
>>>>>>> 909a87140493563d1072b172ce438b2d0325d2f6
print("Correlation analysis completed. Figures saved in reports/figures/")
