#this python script has the gnuplot script for plotting already integrated. Please change the all-cap variables
#according to your needs

import time
import os
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

BitcoinPrice=cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='eur',days=30)
datafile=open('PATH_TO_WHERE_THE_DATA_SHALL_STORED_AS_/data.txt', 'w')
for i in xrange(len(BitcoinPrices['prices'])):
    datafile.write(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime((BitcoinPrices['prices'][i][0])/1000))+' '+str(BitcoinPrices['prices'][i][1])+'\n')
datafile.close()

datafile=open('PATH_TO_WHERE_YOUR_PLOT_SCRIPT_IS_TO_BE_STORED_AS/script.gnu','w')

#you may want to put the whole script in a single line in your IDE
datafile.write(
"set terminal 'pdf'\n 
set output 'PATH_TO_WHERE_THE_PLOT_SHALL_STORED_AS_/plot.pdf'\n 
set title 'historic BTC Price'\n 
set xlabel 'time'\n 
set ylabel 'Price/EUR'\n 
set xdata time\n 
set timefmt '%Y.%m.%d %H:%M:%S'\n 
set format x '"'%m.%d'"'\n 
set xtics'"'STARTDATE_YYYY.MM.DD'"',432000,'"'ENDDATE_YYYY.MM.DD'"'\n 
plot 'PATH_TO_WHERE_THE_DATA_SHALL_STORED_AS_/data.txt' u 1:3 w l notitle")
datafile.close()

os.system('gnuplot PATH_TO_WHERE_YOUR_PLOT_SCRIPT_IS_TO_BE_STORED_AS/script.gnu')
