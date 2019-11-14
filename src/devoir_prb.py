# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:07:46 2019

@author: lucas
"""

#fonction calculant la distribution de P(N=j) avec 13 computations/Heure

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial

t=np.linspace(1,40,40)
d=np.exp(-13)*np.power(13,t)/factorial(t)

plt.plot(t,d,'o')
plt.title("Statistical distribution of N")
plt.xlabel("Computation in one hour")
plt.ylabel("P(N)")
plt.show()

# With this distribution, E(x)=V(x)=13 ==> standart deviation= 3.60555

#fonction calculant la distribution de P()