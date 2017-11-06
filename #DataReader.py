#DataReader

import pandas_datareader as pdr
import datetime 
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import urllib2

import numpy as np


#https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question1

#neo.to_csv('data/neo_ohlc.csv')
#df = pd.read_csv('data/neo_ohlc.csv', header=0, index_col='Date', parse_dates=True)



def data(ticker):
	for market in ticker:
		url = "https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=BTC-"+market+"&tickInterval=day"
		raw_json = requests.get(url).text
		json_dict = json.loads(raw_json)
		omg = pd.DataFrame(json_dict['result'])
	return (omg)
		#datas = map(pd.DataFrame(json_dict['result']), i)
	#return(pd.concat(datas, keys=ticker, names=['Ticker', 'Date']))





tickers = ["NEO", "OMG"]


lis = data(tickers) 

print lis

#neo.set_index('T', inplace=True)

#neo.index = pd.to_datetime(neo.index)



#print(neo.loc[('2017-10-01'):('2017-11-01')])
"""
# Plot the closing prices for `neo`
neo['C'].plot(grid=True)
#plt.show()

print neo.describe()

print neo.head()

print neo.tail()

# Select only the last 10 observations of `Close`
ts = neo['C'][-10:]

# Check the type of `ts` 
print type(ts)

# Assign `Adj Close` to `daily_close`
daily_close = neo['C']

# Daily returns
# Daily returns
daily_pct_change = daily_close.pct_change()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

# Inspect daily returns
#print(daily_pct_change)

# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)

# Print daily log returns
#print(daily_log_returns)

"""