# News Sentiment Analysis and Stock Price Prediction

This repository contains the work for the 10 Academy Week 1 Challenge: **Predicting Price Moves with News Sentiment**.

## Overview

The goal of this project is to analyze the relationship between financial news headlines and stock price movements. We perform sentiment analysis on news data and correlate it with quantitative technical indicators and daily stock returns.

## Project Structure

- `data/`: Contains raw and processed data.
- `notebooks/`: Jupyter notebooks for EDA, technical analysis, and correlation studies.
- `src/`: Python source code for sentiment analysis and data processing modules.
- `scripts/`: Standalone scripts for automation.
- `tests/`: Unit tests for the project.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd news-sentiment-analysis
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   **Note on TA-Lib:** On Windows, you may need to download the pre-compiled binary from [here](https://github.com/cgohlke/talib-build/releases) or follow specific installation instructions for your platform.

## Tasks

- **Task 1:** Git, GitHub, and Exploratory Data Analysis (EDA).
- **Task 2:** Quantitative analysis using `PyNance` and `TA-Lib`.
- **Task 3:** Correlation between news sentiment and stock movement.
