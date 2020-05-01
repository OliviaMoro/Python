# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:57:47 2020

@author: moroo
"""
from math import tan, cos, sin
from bissection import bissection
from newtonRaphson import newtonRaphson
from fixedPoint import iterations

import numpy as np
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


def exo3():
    a = 0.5
    b = 1.5
    tol = 1e-1
    
    def f(x):
        return 1/tan(x) -x
    
    def derf(x):
        return -1/sin(x)**2 -1
    
    x = np.linspace(a,b,50)
    y = np.divide(1,np.tan(x))
    Graph2D(x,[x,y],'x','f(x)','Fixed point ?',['y = x','cotan(x)']).show()
    
    # question b
    xb = bissection(a,b,f,tol)
    print("Bissection : x* = {}".format(xb))
    
    # question c
    xc = newtonRaphson(1,tol,f,derf)
    print("Newton Raphson : x* = {}".format(xc))
    
    

if __name__ == "__main__":
    exo3() 