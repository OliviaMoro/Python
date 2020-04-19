# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 02:11:07 2020

@author: moroo
"""

from math import pi
import rungeKuttaMethod as rk
import numpy as np

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D, plot3DGraph


################### PROBLEM'S CONSTANTS ###########################
h = 6.626e-34             # Plank's constants [J.s]
epsilon0 = 8.854187e-12   # Vacuum permittivity [F/m]
mp = 1.67e-27             # proton's mass [kg]
me = 9.11e-31             # electron's mass [kg]
qe = 1.6e-19              # electron's charge [C]



################### PARTICLE CHOICE ###########################
B0 = 3.12e-5   
m = me
q = qe
omega = q*B0/m
T = 2*pi/omega                   # time unit : cyclotron pulsation 
a0 = h**2*epsilon0/(pi*me*qe**2) # distance unit : Bohr radius



def derx(t,x,vx,y,vy,z,vz):
    return vx


def derVx(t,x,vx,y,vy,z,vz):
    return 2*pi*vy
    

def dery(t,x,vx,y,vy,z,vz):
    return vy


def derVy(t,x,vx,y,vy,z,vz):
    return -2*pi*vx


def derz(t,x,vx,y,vy,z,vz):
    return vz

def derVz(t,x,vx,y,vy,z,vz):
    return 0


def integrationRK4(uCI,dt,n):  
    t = []
    u = []

    t.append(0)
    u.append(uCI) 

    for i in range(1,n+1):
        (tf,uf)=rk.rungeKutta4(dt,t[i-1],u[i-1][0],u[i-1][1],u[i-1][2],u[i-1][3],
        u[i-1][4],u[i-1][5],key1=derx,key2=derVx,key3=dery,key4=derVy,key5=derz,
        key6=derVz)
        t.append(tf)
        u.append(uf)
        
    x = [i for i,j,k,l,m,n in u]
    vx = [j for i,j,k,l,m,n in u]
    y = [k for i,j,k,l,m,n in u]
    vy = [l for i,j,k,l,m,n in u] 
    z = [m for i,j,k,l,m,n in u]
    vz = [n for i,j,k,l,m,n in u]
    
    return t,x,vx,y,vy,z,vz


def particuleEnergy(vx,vy,vz):
    E = []
    E = np.multiply(0.5*m,np.square(vx)+np.square(vy)+np.square(vz))
    return E


if __name__ == "__main__":
    print("T : ",T)
    print("a0 :",a0/1e-10)
    
    u0 = [5,1,0,0.1,0,-0.2]
    dt = 0.01
    n = 1000
    
    t,x,vx,y,vy,z,vz = integrationRK4(u0,dt,n)
    E = particuleEnergy(vx,vy,vz)
    
    Graph2D(t,[E],"timz(s)","Energy(J)","Energy's conservation").show()
    plot3DGraph(x,y,z,"x(Rt)","y(Rt)","z(Rt)","Particle's trajectory")
    
    
    