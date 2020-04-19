# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:11:52 2020

@author: moroo
"""
import numpy as np
from math import isclose


def iterations(f,x0,tol,nMax):
    i = 0
    delta = f(x0)-x0
    x = np.array([])
    y = np.array([])
    
    while (not isclose(delta,0,rel_tol=tol, abs_tol=0.0) and i <= nMax):
        x = np.append(x,x0)
        x = np.append(x,x0)
        y = np.append(y,x0)
        y = np.append(y,f(x0))
        
        x0 = f(x0)
        delta = abs(f(x0)-x0)
        i += 1
        
    return x0,x,y


        
    