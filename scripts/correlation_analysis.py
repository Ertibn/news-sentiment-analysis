import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import os

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
plt.ylabel('Average Daily Return (%)')
plt.savefig('reports/figures/return_by_sentiment_category.png')
plt.close()

# Save final merged data
merged_df.to_csv('data/processed/sentiment_correlation_results.csv', index=False)
print("Correlation analysis completed. Figures saved in reports/figures/")
