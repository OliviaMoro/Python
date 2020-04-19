# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:20:01 2020

@author: moroo
"""

from math import exp, cos, sin
from newtonRaphson import newtonRaphson


def exo2():
    k = 50
    x0 = -0.1
    tol = 1e-4
    
    def f(x):
        return x+exp(-k*x**2)*cos(x)
    
    def derf(x):
        return 1-exp(-k*x**2)*(2*k*x*cos(x)+sin(x))
    
    newtonRaphson(x0,tol,f,derf)


if __name__ == "__main__":
    exo2() 