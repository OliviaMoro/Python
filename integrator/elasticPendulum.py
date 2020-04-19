# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 04:46:03 2020

@author: moroo
"""

import math
import numpy as np
from scipy.integrate import odeint
import rungeKuttaMethod as rk

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D, plotSurf, plotContour


# Problem's constants
m = 0.2
g = 9.8
r0 = 0.44
k = 17.8

def plotPotentiel():
    r = np.arange(0, 2, 0.05)
    theta = np.arange(-math.pi, math.pi, math.pi/10.)
    r, theta = np.meshgrid(r, theta)
    V = 0.5*k*(r-r0)**2-m*g*r*np.cos(theta)

    plotSurf(r,theta,V,'r (m)',r'$\theta$(radians)','','Potential energy')
    plotContour(r,theta,V,'r (m)',r'$\theta$(radians)','Potential energy')


def pend(y,t,m,g,r0,k):
    r, a, theta, b = y
    dydt = [a,
            r*b*b-k*(r-r0)/m+g*math.cos(theta),
            b,
            -2*a*b/r-g*math.sin(theta)/r]
    return dydt


def numpySoluce(y0,dt,n):
    #y0 = [0.66,0,0.03,0]
    t = np.linspace(0,n*dt,n)
    sol = odeint(pend, y0, t, args=(m, g, r0, k))
    
    r = sol[:,0]
    vr = sol[:,1]
    theta = sol[:,2]
    vtheta = sol[:,3]
    return t,r,vr,theta,vtheta


def derR(t,r,vr,theta,vtheta):
    return vr
    

def derVr(t,r,vr,theta,vtheta):  
    der = r*vtheta**2+g*math.cos(theta)-k/m*(r-r0)
    return der
    

def dertheta(t,r,vr,theta,vtheta):  
    return vtheta
    

def derVtheta(t,r,vr,theta,vtheta):  
    der = -(2*vr*vtheta+g*math.sin(theta))/r
    return der


def testRK4(uCI,dt,n):  
    t = []
    u = []

    t.append(0)
    u.append(uCI) 


    for i in range(1,n+1):
        (tf,uf)=rk.rungeKutta4(dt,t[i-1],u[i-1][0],u[i-1][1],u[i-1][2],u[i-1][3],
        key1=derR,key2=derVr,key3=dertheta,key4=derVtheta)
        t.append(tf)
        u.append(uf)
        
    r = [i for i,j,k,l in u]
    vr = [j for i,j,k,l in u]
    theta = [k for i,j,k,l in u]
    vtheta = [l for i,j,k,l in u]
    
    return t,r,vr,theta,vtheta


def testEnergy(r,vr,theta,vtheta):
    E = []
    T = []
    V = []
    
    for i in range(0,len(r)):
        Ec = 0.5*m*(vr[i]**2+r[i]**2*vtheta[i]**2)
        Ep = 0.5*k*(r[i]-r0)**2-m*g*math.cos(theta[i])*r[i]
        T.append(Ec)
        V.append(Ep)
        E.append(Ec+Ep)
    
    return T,V,E

    
def getCartesianArray(r,theta):
    x = r*np.sin(theta)
    y = r*np.cos(theta)
    return x, y    


def aniPendule(dt,n,t,x,y):
    xdata = []
    ydata = []
    
    fig,ax = plt.subplots()
    ax.set_xlim(np.min(x)-0.01,np.max(x)+0.01)
    ax.set_ylim(-1,0)
    #ax.set_aspect('equal')
    ax.grid()
    
    line, = ax.plot([], [], 'o-', lw=2)
    curve, = ax.plot(x[0],y[0],'lightgrey')
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    
    
    def init():
        line.set_data([], [])
        curve.set_data(x[0],y[0])
        time_text.set_text('')
        return line, curve, time_text
    
    
    def animate(i):
        xdata.append(x[i])
        ydata.append(y[i])
        
        thisx = [0, x[i]]
        thisy = [0, y[i]]
    
        line.set_data(thisx, thisy)
        curve.set_xdata(xdata)
        curve.set_ydata(ydata)
        time_text.set_text(time_template % (i*dt))
        return line, curve, time_text
    
    
    ani = animation.FuncAnimation(fig,animate,range(1,len(y)),interval=dt*1000, blit=True, init_func=init)
    plt.show()
    
    

if __name__ == "__main__":
    plotPotentiel()
    
    y1 = [0.55,0,0.03,0]
    y0 = [0.66,0,0.03,0]
    dt = 0.0005
    n = 20000
    #t,r,vr,theta,vtheta = numpySoluce(y0,dt,n)
    t,r,vr,theta,vtheta = testRK4(y0,dt,n)
    #Graph2D(t,[r],"t (s)","r (m)","r(t)").show()
    #Graph2D(t,[theta],"t (s)",r'$\theta$ (radians)',r'$\theta(t)$').show()
    #Graph2D(theta,[r],r'$\theta$ (radians)',"r (m)",r'$r(\theta)$').show()
    x,y = getCartesianArray(r,theta)
    print("min x : ",np.min(x))
    print("max x : ",np.max(x))
    print("min y : ",np.min(y))
    print("max y : ",np.max(y))
    #Graph2D(x,-y,"x (m)","y (m)","y(x)")
    

    #T,V,E = testEnergy(r,vr,theta,vtheta)
    #Graph2D(t,[V],"t","V","Potential energy").show()
    #Graph2D(t,[T],"t","T","Kinetic energy").show()
    #Graph2D(t,[E],"t","E","Total energy").show()
    
    #aniPendule(dt,n,t,x,-y)

    
  

