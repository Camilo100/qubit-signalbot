#IMPORT




print raw_input('initial_capital: ')
initial_capital = raw_input('initial_capital: ')
symbol_list = ['WIKI/MSFT', 'WIKI/AAPL', 'WIKI/GOOG']
bars = QuandlDataHandler(symbol_list)
strategy = BuyAndHoldStrategy(bars, event):
port = NaivePortfolio(bars, events, start_date, initial_capital)
#broker = ExecutionHandler()

while True:
    # Update the bars (specific backtest code, as opposed to live trading)
    if bars.continue_backtest == True:
        bars.update_bars()
    else:
        break
    
    # Handle the events
    while True:
        try:
            event = events.get(False)
        except Queue.Empty:
            break
        else:
            if event is not None:
                if event.type == 'MARKET':
                    strategy.calculate_signals(event)
                    port.update_timeindex(event)

                elif event.type == 'SIGNAL':
                    port.update_signal(event)

                elif event.type == 'ORDER':
                    broker.execute_order(event)

                elif event.type == 'FILL':
                    port.update_fill(event)

    # 10-Minute heartbeat
    time.sleep(10*60)