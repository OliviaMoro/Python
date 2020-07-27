# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:37:50 2020

@author: moroo
"""
import numpy as np
from FDM import Kpos, Kneg, Kimp, KLax

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D



def transport1D(x,c,Tfin,r,opt="upwind"):
    """
        Transport equation resolution (du/dt + c*du/dx = 0 with u(x,0) = f(x))
        for x between x[0] and x[-1] and t between 0 and Tfin. The stability 
        of the algorithm depends on r (check FDM documentation). The method 
        of integration can be specified via opt.
    """
    npt = len(x)
    nx = npt-2
    h = (x[-1]-x[0])/(nx+1)
    X = x[1:-1]
    K = np.zeros((nx,nx))
    
    dt = abs(r*h/c)
    nt = abs(int(Tfin/dt))
    
    if (opt == "upwind"):
        K = Kpos(nx,h) if (c>0) else Kneg(nx,h) 
    elif (opt == "imp"):
        K = Kimp(nx,h,c,dt)  
    elif (opt == "lax"):
        K = -1*KLax(nx,h,c,dt)
    
    #u = np.hstack((np.where(X > 1,X,1),np.where(X <= 1,X,0)))
    u = np.hstack((np.ones_like(X[X <=1]), np.zeros_like(X[X>1])))
    for t in range(0,nt):
        u  = u-c*dt*np.dot(K,u) if (opt != "imp") else np.dot(K,u)
    u = np.hstack([0,u,0])
    return u



def testTransport():
    x = np.linspace(0,4,81)
    c = 1
    Tfin = 2
    r = 0.9
    opt = "imp"
    U = transport1D(x,c,Tfin,r,opt="imp")
    
    graph = Graph2D(x,[U],"x","u","Transport equation {}".format(opt))
    graph.show()   



if __name__ == "__main__":
    testTransport()