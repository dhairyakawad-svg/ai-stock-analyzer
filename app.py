import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="AI Stock Analyzer", layout="wide")

st.title("📈 AI Stock Analyzer")
st.write("Analyze stocks using fundamentals, technicals, and AI reasoning.")

symbol = st.text_input("Enter Stock Symbol (Example: AAPL, TSLA)").upper()

if symbol:
    stock = yf.Ticker(symbol)

    try:
        info = stock.info

        col1, col2, col3 = st.columns(3)

        col1.metric("Company", info.get("shortName", "N/A"))
        col2.metric("Sector", info.get("sector", "N/A"))
        col3.metric("Market Cap", f"${info.get('marketCap', 0):,}")

        st.subheader("📊 Key Metrics")

        metrics = {
            "Current Price": info.get("currentPrice"),
            "PE Ratio": info.get("trailingPE"),
            "EPS": info.get("trailingEps"),
            "Dividend Yield": info.get("dividendYield"),
            "52 Week High": info.get("fiftyTwoWeekHigh"),
            "52 Week Low": info.get("fiftyTwoWeekLow"),
        }

        metrics_df = pd.DataFrame(metrics.items(), columns=["Metric", "Value"])
        st.table(metrics_df)

    except Exception as e:
        st.error("Invalid stock symbol or data unavailable.")
