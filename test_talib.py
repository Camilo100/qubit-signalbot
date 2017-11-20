import talib as ta
import pandas as pd
import numpy
import matplotlib.pyplot as plt


btcusd = pd.read_csv("tBTCUSD BITFINEX 15m")

#print(type(btcusd['CLOSE'].values))

real = ta.RSI(btcusd['CLOSE'].values, timeperiod=14)



print real

"""
plt.plot(real, btcusd['MTS'].values)
plt.ylabel('RSI BTCUSD 15m')
plt.show()
"""
"""
close = numpy.random.random(100)
#Calculate a simple moving average of the close prices:

output = talib.SMA(close)
print(output)

print talib.get_functions()

"""