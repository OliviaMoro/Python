# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 02:06:04 2020

@author: moroo
"""

import math
import numpy as np
from scipy.integrate import odeint
import methode_runge_kutta as rk
import methodes_tracer as plt

#constantes du probleme
g = 9.8  # accélération de la pesanteurterrestre : m/s^2
l = 0.2  # longueur du fil : m
m = 0.03 # masse du poids au bout du fil : kg
w0 = math.sqrt(g/l)

def pend(y,t,w0):
    theta, b = y
    dydt = [b,
            -w0**2*math.sin(theta)]
    return dydt


def numpySoluce(y0,dt,n):
    t = np.linspace(0,n*dt,n)
    sol = odeint(pend, y0, t, args=(w0,))

    theta = sol[:,0]
    vtheta = sol[:,1]
    return t,theta,vtheta


def dertheta(t,theta,vtheta):  
    return vtheta
    
def derVtheta(t,theta,vtheta):  
    der = -w0**2*math.sin(theta)
    return der

def testRK4(uCI,dt,n):  
    t = []
    u = []

    t.append(0)
    u.append(uCI) 


    for i in range(1,n+1):
        (tf,uf)=rk.runge_kutta_4(dt,t[i-1],u[i-1][0],u[i-1][1],
        key1=dertheta,key2=derVtheta)
        t.append(tf)
        u.append(uf)
        
    theta = [i for i,j in u]
    vtheta = [j for i,j in u]
    
    return t,theta,vtheta

def testEnergie(theta,vtheta):
    T = np.multiply(0.5*m*l**2,np.square(vtheta))
    V = m*g*l*(1-np.cos(theta))
    E = T + V
    
    return T,V,E


if __name__ == "__main__":
    #Première résolution : question b
    y0 = np.radians([10.,0.])
    dt = 0.005
    n = 500
    #t,theta,vtheta = numpySoluce(y0,dt,n)
    t,theta,vtheta = testRK4(y0,dt,n)
    x = l*np.sin(theta)
    y = -l*np.cos(theta)
    plt.plotGraph(theta,vtheta,r'$\theta$ (rds)',r'$\dot{\theta}$ (rds/s)',
                  "portrait de phase")
    plt.plotGraph(x,y,"x (m)","y (m)","Trajectoire dans Oxy")
    
    #Vérification de l'énergie
    T,V,E = testEnergie(theta,vtheta)
    plt.plotGraph(t,V,"t","V","énergie potentielle selon t")
    plt.plotGraph(t,T,"t","T","énergie cinétique selon t")
    plt.plotGraph(t,E,"t","E","énergie totale selon t")
    print(E[0]-E[n-1])
    
    
    
    