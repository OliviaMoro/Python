# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:11:52 2020

@author: moroo
"""
import numpy as np
from math import isclose


def iterations(f,x0,tol,nMax):
    """
        Implements the fixed point method to find the solution of x = f(x).
        A starting point x0 is given along with a tolerance tol and a 
        maximum number of iterations nMax. Returns :
            - x0 : the solution
            - x : reconstructs the path along the x-axis used to find x0
            - y : reconstructs the path along the y-axis used to find x0   
    """
    i = 0
    delta = f(x0)-x0
    x = np.array([])
    y = np.array([])
    
    while (not isclose(delta,0,rel_tol=tol, abs_tol=tol) and i <= nMax):
        x = np.append(x,x0)
        x = np.append(x,x0)
        y = np.append(y,x0)
        y = np.append(y,f(x0))
        
        delta = abs(f(x0)-x0)
        x0 = f(x0)
        i += 1
        
    return x0,x,y


        
    