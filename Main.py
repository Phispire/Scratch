import datetime
import time
import requests
#import tkinter as tk
#from coinbase.wallet.client import Client


#Initialize wallet client from coinbase package
#client = Client(api_key, api_secret)
#fills = client.get_orders()



#Define ticker class of functions for different currency pairs.
class TICKERS:
    @classmethod
    def LTC_Ticker(self):
        global LT_TICKER
        global LTC_price
        global LTC_side
        LT_TICKER = requests.get("https://api.gdax.com/products/LTC-USD/trades")
        LTC_price = str("%.2f" % float(LT_TICKER.json()[0]['price']))
        LTC_side = str(LT_TICKER.json()[0]['side'])

    @classmethod
    def BCH_Ticker(self):
        global BC_TICKER
        global BCH_price
        global BCH_side
        BC_TICKER = requests.get("https://api.gdax.com/products/LTC-USD/trades")
        BCH_price = str("%.2f" % float(LT_TICKER.json()[0]['price']))
        BCH_side = str(LT_TICKER.json()[0]['side'])

#Define functions (for testing) such as order making and accounting.
class Market:

    #Define fake accounts for testing.
    LTC_account = 100
    Open_Buys = []
    Open_Sells = []

    #Define a "Buy" function.  Update list of outstanding Buy transactions and USD account value.
    @classmethod
    def Buy(self):
        file = open("USDAccount", "r")
        USDaccount = float(file.read())
        file.close()
        print("Buy $",.1*USDaccount, "at ", float(LT_TICKER.json()[0]['price'])-.05)
        #Market.Open_Buys.append([[datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second], .1 * Market.USD_account, float(LT_TICKER.json()[0]['price'])-.05])
        file = open("USDAccount", "w")
        file.write(str(.9 * USDaccount))
        file.close()

    #Define a "Sell" function.  Update list of outstanding Sell transactions and LTC account value.
    @classmethod
    def Sell(self):
        file = open("LTCAccount", "r")
        LTCaccount = float(file.read())
        file.close()
        print("Sell LTC", .1 * LTCaccount, "at ", float(LT_TICKER.json()[0]['price']) + .05)
        # Market.Open_Buys.append([[datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second], .1 * Market.USD_account, float(LT_TICKER.json()[0]['price'])-.05])
        file = open("LTCAccount", "w")
        file.write(str(.9 * LTCaccount))
        file.close()

#Main loop.
while True:
    TICKERS.LTC_Ticker()
    if float(LT_TICKER.json()[0]['price']) != float(LT_TICKER.json()[1]['price']):
        if float(LT_TICKER.json()[0]['price']) < float(LT_TICKER.json()[1]['price']):
            Market.Buy()
        elif float(LT_TICKER.json()[0]['price']) > float(LT_TICKER.json()[1]['price']):
            Market.Sell()
    time.sleep(.5)

#TICKERS.LTC_Ticker()
#print(LT_TICKER.json())