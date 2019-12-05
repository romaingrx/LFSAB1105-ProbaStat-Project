#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author : Romain Graux, Louis Delait, Lucas Delbecque, Paulin Martin, Louis Lejeune
@date :Sunday, 17 November 2019
"""
#fonction calculant la distribution de P(N=j) avec 13 computations/Heure
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial, comb
from mpl_toolkits.mplot3d import Axes3D
#à ajouter pour plot en 3d
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

# QUESION 1
def Q1():
    t=np.linspace(1,40,40)
    d=np.exp(-13)*np.power(13,t)/factorial(t)
    plt.plot(t,d,'o')
    plt.title("Statistical distribution of N")
    plt.xlabel("Computation in one hour")
    plt.ylabel("P(N)")
    plt.show()
# With this distribution, E(x)=V(x)=13 ==> standart deviation= 3.60555



# QUESTION 2
# On calcule la distribution conditionelle P(N1|n) en considérant n constant pour que lambda le soit aussi
#calcul de la distribution de P(N1|360) :
def Q2():
    n1=np.linspace(0,360,360)
    d=comb(360,n1)*0.2**n1*0.8**(360-n1)

    plt.plot(n1,d,'o')
    plt.title("Statistical distribution of N1|N=n")
    plt.xlabel("Computational requests treated by server 1 if N=360")
    plt.ylabel("P(N1|N=360)")
    plt.show()

#fonction 3d représentant toutes les autres (expérimentale):
#t=np.linspace(20,120,101)
#n=np.linspace(20,120,101)
#d=np.zeros((101,101))
#for i in range(0,101):
#    d[i]=np.exp(-(n[i]*0.2))*np.power(n[i]*0.2,t)/factorial(t)

#Axes3D.plot(t, n, d)
#plt.plot(t,n,d,'o')
#plt.title("Statistical distribution of N1")
#plt.xlabel("Computation in one day")
#plt.ylabel("P(n1|360)")
#plt.show()

#vaut +- 0.033
# toutes les variables dépendent ainsi de n et la formule génerale de la distribution est np.exp(-(n*P(N1)))*np.power(n*P(N1),t)/factorial(t)
# on trouve précisément la valeure de P(N1=64|n=360) avec
"""
d=np.exp(-(360*0.2))*np.power(360*0.2,64)/factorial(64)
print(d)

# =0.031380522985433555 et la somme des points des ordonées de la courbe vaut bien 1 ce qui prouve mon génie
# avec dès lors E(N1|n)=0.2*n=V(N1|n) et donc ==> standart deviation =  sqrt(0.2*n)
"""

# QUESTION 3
#The expression of the exact joint distribution is given by : P(N1=j,N=n)=P(N1=j|N=n)*P(N=n)
#plot en 3D pour N 0-360 et N1 0-60 (On remarque passage que la solution du point 2 est vérifiée):
def Q3():
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



# QUESTION 4
#pmf of N1 = P(N1=j) = Somme (sur les i) des P(N1=j,N=i) = The joint cumulative distribution functionn of N and N1
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

if __name__=='__main__':
    # Q1()
    # Q2()
    Q3()
    # Q4()
