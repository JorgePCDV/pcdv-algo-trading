import time
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

key_path = 'D:\\Projects\\pcdv-algo-trading\\1_getting_data\\alpha_vantage_key.txt'

# extracting data for a single ticker
ts = TimeSeries(key=open(key_path, 'r').read(), output_format='pandas')
#data = ts.get_daily(symbol='EURUSD', outputsize='full')[0]
#data.columns = ["open", "high", "low", "close", "volume"]
#data = data.iloc[::-1]

all_tickers = ["AAPL", "MSFT", "CSCO", "AMZN", "GOOG"]
close_prices = pd.DataFrame()
api_call_count = 0
for ticker in all_tickers:
    start_time = time.time()
    data = ts.get_intraday(symbol=ticker, interval='1min', outputsize='full')[0]
    api_call_count += 1
    data.columns = ["open", "high", "low", "close", "volume"]
    data = data.iloc[::-1]
    close_prices[ticker] = data["close"]
    if api_call_count == 5:
        api_call_count = 0
        time.sleep(60 - (time.time() - start_time) % 60)
