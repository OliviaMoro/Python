# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:25:16 2020

@author: moroo
"""

import numpy as np
from FDM import matHexp as Hd

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


def heat1D(x,r,Tfin):
    """
        1D heat equation resolution (du/dt = u''(x), u(x,0) = g(x)) with the
        finite differences method : 
            - r (dt/h**2) : must be <= 1/2. for stability
    """
    npt = len(x)
    n = npt-2
    h = (x[-1]-x[0])/npt
    dt = r*h**2
    A = Hd(n,h,dt)
    
    nt = int(Tfin/dt)
    X = x[1:-1]
    u = np.hstack([X[X<=0.5],1-X[X>0.5]])
    U = [np.hstack([0,u,0])]
    for t in range(0,nt):
        # Explicit Euler
        u = np.dot(A,u)
        if(t%10 == 0):
            U.append(np.hstack([0,u,0]))
    
    return U
    
  
    
def testHeat():
    L = 1
    npt = 21
    r1 = 0.496 # r < 1/2 - stable
    r2 = 0.508 # r > 1/2 - instable
    x = np.linspace(0,L,npt)
    
    Tfin = 0.13
    U = heat1D(x,r1,Tfin)
    
    graph = Graph2D(x,U,"x","u","heat equation solution")
    graph.show()



if __name__ == "__main__":
    testHeat()