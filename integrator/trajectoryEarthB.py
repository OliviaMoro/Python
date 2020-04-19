# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 02:53:20 2020

@author: moroo
"""
from math import pi, cos, sin,sqrt
import rungeKuttaMethod as rk
import numpy as np

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D, plot3DGraph


################### PROBLEM'S CONSTANTS ###########################
R = 6371000                                # Earth radius [m]
lat = 46*pi/180.                           # latitude France [radians]
long = 2*pi/180.                           # longitude France [radians]

xi = R*cos(lat)*cos(long)
yi = R*cos(lat)*sin(long)
zi = R*sin(lat)

qe = 1.6e-19                               # electron's charge [C]
m_e = 9.11e-31                             # electron's mass [kg]
m_p = 1.67e-27                             # proton's mass [kg]
mu = 4*pi*1e-7                             # void's permeability
B0 = 3.12e-5                               # terrestrial magnetic fields at 
                                           # the equator [T]
B = 46600e-9                                
Mz = -4*pi*R**4*B/(mu*sqrt(3*zi**2+R**2))  # Earth magnetic moment

################### PARTICULE CHOICE ###########################
m = 4.0*m_p                                
q = 2.0*qe
C = q*mu*Mz/(4*pi*m*R**3)


def Bnorm(r,m):
    rnorm = np.linalg.norm(r)
    C = Mz*mu/(4*pi*B0*R**3)
    B = C*(3*r*np.dot(m,r)-rnorm**2*m)
    return B


def derx(t,x,vx,y,vy,z,vz):
    return vx


def derVx(t,x,vx,y,vy,z,vz):
    r = sqrt(x**2+y**2+z**2)
    der = C*(vy*(3*z**2-r**2)-3*vz*y*z)/r**5
    return der
    

def dery(t,x,vx,y,vy,z,vz):
    return vy


def derVy(t,x,vx,y,vy,z,vz):
    r = sqrt(x**2+y**2+z**2)
    der = C*(3*vz*x*z-vx*(3*z**2-r**2))/r**5
    return der


def derz(t,x,vx,y,vy,z,vz):
    return vz


def derVz(t,x,vx,y,vy,z,vz):
    r = sqrt(x**2+y**2+z**2)
    der = C*3*z*(vx*y-vy*x)/r**5
    return der


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
    ev = 1.602176634e-19
    c = 3e8
    E0 = m*c**2
    print("E0 :",E0)
    print("mz : ",Mz)
    
    #m = E0/(c**2)
    vx0 = 0.1
    vy0 = 0.1
    vz0 = 0.1
    x0 = -4.
    y0 = -1.
    z0 = -6.
    u0 = [x0,vx0,y0,vy0,z0,vz0]
    dt = 0.0001
    n = 1000000
    
    t,x,vx,y,vy,z,vz = integrationRK4(u0,dt,n)
    E = particuleEnergy(vx,vy,vz)
    
    Graph2D(t,[E],"time(s)","Energy(J)","Energy's conservation").show()
    Graph2D(x,[y],"x(Rt)","y(Rt)").show()
    plot3DGraph(x,y,z,"x(Rt)","y(Rt)","z(Rt)","Particle's trajectory")    
    

