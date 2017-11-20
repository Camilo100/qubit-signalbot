
#https://wkhtmltopdf.org/downloads.html

import data
#import financial_analysis
import telegram_bot as tel
import talib


"""

tickers = ["BTC-NEO", "BTC-OMG", "BTC-ADX", "BTC-ARK"]
token = '482503768:AAGQufAjZF4zj9cnnqLcNxrgXzc1BUURNak'
chat_id = '413830610'


all_data = data.get(tickers) #le pasas lista de tickers y te devuelve un dataframe

bot = tel.telegram_bot(token, chat_id) #crea el bot de telegram con tu token

i = "BTC-NEO"
all_data.loc[i]['C'].plot(grid=True, legend= True, title=i) #plotea 
photo_addrs = i +'.png'
data.plt.savefig(photo_addrs) # guarda el plot

bot.send_photo(photo_addrs) # lo envia





"""
for i in tickers:
 	all_data.loc[i]['C'].plot(grid=True, legend= True, title=i)
 	photo_addrs = i +'.png'
 	data.plt.savefig(photo_addrs)
	bot.send_photo(photo_addrs) #envia texto al id 	
"""
"""
all_data['C'].plot(grid=True, , title="BTC-ADX", x=['Date'])

# Show the plot

"""

"""



"""

#descr = all_data.describe()

#html =  descr.to_html('test2.html')





bot.send_photo(photo_addrs) #envia texto al id
"""