# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:21:08 2020

@author: moroo
"""
import numpy as np



def matK(n,h):
    """
        Definition of the stiffness matrix (tridiagonal matrix) of size n
        for the 1D Laplace/Poisson equation :
            - diagonal elements equal to 2
            - upper diagonal values : -1
            - lower diagonal values : -1
            
    """
    D = np.eye(n,n)
    S = np.ones(n-1)
    K = 2*D-np.diag(S,-1)-np.diag(S,1)
    return K/h**2



def matA(n,h):
    """
        Definition of the tridiagonal matrix of size n :
            - diagonal elements equal to 0
            - upper diagonal values : -1
            - lower diagonal values : 1
    """
    S = np.ones(n-1)
    A = np.diag(S,-1)-np.diag(S,1)
    return A/h



def matHexp(n,h,dt):
    """
        Definition of the tridiagonal matrix A of size n for the 1D heat 
        equation with the explicit Euler method (stable if dt/h^2 <= 1/2) :
            - dt : time step       
    """
    I = np.eye(n)
    A = I-dt*matK(n,h)
    return A



def matHimp(n,h,dt,u):
    """
        Definition of the tridiagonal matrix A of size n for the 1D heat 
        equation with the implicit Euler method (always stable) :
            - dt : time step       
    """
    I = np.eye(n)
    A = I+dt*matK(n,h)
    u = np.linalg.solve(A,u)
    return u



def matHcn(n,h,dt,u):
    """
        Definition of the tridiagonal matrix A of size n for the 1D heat 
        equation with the Crank-Nicolson method (always stable) :
            - dt : time step      
    """
    I = np.eye(n)
    A = I+dt/2.*matK(n,h)
    B = I-dt/2.*matK(n,h)
    u = np.linalg.solve(A,np.dot(B,u))
    return u



def Kpos(n,h):
    """
        Definition of the matrix of size n for the 1D Bürgers equation, 
        transport equation du/dt+c*du/dx = 0 with the progressive upwind
        pattern :
            - h : space step
            - stable under the condition 0 < c*dt/h < 1
    """
    S = np.ones((n-1))
    K = np.eye(n)-np.diag(S,-1)
    return K/h



def Kneg(n,h):
    """
        Definition of the matrix of size n for the 1D Bürgers equation, 
        transport equation du/dt+c*du/dx = 0 with the regressive upwind
        pattern : 
            - stable under the condition 0 < -c*dt/h < 1 (thus c < 0)
    """     
    S = np.ones((n-1))
    K = -np.eye(n,n)+np.diag(S,1)
    return K/h



def Kimp(n,h,c,dt):
    """
        Definition of the matrix of size n for the 1D Bürgers equation, 
        transport equation du/dt+c*du/dx = 0 with the implicit euler
        pattern : 
            - always stable
    """     
    K = np.linalg.inv(np.eye(n,n)- dt*c/2.*matA(n,h))
    return K
    


def KLax(n,h,c,dt):
    """
        Definition of the matrix of size n for the 1D Bürgers equation, 
        transport equation du/dt+c*du/dx = 0 with the Lax-Wendroff
        pattern : 
            - stable under the condition 0 < |c*dt/h| < 1 
    """     
    A = matA(n,h)
    K = matK(n,h)
    M = c*dt/2.*A - (c*dt)**2/2.*K
    return M



def matWexp(n,h,c,dt):
    """
        Matrix definition for the 1D waves equation with the explicit pattern
        (stable for h/(c*dt) >= 1) :
            - n : matrix size
            - h : space step
            - dt : time step
            - c : velocity
    """
    I = np.eye(n,n)
    r = c**2*dt**2
    A = 2*I-r*matK(n,h)
    return A



def matWimp(n,h,c,dt):
    """
        Matrix definition for the 1D waves equation with the implicit pattern
        (always stable) 
    """
    I = np.eye(n,n)
    r = c**2*dt**2
    A = I+r*matK(n,h)
    return A



def timeIterations(dt,Tf,u0,A,f,plt=10):
    """
        Time integration of a differential system represented by the matrix
        A :
            - dt : time step
            - Tf : final time
            - u0 : initial conditions
            - f : integration method
            - plt : the solution is saved every plt time step
    """
    graphU = []
    graphU.append(np.hstack([0,u0,0]))

    # time iterations
    u1 = np.copy(u0)
    nt = int(Tf/dt)

    for i in range(0,nt+1):
        u = f(A,u0,u1)
        u0 = u1
        u1 = u
        if (i%plt == 0):
            graphU.append(np.hstack([0,u,0]))
            
    return graphU





 
    
    