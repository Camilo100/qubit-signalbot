"""
The strategy that you will be developing is simple: 
you create two separate Simple Moving Averages (SMA) 
of a time series with differing lookback periods,
lets say, 40 days and 100 days. If the short moving average 
exceeds the long moving average then you go long, if the long 
moving average exceeds the short moving average then you exit.
"""

#https://www.quantstart.com/articles/Backtesting-a-Moving-Average-Crossover-in-Python-with-pandas
import pandas_datareader as pdr
import datetime 
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import urllib2
#import SciPy
import numpy as np
import data


tickers = ["USDT-NEO","USDT-BTC", "USDT-ETH"]
all_data = data.get(tickers)
i = tickers[1]
omg = all_data.loc[i]
# Initialize the short and long windows
short_window = 40
long_window = 100

# Initialize the `signals` DataFrame with the `signal` column
signals = pd.DataFrame(index=omg.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = omg['C'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = omg['C'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)

# Initialize the plot figure
fig = plt.figure()

# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111,  ylabel='Price in $')

# Plot the closing price
omg['C'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')
         
# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')
         
# Show the plot
plt.show()





