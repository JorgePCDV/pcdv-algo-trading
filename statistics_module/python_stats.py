import pandas as pd
import pandas_datareader.data as pdr
import datetime

tickers = ['MSFT', 'AMZN', 'AAPL', 'CSCO', 'IBM', 'FB']

close_prices = pd.DataFrame()
attempt = 0
drop = []

while len(tickers) != 0 and attempt <= 5:
    tickers = [j for j in tickers if j not in drop]
    for i in range(len(tickers)):
        try:
            temp = pdr.get_data_yahoo(tickers[i], datetime.date.today() - datetime.timedelta(3650),
                                      datetime.date.today())
            temp.dropna(inplace=True)
            close_prices[tickers[i]] = temp['Adj Close']
            drop.append(tickers[i])
        except:
            print(tickers[i], ' :failed to fetch data...retrying')
    attempt += 1

close_prices.fillna(method='bfill', axis=0, inplace=True)
close_prices.mean()
