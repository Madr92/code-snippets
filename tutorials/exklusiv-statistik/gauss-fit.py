import numpy as np
import os
import collections

#get your coin data from coingecko and save it as textfile with date and price in it
#rename the textfile as "data.txt" or store it accordingly (appended testdata are ltc prices)
#make sure you use the tab delimiter or increase usecols to 2, if you used space before!

outputfolder='/home/crypto/Desktop/'
coin=np.genfromtxt(outputfolder+'/data.txt',delimiter='\t', usecols=1)

mean=np.mean(coin)
std=np.std(coin)
#-------------
#get price distribution
#first sort the prices convert to ints
bars=[]
for i in xrange(len(coin)):
    bars.append(int(coin[i]))
bars2=sorted(bars)

#second count occurences in converted array using collection module
#and then sort them to plotable file
def CountFrequency(arr):
    return collections.Counter(arr)
bars3 = CountFrequency(bars2)

datafile=open(outputfolder+'stats.txt','w')
for (key, value) in bars3.items():
    datafile.write(str(key)+' '+str(value)+'\n')
datafile.close()

#now prepare the output including distribution function
datafile=open(outputfolder+'script.gnu','w')
datafile.write("set terminal 'pdf'\n set output '"+outputfolder+"plot.pdf'\n set ylabel 'Anzahl'\n "
               "set xtics rotate by -35\n "
               "set xlabel 'price'\n "
               "f(x)=amplitude/("+str(std)+"*sqrt(2.*pi))*exp(-(x-"+str(mean)+")**2/(2.*"+str(std)+"**2))\n "
            "fit f(x) '"+outputfolder+"stats.txt' u 1:2 via amplitude\n plot '"+outputfolder+"stats.txt' u 1:2 w i notitle,f(x) title 'Gauss-Fit'\n")
datafile.close()

os.system('gnuplot '+outputfolder+'/script.gnu')

