# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 01:52:40 2020

@author: moroo
"""

import numpy as np

def gaussSeidel(A,b,x0,kmax=10,err=1e-4):
    """
        Jacobi method implementation used to solve A*x = b given an initial
        approximation of x using previously computed x value to accelerate the 
        convergence (Gauss-Seidel method) :
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
            s1 = np.dot(A[i][0:i],x[0:i])
            s2 = np.dot(A[i][i+1:n],x0[i+1:n])
            x[i] = (b[i]-s1-s2)/A[i][i]
         
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
    
    x1 = gaussSeidel(A,b,x0,4)
    print(x1)