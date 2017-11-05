symbol_list = ['WIKI/MSFT', 'WIKI/AAPL', 'WIKI/GOOG' ]
d = dict( (k,v) for k, v in [(s, 0) for s in symbol_list] )
d['datetime'] = 'pato'
print(d)