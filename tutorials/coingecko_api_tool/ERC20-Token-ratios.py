import os
import time
import numpy as np

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

#-----------------------------------------------------------------------
#variables declaration
outputfolder="/PATH_TO_OUTPUT"
tokenadd1='address of contract for token one' #get this from etherscan.io
tokenadd2='address of contract for token two'


#get historical chart
token1=cg.get_coin_market_chart_from_contract_address_by_id(id='ethereum',contract_address=tokenadd1,vs_currency='eur', days=30)
token2=cg.get_coin_market_chart_from_contract_address_by_id(id='ethereum',contract_address=tokenadd2,vs_currency='eur', days=30)

datafile=open(outputfolder+'/token1.txt','w')
for i in xrange(len(token1['prices'])):
    datafile.write(str(token1['prices'][i][0])+' '+str(token1['prices'][i][1])+'\n')
datafile.close()

datafile=open(outputfolder+'/token2.txt','w')
for i in xrange(len(token2['prices'])):
    datafile.write(str(token2['prices'][i][0])+' '+str(token2['prices'][i][1])+'\n')
datafile.close()

token1time=np.genfromtxt(outputfolder+'/token1.txt',delimiter=' ',usecols=0)/1000
token2time=np.genfromtxt(outputfolder+'/token2.txt',delimiter=' ',usecols=0)/1000
token1price=np.genfromtxt(outputfolder+'/token1.txt',delimiter=' ',usecols=1)
token2price=np.genfromtxt(outputfolder+'/token2.txt',delimiter=' ',usecols=1)

#-------------------------------------
#some stats here to check if there is not much delay in the raw data:
#delaytime=[]
#for i in xrange(len(token1time)):
#    delaytime.append(token1time[i]-token2time[i]))
#
#print(np.mean(delaytime),np.std(delaytime)
#
#--------------------------------------

datafile=open(outputfolder+'/ratio.txt','w')
for i in xrange(len(token2time)):
    datafile.write(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime((token2time[i]+token1time[i])/2))+' '+str(token2price[i]/token1price[i])+'\n')
datafile.close()

datafile=open(outputfolder+'/ratio.gnu','w')
datafile.write("set terminal 'pdf'\n set output '"+outputfolder+"/plot.pdf'\n set title 'POWR:POLY Ratio'\n set xlabel 'time'\n set ylabel 'POWR/POLY'\n set xdata time\n set timefmt '%Y.%m.%d %H:%M:%S'\n set format x '"'%m.%d'"'\n set xtics '"'2020.03.21'"',432000,'"'2020.04.20'"'\n plot '"+outputfolder+"/ratio.txt' u 1:3 w l notitle")
datafile.close()

os.system('gnuplot '+outputfolder+'/ratio.gnu')
