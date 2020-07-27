# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:11:42 2020

@author: moroo
"""
import numpy as np
from FEM import matK as Ke, matM as Me

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


def heat1D(x,r,Tfin):
    """
        1D heat equation resolution (du/dt = u''(x), u(x,0) = g(x)) with the
        finite elements method
    """
    npt = len(x)
    n = len(x)-2
    h = x[1:npt+1]-x[0:-1]
    X = x[1:-1]
    
    M = Me(n,h)
    K = Ke(n,h)
    dt = r*np.min(h)**2
    nt = int(Tfin/dt)
    u = np.hstack([X[X<=0.5],1-X[X>0.5]])
    U = [np.hstack([0,u,0])]
    for t in range(0,nt):
        v = np.linalg.solve(M,np.dot(K,u))
        u = u - dt*v
        if(t%1000 == 0):
            U.append(np.hstack([0,u,0]))
    
    return U



def testHeat():
    x = np.array([0,0.025,0.05,0.125,0.175,0.2,0.25,0.3,0.4,0.425,0.5,0.575,
                  0.6,0.675,0.725,0.75,0.8,0.85,0.95,0.975,1])
    
    r = 0.09
    Tfin = 1
    U = heat1D(x,r,Tfin)
    graph = Graph2D(x,U,"x","u","1D Heat equation solution")
    graph.show()
    
    
if __name__ == "__main__":
    testHeat()
