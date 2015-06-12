# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 16:21:04 2015

@author: Emily Yang

Plots in linear and x-logscale the different variables vs distance from the
Rhein for the mean and each season's values, and produces the equation and the
R^2 value. Also finds Spearman correlation coefficients and 2-tailed p-values.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

distfromrhein = np.array([12133.,11163.,13138.,23708.,38682.,3913.,54630.,60485.,60447.,100681.,60900.,55906.,53653.])


pco2 = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (1), skip_header = 1)
temp = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (2), skip_header = 1)
ec = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (3), skip_header = 1)
pges = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (4), skip_header = 1)
o2 = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (5), skip_header = 1)
toc = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (6), skip_header = 1)
cat = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (7), skip_header = 1)
an = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (8), skip_header = 1)
pH = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (9), skip_header = 1)
alk = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (10), skip_header = 1)
na = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (11), skip_header = 1)
k = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (12), skip_header = 1)
ca = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (13), skip_header = 1)
mg = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (14), skip_header = 1)
no3 = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (15), skip_header = 1)
cl = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (16), skip_header = 1)
so4 = np.genfromtxt("meanvalues.txt", delimiter = '\t', usecols = (17), skip_header = 1)

wpco2 = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (1), skip_header = 1)
wtemp = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (2), skip_header = 1)
wec = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (3), skip_header = 1)
wpges = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (4), skip_header = 1)
wo2 = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (5), skip_header = 1)
wtoc = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (6), skip_header = 1)
wcat = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (7), skip_header = 1)
wan = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (8), skip_header = 1)
wpH = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (9), skip_header = 1)
walk = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (10), skip_header = 1)
wna = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (11), skip_header = 1)
wk = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (12), skip_header = 1)
wca = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (13), skip_header = 1)
wmg = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (14), skip_header = 1)
wno3 = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (15), skip_header = 1)
wcl = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (16), skip_header = 1)
wso4 = np.genfromtxt("winteravgs.txt", delimiter = '\t', usecols = (17), skip_header = 1)

sppco2 = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (1), skip_header = 1)
sptemp = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (2), skip_header = 1)
spec = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (3), skip_header = 1)
sppges = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (4), skip_header = 1)
spo2 = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (5), skip_header = 1)
sptoc = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (6), skip_header = 1)
spcat = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (7), skip_header = 1)
span = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (8), skip_header = 1)
sppH = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (9), skip_header = 1)
spalk = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (10), skip_header = 1)
spna = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (11), skip_header = 1)
spk = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (12), skip_header = 1)
spca = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (13), skip_header = 1)
spmg = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (14), skip_header = 1)
spno3 = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (15), skip_header = 1)
spcl = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (16), skip_header = 1)
spso4 = np.genfromtxt("springavgs.txt", delimiter = '\t', usecols = (17), skip_header = 1)

supco2 = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (1), skip_header = 1)
sutemp = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (2), skip_header = 1)
suec = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (3), skip_header = 1)
supges = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (4), skip_header = 1)
suo2 = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (5), skip_header = 1)
sutoc = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (6), skip_header = 1)
sucat = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (7), skip_header = 1)
suan = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (8), skip_header = 1)
supH = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (9), skip_header = 1)
sualk = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (10), skip_header = 1)
suna = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (11), skip_header = 1)
suk = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (12), skip_header = 1)
suca = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (13), skip_header = 1)
sumg = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (14), skip_header = 1)
suno3 = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (15), skip_header = 1)
sucl = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (16), skip_header = 1)
suso4 = np.genfromtxt("summeravgs.txt", delimiter = '\t', usecols = (17), skip_header = 1)

fpco2 = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (1), skip_header = 1)
ftemp = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (2), skip_header = 1)
fec = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (3), skip_header = 1)
fpges = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (4), skip_header = 1)
fo2 = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (5), skip_header = 1)
ftoc = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (6), skip_header = 1)
fcat = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (7), skip_header = 1)
fan = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (8), skip_header = 1)
fpH = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (9), skip_header = 1)
falk = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (10), skip_header = 1)
fna = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (11), skip_header = 1)
fk = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (12), skip_header = 1)
fca = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (13), skip_header = 1)
fmg = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (14), skip_header = 1)
fno3 = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (15), skip_header = 1)
fcl = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (16), skip_header = 1)
fso4 = np.genfromtxt("fallavgs.txt", delimiter = '\t', usecols = (17), skip_header = 1)




def plotallavgs(var,wvar,spvar,suvar,fvar,varname,unit,log=False):
    '''
    plots the mean, winter, spring, summer, and fall avgs vs dist from Rhein
    e.g. plotallavgs(cl,wcl,spcl,sucl,fcl,'Cl','mg/l',True)
    '''
    
    f = plt.figure()
    ax = f.add_subplot(111)
    if log == False:
        slope, intercept, r_value, p_value, std_err = stats.linregress(distfromrhein,[var[x] for x in range(13)])    
        plt.plot(distfromrhein,[var[x] for x in range(13)],'o')
        plt.plot(np.linspace(min(distfromrhein),max(distfromrhein)),slope*np.linspace(min(distfromrhein),max(distfromrhein))+intercept)
        plt.text(0.65, 0.9,'y = '+str(slope)+'x + '+str(intercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(r_value**2), ha='center', va='center',transform=ax.transAxes)    
    else:
        logx = np.zeros(len(distfromrhein))
        for i in range(len(distfromrhein)):
            logx[i] = math.log(distfromrhein[i])
        
        slope, intercept, r_value, p_value, std_err = stats.linregress(logx,[var[x] for x in range(13)])
        
        plt.plot(distfromrhein,[var[x] for x in range(13)],'o')
        plt.plot([min(distfromrhein),max(distfromrhein)],[slope*math.log(min(distfromrhein))+intercept,slope*math.log(max(distfromrhein))+intercept])
        plt.xscale('log')
        plt.text(0.65, 0.9,'y = '+str(slope)+'ln(x) + '+str(intercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(r_value**2), ha='center', va='center',transform=ax.transAxes)    
        
    plt.xlabel('Distance from Rhein [m]')
    plt.ylabel(varname+' ['+unit+']')
    plt.title('Mean '+varname+' vs dist from Rhein')
    
    
    
    
    f = plt.figure()
    ax = f.add_subplot(111)
    if log == False:
        wslope, wintercept, wr_value, wp_value, wstd_err = stats.linregress(distfromrhein,[wvar[x] for x in range(13)])
        plt.plot(distfromrhein,[wvar[x] for x in range(13)],'o')
        plt.plot(np.linspace(min(distfromrhein),max(distfromrhein)),wslope*np.linspace(min(distfromrhein),max(distfromrhein))+wintercept)
        plt.text(0.65, 0.9,'y = '+str(wslope)+'x + '+str(wintercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(wr_value**2), ha='center', va='center',transform=ax.transAxes)    
    else:
        logx = np.zeros(len(distfromrhein))
        for i in range(len(distfromrhein)):
            logx[i] = math.log(distfromrhein[i])
        
        wslope, wintercept, wr_value, wp_value, wstd_err = stats.linregress(logx,[wvar[x] for x in range(13)])
        
        plt.plot(distfromrhein,[wvar[x] for x in range(13)],'o')
        plt.plot([min(distfromrhein),max(distfromrhein)],[wslope*math.log(min(distfromrhein))+wintercept,wslope*math.log(max(distfromrhein))+wintercept])
        plt.xscale('log')
        plt.text(0.65, 0.9,'y = '+str(wslope)+'ln(x) + '+str(wintercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(wr_value**2), ha='center', va='center',transform=ax.transAxes)    
        
    plt.xlabel('Distance from Rhein [m]')
    plt.ylabel(varname+' ['+unit+']')
    plt.title('Winter '+varname+' vs dist from Rhein')
    
    
    
    
    f = plt.figure()
    ax = f.add_subplot(111)
    if log == False:
        spslope, spintercept, spr_value, spp_value, spstd_err = stats.linregress(distfromrhein,[spvar[x] for x in range(13)])
        plt.plot(distfromrhein,[spvar[x] for x in range(13)],'o')
        plt.plot(np.linspace(min(distfromrhein),max(distfromrhein)),spslope*np.linspace(min(distfromrhein),max(distfromrhein))+spintercept)
        plt.text(0.65, 0.9,'y = '+str(spslope)+'x + '+str(spintercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(spr_value**2), ha='center', va='center',transform=ax.transAxes)
    else:
        logx = np.zeros(len(distfromrhein))
        for i in range(len(distfromrhein)):
            logx[i] = math.log(distfromrhein[i])
        
        spslope, spintercept, spr_value, spp_value, spstd_err = stats.linregress(logx,[spvar[x] for x in range(13)])
        
        plt.plot(distfromrhein,[spvar[x] for x in range(13)],'o')
        plt.plot([min(distfromrhein),max(distfromrhein)],[spslope*math.log(min(distfromrhein))+spintercept,spslope*math.log(max(distfromrhein))+spintercept])
        plt.xscale('log')
        plt.text(0.65, 0.9,'y = '+str(spslope)+'ln(x) + '+str(spintercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(spr_value**2), ha='center', va='center',transform=ax.transAxes)    
        
    plt.xlabel('Distance from Rhein [m]')
    plt.ylabel(varname+' ['+unit+']')
    plt.title('Spring '+varname+' vs dist from Rhein')
    
    
    
    
    f = plt.figure()
    ax = f.add_subplot(111)
    if log == False:
        suslope, suintercept, sur_value, sup_value, sustd_err = stats.linregress(distfromrhein,[suvar[x] for x in range(13)])
        plt.plot(distfromrhein,[suvar[x] for x in range(13)],'o')
        plt.plot(np.linspace(min(distfromrhein),max(distfromrhein)),suslope*np.linspace(min(distfromrhein),max(distfromrhein))+suintercept)
        plt.text(0.65, 0.9,'y = '+str(suslope)+'x + '+str(suintercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(sur_value**2), ha='center', va='center',transform=ax.transAxes)
    else:
        logx = np.zeros(len(distfromrhein))
        for i in range(len(distfromrhein)):
            logx[i] = math.log(distfromrhein[i])
        
        suslope, suintercept, sur_value, sup_value, sustd_err = stats.linregress(logx,[suvar[x] for x in range(13)])
        
        plt.plot(distfromrhein,[suvar[x] for x in range(13)],'o')
        plt.plot([min(distfromrhein),max(distfromrhein)],[suslope*math.log(min(distfromrhein))+suintercept,suslope*math.log(max(distfromrhein))+suintercept])
        plt.xscale('log')
        plt.text(0.65, 0.9,'y = '+str(suslope)+'ln(x) + '+str(suintercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(sur_value**2), ha='center', va='center',transform=ax.transAxes)    
        
    plt.xlabel('Distance from Rhein [m]')
    plt.ylabel(varname+' ['+unit+']')
    plt.title('Summer '+varname+' vs dist from Rhein')
    
    
    
    
    f = plt.figure()
    ax = f.add_subplot(111)
    if log == False:
        fslope, fintercept, fr_value, fp_value, fstd_err = stats.linregress(distfromrhein,[fvar[x] for x in range(13)])
        plt.plot(distfromrhein,[fvar[x] for x in range(13)],'o')
        plt.plot(np.linspace(min(distfromrhein),max(distfromrhein)),fslope*np.linspace(min(distfromrhein),max(distfromrhein))+fintercept)
        plt.text(0.65, 0.9,'y = '+str(fslope)+'x + '+str(fintercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(fr_value**2), ha='center', va='center',transform=ax.transAxes)
    else:
        logx = np.zeros(len(distfromrhein))
        for i in range(len(distfromrhein)):
            logx[i] = math.log(distfromrhein[i])
        
        fslope, fintercept, fr_value, fp_value, fstd_err = stats.linregress(logx,[fvar[x] for x in range(13)])
        
        plt.plot(distfromrhein,[fvar[x] for x in range(13)],'o')
        plt.plot([min(distfromrhein),max(distfromrhein)],[fslope*math.log(min(distfromrhein))+fintercept,fslope*math.log(max(distfromrhein))+fintercept])
        plt.xscale('log')
        plt.text(0.65, 0.9,'y = '+str(fslope)+'ln(x) + '+str(fintercept), ha='center', va='center',transform=ax.transAxes)
        plt.text(0.8, 0.85,'R^2 = '+str(fr_value**2), ha='center', va='center',transform=ax.transAxes)    
        
    plt.xlabel('Distance from Rhein [m]')
    plt.ylabel(varname+' ['+unit+']')
    plt.title('Fall '+varname+' vs dist from Rhein')
    

def spearman(var,wvar,spvar,suvar,fvar,varname):
    '''
    finds Spearman rank coefficients and the probability that the values
    are random, for each season
    '''
    
    meanspear = stats.spearmanr(distfromrhein,[var[x] for x in range(13)])
    winterspear = stats.spearmanr(distfromrhein,[wvar[x] for x in range(13)])
    springspear = stats.spearmanr(distfromrhein,[spvar[x] for x in range(13)])
    summerspear = stats.spearmanr(distfromrhein,[suvar[x] for x in range(13)])
    fallspear = stats.spearmanr(distfromrhein,[fvar[x] for x in range(13)])
    
    
    print 'Mean ',varname,' Spearman correlation coefficient: ',meanspear[0]
    print 'Mean ',varname,' 2-tailed p-value: ',meanspear[1]
    print 'Winter ',varname,' Spearman correlation coefficient: ',winterspear[0]
    print 'Winter ',varname,' 2-tailed p-value: ',winterspear[1]
    print 'Spring ',varname,' Spearman correlation coefficient: ',springspear[0]
    print 'Spring ',varname,' 2-tailed p-value: ',springspear[1]
    print 'Summer ',varname,' Spearman correlation coefficient: ',summerspear[0]
    print 'Summer ',varname,' 2-tailed p-value: ',summerspear[1]
    print 'Fall ',varname,' Spearman correlation coefficient: ',fallspear[0]
    print 'Fall ',varname,' 2-tailed p-value: ',fallspear[1]
    
