# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:39:23 2020

@author: moroo
"""
import numpy as np
from math import sqrt

def leastSquare(x,y,si2):   
    """
        Least squares method implementation to find coefficients a and b 
        satisfying a*x + b = y :
            - si2 = 1/sigma_{i}**2 where sigma_{i}**2 is y dataset variance
    """
    u = np.divide(np.ones((len(x))),si2)
    x2 = np.square(x)
    xy = np.multiply(x,y)
    S = np.sum(u)

    Sx = np.sum(np.multiply(x,u))
    Sxx = np.sum(np.multiply(x2,u))
    Sy = np.sum(np.multiply(y,u))
    Sxy = np.sum(np.multiply(xy,u))
    delta = S*Sxx-Sx*Sx

    a = (S*Sxy-Sx*Sy)/delta
    b = (Sxx*Sy-Sx*Sxy)/delta
    sA = sqrt(S/delta)
    sB = sqrt(Sxx/delta)
    
    return a,b,sA,sB
