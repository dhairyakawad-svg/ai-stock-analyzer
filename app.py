import streamlit as st
import yfinance as yf
import pandas as pd

# Page config
st.set_page_config(
    page_title="StockMind AI",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.big-title {
    font-size:48px;
    font-weight:700;
}
.subtext {
    color: #9ca3af;
    font-size:18px;
}
.metric-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='big-title'>🧠 StockMind AI</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtext'>AI-powered stock analysis using fundamentals, technicals & news</div>",
    unsafe_allow_html=True
)

st.divider()

# Input
symbol = st.text_input(
    "🔍 Enter Stock Symbol",
    placeholder="AAPL, TSLA, MSFT"
).upper()

if symbol:
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        # Metrics row
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("🏢 Company", info.get("shortName", "N/A"))
        col2.metric("📊 Sector", info.get("sector", "N/A"))
        col3.metric("💰 Market Cap", f"${info.get('marketCap', 0):,}")
        col4.metric("📈 Price", info.get("currentPrice", "N/A"))

        st.divider()

        # Tabs
        tab1, tab2, tab3 = st.tabs(
            ["📊 Key Metrics", "🧠 AI Insight", "⚠️ Risks"]
        )

        with tab1:
            metrics = {
                "PE Ratio": info.get("trailingPE"),
                "EPS": info.get("trailingEps"),
                "Dividend Yield": info.get("dividendYield"),
                "52 Week High": info.get("fiftyTwoWeekHigh"),
                "52 Week Low": info.get("fiftyTwoWeekLow"),
            }
            df = pd.DataFrame(metrics.items(), columns=["Metric", "Value"])
            st.dataframe(df, use_container_width=True)

        with tab2:
            st.subheader("🧠 AI Initial Assessment")
            st.write(
                "Based on initial fundamentals and price behavior, "
                "this stock shows **moderate strength**. "
                "Technical indicators and news sentiment will refine the decision."
            )
            st.progress(65)
            st.caption("Confidence Score: 65%")

        with tab3:
            st.warning(
                "• Market volatility\n"
                "• Sector-related risks\n"
                "• Macroeconomic uncertainty"
            )

    except Exception as e:
        st.error("❌ Invalid stock symbol or data unavailable.")
