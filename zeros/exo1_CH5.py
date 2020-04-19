# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:08:46 2020

@author: moroo
"""
from math import sin, cos
from bissection import bissection
from newtonRaphson import newtonRaphson
from regulaFalsi import regulaFalsi
from fixedPoint import iterations
from secant import secant

import numpy as np
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


def exo1():
    
    def f(x):
        return x-0.2*sin(x)-0.5
    
    def derf(x):
        return 1-0.2*cos(x)
    
    def g(x):
        return 0.2*sin(x)+0.5
    
    tol = 1e-5
    n = 20
    a = 0
    b = 1
    # with bissection method
    xa = bissection(a,b,f,tol)
    print("Bissection : x* = {}".format(xa))
    
    # with regulaFalsi method
    xb = regulaFalsi(a,b,f,tol,n)
    print("Regula Falsi : x* = {}".format(xb))
    
    # with NewtonRaphson method
    xc = newtonRaphson(b,tol,f,derf)
    print("Newton Raphson : x* = {}".format(xc))
    
    # with fixed point method
    xd,x,y = iterations(g,0,tol,n)
    xf = np.linspace(a,b,50)
    yf = [g(x) for x in xf]
    print("Fixed Points : x* = {}".format(xd))
    legend = ['x','f','iteration']
    graph = Graph2D([xf,xf,x],[xf,yf,y],'x','f(x)','f(x)=x',legend)
    #graph.show()
    
    # with secant method
    xe = secant(a,b,f,tol,n)
    print("Secant : x* = {}".format(xe))


if __name__ == "__main__":
    exo1() 