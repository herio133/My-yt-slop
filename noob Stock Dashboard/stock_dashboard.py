import altair as alt
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf

# --- CACHE FUNCTIONS ---
@st.cache_data
def fetch_stock_info(symbol):
    stock = yf.Ticker(symbol)
    return stock.info

@st.cache_data
def fetch_quarterly_financials(symbol):
    stock = yf.Ticker(symbol)
    return stock.quarterly_financials.T

@st.cache_data
def fetch_annual_financials(symbol):
    stock = yf.Ticker(symbol)
    return stock.financials.T

@st.cache_data
def fetch_weekly_price(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period='1y', interval='1wk')

# --- APP ---
st.title('📊 Stock Dashboard')

symbol = st.text_input('Enter a stock symbol:', 'AAPL').upper()

try:
    info = fetch_stock_info(symbol)

    st.header('🏢 Company Information')
    st.subheader(f"**Name:** {info.get('longName', 'N/A')}")
    st.subheader(f"**Market Cap:** {info.get('marketCap', 'N/A'):,}")
    st.subheader(f"**Sector:** {info.get('sector', 'N/A')}")

    # Plot stock price using Altair
    st.header("📈 Weekly Stock Prices (1Y)")
    data = fetch_weekly_price(symbol).reset_index()
    chart = (
        alt.Chart(data)
        .mark_line()
        .encode(
            x='Date:T',
            y='Close:Q',
            tooltip=['Date:T', 'Close:Q']
        )
        .interactive()
    )
    st.altair_chart(chart, use_container_width=True)

except Exception as e:
    st.error(f"Error fetching data for {symbol}: {e}")
