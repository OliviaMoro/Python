# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 02:06:58 2020

@author: moroo
"""

import math
import numpy as np
from scipy.integrate import odeint
import rungeKuttaMethod as rk

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


###################################################### problem's constants
g = 9.8  # acceleration of the earth’s gravity : m/s^2
l = 67   # wire's length : m
m = 28   # mass of the weight at the end of the wire : kg
Tt = 365.25*24*60*60
omega = 2*math.pi/Tt
lat = math.pi*48/180.
alpha = omega*math.sin(lat) 
w0 = math.sqrt(g/l)
###################################################### problem's constants

def pend(y0,t,w0,alpha):
    x,vx,y,vy = y0
    dydt = [vx,
            -x*w0**2 + 2*alpha*vy,
            vy,
            -y*w0**2 - 2*alpha*vx]
    return dydt


def numpySoluce(y0,dt,n):
    t = np.linspace(0,n*dt,n)
    sol = odeint(pend, y0, t, args=(w0,alpha))

    x = sol[:,0]
    vx = sol[:,1]
    y = sol[:,2]
    vy = sol[:,3]
    return t,x,vx,y,vy


def dx(t,x,vx,y,vy):  
    return vx
    

def dVx(t,x,vx,y,vy):  
    der =  -x*w0**2 + 2*alpha*vy
    return der


def dy(t,x,vx,y,vy):  
    return vy
    

def dVy(t,x,vx,y,vy):  
    der =  -y*w0**2 - 2*alpha*vx
    return der


def testRK4(uCI,dt,n):  
    t = []
    u = []

    t.append(0)
    u.append(uCI) 

    for i in range(1,n+1):
        (tf,uf)=rk.rungeKutta4(dt,t[i-1],u[i-1][0],u[i-1][1],u[i-1][2],u[i-1][3],
        key1=dx,key2=dVx,key3=dy,key4=dVy)
        t.append(tf)
        u.append(uf)
        
    x = [i for i,j,k,l in u]
    vx = [j for i,j,k,l in u]
    y = [k for i,j,k,l in u]
    vy = [l for i,j,k,l in u]
    
    return t,x,vx,y,vy



if __name__ == "__main__":
    y0 = np.array([15.,0,0,0])
    dt = 0.005
    n = 5000
    #t,theta,vtheta = numpySoluce(y0,dt,n)
    t,x,vx,y,vy = testRK4(y0,dt,n)

    Graph2D(x,[y],r'x (m)',r'y (m)',"Pendulum's trajectory").show()


