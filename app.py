import streamlit as st

st.set_page_config(page_title="AI Stock Analyzer", layout="wide")

st.title("📈 AI Stock Analyzer")
st.write("Analyze stocks using fundamentals, technicals, and AI reasoning.")

symbol = st.text_input("Enter Stock Symbol (Example: AAPL, TSLA)")

if symbol:
    st.success(f"Stock selected: {symbol.upper()}")
