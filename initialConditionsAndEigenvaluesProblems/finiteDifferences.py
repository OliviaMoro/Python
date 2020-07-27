# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:33:25 2020

@author: moroo
"""
import numpy as np



def matrix(A,B,q,g,a,b,x):
    """
        Computes finite-differences matrix for a differential system of the
        form : y'' + q(x)*y = g(x) where y(a) = A and y(b) = B. Thus :
            - a, b : boundaries (float)
            - A, B : boundaries conditions (float)
            - x : array of float 
            - q, g : functions 
    """
    n = len(x)-2
    M = np.zeros((n,n))
    S = np.ones(n-1)
    h = (b-a)/(n+1)

    c = []
    print("h^2 : {}".format(h**2))
    for i in range(0,n):
        M[i][i] = -2 + h**2*q(x[i+1])
        #cElt = ( (i==1) ? g(x[1])*h**2-A : ( (i==n) ? g(x[n])*h**2-B : g(x[i])*h**2 ) ) 
        cElt = g(x[1])*h**2-A if (i==0) else (g(x[n])*h**2-B if (i==n-1) else g(x[i+1])*h**2)
        #print("i : {}, cElt : {}".format(i,cElt))
        #print("i : {}, Mii : {}".format(i,M[i][i]))
        c.append(cElt)
    
    M += np.diag(S,-1) + np.diag(S,1) 
    
    return M,c
