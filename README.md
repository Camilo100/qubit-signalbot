# Qubit-signalbot




##DataHandler
The DataHandler is an abstract base class (ABC) that presents an interface for handling both historical or live market data. This provides significant flexibility as the Strategy and Portfolio modules can thus be reused between both approaches. 

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

##Strategy
The Strategy is also an ABC that presents an interface for taking market data and generating corresponding SignalEvents, which are ultimately utilised by the Portfolio object. A SignalEvent contains a ticker symbol, a direction (LONG or SHORT) and a timestamp.

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

##Portfolio
### Como usar el bot de Telegram
Falta integrar con el execution handler. 

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
##Financial Analisys
### Como hacer analisis financieros sobre los datos (ALPHA)

La clase financial_analisys posee diferentes metodos para realizar analisis financieros sobre datos. Al inicializar la clase debemos darle un objeto pandas con la columna CLOSE. Los diferentes metedos que podemos usar son:


+ daily_percentage_change(): devuelve un numpy array con los cambios diarios. (ESTO DEBE SER MEJORADOS PARA CALCULAR PARA CUALQUIER NUMERO DE DIAS)
+ daily_log_returns(): devuelve un numypy array con los retornos logaritmicos.
+ plot_daily_pct_change(): 

##ExecutionHandler
The ExecutionHandler simulates a connection to a brokerage. The job of the handler is to take OrderEvents from the Queue and execute them, either via a simulated approach or an actual connection to a liver brokerage. Once orders are executed the handler creates FillEvents, which describe what was actually transacted, including fees, commission and slippage (if modelled).

### Como usar ExecutionHandler

```python

rex=BittrexClient()
finex=BitfinexClient()

orden=finex.new_order('XMRUSD',0.01,1,'buy','exchange market')
#Devuelve un JSON con el id de la orden,simbolo,mercado,etc.
#Si hay un error (i.e falta saldo) imprime el cod y la aclaracion

orden=rex.buy_limit('BTC-LTC',0.001, 500)
#Devuelve un JSON con el resultado, aclaracion y un booleano
```

Las ordenes en cada exchange piden distintos argumentos y no estan todas las funciones en ambos.
Fix en proximo commit.
 
**Funciones:**

1. **Finex:**

* balances
* trading_fees
* withdrawal_fees
* deposit_address
* trade_hist
* new_order
* cancel_order 
* cancel_all_orders
* replace_order
* order_status
* active_orders

2. **Bittrex:** 
* buy_limit
* sell_limit
* cancel_order
* open_orders
* balances
* balance_moneda 
* deposit_address
* withdraw
* get_order
* get_order_history
* get_withdrawal_history
* get_deposit_history



##Backtest
### Como hacer backtest (ALPHA)

##Live
### Como ejecutar en tiempo real (ALPHA)




## Documentacion

+ Formateo del readme: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
+ Tutorial basico: https://www.datacamp.com/community/tutorials/finance-python-trading#financialanalyses
+ Tutorial avanzado: https://www.quantstart.com/articles/Event-Driven-Backtesting-with-Python-Part-I
