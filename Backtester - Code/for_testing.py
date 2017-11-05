from data import *
class Backtest(object):
	#	Enscapsulates the settings and components for carrying out 	an event-driven backtest.
	def __init__(self, symbol_list, data_handler):

		self.symbol_list = symbol_list
		
		self.data_handler_cls = data_handler

		self._generate_trading_instances()

	def _generate_trading_instances(self):
		print("Creating DataHandler, Strategy, Portfolio and ExecutionHandler")
		self.data_handler = self.data_handler_cls(self.symbol_list)
		#self.execution_handler = self.execution_handler_cls(self.events)

symbol_list = ['WIKI/MSFT', 'WIKI/GOOG']
a = Backtest(symbol_list, QuandlDataHandler)
print sape
