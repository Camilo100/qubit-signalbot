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

### Como hacer analisis financieros sobre los datos (ALPHA)

La clase financial_analisys posee diferentes metodos para realizar analisis financieros sobre datos. Al inicializar la clase debemos darle un objeto pandas con la columna CLOSE. Los diferentes metedos que podemos usar son:


+ daily_percentage_change(): devuelve un numpy array con los cambios diarios. (ESTO DEBE SER MEJORADOS PARA CALCULAR PARA CUALQUIER NUMERO DE DIAS)
+ daily_log_returns(): devuelve un numypy array con los retornos logaritmicos.
+ plot_daily_pct_change(): 

### Como usar metodo rest publico de bitfinex

```python

ticker = "tBTCUSD"
bitfinex = bitfinex_data()

"""
Trae un pandas con las ultimas 10 velas de la forma OPEN,CLOSE,HIGH,LOW,VOLUME
"""
BTCUSD = bitfinex.get_historical_server(ticker=ticker, timeframe="15m", limit='10')

"""
Ultima vela
"""
BTCUSD = bitfinex.get_lastest(ticker=ticker, timeframe="15m")

```

### Como usar ExecutionHandler

```python

rex=BittrexClient()
finex=BitfinexClient()

#Las ordenes en cada exchange piden distintos argumentos y no estan todas las funciones en ambos.Fix en proximo commit

''' 
Finex:
balances,trading_fees, withdrawal_fees, deposit_address, trade_hist, new_order, cancel_order, cancel_all_orders, replace_order, order_status, active_orders
'''

''' Bittrex: 
buy_limit,sell_limit, cancel_order, open_orders, balances, balance_moneda, deposit_address, withdraw, get_order, get_order_history,
get_withdrawal_history, get_deposit_history
```
#EJ: si se puede enviar la order (saldo suficiente, montos permitidos,etc) devuelve un JSON con el id de la orden,simbolo,mercado,etc.
#Si no imprime el codigo de error y la aclaracion

orden=finex.new_order('XMRUSD',0.01,1,'buy','exchange market')


### Como usar RSI strategy (BETA)
Esta estrategia (por el momento) envia señales usando el telegram bot, cuando el RSI de un ticker (o una lista de ellos) llega a un nivel deseado. Hay que inicializar el data handler y el telegram bot. 

```python

token = '482503768:AAGQufAjZF4zj9cnnqLcNxrgXzc1BUURNak'
chat_id = '413830610'
bot = tel.telegram_bot(token, chat_id) #crea el bot de telegram con tu token
bitfinex = data.bitfinex_data()
tickers = 'tBTCUSD'
RSI = simple_RSI(bitfinex, bot, tickers, 15, 75)

```

### Como hacer backtest (ALPHA)

### Como ejecutar en tiempo real (ALPHA)




###### Documentacion para este formato: (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
