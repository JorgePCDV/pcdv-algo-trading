import time

from alpha_vantage.timeseries import TimeSeries
import pandas as pd

key_path = 'D:\\Projects\\pcdv-algo-trading\\1_getting_data\\alpha_vantage_key.txt'

# extracting data for a single ticker
ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')

#data = ts.get_daily(symbol='EURUSD', outputsize='full')[0]
#data.columns = ["open", "high", "low", "close", "volume"]

all_tickers = ["AAPL", "MSFT", "CSCO", "AMZN", "GOOG"]
close_prices = pd.DataFrame()
for ticker in all_tickers:
    start_time = time.time()
    data = ts.get_intraday(symbol=ticker, interval='1min', outputsize='full')[0]
    data.columns = ["open", "high", "low", "close", "volume"]
    close_prices[ticker] = data["close"]

