import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ['AMZN','MSFT','FB','GOOG']
start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohlcv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)['Adj Close']

cl_price.fillna(0, inplace=True)
