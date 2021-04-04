import yfinance as yf

data_period = yf.download("MSFT", period="6mo")
data_interval = yf.download("MSFT", start="2019-01-01", end="2021-01-01")
data_granularity = yf.download("MSFT", period="1mo", interval="5m")

print("yfinance script end.")
