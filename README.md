# S-P500-Stock-Prediction
Visualisation Application of the S&amp;P 500 Stocks powered by Streamlit.

## Overview
This Streamlit-powered application allows users to visualise and analyse the historical stock price data of S&P 500 companies. It provides an interactive interface to explore price trends, including the option to forecast the stock prices through the use of Linear Regression. The project is developed in Python and utilizes the yFinance library to gather data from Yahoo Finance and Plotly for data visualization.

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/your-username/sp500-stock-prediction.git
   cd sp500-stock-prediction
2. **Create a virtual environment (venv):**

   ```
   python -m venv venv
3. **Activate the virtual environment:**

   On Windows:
   ```
   venv\Scripts\activate
   
   or
   
   source venv/bin/activate
4. **Install the required Python packages:**
   ```
   pip install -r requirements.txt
5. Run the Streamlit app:
   ```
   streamlit run sp500.py
Access the application:
Open your web browser and go to http://localhost:8501 to use the application.

Usage:
Enter S&P 500 stock symbols (comma-separated) in the input field.
Select a custom start and end date for data analysis.
View the historical stock price data and its linear regression in interactive graphs.
Use the provided disclaimer for informational purposes only; always consult a qualified financial advisor before making investment decisions.

