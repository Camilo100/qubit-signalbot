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
"""
neo = pdr.get_data_yahoo('neo', 
                          start=datetime.datetime(2006, 10, 1), 
                          end=datetime.datetime(2012, 1, 1))
"""
market = "NEO"
url = "https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=BTC-"+market+"&tickInterval=day"
raw_json = requests.get(url).text
json_dict = json.loads(raw_json)
neo = pd.DataFrame(json_dict['result'])

neo.set_index('T', inplace=True)

neo.index = neo.index.to_datetime()



"""
#print(neo.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())

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
"""

# Assign `Adj Close` to `daily_close`
daily_close = neo['C']

# Daily returns
# Daily returns
daily_pct_change = daily_close.pct_change()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

# Inspect daily returns
print(daily_pct_change)

# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)

# Print daily log returns
print(daily_log_returns)