# https://analyticsindiamag.com/hands-on-guide-to-using-yfinance-api-in-python/

# 1) Display some random ticker data and graph
# 2) Display line graph
# 3) Add horizontal line at given price
# 4) Write a function that auto-finds Support/Ressistance (SR) lines
#	  a. Study how to find SR by hand
#	  b. 
# 5) Given a list of SR lines identify a kangaroo tail (KT) trade
#	  a. Study how to find KT 
#	  b. Write down logic 
import yfinance as yf
import plotly.graph_objects as go

def make_candle(ticker,start,end,interval):	# ALL STRINGS
  stock = yf.Ticker(ticker).history(start=start, end=end, interval=interval).reset_index()
  for i in ['Open', 'High', 'Close', 'Low']:   # convert data to float64
      stock[i]  =  stock[i].astype('float64')
  fig = go.Figure(data=[go.Candlestick(x=stock['Date'],
	    open=stock['Open'],
	    high=stock['High'],
	    low=stock['Low'],
	    close=stock['Close'])])
  return fig

def make_line(ticker,start,end,interval):
  stock = yf.Ticker(ticker).history(start=start, end=end, interval=interval).reset_index()
  for i in ['Close']:   # convert data to float64
    stock[i]  =  stock[i].astype('float64')
  fig = go.Figure(data=[go.Scatter(x=stock['Date'],y=stock['Close'])])
  return fig

#-------------------------------

start = "2016-01-01"
end = "2017-01-01"
ticker = 'MSFT'
interval = '1d'

sr = [44.5,46.44,48.35,49.95,52.00,52.96,53.77,56.82]

#fig = make_line(ticker,start,end,interval)
fig = make_candle(ticker,start,end,interval)
for s in range(len(sr)):
  fig.add_hline(y=sr[s], line_dash="dash", line_width=1, line_color='purple')

fig.layout.plot_bgcolor = '#0e1215'
fig.show()

'''
msft = yf.Ticker("MSFT").history(start=start, end=end, interval='1mo')
#Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

msft = msft.reset_index()   # pd function to add column of sequential indices in front

for i in ['Open', 'High', 'Close', 'Low']:   # convert data to float64
      msft[i]  =  msft[i].astype('float64')

fig = go.Figure(data=[go.Candlestick(x=msft['Date'],
	open=msft['Open'],
	high=msft['High'],
	low=msft['Low'],
	close=msft['Close'])])

fig.layout.plot_bgcolor = '#0e1215'
fig.show()
'''