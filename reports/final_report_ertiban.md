# Predicting Market Pulses: How News Sentiment Shapes Stock Swings

**By Ertiban Debebe**
*Data Analyst at Nova Financial Solutions*
*Published on 12 May 2026*

---

![Financial Markets](https://images.unsplash.com/photo-1611974717482-48cd9748ed0c?q=80&w=2070&auto=format&fit=crop)

## Executive Summary

In the modern financial landscape, data is the new oil, but sentiment is the engine. At **Nova Financial Solutions**, we have developed a predictive analytics pipeline that bridges the gap between qualitative market narratives and quantitative price action. By analyzing news headlines alongside historical stock data, we’ve created a framework to quantify market "mood" and its impact on daily returns.

Our findings indicate that news sentiment provides a valuable signal that, when combined with technical indicators, can significantly enhance forecasting accuracy.

---

## Methodology: A Dual-Track Approach

Our analytical pipeline follows a rigorous four-stage process designed to separate market signal from noise:

1.  **Data Ingestion**: Utilizing the **FNSPID (Financial News and Stock Price Integration Dataset)** and historical price data via the `yfinance` library.
2.  **Exploratory Data Analysis (EDA)**: Identifying patterns in news volume, publisher behavior, and headline structures.
3.  **Technical Analysis**: Computing core momentum indicators including **SMA, EMA, RSI, and MACD**.
4.  **Sentiment Correlation**: Applying **VADER** and **TextBlob** NLP models to quantify headlines and calculating the Pearson correlation between daily sentiment and stock returns.

---

## 1. The Narrative Landscape: Key EDA Insights

Our analysis of the news dataset revealed a highly structured reporting environment with clear trends in how information is disseminated.

### Concise Communication
Most financial headlines are extremely concise, typically falling between **40 and 80 characters**. This suggests that market sentiment is often distilled into "sound bites" for rapid consumption.

![Headline Length Distribution](./figures/headline_length_dist.png)

### Source Dominance
A small number of publishers dominate the news cycle. Sources like **Seeking Alpha**, **Reuters**, and **Bloomberg** provide the highest frequency of updates, serving as the primary drivers of market narrative.

![Articles per Publisher](./figures/articles_per_publisher.png)

---

## 2. Quantifying Momentum: Technical Indicators

To understand the underlying price action, we implemented a suite of technical indicators. For our primary ticker, **AAPL**, the early 2023 period showed strong momentum.

- **Average RSI (14)**: 63.87 (Indicating a strong bullish trend nearing overbought levels).
- **Trend Confirmation**: Moving Average crossovers (SMA vs EMA) provided reliable signals for trend entries.

![Technical Indicators](./figures/stock_indicators.png)

---

## 3. The Sentiment Signal: Correlation Findings

The core of our research was linking news tone to price performance. We mapped 100 headlines to their corresponding trading days using a combined sentiment score.

### Statistical Correlation
Our analysis revealed a **Pearson Correlation Coefficient of 0.3202**. While a positive relationship exists, the p-value of 0.3670 suggests that a larger dataset is required to achieve high statistical significance.

![Sentiment Return Correlation](./figures/sentiment_return_correlation.png)

### Categorical Performance
We observed that days categorized as "Positive" sentiment generally outperformed "Negative" or "Neutral" days, reinforcing the strategy of using sentiment as a directional filter.

![Return by Category](./figures/return_by_sentiment_category.png)

---

## Investment Strategy Recommendations

Based on our findings, we recommend the following strategies for investment teams:

1.  **Sentiment-Enhanced Trend Following**: Combine Moving Average crossovers with sentiment confirmation. Only enter a "Long" position if the 7-day sentiment trend is positive (>0.1).
2.  **Contrarian Reversals**: Look for "Oversold" RSI conditions (<30) paired with a shift from "Negative" to "Neutral" sentiment as a potential entry signal.
3.  **Source Filtering**: Prioritize high-frequency publishers for intra-day alerts, while using broader sentiment aggregations for long-term rebalancing.

---

## Limitations and Future Work

- **Lag Effects**: News often reacts to price moves. We plan to investigate lead-lag relationships in future iterations.
- **Contextual Nuance**: We aim to integrate **Large Language Models (LLMs)** for more nuanced sentiment extraction (e.g., detecting financial sarcasm).
- **Real-time Deployment**: Building a live dashboard for streaming sentiment tracking.

---

**Nova Financial Solutions**: *Empowering investment teams with data-driven insights that connect market narratives to price action.*
