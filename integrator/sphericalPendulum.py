# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 02:06:27 2020

@author: moroo
"""

import math
import numpy as np
from scipy.integrate import odeint
import rungeKuttaMethod as rk

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D, plot3DGraph

###################################################### problem's constants
g = 9.8  # acceleration of the earth’s gravity : m/s^2
l = 0.2  # wire's length : m
m = 0.03 # masse du poids au bout du fil : kg
w0 = math.sqrt(g/l)
###################################################### problem's constants

def pend(y,t,w0):
    theta,vtheta,phi,vphi = y
    dydt = [vtheta,
            math.sin(theta)*(vphi**2*math.cos(theta)-w0**2),
            vphi,
            -2*vphi*vtheta/math.tan(theta)]
    return dydt


def numpySoluce(y0,dt,n):
    t = np.linspace(0,n*dt,n)
    sol = odeint(pend, y0, t, args=(w0,))

    theta = sol[:,0]
    vtheta = sol[:,1]
    phi = sol[:,2]
    vphi = sol[:,3]
    return t,theta,vtheta,phi,vphi


def dtheta(t,theta,vtheta,phi,vphi):  
    return vtheta
    

def dVtheta(t,theta,vtheta,phi,vphi):  
    der = math.sin(theta)*(vphi**2*math.cos(theta)-w0**2)
    return der


def dphi(t,theta,vtheta,phi,vphi):  
    return vphi

    
def dVphi(t,theta,vtheta,phi,vphi):  
    der = -2*vphi*vtheta/math.tan(theta)
    return der


def testRK4(uCI,dt,n):  
    t = []
    u = []

    t.append(0)
    u.append(uCI) 

    for i in range(1,n+1):
        (tf,uf)=rk.rungeKutta4(dt,t[i-1],u[i-1][0],u[i-1][1],u[i-1][2],u[i-1][3],
        key1=dtheta,key2=dVtheta,key3=dphi,key4=dVphi)
        t.append(tf)
        u.append(uf)
        
    theta = [i for i,j,k,l in u]
    vtheta = [j for i,j,k,l in u]
    phi = [k for i,j,k,l in u]
    vphi = [l for i,j,k,l in u]
    
    return t,theta,vtheta,phi,vphi



def testEnergy(theta,vtheta,phi,vphi):
    T = np.multiply(0.5*m*l**2,np.square(vtheta))+ np.multiply(0.5*m*l**2,np.square(np.multiply(vphi,np.sin(theta))))
    V = m*g*l*(1-np.cos(theta))
    E = T + V
    
    return T,V,E


if __name__ == "__main__":
    y0 = np.radians([60.,0.1,50.,0.])
    dt = 0.005
    n = 500
    #t,theta,vtheta = numpySoluce(y0,dt,n)
    t,theta,vtheta,phi,vphi = testRK4(y0,dt,n)
    x = l*np.multiply(np.sin(theta),np.cos(phi))
    y = l*np.multiply(np.sin(theta),np.sin(phi))
    z = -l*np.cos(theta)
    
    #Trajectory
    Graph2D(theta,[vtheta],r'$\theta$ (rds)',r'$\dot{\theta}$ (rds/s)',
                  "Phase portrait").show
    Graph2D(t,[phi],"t",r'$\phi$ (rds)',"Phase portrait").show()
    plot3DGraph(x,y,z,"x (m)","y (m)","z (m)","Trajectory")
    

    T,V,E = testEnergy(theta,vtheta,phi,vphi)
    legend = ['V','T','E']
    Graph2D(t,[V,T,E],"t","Energie","Energy's conservation",legend).show()
