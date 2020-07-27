# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 00:23:39 2020

@author: moroo
"""

import numpy as np



def jacobi(A,b,x0,kmax=10,err=1e-4):
    """
        Jacobi method implementation used to solve A*x = b given an initial
        approximation of x :
            - A : square matrix
            - b : array
            - x0 : initial approximation of the solution
    """
    n = len(A)
    k = 0
    x = np.ones(n)
    delta = 1
    
    while (k < kmax):
        k += 1
        for i in range(0,n):
            s = b[i]-np.dot(A[i][:],x0)
            x[i] = x0[i]+s/(A[i][i]*1.)
         
        delta = max(abs(x-x0))
        if (delta < err):
            break
        x0 = np.copy(x)
        print(x)
        
    return x
    

    
if __name__ == "__main__":
    A = np.array([[3.,1.],[-1.,2]])
    b = np.transpose(np.array([2.,-2.]))
    x0 = np.transpose(np.array([0,0]))
    
    x1 = jacobi(A,b,x0,6)
    print(x1)