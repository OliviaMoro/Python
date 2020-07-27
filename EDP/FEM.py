# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:16:07 2020

@author: moroo
"""
import numpy as np
from scipy.integrate import quad
from FDM import matK as Kd



def matK(n,h):
    """
        Definition of the stiffness matrix (tridiagonal matrix) of size n 
        for different step sizes h for the 1D Laplace/Poisson equation :
            - h : arrays of step sizes
        With h elements all identical to one another, K is the same as 
        defined in FDM.matK.
    """
    K = np.zeros((n,n))
    K[0][0] = 1/h[0]
    for i in range(1,n):
        K[i-1][i-1] = K[i-1][i-1]+1/h[i] 
        K[i][i] = 1/h[i]
        K[i-1][i] = -1/h[i] 
        K[i][i-1] = K[i-1][i]
    K[n-1][n-1] = K[n-1][n-1]+1/h[n]
    return K



def matM(n,h):
    """
        Definition of the mass matrix (tridiagonal matrix) of size n 
        for different step sizes h for the 1D heat equation :
            - h : arrays of step sizes
    """
    M = np.zeros((n,n))
    M[0][0] = h[0]/3.
    for i in range(1,n):
        M[i-1][i-1] = M[i-1][i-1]+h[i]/3. 
        M[i][i] = h[i]/3.
        M[i-1][i] = h[i] /6.
        M[i][i-1] = M[i-1][i]
    M[n-1][n-1] = M[n-1][n-1]+h[n]/3.
    return M
    
    

def matMct(n,h):
    """
        Definition of the mass matrix (tridiagonal matrix) of size n 
        for the 1D heat equation with a constant step h.
    """
    D = np.eye(n,n)
    S = np.ones(n-1)
    M = 2/3.*D+1/6.*np.diag(S,-1)+1/6.*np.diag(S,1)

    return h*M


    
def matCD(n,h,eps,lamb):
    """
        Convection diffusion matrix definition of size n with constant step h :
            - -eps*u''(x)+lamb*u'(x) = 0
    """
    S = np.ones(n-1)
    A = (1*np.diag(S,1)-1*np.diag(S,-1))/2.
    return eps*h*Kd(n,h)+lamb*A

    

def arrayF(h,f,x):
    """
        Computation of f values at the x points :
            - h : step sizes array
            - f : second member function
    """
    n = len(x)-2
    X = x[1:-1]
    
    F = np.zeros(n)
    F[0],err = quad(lambda u: f(u)*(u-x[0])/h[0],x[0],X[0])
    for i in range(1,n):
        # On [xi-1,xi] : 
        F[i-1],err = F[i-1]+quad(lambda u: f(u)*(X[i]-u)/h[i],X[i-1],X[i])
        # On [xi,xi+1]
        F[i],err = quad(lambda u: f(u)*(u-X[i-1])/h[i],X[i-1],X[i])
    F[-1],err = F[-1]+quad(lambda u: f(u)*(x[-1]-u)/h[-1],X[-1],x[-1])
    
    return F



    
        