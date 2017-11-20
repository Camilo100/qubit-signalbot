import requests  
import json
import base64
import hashlib
import hmac
import os
import time 
import talib
import calendar

pares = [
        'tBTCUSD',
        'tETCBTC',
        'tETCUSD',
        'tETHBTC',
        'tETHUSD',
        'tXMRBTC',
        'tXMRUSD',
        'tZECBTC',
        'tZECUSD'
    ]


class BitfinexClient(object):

    BASE_URL = 'https://api.bitfinex.com/'
    #READ KEY='0GPBbZIKwT3Lj9ZZOWbbE39ikVFDVx1yPThlzOX1jsl'
    #READ SECRET= b'cDNVX0Cpslmb2173hv8v06Jio5Lrqfo1EeQ2tXXmf4U'
    KEY='C270gyWZWOyx4i4fskB4fFBMfWGFpKL89Zat2mJqhiY' 
    SECRET= 'UYU0KYWWbGgdVWBaBYLrbWAFqNOpYlQxKX70vAcopJT'
    G_payload = {
           'request':'',
           'nonce':0,
            }   


    def _nonce(self):
       
        return str(int(round(time.time() * 10000)))

    def _headers(self, path, nonce, payload_json):
        #signature = "/api/" + path + nonce + payload_json
        #h = hmac.new(self.SECRET, signature, hashlib.sha384)
        #h = hmac.new(str(self.SECRET).encode('utf-8'), signature.encode('utf-8'), hashlib.sha384)
        bload = str.encode(payload_json, 'utf-8')
        payload = base64.b64encode(bload)
        m = hmac.new(self.SECRET, payload, hashlib.sha384)
        m = m.hexdigest()

        return {
            'X-BFX-APIKEY': self.KEY,
            'X-BFX-PAYLOAD': payload,
            'X-BFX-SIGNATURE': m

            }

    def req(self, path):
 
        nonce= self._nonce()
        self.G_payload['nonce'] = nonce
        self.G_payload['request']=path
        print (self.G_payload)
        payload_json = json.dumps(self.G_payload)

        headers = self._headers(path, nonce, payload_json)
        url = self.BASE_URL + path
        #print(url)
        #print(payload_json)
        #print(headers)
        resp = requests.post(url, data={}, headers=headers)

        #resp = requests.post(url, headers=headers, data=payload_json, verify=True)

        return resp
        
          
    def balances(self):
        
        response = self.req("/v1/balances")
        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''
    
    def trading_fees(self):
        
        response = self.req("/v1/account_infos")
        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''

    def withdrawal_fees(self):

        response = self.req("/v1/account_fees")
        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''

    def deposit_address(self):

        self.G_payload['method']='bitcoin'
        self.G_payload['wallet_name']='exchange' 
        self.G_payload['renew']= 1
        
        response = self.req("/v1/deposit/new")


        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''

    def trade_hist(self, par, tiempo):
        # limite de 50k trades, sin limite https://api.bitfinex.com/v2/trades/tBTCUSD/hist?start=1453322537000&end=1453408937000
        self.G_payload['symbol']=par
        tiempo= time.mktime(time.strptime(tiempo, "%d.%m.%Y %H:%M:%S"))
        self.G_payload['timestamp']= str(tiempo)
        self.G_payload['until']=str(time.time())
        self.G_payload['limit_trades']=50
        self.G_payload['reverse']=0
        response = self.req("/v1/mytrades")

        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''
    
    def new_order(self, ticker, monto, precio, side, tipo):
        self.G_payload['symbol']=ticker
        self.G_payload['amount']=monto
        self.G_payload['price']=precio 
        self.G_payload['exchange']='bitfinex'
        self.G_payload['side']=side 
        self.G_payload['type']=tipo
        response= self.req("/v1/order/new")
        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''
        return ''
    
    def cancel_all_orders(self):

        response=self.req("/v1/order/cancel/all")

        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''
        return ''

    
    def replace_order(self,id,ticker, monto, precio, side, tipo):

        self.G_payload['order_id']=id
        self.G_payload['symbol']=ticker
        self.G_payload['amount']=monto
        self.G_payload['price']=precio 
        self.G_payload['exchange']='bitfinex'
        self.G_payload['side']=side 
        self.G_payload['type']=tipo
        response= self.req("/v1/order/cancer/replace")
        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''
        return ''

    def order_status(self,id):
        self.G_payload['order_id']=id
        response=self.req("/v1/order/status")
        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''
        return ''               

client = BitfinexClient()
print client.withdrawal_fees()
print client.trading_fees()
print client.deposit_address()
print client.new_order('XMRUSD',str(0.01),str(1),'buy','exchange market')
print client.trade_hist('XMRBTC',"10.8.2017 11:05:02")
