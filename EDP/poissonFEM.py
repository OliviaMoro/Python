# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:11:29 2020

@author: moroo
"""
import numpy as np
from FEM import matK as Ke, arrayF

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D



def poisson1D(x,f):
    """
        1D Poisson equation resolution (-u''(x) = f(x), u(0) = u(L) = 0) 
        with the finite elements method for a given x array :
            - x : array of values between x = 0 and x = L
            - f : second member function
    """
    n = len(x)-2
    h = x[1:len(x)+1]-x[0:n+1]
    
    K = Ke(n,h)
    F = arrayF(h,f,x)
    u = np.linalg.solve(K,F)
    u = np.hstack([0,u,0])
    return u


def testPoisson():
    def f(x):
        return x*(1-x)
    
    x = np.array([0,0.025,0.05,0.125,0.175,0.2,0.25,0.3,0.4,0.425,0.5,0.575,
                  0.6,0.675,0.725,0.75,0.8,0.85,0.95,0.975,1])
    u = poisson1D(x,f)

    graph = Graph2D(x,[u],"x","u","1D Poisson equation solution")
    graph.show()




if __name__ == "__main__":
    testPoisson()
    