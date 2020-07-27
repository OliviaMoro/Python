# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:24:28 2020

@author: moroo
"""
import numpy as np
from FDM import matK as Kd

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import plotSurf



def poisson2D(x,y,F):
    """
        2D Poisson equation resolution (-∇u = f(x), u(0) = u(L) = 0) 
        with the finite elements method for a given x array :
            - x : array of values between x = 0 and x = L
            - f : second member function
    """
    nx = len(x)-2
    hx = (x[0]-x[-1])/(nx+1)
    
    ny = len(y)-2
    hy = (y[0]-y[-1])/(ny+1)

    Kx = Kd(nx,hx)
    Ky = Kd(ny,hy)
    K2D = np.kron(np.eye(ny),Kx)+np.kron(Ky,np.eye(nx))
    
    U = np.linalg.solve(K2D,F)
    u = np.reshape(U,(nx,ny))
        
    return u



def testPoisson():
    x = np.linspace(0,1,21)
    y = np.linspace(0,4,41)
    X = x[1:-1]
    Y = y[1:-1]

    F =  100*np.kron(Y*(4-Y),X*(1-X))
    u = poisson2D(x,y,F)
    zeroY = np.zeros((1,len(y)))
    zeroX = np.zeros((len(x)-2,1))
    
    u = np.vstack((zeroY,np.hstack((zeroX,u,zeroX)),zeroY))
    print(np.shape(u))
    X,Y = np.meshgrid(x,y)
    print(np.shape(X),np.shape(Y))
    
    plotSurf(X,Y,u.transpose(),"x","y","u","Poisson equation (Dirichlet conditions)")



if __name__ == "__main__":
    testPoisson()
