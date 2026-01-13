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
    color: #b0b0b0;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='big-title'>🧠 StockMind AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>AI-powered stock ana
