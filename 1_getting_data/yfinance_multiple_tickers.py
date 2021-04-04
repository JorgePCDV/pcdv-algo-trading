import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS"]
end = dt.datetime.today()
start = end - dt.timedelta(30)
cl_price = pd.DataFrame()
ohlcv_data = {}

for ticker in stocks:
    ticker_info = yf.download(ticker, start, end)
    cl_price[ticker] = ticker_info["Adj Close"]
    ohlcv_data[ticker] = ticker_info

print("yfinance multiple tickers script end.")
