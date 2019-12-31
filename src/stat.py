#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author : Romain Graux, Louis Delait, Lucas Delbecque, Paulin Martin, Louis Lejeune
@date : Friday, 08 November 2019
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils import readCPU1, readCPU2
# ================ GLOBAL VARIABLES ===================
VAR = 100.0
STD = np.sqrt(VAR)



# ================ HOW TO DO ===================
# ----------------   Plots   -------------------
# Utilisez le 'purple' de préférence pour vos graphs
# Mettez vos axes en notations scientifiques
# Labelisez bien vos axes comme ceci : 'Nom (unités)'
# Ajoutez une légende propre pour chaque courbe comme ceci
# EXEMPLE:
#       def Harry_ploter(save=False, name='Harry')
#           plt.Figure(figsize=(15,20))
#           plt.title('Harry mon bon ploter')
#           plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0)) # Notation scientifique
#           plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0)) # Notation scientifique
#           plt.xlabel('Temps (s)')
#           plt.ylabel('Energie reçue (kWh)')
#           id1 = plt.plot(x1, y1, 'o', color='purple')
#           id2 = plt.plot(x2, y2, 'o', color='orange')
#           plt.legend([id1, id2],['Courbe 1', 'Courbe 2']
#           if save: plt.savefig('%s.png'%(name))
#           else: plt.show()
COLORS = [purple, orange, blue] = ['#9400D3', '#FFA500', '#0080FF']

def Q3():
    df = readCPU1()
    dfLow  = np.array(df.loc[df['LowCPU'] == True]['OperatingTime'])
    dfHigh = np.array(df.loc[df['LowCPU'] == False]['OperatingTime'])
    
    nLow = np.size(dfLow)  #ok
    nHigh = np.size(dfHigh) #ok
    
    varLow = np.var(dfLow) #ok
    varHigh = np.var(dfHigh) #ok
    
    meanLow = np.mean(dfLow) #ok
    meanHigh = np.mean(dfHigh) #ok
    
    
    Sp2 = 100 #v(((nLow-1)*(varLow))+((nHigh-1)*(varHigh)))/(nLow+nHigh-2)
    
    t0 = ((meanLow-meanHigh))/(np.sqrt(Sp2*((1/nLow)+(1/nHigh))))
    
    tnn = nLow+nHigh-2
    
    alpha2 = 0.05/2
    
    ttab = 2.101 # juste la valeur dans vos tables avec df = 18 et t0.025
    
    #print('Number of low CPUs :',nLow)
    #print('Number of high CPuS :',nHigh)
    
    #print('--------------------------')
    
    #print('Variance of Low CPUs =',varLow)
    #print('Variance of High CPUs =', varHigh)
    
    #print('--------------------------')
    
    #print('Mean of Low CPUs =',meanLow)
    #print('Mean of High CPUs =',meanHigh)
    
    #print('--------------------------')
    
    #print('Sp^2 =',Sp2)
    #print('T0 =', t0)
    #print('Tnn,alpha/2 = (',tnn,',',alpha2,') =', ttab)
    return None
    
def Q4(): 
    
    df = readCPU1()
    dfLow  = np.array(df.loc[df['LowCPU'] == True]['OperatingTime'])
    dfHigh = np.array(df.loc[df['LowCPU'] == False]['OperatingTime'])
    
    nLow = np.size(dfLow)  
    nHigh = np.size(dfHigh) 
    
    meanLow = np.mean(dfLow) 
    meanHigh = np.mean(dfHigh) 
    
    meanTot = np.mean(df)[0]
    
    nTot = nLow+nHigh
    k = 2 #number of treatment 
    SST = nLow*(meanLow-meanTot)**2+nHigh*(meanHigh-meanTot)**2
    print('SST =', SST)
    
    SSEn1 = 0.0
    SSEn2 = 0.0
    
    for i in range(nLow):
        
        SSEn1 += (dfLow[i]-meanLow)**2
        
   
        
    for j in range(nHigh):
        
        SSEn2 += (dfHigh[j]-meanHigh)**2
        
    SSE = SSEn1 + SSEn2
    
    print('SSEn1 =', SSEn1)
    print('SSEn2 =', SSEn2)   
    print('SSE =', SSE)
    
    MST = SST/(k-1)
    MSE = SSE/(nTot-k)
    
    Fobs = MST/MSE
    
    print('F_obs =',Fobs)
    return None



if __name__=='__main__':
    Q3()
    Q4()
    






