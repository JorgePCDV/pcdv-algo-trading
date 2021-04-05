import pandas as pd
from yahoofinancials import YahooFinancials
import datetime

all_tickers = ["AAPL", "MSFT", "CSCO", "AMZN", "INTC"]
ticker = "MSFT"

close_prices = pd.DataFrame()
end_date = (datetime.date.today()).strftime("%Y-%m-%d")
start_date = (datetime.date.today()-datetime.timedelta(365)).strftime("%Y-%m-%d")
for ticker in all_tickers:
    yahoo_financials = YahooFinancials(ticker)
    json_obj = yahoo_financials.get_historical_price_data(start_date,end_date,"daily")
    ohlv = json_obj[ticker]["prices"]
    temp = pd.DataFrame(ohlv)[["formatted_date","adjclose"]]
    temp.set_index("formatted_date", inplace=True)
    temp.dropna(inplace=True)
    close_prices[ticker] = temp["adjclose"]
print("yahoo financials script end.")