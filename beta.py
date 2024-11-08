import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

def calculate_beta(stock_returns, market_returns):
    # Align the data
    df = pd.DataFrame({'portfolio': stock_returns, 'market': market_returns})
    df = df.dropna()  # Remove any NaN values
    
    if len(df) == 0:
        return None
        
    covariance_matrix = np.cov(df['portfolio'], df['market'])
    beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]
    return beta

st.title('Portfolio Beta Calculator')

# User inputs
tickers = st.text_input('Enter your holdings (comma separated):', 'AAPL, MSFT, GOOG')
market_index = st.text_input('Enter the market index:', 'SPY')
frequency = st.selectbox('Select frequency of returns:', ['Daily', 'Weekly', 'Monthly'])
period = st.selectbox('Select period for data collection:', ['1y', '2y', '5y'])


# Process tickers first
tickers = tickers.split(',')
tickers = [ticker.strip() for ticker in tickers]

# Get shares for each ticker
shares_dict = {}
st.subheader('Enter number of shares for each holding:')
for ticker in tickers:
    shares_dict[ticker] = st.number_input(f'Number of shares for {ticker}:', min_value=1, value=1)

if st.button('Calculate Beta'):
    try:
        if frequency == 'Daily':
            frequency = '1d'
        elif frequency == 'Weekly':
            frequency = '1wk'
        elif frequency == 'Monthly':
            frequency = '1mo'
        else:
            st.error('Invalid frequency selected')
        # Download data
        data = yf.download(tickers + [market_index], period=period, interval=frequency.lower())  # Use first letter of frequency
        # Verify data download
        if data.empty:
            st.error(f"No data received for tickers {tickers} and {market_index}")
            st.stop()
        # Debug info
        # st.write("Data shape:", data.shape)
        # st.write("Date range:", data.index[0], "to", data.index[-1])

        # Calculate market returns
        market_returns = data['Adj Close'][market_index].pct_change().dropna()

        # Calculate weighted portfolio returns
        portfolio_values = pd.DataFrame()
        for ticker in tickers:
            portfolio_values[ticker] = data['Adj Close'][ticker] * shares_dict[ticker]

        total_portfolio = portfolio_values.sum(axis=1)
        portfolio_returns = total_portfolio.pct_change().dropna()

        # Align dates
        common_dates = portfolio_returns.index.intersection(market_returns.index)
        portfolio_returns = portfolio_returns[common_dates]
        market_returns = market_returns[common_dates]

        # Debug info
        # st.write("Number of valid returns:", len(portfolio_returns))

        if len(portfolio_returns) > 0 and len(market_returns) > 0:
            # Calculate beta
            beta = calculate_beta(portfolio_returns, market_returns)
            
            if beta is not None:
                st.write(f'The beta of your portfolio is: {beta:.2f}')
            else:
                st.error('Unable to calculate beta - insufficient data')
    except Exception as e:
        st.error('No valid data available for beta calculation')