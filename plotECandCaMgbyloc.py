# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 11:19:42 2015

@author: Emily Yang
"""

import numpy as np
import matplotlib.pyplot as plt



pco2 = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (0), skip_header = 1)
temp = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (1), skip_header = 1)
ec = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (2), skip_header = 1)
pges = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (3), skip_header = 1)
o2 = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (4), skip_header = 1)
toc = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (5), skip_header = 1)
cat = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (6), skip_header = 1)
an = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (7), skip_header = 1)
pH = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (8), skip_header = 1)
alk = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (10), skip_header = 1)
na = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (11), skip_header = 1)
k = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (12), skip_header = 1)
ca = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (13), skip_header = 1)
mg = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (14), skip_header = 1)
no3 = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (15), skip_header = 1)
cl = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (16), skip_header = 1)
so4 = np.genfromtxt("pCO2_etc.txt", delimiter = '\t', usecols = (17), skip_header = 1)






def locsep(index1,index2):
    length = index2-index1+1
    data = np.zeros((17,length))
    for i in range(length):
        data[0,i]  = pco2[i+index1]
        data[1,i]  = temp[i+index1]
        data[2,i]  = ec[i+index1]
        data[3,i]  = pges[i+index1]
        data[4,i]  = o2[i+index1]
        data[5,i]  = toc[i+index1]
        data[6,i]  = cat[i+index1]
        data[7,i]  = an[i+index1]
        data[8,i]  = pH[i+index1]
        data[9,i]  = alk[i+index1]
        data[10,i] = na[i+index1]
        data[11,i] = k[i+index1]
        data[12,i] = ca[i+index1]
        data[13,i] = mg[i+index1]
        data[14,i] = no3[i+index1]
        data[15,i] = cl[i+index1]
        data[16,i] = so4[i+index1]
    return data


nahe1 = locsep(0,11)
nahe2 = locsep(12,24)
nahe3 = locsep(25,37)
nahe4 = locsep(38,50)
nahe5 = locsep(51,63)
nahe6 = locsep(64,85)
nahe7 = locsep(86,98)
nahe8 = locsep(99,111)
nahe9 = locsep(112,124)
nahe10 = locsep(125,137)
nahe11 = locsep(138,150)
nahe12 = locsep(151,163)
nahe13 = locsep(164,176)



ngw1 = locsep(177,188)
ngw2 = locsep(189,200)
ngw3 = locsep(201,212)
ngw4 = locsep(213,224)
ngw5 = locsep(225,236)
ngw6 = locsep(237,248)
ngw7 = locsep(249,260)
ngw8 = locsep(261,272)
ngw9 = locsep(273,284)
ngw10 = locsep(285,296)
ngw11 = locsep(297,308)
ngw12 = locsep(309,320)
ngw13 = locsep(321,332)
ngw14 = locsep(333,344)
ngw15 = locsep(345,356)
ngw16 = locsep(357,368)



rhein1 = locsep(369,380)
rhein2 = locsep(381,392)
rhein3 = locsep(393,404)
rhein4 = locsep(405,416)
rhein5 = locsep(417,428)
rhein6 = locsep(429,440)
rhein7 = locsep(441,452)
rhein8 = locsep(453,464)
rhein9 = locsep(465,476)
rhein10 = locsep(477,488)



list = [nahe1,nahe2,nahe3,nahe4,nahe5,nahe6,nahe7,nahe8,nahe9,nahe10,nahe11,\
        nahe12,nahe13,ngw1,ngw2,ngw3,ngw4,ngw5,ngw6,ngw7,ngw8,ngw9,ngw10,ngw11,\
        ngw12,ngw13,ngw14,ngw15,ngw16,rhein1,rhein2,rhein3,rhein4,rhein5,\
        rhein6,rhein7,rhein8,rhein9,rhein10]
        
        

#for i in range(len(list)):
#    plt.figure()
#    plt.plot(np.linspace(0,len(list[i][2]-1),len(list[i][2])),list[i][2],'o')

    
#for i in range(len(list)):
#    plt.figure()
#    plt.plot(np.linspace(0,len(list[i][12]-1),len(list[i][12])),list[i][12]+list[i][13],'o')
#    
    
    
    
    



#i=0
#fig, ax1 = plt.subplots()
#x = np.linspace(0,len(list[i][12]-1),len(list[i][12]))
#y1 = list[i][2]
#ax1.plot(x, y1,'o', color='b')
#ax1.set_xlabel('count')
## Make the y-axis label and tick labels match the line color.
#ax1.set_ylabel('EC', color='b')
#for tl in ax1.get_yticklabels():
#    tl.set_color('b')
#
#
#ax2 = ax1.twinx()
#y2 = list[i][12]+list[i][13]
#ax2.plot(x, y2,'o', color='r')
#ax2.set_ylabel('Ca+Mg', color='r')
#for tl in ax2.get_yticklabels():
#    tl.set_color('r')
#plt.show()


for i in range(len(list)):
    fig, ax1 = plt.subplots()
    x = np.linspace(1,len(list[i][12]),len(list[i][12]))
    y1 = list[i][2]
    ax1.plot(x, y1,'o', color='b')
    ax1.set_xlabel('count')
    # Make the y-axis label and tick labels match the line color.
    ax1.set_ylabel('EC', color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')
    
    
    ax2 = ax1.twinx()
    y2 = list[i][12]+list[i][13]
    ax2.plot(x, y2,'o', color='r')
    ax2.set_ylabel('Ca+Mg', color='r')
    for tl in ax2.get_yticklabels():
        tl.set_color('r')
        
    plt.title(str(i))
