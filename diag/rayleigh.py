# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 04:03:28 2020

@author: moroo
"""
import numpy as np



def coef(A,x):
    """
        Computation of the Rayleigh coefficient :
            - A : square matrix of shape (n,n)
            - x : array of shape (n,)
    """
    n = len(A)
    
    try:
        assert(np.shape(A)==(n,n) and np.shape(x)==(n,))
    except AssertionError:
        print("Shapes aren't compatible.")
        return
    
    num = np.dot(np.transpose(x),np.dot(A,x))
    den = np.dot(np.transpose(x),x)
    
    return num/den


if __name__ == "__main__":
    A = np.array([[2,-1],[-1,2]])
    x = np.transpose(np.array([1,0]))  
    R = coef(A,x)
    print("coef Rayleight : {}".format(R))     