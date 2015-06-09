# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:42:50 2015

@author: Emily Yang
"""

import numpy as np
import csv

descap = np.genfromtxt("wwtpinfo.txt", delimiter = '\t', usecols = (0), skip_header = 1)

def wwtpdata(FID):
    data1 = np.genfromtxt("wwtpinfo.txt", delimiter = '\t', usecols = (FID+1), skip_header = 1)
    mask = ~np.isnan(data1)
    data = data1[mask]
    return data


wwtplist = [ wwtpdata(FID) for FID in range(100) ]

def totdescap(FID):
    length = len(wwtpdata(FID))
    descapvals = np.zeros(length)    
    for i in range(length):
        descapvals[i] = descap[int(wwtplist[FID][i])]
    return sum(descapvals)


totupstrmdescap = np.zeros(100)
for i in range(100):
    totupstrmdescap[i] = totdescap(i)
    
    
with open('upstreamdesigncapacities.txt', 'wb') as f:

    writer = csv.writer(f,delimiter='\t')
    for i in range(len(totupstrmdescap)):
        writer.writerow([totupstrmdescap[i]])
