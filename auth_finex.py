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
    #read onlys de mi cuenta
    BASE_URL = "https://api.bitfinex.com/"
    KEY="0GPBbZIKwT3Lj9ZZOWbbE39ikVFDVx1yPThlzOX1jsl"
    SECRET="cDNVX0Cpslmb2173hv8v06Jio5Lrqfo1EeQ2tXXmf4U"

    def _nonce(self):
        """
        Returns a nonce
        Used in authentication
        """
        return str(int(round(time.time() * 10000)))

    def _headers(self, path, nonce, body):
        signature = "/api/" + path + nonce + body
        #h = hmac.new(self.SECRET, signature, hashlib.sha384)
        h = hmac.new(str(self.SECRET).encode('utf-8'), signature.encode('utf-8'), hashlib.sha384)
        signature = h.hexdigest()
        return {
            "bfx-nonce": nonce,
            "bfx-apikey": self.KEY,
            "bfx-signature": signature,
            "content-type": "application/json"
        }

    def req(self, path, params = {}):
        nonce = self._nonce()
        body = params
        rawBody = json.dumps(body)
        headers = self._headers(path, nonce, rawBody)
        url = self.BASE_URL + path
        resp = requests.post(url, headers=headers, data=rawBody, verify=True)
        return resp
        
    def active_orders(self):
        
        response = self.req("v2/auth/r/orders")
        if response.status_code == 200:
          return response.json()
        else:
          print response.status_code
          print response
          return ''
    
    def wallets(self):
        
        response = self.req("v2/auth/r/wallets")
        if response.status_code == 200:
          return response.json()
        else:
          print response.status_code
          print response
          return ''

    def order_hist(self):
        response= self.req("v2/auth/r/orders/tBTCUSD/hist/")
        if response.status_code == 200: 
            return response.json()
        else:
            print response.status_code
            print response
            return ''


client = BitfinexClient()
print client.active_orders()
print client.wallets()
print client.order_hist()
