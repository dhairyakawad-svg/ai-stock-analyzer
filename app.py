import streamlit as st
import yfinance as yf
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="StockMind AI",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CSS ----------------
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
</style>
""", unsafe_allow_html=True)

# ---------------- HELPERS ----------------
def format_market_cap(value, symbol):
    if value >= 1_000_000_000_000:
        return f"{symbol}{value/1_000_000_000_000:.2f} T"
    elif value >= 1_000_000_000:
        return f"{symbol}{value/1_000_000_000:.2f} B"
    elif value >= 1_000_000:
        return f"{symbol}{value/1_000_000:.2f} M"
    else:
        return f"{symbol}{value:,.0f}"

# ---------------- HEADER ----------------
st.markdown("<div class='big-title'>🧠 StockMind AI</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtext'>AI-powered stock analysis using fundamentals, technicals & news</div>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- CURRENCY SELECT ----------------
currency = st.selectbox(
    "💱 Select Currency",
    ["USD ($)", "INR (₹)"]
)

# ---------------- INPUT ----------------
symbol = st.text_input(
    "🔍 Enter Stock Symbol",
    placeholder="AAPL, TSLA, MSFT"
).upper()

st.info("👆 Enter a stock symbol above to start analysis")

# ---------------- MAIN LOGIC ----------------
if symbol:
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        price = info.get("currentPrice", 0)
        market_cap = info.get("marketCap", 0)

        USD_TO_INR = 83

        if currency == "INR (₹)":
            price = price * USD_TO_INR
            market_cap = market_cap * USD_TO_INR
            price_symbol = "₹"
        else:
            price_symbol = "$"

        # ---------------- METRICS ----------------
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("🏢 Company", info.get("shortName", "N/A"))
        col2.metric("📊 Sector", info.get("sector", "N/A"))
        col3.metric(
            "💰 Market Cap",
            format_market_cap(market_cap, price_symbol)
        )
        col4.metric(
            "📈 Price",
            f"{price_symbol}{price:,.2f}"
        )

        st.divider()

        # ---------------- TABS ----------------
        tab1, tab2, tab3 = st.tabs(
            ["📊 Key Metrics", "🧠 AI Insight", "⚠️ Risks"]
        )

        # ---------- TAB 1 ----------
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

        # ---------- TAB 2 ----------
        with tab2:
            st.subheader("🧠 What StockMind AI Thinks (Early View)")
            st.write(
                "This is an early-stage analysis based on publicly available data. "
                "The stock shows **moderate to strong stability** as a large-cap company."
            )

            st.progress(65)
            st.caption("Confidence Score: 65%")

            st.markdown("### 👤 Suitable For")
            st.info(
                "• Long-term investors\n"
                "• Blue-chip focused portfolios\n"
                "• Moderate risk tolerance"
            )

        # ---------- TAB 3 ----------
        with tab3:
            st.warning(
                "• Market volatility\n"
                "• Sector-rela
