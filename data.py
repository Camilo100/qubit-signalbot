#DataReader
#https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question1

import pandas_datareader as pdr
import datetime 
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import urllib2
#import SciPy
import numpy as np





#Le pasas una lista de alts en bittrex y te devuelve los precios historicos por dia
def get(tickers):
  def data(ticker):
  	url = "https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName="+ticker+"&tickInterval=day"
	raw_json = requests.get(url).text
	json_dict = json.loads(raw_json)
	result = pd.DataFrame(json_dict['result'])
	result.set_index('T', inplace=True)
	result.index = pd.to_datetime(result.index)
	return(result)
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))







