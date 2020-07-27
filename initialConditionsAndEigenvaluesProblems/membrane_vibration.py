# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 02:19:19 2020

@author: moroo
"""

import numpy as np
import matplotlib.pyplot as plt
from math import isclose, pi
from scipy.special import jv

from methodTir import tirRK


import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D 



m = 1 
a = 1


"""
    We redefine the differential system as :
        s' = t                            - sDer
        t' = -t:rho - ((k*a)^2-m^2/rho^2) - tDer
"""
def sDer(rho,s,t):
    return t
    
    
def tDer(rho,s,t):
    global k
    res = -t/rho -((k*a)**2-(m/rho)**2)*s
    return res


def plotUmp(m,k,s0,t0):
    r = np.linspace(0,a,100)
    phi = np.arange(0,2*pi,pi/100.)
    r, phi = np.meshgrid(r,phi)
    
    rho = jv(m,k*a*r)
    U = a*rho*np.cos(m*phi)
                         
    x,y = r*np.cos(phi),r*np.sin(phi)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x,y,U,cmap=plt.cm.YlGnBu_r)

    ax.set_zlim(0, 1)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_zlabel(r'$Ump$')

    plt.show()
    
    
    
def searchK(n,x0,s0,t0,k1,k2):
    global k
    delta = 1
    tol = 1e-3
    nmax = 20
    i = 0
    
    while (not isclose(delta,0,rel_tol=tol, abs_tol=tol) and i <= nmax):
        i += 1
        # The interval is cut in two
        k0 = (k1+k2)/2.
        
        k = k1
        r,s1,t1 = tirRK(n,1,s0,t0,sDer,tDer,x0)
        k = k0 
        r,s2,t2 = tirRK(n,1,s0,t0,sDer,tDer,x0)
        print("k : {}".format(k))

        # root is in [a,x0] : the sign changed 
        if (s1[-1]*s2[-1] < 0 ):
            k2 = k0
        # root is in [x0,b] : sign unchanged  
        elif (s1[-1]*s2[-1] > 0):
            k1 = k0
        delta = s2[-1]
    
    print("[k1,k2] = [{},{}], i = {}".format(k2,k1,i))
    return k0
    

    
def pinpointK(n,x0,s0,t0,k1,k2):
    global k
    k = k1; k1 = k
    r,s1,t1 = tirRK(n,1,s0,t0,sDer,tDer,x0)
    print("S(1) : {}".format(s1[-1]))
    
    k = k2; k2 = k
    r,s2,t2 = tirRK(n,1,s0,t0,sDer,tDer,x0)
    print("S(1) : {}".format(s2[-1]))
    
    legend = ["k = "+str(k1),"k = "+str(k2)]
    graph = Graph2D(r,[s1,s2],"rho","S(rho)","Méthode du tir",legend)
    graph.show()




if __name__ == "__main__":
    k1 = 3.85040283203125
    k2 = 7.0458984375
    k3 = 10.208740234375
    k4 = 13.353515625
    k5 = 16.48193359375
    k6 = 19.5927734375
    n = 100
    x0 = 1/(n+1.)
    s0 = 1
    t0 = 0
    
    global k
    k = k4
    #plotUmp(2,k3,s0,t0)
    #pinpointK(n,x0,s0,t0,k1,k2)
    searchK(n,x0,s0,t0,0,5)
    

    