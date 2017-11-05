from data import *
import datetime
symbol_list = ['WIKI/MSFT', 'WIKI/AAPL', 'WIKI/GOOG']
start_date = datetime.date(2016,10, 10) #raw_input('start_date: ')
event = 2
a = QuandlDataHandler(event, symbol_list, start_date)
for i in range(60):
	a.update_bars()
	print(a.get_latest_bar('WIKI/MSFT'))