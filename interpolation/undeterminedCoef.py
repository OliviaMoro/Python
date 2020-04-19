# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 01:38:06 2020

@author: moroo
"""

import numpy as np


def getCoef(a,f):
    """
        computes coefficients of the polynomial interpolation of a dataset :
            - a : points
            - f : values
        a and f must have the same length
    """
    try:
        assert(len(a)==len(f))
    except AssertionError:
        print("Given arrays aren't the same length.")
        return
        
    
    vander = np.vander(a,increasing = True)
    delta = np.linalg.det(vander)
    coef = np.array([])
    
    for i in range(0,len(a)):
        X = np.vander(a,increasing = True)
        X[:,i] = f
        coef = np.append(coef,np.linalg.det(X)/delta)
    return coef
    
    
def test():
    a = np.array([-2,0,1])
    f = np.array([-27,-1,0])
    coef = getCoef(a,f)
    print(coef)
    
if __name__ == "__main__":
    test()