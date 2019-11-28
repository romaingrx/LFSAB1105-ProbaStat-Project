#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author : Romain Graux, Louis Delait, Lucas Delbecque, Paulin Martin, Louis Lejeune
@date :Sunday, 17 November 2019
"""
#fonction calculant la distribution de P(N=j) avec 13 computations/Heure
import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#à ajouter pour plot en 3d
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

PN1 = 0.2
PN2 = 0.5
PN3 = 0.3
DAY_MEAN  = 312
HOUR_MEAN = DAY_MEAN/24

def poisson(t, lam):
    return np.exp(-lam)*np.power(lam,t)/factorial(t)

# QUESTION 1
def Q1():
    t = np.linspace(1,40,40)
    d = poisson(t, 13)
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
    global DAY_MEAN, PN1
    t = np.linspace(20,120,101)
    d = poisson(t, DAY_MEAN*PN1)

    plt.plot(t,d,'o')
    plt.title("Statistical distribution of N1")
    plt.xlabel("Computation in one day")
    plt.ylabel("P(N1|360)")
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
#plot de la pmf d'abord pour un n défini(13) ensuite en 3D:
def Q3():
    t=np.linspace(1,25,25)
    d1=np.exp(-13)*(np.power(13,13))/factorial(13)
    # print(np.power(13,13))
    #print(13**(13))         ça donne pas la même chose Romaim Graux aide moi
    d2=np.exp(-(13*0.2))*np.power(13*0.2,t)/factorial(t)
    d=d1*d2
    plt.plot(t,d,'o')
    plt.title("pmf of the joint distribution of N1 and N")
    plt.xlabel("Computation in one hour")
    plt.ylabel("P(N1=j,N=n)")
    plt.show()
#ça , ça donne les probabilités que n vale 13 et que N1 vale l'absisse , il manque plus qu'a faire un plot en 3D je suppose.



#fonction calculant la distribution de P()
# QUESTION 4
#pmf of N1 = P(N1=j) = Somme (sur les i) des P(N1=j,N=i) = The joint cumulative distribution functionn of N and N1
def Q4():
    d=0
    t=np.linspace(1,40,40)
    for i in range(2000):
        d+=np.exp(-i*PN1)*np.power(i*PN1,t)/factorial(t)
    plt.plot(t,d,'o')
    plt.title("Statistical distribution of N1")
    plt.xlabel("Computation in one hour")
    plt.ylabel("P(N1)")
    plt.show()

if __name__=='__main__':
    # Q1()
    # Q2()
    # Q3()
    # Q4()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    x = z*0
    y = z**2
    ax.scatter(x, y, z, label='parametric curve')
    ax.legend()

    plt.show()
