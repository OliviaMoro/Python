# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:48:46 2020

@author: moroo
"""
import numpy as np

def polynome(x,x0,f):
    """
        Approximates Lagrange polynome for the values 'f' at the given 
        points 'x0' at x 
    """
    try:
        assert(len(x0)==len(f))
    except AssertionError:
        print("Given arrays aren't the same length.")
        return

    P = f
    j = 1
    
    while (len(P)>1):
        L = np.array([])
        n = len(P)
        

        for i in range(0,n-1):
            temp = ((x-x0[i])*P[i+1]-(x-x0[i+j])*P[i])/(x0[i+j]-x0[i])
            L = np.append(L,temp)
        P = L
        j += 1
    
    return P[0]



if __name__ == "__main__":
    x0 = np.array([-2,-1,0,1,2,3])
    f = np.array([-5,1,1,1,7,25])
    x = 3.5
    result = polynome(x,x0,f)
    print("result : {}".format(result))
    
    x0 = np.array([1,1.3,1.6,1.9,2.2])
    f = np.array([0.7651,0.6200,0.4554,0.2818,0.1103])
    x = 1.5
    result = polynome(x,x0,f)
    print("result : {}".format(result))