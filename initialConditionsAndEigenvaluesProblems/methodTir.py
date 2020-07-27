# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 22:01:31 2020

@author: moroo
"""
import numpy as np

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'integrator')))
from rungeKuttaMethod import rungeKutta4, rungeKutta2
from eulerMethod import explicitEuler, regressiveEuler



def tirEuler(n,L,y0,z0,yDer,zDer):
    h = L/n
    m = int(n/2)
    x = np.zeros((n)); u = np.zeros((n,2))
    
    x[0] = 0; x[-1] = L
    u[0,:] = [y0[0],z0[0]] 
    u[-1,:] = [y0[-1],z0[-1]]
    
    for i in range(1,m+1):
        (xf,uf)=explicitEuler(h,x[i-1],u[i-1][0],u[i-1][1],key1=yDer,key2=zDer)
        x[i] = xf
        u[i,:] = uf
        
    for i in range(n-2,m,-1):
        (xf,uf)=regressiveEuler(h,x[i+1],u[i+1][0],u[i+1][1],key1=yDer,key2=zDer)
        x[i] = xf
        u[i,:] = uf
    
    y = [i for i,j in u]
    z = [j for i,j in u]

    return x,y,z



def tirRK(n,L,y0,z0,yDer,zDer,x0=0,opt=2):
    """
        Integrates between x = 0 or x0 and x = L :
            opt = 2 : rungeKutta2
            opt = 4 : rungeKutta4
    """
    h = L/n
    x = []; u = []
    
    x.append(x0)
    u.append([y0,z0]) 
    
    for i in range(1,n+1):
        if(opt == 2):
            (xf,uf)= rungeKutta2(h,x[i-1],u[i-1][0],u[i-1][1],key1=yDer,key2=zDer)
        elif(opt == 4):    
            (xf,uf)= rungeKutta4(h,x[i-1],u[i-1][0],u[i-1][1],key1=yDer,key2=zDer)
        elif(opt == 0):
            (xf,uf)= explicitEuler(h,x[i-1],u[i-1][0],u[i-1][1],key1=yDer,key2=zDer)
        x.append(xf)
        u.append(uf)
    
    y = [i for i,j in u]
    z = [j for i,j in u]

    return x,y,z
