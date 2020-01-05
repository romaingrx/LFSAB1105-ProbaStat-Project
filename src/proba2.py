from scipy.special import factorial, comb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def Q4():

    d=0

    t=np.linspace(1,40,40)

    for i in np.linspace(0,10):

        d+=np.exp(-i*0.2)*np.power(i*0.2,t)/factorial(t)

        print (d)

    plt.plot(t,d,'o')

    plt.title("Statistical distribution of N1")

    plt.xlabel("Computation in one hour")

    plt.ylabel("P(N1)")

    plt.show()

    
#how to calculate E(N1) and V(N1).

t=np.linspace(0,150,151)

def Po(p):

    return np.exp(-p)*np.power(p,t)/factorial(t)

def E(y,p):

    return y@Po(0.2*p)

#E(N1)

print(E(t,312))

#E(N1**2)

print(E(t**2,312))

#E(N1)**2

print(E(t,312)**2)

#V(N1)

print(E(t**2,312)-E(t,312)**2)
