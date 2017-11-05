import data
import datetime



class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


class Complex(MyClass):
     def __init__(self, date):
         self.date2 = date
         print self.date2.isoformat()


class test:
	def __init__(self, QuandlDataHandler):
		#self.Complex_cls = Complex
		symbol_list = ['WIKI/MSFT', 'WIKI/GOOG']
		bars = QuandlDataHandler(symbol_list)


mydate = datetime.date(1943,3, 13)  #year, month, day
a = Complex(mydate)
mydate = mydate + datetime.timedelta(days=1)



