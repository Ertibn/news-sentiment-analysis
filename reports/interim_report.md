# Interim Report: Predicting Price Moves with News Sentiment

**Date:** 11 May 2026
**Author:** Antigravity (AI Assistant)
**Organization:** Nova Financial Solutions

## 1. Summary of Data Loading and Cleaning

For this interim phase, we focused on setting up the analytical pipeline and conducting initial exploratory analysis on the Financial News and Stock Price Integration Dataset (FNSPID) and historical stock data.

- **News Dataset:** We loaded a subset of the FNSPID data containing headlines, stock symbols, and publication dates.
- **Cleaning:**
    - Handled date-time formatting to ensure consistency across datasets.
    - Checked for missing values in headlines and stock symbols (none found in the sample).
    - Normalized stock symbols to uppercase.
- **Stock Data:** Historical price data for major tickers (e.g., AAPL) was fetched using the `yfinance` library, covering the early 2023 period.

## 2. Key EDA Findings

Our initial exploratory data analysis revealed several interesting patterns:

- **Headline Length:** The majority of news headlines are between 40 and 80 characters long, indicating a concise style typical of financial reporting.
- **Publisher Activity:** Sources like Reuters and Bloomberg were identified as highly active, providing the bulk of the news volume.
- **News Volume:** We observed spikes in news volume on certain days, which we plan to correlate with specific market events (e.g., earnings releases or economic announcements).
- **Stock Coverage:** The dataset provides broad coverage across major S&P 500 companies, allowing for diverse ticker-based analysis.

## 3. Initial Stock Price Analysis (Technical Indicators)

We implemented several core technical indicators to characterize stock price behavior:

- **Moving Averages:** Simple Moving Average (SMA) and Exponential Moving Average (EMA) were calculated to identify trend direction.
- **Relative Strength Index (RSI):** Used to identify overbought (>70) and oversold (<30) conditions.
- **MACD:** Computed to detect momentum shifts and trend reversals.

Initial visualizations show a clear relationship between the Moving Averages and price trends, providing a baseline for quantitative analysis.

## 4. Challenges Encountered

- **Environment Setup:** Installing `TA-Lib` on Windows proved challenging due to C++ dependency requirements. We implemented manual versions of the indicators using `pandas` to ensure progress while working on a robust installation solution.
- **Data Volume:** The full FNSPID dataset is massive. Efficient sampling and data loading strategies are necessary for the final phase.

## 5. Plans for Final Submission

- **Sentiment Analysis:** Apply NLTK VADER and TextBlob to assign sentiment scores to all headlines.
- **Correlation Study:** Calculate the Pearson correlation between sentiment scores and daily returns.
- **Aggregated Insights:** Group sentiment by day and analyze the impact on the next day's opening/closing price.
- **Final Report:** Create a publication-quality Medium-style blog post summarizing the strategy.
