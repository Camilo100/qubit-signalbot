import quandl
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import datetime

quandl.ApiConfig.api_key = "-XmoEyfxpMkr8xqD41hw"

date = datetime.date(2016,10, 10)
symbol_list = ['WIKI/MSFT', 'WIKI/AAPL', 'WIKI/GOOG' ]
data = {}
for s in symbol_list:
	data[s] = quandl.get(s, returns="pandas", start_date='2010-12-31')


def gene(symbol):
	for q in data[symbol].itertuples():
		yield(q)
	

"""
f = gene('WIKI/MSFT')
f.next()
f.next()
f.next()
bar = f.next()
print(bar)

"""
f = gene('WIKI/MSFT')
for i in range(60):
	bar = f.next()
	print(bar[4])
"""

for a in data['WIKI/MSFT'].itertuples():
	print(a)

"""

#data.plot()
#plt.show()
