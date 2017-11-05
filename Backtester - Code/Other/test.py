from __future__ import (absolute_import, division, print_function, unicode_literals)
import backtrader as bt
import backtrader.feeds as btfeed
import os.path


class TestStrategy(bt.Strategy):
	def log(self, txt, dt=None):
	
		dt = dt or self.datas[0].datetime.date(0)
		print('%s, %s' % (dt.isoformat(), txt))
	def __init__(self):
	# Keep a reference to the "close" line in the data[0] dataseries
		self.dataclose = self.datas[0].close
	def next(self):
	# Simply log the closing price of the series from the reference
		self.log('Close, %.2f' % self.dataclose[0])
		if self.dataclose[0] < self.dataclose[-1]:
			if self.dataclose[-1] < self.dataclose[-2]:
				self.log('BUY CREATE, %.2f' % self.dataclose[0])
				self.buy()
			

if __name__ == '__main__':

	cerebro = bt.Cerebro()

	data = bt.feeds.YahooFinanceCSVData(dataname='table.csv')
	
	cerebro.addstrategy(TestStrategy)

	cerebro.adddata(data)
	cerebro.broker.setcash(100000.0)
	print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
	cerebro.run()
	print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
		# Datas are in a subfolder of the samples. Need to find where the script is
	# because it could have been called from anywhere
		
