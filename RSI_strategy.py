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
import talib as ta
import telegram_bot as tel


class simple_RSI(object):
	def __init__(self, data, telegram, tickers):
		self.data = data
		self.telegram = telegram
		self.tickers = tickers
		self.start()

	def start(self):
		self.bars = self.data.get_historical_server(ticker=self.tickers,  limit='15')
		print(self.bars['CLOSE'].values)
		self.RSI = ta.RSI(self.bars['CLOSE'].values, timeperiod=14)
		self.text = pd.Series(self.RSI).tail(1).to_json(orient='values')
		self.telegram.send_text(self.text)
		print(type(self.text))


token = '482503768:AAGQufAjZF4zj9cnnqLcNxrgXzc1BUURNak'
chat_id = '413830610'
bot = tel.telegram_bot(token, chat_id) #crea el bot de telegram con tu token
bitfinex = data.bitfinex_data()
tickers = 'tBTCUSD'
RSI = simple_RSI(bitfinex, bot, tickers)




