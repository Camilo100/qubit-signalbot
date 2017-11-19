
#https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods




class web_socket(object):
	pass

class ws_bitfinex(web_socket):
	"""docstring for ws_bitfinex"web_socket"""
	def __init__(self, channel, symbol):
		super(ws_bitfinex,web_socket).__init__()
		self.arg = arg


	def listen(self):
		def on_message(ws, message):
    		return(json.loads(message))
		