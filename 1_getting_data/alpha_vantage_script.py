from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='API_KEY')
data, meta_data = ts.get_intraday('GOOGL')
