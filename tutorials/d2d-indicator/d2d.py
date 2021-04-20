import time
import numpy as np

inputpath="HIER DAS VERZEICHNIS EINGEBEN"

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

bitcoin=cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='eur',days=2000)
datafile=open(inputpath+'/test.txt', 'w')
for i in xrange(len(bitcoin['prices'])):
    datafile.write(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime((bitcoin['prices'][i][0])/1000))+' '+str(bitcoin['prices'][i][1])+'\n')
datafile.close()

price=np.genfromtxt(inputpath+'/test.txt',delimiter=' ',usecols=2)
date=np.genfromtxt(inputpath+'/test.txt',delimiter=' ',usecols=0, dtype=str)

d2d=[]
for i in xrange(len(price)):
    for j in xrange(i,len(price),1):
        if(price[j]<0.381*price[i]):
            d2d.append(j-i)
            break

datafile=open(inputpath+'/data.txt','w')
for i in xrange(len(d2d)):
    datafile.write(str(date[i])+' '+str(d2d[i])+'\n')
datafile.close()
