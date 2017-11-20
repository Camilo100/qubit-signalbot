# Qubit-signalbot

### Como usar el bot de Telegram

```python
import telegram_bot

token = '482503768:AAGQufAjZF4zj9cnnqLcNxrgXzc1BUURNak'
chat_id = '413830610' 
"""
crea el bot de telegram con tu token y chat id 
"""
bot = tel.telegram_bot(token, chat_id)
bot.send_text('Hola')
bot.send_photo(photo_addrs)

```


### Como usar metodo rest bitfinex

```python

tickers = "tBTCUSD"
bitfinex = bitfinex_data()

"""
Trae un pandas con las ultimas 10 velas de la forma OPEN,CLOSE,HIGH,LOW,VOLUME
"""
BTCUSD = bitfinex.get_historical_server(ticker="tBTCUSD", timeframe="15m", limit='10') 

```
