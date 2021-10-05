# https://python.plainenglish.io/python-how-to-get-live-forex-data-in-less-than-3-lines-of-code-bdd94022f987

import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

data = yf.download(tickers = 'JPYAUD=X' ,period ='1d', interval = '15m')

fig = go.Figure(data=[go.Candlestick(x=data.index,
    open=data['Open'], high=data['High'],
    low=data['Low'], close=data['Close'], 
    name = 'market data')])

fig.update_layout(title='Japanese Yen/Australian Dollar')
fig.show()