import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    '''
    # Simple stock price app
    Shown are the stock closing price and volume of Google!
    '''
)

trickerSymbol = 'GOOGL'

trickerData = yf.Ticker(trickerSymbol)

trickerDf = trickerData.history(period = 'id', start = '2011-5-31', end = '2021-5-31')

st.line_chart(trickerDf.Close)

st.line_chart(trickerDf.Volume)