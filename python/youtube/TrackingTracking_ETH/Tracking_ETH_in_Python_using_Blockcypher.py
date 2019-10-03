#! /usr/bin/env/ python2.7

import requests
import numpy as np
from time import sleep

inputfile="PATH_TO_YOUR_ADDRESSES.TXT_FILE"
addr=np.genfromtxt(inputfile+"addresses.txt", delimiter="\t", usecols=0, dtype=str)
comment=np.genfromtxt(inputfile+"addresses.txt", delimiter="\t", usecols=1, dtype=str)

ethbalance=[]

for i in xrange(len(addr)):
	ethbalance.append(float((requests.get("https://api.blockcypher.com/v1/eth/main/addrs/"+addr[i])).json()["balance"])/10**18)
	sleep(5)
	print(ethbalance[i],comment[i])
print(np.sum(ethbalance))
