#DataReader
#https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question1

#https://github.com/thebotguys/golang-bittrex-api/wiki/Bittrex-API-Reference-(Unofficial)


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

"""
Dos opciones


https://github.com/websocket-client/websocket-client


https://github.com/nlsdfnbch/bitex

BITTREX WEB SOCKET
Those are the 2 messages their websocket publish.
UpdateSummaryState will send you the all the basic ticker information when updates are available.
updateExchangeState will send you the "specific ticker" you subscribed. The push alert includes orderbook changes, filled orders. Check the document I posted above.

"""
#Le pasas una lista de alts en bittrex y te devuelve los precios historicos por dia




"""
CLASE DATOS, sus funciones son:
+interactuar con los servidores de los exchanges y pedirle los datos necesarios.
+darle los datos necesarios a las estrategias, ya sea historicos o ultimos. 
+

"""
class DataHandler():
	pass
"""
	__metaclass__ = ABCMeta

	@abstractmethod
	def get_latest_bars(self, symbol):
        raise NotImplementedError("Should implement get_latest_bars()")

    @abstractmethod
    def update_bars(self):
        raise NotImplementedError("Should implement get_latest_bars()")

"""


#IMPLEMENTAR TODOS LOS METODOS POSIBLES


class bittrex_data(DataHandler):
	def __init__(self):
		self.url = "https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName="
		self.interval = "&tickInterval=day"		#agregar para poder cambiar el dia

	def get(self, tickers):
		self.datas = map (self.data, tickers)
	 	return(pd.concat(self.datas, keys=tickers, names=['Ticker', 'Date']))


	def data(self, ticker):
	  	self.url_full =  self.url + ticker + self.interval
		self.raw_json = requests.get(self.url_full).text
		self.json_dict = json.loads(self.raw_json)
		self.result = pd.DataFrame(self.json_dict['result'])
		self.result.set_index('T', inplace=True)
		self.result.index = pd.to_datetime(self.result.index)
		return(self.result)


"""
bittrex = bittrex_data()
tickers = bittrex.get(["BTC-NEO", "BTC-OMG"])
"""

class bitfinex_data(DataHandler):
	def __init__(self):
		pass

	def get_historical_server(self, ticker, timeframe):
		self.url="https://api.bitfinex.com/v2/candles/trade:"
		self.url_full= self.url+timeframe+":"+ticker+"/hist?&limit=1000"
		#print(self.url_full)
		self.raw_json = requests.get(self.url_full).text
		self.json_dict = json.loads(self.raw_json)
		self.result = pd.DataFrame(self.json_dict, columns=['MTS','OPEN','CLOSE', 'HIGH', 'LOW', 'VOLUME' ])
		self.result.set_index('MTS', inplace=True)
		self.result.index = pd.to_datetime(self.result.index, unit='ms')
		return(self.result)


	def get_lastest(self, ticker):
		self.update_rest(ticker)

		#dar lastest csv


	def update_rest(self, ticker):
		self.url="https://api.bitfinex.com/v2/ticker/"
		self.url_full = self.url + ticker
		self.raw_json = requests.get(self.url_full).text
		self.json_dict = json.loads(self.raw_json)
		self.result = pd.DataFrame(self.json_dict)#, columns=['MTS','OPEN','CLOSE', 'HIGH', 'LOW', 'VOLUME'])
		print(self.result)
		#print(self.json_dict)
		#aNadir al csv


tickers = ["tOMGUSD", "tOMGBTC", "tETHUSD", "tETHBTC"]
bitfinex = bitfinex_data()
#BTCUSD = bitfinex.get_historical_server("tBTCUSD", "3h")
#print(BTCUSD.describe())
#print(BTCUSD.head())
#print(BTCUSD.tail())

#bitfinex.get_lastest("tBTCUSD")
for i in tickers:
	t = bitfinex.get_historical_server(i, "1h")
	name = i + ' BITFINEX 1H'
	t.to_csv(name)

