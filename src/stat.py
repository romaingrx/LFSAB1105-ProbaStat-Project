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

def main():
    return 0

if __name__=='__main__':
    df = readCPU1()
    print(df[df.columns[1]])
