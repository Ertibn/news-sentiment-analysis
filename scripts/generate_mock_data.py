import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Sample data generation
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
publishers = ['Reuters', 'Bloomberg', 'Seeking Alpha', 'The Motley Fool', 'CNBC']
headlines = [
    "Apple hits record high as iPhone sales soar",
    "Microsoft announces new AI integration in Office 365",
    "Google faces antitrust probe in Europe",
    "Amazon reports stellar earnings beat",
    "Tesla stock plunges after production delays",
    "Market rallies on news of lower interest rates",
    "Tech stocks lead gains in afternoon trading",
    "Analysts raise price target on MSFT",
    "AAPL to launch new wearable device next month",
    "Oil prices rise amid global supply concerns"
]

data = []
start_date = datetime(2023, 1, 1)
for i in range(100):
    date = start_date + timedelta(days=np.random.randint(0, 30), hours=np.random.randint(0, 24))
    data.append({
        'headline': np.random.choice(headlines),
        'url': f"https://example.com/article/{i}",
        'publisher': np.random.choice(publishers),
        'date': date.strftime("%Y-%m-%d %H:%M:%S"),
        'stock': np.random.choice(stocks)
    })

df = pd.DataFrame(data)
df.to_csv('data/raw/raw_analyst_ratings.csv', index=False)
print("Mock data generated in data/raw/raw_analyst_ratings.csv")
