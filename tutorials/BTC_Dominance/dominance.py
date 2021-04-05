#Bitcoin Dominanz basierend auf den TOP3 Coins Bitcoin, Ethereum und Binance Coin 
#Dies ist das Skript zum Video auf meinem Youtube Kanal

#Denkt daran in Zeile 13 und 32 den Ausgabepfad für Euer Betriebssystem anzupassen!

import os
import numpy as np
import time

from pycoingecko import CoinGeckoAPI
cg=CoinGeckoAPI()

outputfolder='...'

coin1='bitcoin'
coin2='ethereum'
coin3='binancecoin'

duration=30 #days

coin1data=cg.get_coin_market_chart_by_id(id=coin1,vs_currency='eur',days=duration)
coin2data=cg.get_coin_market_chart_by_id(id=coin2,vs_currency='eur',days=duration)
coin3data=cg.get_coin_market_chart_by_id(id=coin3,vs_currency='eur',days=duration)

btc_dominance=[]
xaxis=[]

for i in xrange(len(coin1data['market_caps'])):
    btc_dominance.append((coin1data['market_caps'][i][1]/(coin1data['market_caps'][i][1]+coin2data['market_caps'][i][1]+coin3data['market_caps'][i][1])))
    xaxis.append(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime((coin1data['prices'][i][0]/1000))))

datafile=open(outputfolder+'/data.txt','w')
for i in xrange(len(xaxis)):
    datafile.write(str(xaxis[i])+' '+str(btc_dominance[i])+'\n')
datafile.close()
