#this is to synch the raw data and to calculate the MMRI according to the formula provided by Mr. Gregory Mannarino
#please make sure you change your folder settings accordingly

import numpy as np
#--------------------
#read the rawdata from their csv files
#please make sure to edit the path to the data accordingly

#reading from txt file
time1=np.genfromtxt('YOUR PATH TO/tnx.txt', delimiter=',', usecols=0, dtype=str)
time2=np.genfromtxt('YOUR PATH TO/dxy.txt', delimiter=',', usecols=0, dtype=str)
tnx=np.genfromtxt('YOUR PATH TO/tnx.txt', delimiter=',', usecols=1)
dxy=np.genfromtxt('YOUR PATH TO/dxy.txt', delimiter=',', usecols=1)

#synching data and calculate mmri
datafile=open('YOUR PREFERRED OUTPUTPATH/mmri.txt','w')
for i in xrange(len(time1)):
    for j in xrange(len(time2)):
        if ((time1[i]==time2[j])):
            datafile.write(str(time1[i])+'\t'+str(dxy[j])+'\t'+str(tnx[i])+'\t'+str(dxy[j]*tnx[i]/1.61)+'\n')
datafile.close()
