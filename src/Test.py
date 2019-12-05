import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial, comb
from mpl_toolkits.mplot3d import Axes3D
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
N=np.linspace(0,360,300)
N1=np.linspace(0,60,60)
N1,N=np.meshgrid(N1,N)

plt.xlabel("$N1$", fontsize=16)         
plt.ylabel("$N$", fontsize=16)

Z=comb(N,N1)*0.2**N1*0.8**(N-N1)
ax.plot_wireframe(N1, N, Z, rstride=2, cstride=2) 
plt.show()


