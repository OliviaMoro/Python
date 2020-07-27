# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:58:49 2020

@author: moroo
"""
import numpy as np
from FDM import matWexp, matWimp, timeIterations

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D 



def waves(n,h,c,Tf,u0,opt="exp"):
    """
        1D waves equation resolution implementation using finites differences 
        method (d^2u/dt^2-c**2*d^2u/dx^2) = 0) :
            - n : system matrix size
            - h : space step
            - c : waves propagation velocity
            - Tf : final time
            - u0 : initial condition
            - opt : - "exp" explicit euler method,
                    - "imp" regressive euler method.       
    """
    dt = 0.9*h/c if (opt == "exp") else 0.1
    #Differential system Matrix
    A = matWexp(n,h,c,dt) if (opt == "exp") else matWimp(n,h,c,dt)
    
    #Time integration method
    f = lambda A,u0,u1 : np.dot(A,u1)-u0 
    if (opt == "imp"):
        f = lambda A,u0,u1 : np.linalg.solve(A,2*u1-u0)
     
    graphU = timeIterations(dt,Tf,u0,A,f,plt=1)
    return graphU


if __name__ == "__main__":
    c = 1
    npt = 81; n = npt-2
    xi = 0; xf = 4.; h = (xf-xi)/(n+1)
    X = np.linspace(xi,xf,npt); x = X[1:-1]
    
    Tf = 1.
    z = np.zeros(n)
    p1 = z[x <= 1.5]; p4 = z[x > 2.5]
    x2 = x[x > 1.5]; p2 = x2[x2 <= 2]-1.5
    x3 = x[x > 2]; p3 = 2.5-x3[x3 <= 2.5]
    u0 = np.hstack([p1,p2,p3,p4])
    
    graphU = waves(n,h,c,Tf,u0,opt="imp")
    graph = Graph2D(X,graphU,"x","u","Waves equation resolution")
    graph.show()
    
    
    