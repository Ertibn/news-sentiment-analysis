import pandas as pd
import os

# Load all processed data
news_df = pd.read_csv('data/processed/news_sentiment.csv')
stock_df = pd.read_csv('data/processed/stock_with_indicators.csv', header=[0, 1, 2], index_col=0)
stock_df.columns = stock_df.columns.get_level_values(0)

print("="*40)
print(" FINANCIAL NEWS SENTIMENT ANALYSIS RESULTS ")
print("="*40)

print(f"\n[1] NEWS DATA SUMMARY")
print(f"Total Headlines Analyzed: {len(news_df)}")
print(f"Top Publisher: {news_df['publisher'].mode()[0]}")
print(f"Average Sentiment Score: {news_df['sentiment_avg'].mean():.4f}")

print(f"\n[2] TECHNICAL ANALYSIS SUMMARY (AAPL)")
print(f"Data Points: {len(stock_df)}")
print(f"Average RSI (14): {stock_df['RSI_14'].mean():.2f}")
print(f"Last Closing Price: ${stock_df['Close'].iloc[-1]:.2f}")

# Re-run correlation logic to get the number
news_df['date'] = pd.to_datetime(news_df['date']).dt.date
stock_df.index.name = 'Date'
stock_df = stock_df.reset_index()
stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date

daily_sentiment = news_df.groupby(['date', 'stock'])['sentiment_avg'].mean().reset_index()
price_col = 'Adj Close' if 'Adj Close' in stock_df.columns else 'Close'
stock_df['daily_return'] = stock_df[price_col].pct_change() * 100
merged_df = pd.merge(daily_sentiment[daily_sentiment['stock'] == 'AAPL'], stock_df, left_on='date', right_on='Date')
merged_df.dropna(subset=['sentiment_avg', 'daily_return'], inplace=True)

print(f"\n[3] CORRELATION ANALYSIS")
if not merged_df.empty:
    from scipy.stats import pearsonr
    corr, p = pearsonr(merged_df['sentiment_avg'], merged_df['daily_return'])
    print(f"Overlapping Trading Days: {len(merged_df)}")
    print(f"Pearson Correlation: {corr:.4f}")
    print(f"P-Value: {p:.4f}")
else:
    print("No overlapping trading days found for correlation.")

print("\n" + "="*40)
print(" PROJECT ANALYSIS COMPLETE ")
print("="*40)
