import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial, comb
from mpl_toolkits.mplot3d import Axes3D

X=np.linspace(0,5,5)
i=0
while i<len(X)+1:
    Y=np.linspace(0,i,i)
    i=i+1
    print(Y)