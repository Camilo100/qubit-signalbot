import requests  
import json
import base64
import hashlib
import hmac
import os
import time 
import talib

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
    KEY='0GPBbZIKwT3Lj9ZZOWbbE39ikVFDVx1yPThlzOX1jsl'
    SECRET= b'cDNVX0Cpslmb2173hv8v06Jio5Lrqfo1EeQ2tXXmf4U'

    G_payload = {
           'request':'',
           'nonce':0,
           #'options':{}
           #'method':'bitcoin',
           #'wallet_name':'exchange'
            }   
# payload = { 
#            'request':'/v1/order/new',
#            'nonce':time.time(),
#            'options' : {'symbol':'btcusd',
#             'amount':'100.00000000',
#             'price':'1.00',
#             'exchange':'bitfinex',
#             'side':'buy',
#             'type':'limit'}
#            }

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
        print(url)
        print(payload_json)
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

    def trade_hist(self):
        response = self.req("/v1/mytrades")
        G_payload['symbol']='tBTCUSD'
        G_payload['timestamp']='10/05/2017'
        G_payload['until']='11/17/2017'
        G_payload['limit_trades']=50
        G_payload['reverse']=0
        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''
    
    def new_order(self):
        return ''
     

    

client = BitfinexClient()
print client.balances()
print client.trading_fees()
#print client.trade_hist()
print client.deposit_address()
'''
print client.active_orders()
print client.wallets()
print client.order_hist()

'''