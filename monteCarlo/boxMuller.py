# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 02:55:37 2020

@author: moroo
"""
import numpy as np
from math import sqrt, log
from random import uniform




def boxMuller(N):
    """
        Box-Muller algorithm implementation :
            N : number of points
    """
    x = np.zeros((N))
    y = np.zeros((N))
    
    i = 0
    while (i < 1000):
        u1 = uniform(0,1)
        u2 = uniform(0,1)
        v1 = 2*u1-1
        v2 = 2*u2-1
        s = v1**2+v2**2
        if (s <= 1):
            x1 = v1*sqrt(-2*log(s)/s)
            x2 = v2*sqrt(-2*log(s)/s)
            x[i] = x1
            y[i] = x2
        else:
            continue
        i += 1
    
    return x,y
