
"""
class financial analysis
sub class daily percentage change
method calculate
method plot??

"""

import pandas_datareader as pdr
import datetime 
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import urllib2
#import SciPy
import numpy as np
from abc import ABCMeta, abstractmethod
import os
import statsmodels.api as sm
import data

class financial_analisys(object):
 	def __init__(self, data):
 		self.data = data
 		#self.daily_percentage_change()


 	def daily_percentage_change(self):
		self.daily_close = self.data[['CLOSE']] 	# Assign `Adj Close` to `daily_close`
		self.daily_pct_change = self.daily_close.pct_change() # Daily returns
		self.daily_pct_change.fillna(0, inplace=True) # Replace NA values with 0
		return (self.daily_pct_change)

	def plot_daily_pct_change(self):
		self.daily_percentage_change().hist(bins=50)
		plt.show()


	def daily_log_returns(self):
		self.daily_log_returns = np.log(self.daily_percentage_change()+1)
		return (self.daily_log_returns)



	def cum_daily_return(self):
		# Calculate the cumulative daily returns
		self.cum_daily_return = (1 + self.daily_percentage_change()).cumprod()
		return(self.cum_daily_return)

	def plot_cum_daily_return(self):
		self.cum_daily_return().plot(figsize=(12,8))
		plt.show()

"""
#no funciona
	def multi_plot(self):
		# Isolate the `Adj Close` values and transform the DataFrame
		daily_close_px = all_data[['C']].reset_index().pivot('Date', 'Ticker', 'C')

		# Calculate the daily percentage change for `daily_close_px`
		daily_pct_change = daily_close_px.pct_change()

		# Plot the distributions
		daily_pct_change.hist(bins=50, sharex=True, figsize=(12,8))

		# Show the resulting plot
		plt.show()

class moving_avg(object): #falta
	def __init__(self, data):
		self.data = data

	def moving_average(self):
		self.adj_close_px = self.data['C']

		# Calculate the moving average
		moving_avg = adj_close_px.rolling(window=40).mean()


	def ():
		pass

"""



bitfinex = data.bitfinex_data()
ticker = 'tBTCUSD'
BTCUSD = bitfinex.get_historical_server(ticker=ticker,  limit='10')
finance = financial_analisys(BTCUSD)
finance.daily_percentage_change()
finance.daily_log_returns()
finance.plot_daily_pct_change()

