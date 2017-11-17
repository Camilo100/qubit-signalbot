import websocket
import thread
import time
import json 


def on_message(ws, message):
    print(json.loads(message))

def on_error(ws, error):
    print(json.loads(error))

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send(json.dumps({
    "event":"subscribe",
    "channel":"candles",
    "key":"trade:1m:BTCUSD"
}))



"""
def run(*args):
        for i in range(3):
            time.sleep(1)
            
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())
"""

websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://api.bitfinex.com/ws/2",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close
                            )
ws.on_open = on_open
ws.run_forever()