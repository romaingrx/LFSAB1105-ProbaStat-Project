import numpy as np
from scipy.stats import binom, poisson
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def joint_distribution():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    N=np.arange(250,370,1)
    N1=np.arange(10,110,1)
    N1,N=np.meshgrid(N1,N)
    plt.xlabel("$N1$ = number of requests that the first computer performs", fontsize=7)
    plt.ylabel("$N$ :number of requests per day", fontsize=7)
    Z=poisson.pmf(N,312)*binom.pmf(N1,N,0.2)
    ax.plot_wireframe(N1, N, Z, rstride=5, cstride=5)
    plt.show()
