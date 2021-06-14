# https://analyticsindiamag.com/hands-on-guide-to-using-yfinance-api-in-python/

# Goal: Display some random ticker data
import yfinance as yf
import plotly.graph_objects as go

apple = yf.Ticker('aapl')
old = apple.history(start="2015-01-01", end="2015-12-31")
#print(old.head())

old = old.reset_index()   # pd function to add column of sequential indices in front
#print(old.head())

for i in ['Open', 'High', 'Close', 'Low']:   # convert data to float64
      old[i]  =  old[i].astype('float64')

fig = go.Figure(data=[go.Candlestick(x=old['Date'],
	open=old['Open'],
	high=old['High'],
	low=old['Low'],
	close=old['Close'])])

fig.layout.plot_bgcolor = '#0e1215'

fig.show()
