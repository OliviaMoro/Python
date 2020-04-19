# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 05:38:52 2020

@author: moroo
"""
import numpy as np

def H(n,x):
    """
        Hermite's polynomials evaluation's method using the recurrence's 
        relation for a given x up to the n-th polynomial 
    """
    if(n == 0):
        hn = 1
    elif(n == 1):
        hn = 2*x
    else:
        Hnm1 = 1; Hn = 2*x
        for i in range(1,n):
            H = 2*x*Hn - 2*i*Hnm1
            Hnm1 = Hn
            Hn = H
            hn = H
    return hn
  
  
def formHn(n,min,max,N):
    """
        Computes Hermite's polynom Hn between min and max with N points
    """
    pas = abs((max-min)/N)
    x = min
    result = np.array([])
      
    for i in range(0,N):
        result = np.append(result,H(n,x))
        x += pas 
    return result