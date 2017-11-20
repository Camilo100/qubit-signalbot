import requests  
import json
import base64
import hashlib
import hmac
import os
import time 
from decimal import Decimal
import urllib
import urllib2

#import talib
#import calendar
#import numpy

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


class ExecutionHandler():
    pass

class BitfinexClient(ExecutionHandler):

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
        self.G_payload['amount']=str(monto)
        self.G_payload['price']=str(precio) 
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

    def cancel_order(self,id):
        self.G_payload['order_id']=id
        responde=self.req("/v1/order/cancel")
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

    def active_orders(self):
        responde=self.req("/v1/orders")          
        if response.status_code == 200:
          return response.json()
        else:
            print ("Codigo "+str(response.status_code))
            print (" respuesta "+str(response.content))
            return ''
        return ''


#https://github.com/ppm0/bittrex3/blob/master/bittrex3/bittrex3.py

class BittrexClient():

   
    market_set = ['getopenorders', 'cancel', 'sellmarket', 'selllimit', 'buymarket', 'buylimit']

    account_set = ['getbalances', 'getbalance', 'getdepositaddress', 'withdraw', 'getorder', 'getorderhistory',
                'getwithdrawalhistory', 'getdeposithistory']


    KEY='83d99f2465a049199707e3e2fecde762'
    SECRET='2c3dfee28bbe483bb64e8531a8f19672'

    def req(self, method, options=None):
        """
        Queries Bittrex with given method and options
        :param method: Query method for getting info
        :type method: str
        :param options: Extra options for query
        :type options: dict
        :return: JSON response from Bittrex
        :rtype : dict
        """
        if not options:
            options = {}

        nonce = str(int(time.time() * 1000))
        base_url = 'https://bittrex.com/api/v1.1/%s/'
        request_url = ''
        '''
        if method in self.public_set:
            request_url = (base_url % 'public') + method + '?'
        '''
        if method in self.market_set:
            request_url = (base_url % 'market') + method + '?apikey=' + self.KEY + "&nonce=" + nonce + '&'
        elif method in self.account_set:
            request_url = (base_url % 'account') + method + '?apikey=' + self.KEY + "&nonce=" + nonce + '&'

        request_url += urllib.urlencode(options)

        signature = hmac.new(self.SECRET.encode(), request_url.encode(), hashlib.sha512).hexdigest()

        headers = {"apisign": signature}
        print request_url
        print headers
        sresponse = requests.get(request_url, headers=headers).content.decode('utf-8')
        return json.loads(sresponse, parse_float=Decimal, parse_int=Decimal)
    

    def buy_limit(self, market, quantity, rate):
        
        opt={'market': market, 'quantity': quantity, 'rate': rate}
        return self.req('buylimit',opt)

    def sell_limit(self, market, quantity, rate):

        opt={'market': market, 'quantity': quantity, 'rate': rate}
        return self.req('selllimit',opt)

    def cancel_order(self, uuid):
        #ID de la orden
        uuid={'uuid': uuid}
        return self.req('cancel', uuid)

    def open_orders(self, market):
        market ={'market': market}
        return self.req('getopenorders',market)

    def balances(self):
        return self.req('getbalances', {})

    def balance_moneda(self, currency):
        
        currency={'currency':currency}
        return self.req('getbalance', currency)

    def deposit_address(self,currency):
    
        currency={'currency':currency}
        print currency
        return self.req('getdepositaddress',currency)
    
    def withdraw(self, currency, quantity, address):
        
        withdraw={'currency': currency, 'quantity': quantity, 'address': address}
        return self.req('withdraw',withdraw )

    def get_order(self, uuid):
        
        uuid={'uuid': uuid}
        return self.req('getorder', uuid)

    def get_order_history(self, market=""):
        
        market={'market': market}
        return self.req('getorderhistory',market)

    def get_withdrawal_history(self, currency=""):
       
        withdraw={'currency': currency}

        return self.req('getwithdrawalhistory', withdraw)

    def get_deposit_history(self, currency=""):
        
        withdraw={'currency': currency}
        return self.req('getdeposithistory', withdraw)        

rex=BittrexClient()
print(rex.deposit_address('BTC'))
print (rex.buy_limit('BTC-LTC',0.001, 500))

client = BitfinexClient()
print client.withdrawal_fees()
print client.trading_fees()
print client.deposit_address()
print client.new_order('XMRUSD',0.01,1,'buy','exchange market')
print client.trade_hist('XMRBTC',"10.8.2017 11:05:02")
