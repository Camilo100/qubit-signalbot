import data
#import financial_analysis
import telegram_bot as tel

tickers = ["BTC-NEO", "BTC-OMG", "BTC-ADX", "BTC-ARK"]


all_data = data.get(tickers)
descr = all_data.describe()
html =  descr.to_json()

token = '482503768:AAGQufAjZF4zj9cnnqLcNxrgXzc1BUURNak'
chat_id = '413830610'

bot = tel.telegram_bot(token, chat_id)

bot.send(html) #envia texto al id
