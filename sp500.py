import streamlit as st
from datetime import datetime, date, timedelta
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

START = "1900-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('S&P 500 Stock Price Prediction with Linear Regression')

st.markdown(
    "**Disclaimer:** This app is for informational purposes only and should not be used for making investment decisions. Always consult with a qualified financial advisor before making investment choices."
)

sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
sp500_symbols = sp500["Symbol"].tolist()

stocks_input = st.text_input(
    'Enter S&P 500 stock symbols (comma-separated)', ''
)
selected_stocks = [
    symbol.strip().upper()
    for symbol in stocks_input.split(',')
    if symbol.strip() and symbol.strip().upper() in sp500_symbols
]

if not selected_stocks:
    st.warning('Please enter at least one valid S&P 500 stock symbol.')
else:
    min_date = st.date_input(
        'Select a start date', datetime.strptime(START, "%Y-%m-%d")
    )
    max_date = st.date_input(
        'Select an end date', datetime.strptime(TODAY, "%Y-%m-%d")
    )

    years_into_future = st.number_input('Years into the Future', min_value=1, max_value=10, step=1)

    data_load_state = st.text('Loading data...')

    for symbol in selected_stocks:
        data = yf.download(
            symbol,
            min_date.strftime("%Y-%m-%d"),
            max_date.strftime("%Y-%m-%d"),
        )

        st.write(f'{symbol} Historical Stock Prices:')
        st.write(data)

        # Linear regression to predict stock prices
        data['Date'] = np.arange(len(data))  # Use numerical index as X-axis
        X = data[['Date']].values
        y = data['Close'].values

        model = LinearRegression()
        model.fit(X, y)

        future_dates = [max_date + timedelta(days=i) for i in range(1, 365 * years_into_future)]
        future_dates_as_numbers = np.arange(len(data), len(data) + len(future_dates))

        future_prices = model.predict(future_dates_as_numbers.reshape(-1, 1))

        historical_performance_fig = go.Figure()
        historical_performance_fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=f'{symbol} Historical Price'))
        historical_performance_fig.add_trace(go.Scatter(x=future_dates, y=future_prices, mode='lines', name=f'{symbol} Predicted Price'))

        historical_performance_fig.update_layout(
            title=f'Historical and Predicted Performance of {symbol}',
            xaxis_title='Date',
            yaxis_title='Stock Price',
            template='plotly_dark'
        )

        st.plotly_chart(historical_performance_fig)

    data_load_state.text('Loading data... done!')
