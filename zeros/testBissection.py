# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:09:08 2020

@author: moroo
"""

from math import exp
from bissection import bissection
import numpy as np
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D

# racine entre -1 et 1
def test1(x):
    return x**5 - 2*x**4 + 100*x**3 - 2

# racine entre -2 et 0
def test2(x):
    return x + exp(x)
    


if __name__ == "__main__":
    tol = 1e-5
    n = 100
    x1 = np.linspace(-5,5,n)
    x2 = np.linspace(-2,5,n)
    f1 = np.array([])
    f2 = np.array([])
    
    for i in range(0,n):
        f1 = np.append(f1,test1(x1[i]))
        f2 = np.append(f2,test2(x2[i]))
    
    Graph2D(x1,[f1]).show()
    Graph2D(x2,[f2]).show()
    
    racine1 = bissection(-2,2,test1,tol)
    racine2 = bissection(-2,0,test2,tol)
    print("racine1 : {}, racine2 : {}".format(racine1,racine2))
    
    
