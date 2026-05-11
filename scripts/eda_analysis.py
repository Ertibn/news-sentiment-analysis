import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Create reports/figures directory
os.makedirs('reports/figures', exist_ok=True)

# Load data
df = pd.read_csv('data/raw/raw_analyst_ratings.csv')
df['date'] = pd.to_datetime(df['date'])

# 1. Descriptive Statistics: Headline Length
df['headline_length'] = df['headline'].apply(len)
plt.figure(figsize=(10, 6))
sns.histplot(df['headline_length'], bins=20, kde=True)
plt.title('Distribution of Headline Lengths')
plt.xlabel('Character Count')
plt.ylabel('Frequency')
plt.savefig('reports/figures/headline_length_dist.png')
plt.close()

# 2. Articles per Publisher
plt.figure(figsize=(12, 6))
df['publisher'].value_counts().plot(kind='bar')
plt.title('Number of Articles per Publisher')
plt.xlabel('Publisher')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/articles_per_publisher.png')
plt.close()

# 3. Trends over Time (News Volume)
df['date_only'] = df['date'].dt.date
plt.figure(figsize=(12, 6))
df.groupby('date_only').size().plot()
plt.title('News Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.savefig('reports/figures/news_volume_time.png')
plt.close()

# 4. Stock Analysis
plt.figure(figsize=(10, 6))
df['stock'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Stock Coverage Distribution')
plt.savefig('reports/figures/stock_distribution.png')
plt.close()

print("EDA analysis completed. Figures saved in reports/figures/")
