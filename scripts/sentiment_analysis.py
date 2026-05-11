import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import os

# Create data/processed directory if not exists
os.makedirs('data/processed', exist_ok=True)

def get_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)['compound']

def get_sentiment_textblob(text):
    return TextBlob(text).sentiment.polarity

# Load data
print("Loading news data...")
df = pd.read_csv('data/raw/raw_analyst_ratings.csv')

# Perform sentiment analysis
print("Analyzing sentiment with VADER...")
df['sentiment_vader'] = df['headline'].apply(get_sentiment_vader)

print("Analyzing sentiment with TextBlob...")
df['sentiment_textblob'] = df['headline'].apply(get_sentiment_textblob)

# Combined sentiment score (average)
df['sentiment_avg'] = (df['sentiment_vader'] + df['sentiment_textblob']) / 2

# Save processed data
df.to_csv('data/processed/news_sentiment.csv', index=False)
print("Sentiment analysis completed. Results saved in data/processed/news_sentiment.csv")
