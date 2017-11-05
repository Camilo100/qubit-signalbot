# data.py

"""
Diference between self.symbol_data = {} ; self.latest_symbol_data = {}

"""
import datetime
import os, os.path
import pandas as pd
import quandl

from abc import ABCMeta, abstractmethod

from event import MarketEvent

quandl.ApiConfig.api_key = "-XmoEyfxpMkr8xqD41hw"

class DataHandler(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_latest_bars(self, symbol):
        raise NotImplementedError("Should implement get_latest_bars()")

    @abstractmethod
    def update_bars(self):
        raise NotImplementedError("Should implement get_latest_bars()")

class QuandlDataHandler(DataHandler):
	def __init__(self, events, symbol_list, date):
		self.events = events
		self.symbol_list = symbol_list
		self.symbol_data = {}
		self.latest_symbol_data = {}
		self.continue_backtest = True
		self.date = date
		self.yieldlist = {}
		self.Quandl()
		self.initYield()



	def initYield(self):
		for s in self.symbol_list:
			self.yieldlist[s] = self._get_new_bar(s)


	def Quandl(self):
		for s in self.symbol_list:
			self.symbol_data[s] = quandl.get(s, returns="pandas", start_date=self.date.isoformat()) #returns last row
			self.latest_symbol_data[s] = []
		#self.date = self.date + datetime.timedelta(days=1)
		
	def get_latest_bars(self, symbol,  N=1):
		try:
			bars_list = self.latest_symbol_data[symbol]
		except KeyError:
			print "That symbol is not available in the historical data set."
		else:
			return bars_list[-N]

	def get_latest_bar_value(self, symbol, val_type):
		try:
			bars_list = self.latest_symbol_data[symbol]
		except KeyError:
			print("That symbol is not available in the historical data set.")
			raise
		else:
			return bars_list[val_type]

#http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python

	def _get_new_bar(self, symbol):
		for row in self.symbol_data[symbol].itertuples():
			yield row



	def update_bars(self):
		for s in self.symbol_list:
			try:
				bar = self.yieldlist[s].next()
			except StopIteration:
				self.continue_backtest = False
			else:
				if bar is not None:
					self.latest_symbol_data[s].append(bar)
		self.events.put(MarketEvent())

