# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 01:38:35 2020

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

m1 = 1
m2 = 1
l1 = 0.2
l2 = 0.2
g = 9.8


def plotPotentiel():
    theta1 = np.arange(-math.pi,math.pi,math.pi/10.)
    theta2 = np.arange(-math.pi,math.pi,math.pi/10.)
    theta1, theta2 = np.meshgrid(theta1, theta2)
    V = -g*l1*(m1+m2)*np.cos(theta1)-m2*l2*g*np.cos(theta2)

    labelx = r'$\theta_{1}$(radians)'
    labely = r'$\theta_{2}$(radians)'
    title = 'Potential energy'
    plotSurf(theta1,theta2,V,labelx,labely,'',title)
    plotContour(theta1,theta2,V,labelx,labely,title)


def pend(y,t,m1,m2,g,l1,l2):
    x1, y1, x2, y2 = y
    c1 = m2*math.sin(x1-x2)/(m1+m2*math.sin(x1-x2)**2)
    c2 = m1*math.sin(x1)/(m1+m2*math.sin(x1-x2)**2)
    c3 = (m1+m2)*math.sin(x1-x2)/(m1+m2*math.sin(x1-x2)**2)
    dydt = [y1,
            -c1*math.cos(x1-x2)*y1**2-l2*c1/l1*y2**2-g/l1*(c1+c2*math.cos(x1)),
            y2,
            c1*math.cos(x1-x2)*y2**2+l1/l2*c3*y1**2+g/l2*c3*math.cos(x1)]
    return dydt


def numpySoluce(y0,dt,n):
    #y0 = [0.66,0,0.03,0]
    t = np.linspace(0,n*dt,n)
    sol = odeint(pend, y0, t, args=(m1,m2,g,l1,l2))
    
    x1 = sol[:,0]
    y1 = sol[:,1]
    x2 = sol[:,2]
    y2 = sol[:,3]
    return t,x1,y1,x2,y2


# X1 = theta1, X2 = theta2
def derX1(t,x1,y1,x2,y2):
    return y1
    
    
def derY1(t,x1,y1,x2,y2):
    C11 = -m2*math.sin(x1-x2)/(m1+m2*math.sin(x1-x2)**2)
    C12 = -g/l1*m1*math.sin(x1)/(m1+m2*math.sin(x1-x2)**2)
    der = C11*(math.cos(x1-x2)*y1**2+l2*y2**2/l1+g*math.cos(x2)/l1)+C12
    return der
    
    
def derX2(t,x1,y1,x2,y2):    
    return y2
    
    
def derY2(t,x1,y1,x2,y2):    
    C2 = (m1+m2)*math.sin(x1-x2)/(m1+m2*math.sin(x1-x2)**2)
    der = C2*(m2*math.cos(x1-x2)*y2**2/(m1+m2)+l1*y1**2/l2+g*math.cos(x1)/l2)
    return der


def testRK4(uCI,dt,n):
    t = []
    u = []

    t.append(0)
    u.append(uCI) 
    
    p = 10 # sampling step
    tTemp =[]
    uTemp = []
    tTemp.append(0)
    uTemp.append(uCI)
        
    print("t0 :",tTemp[0])
    for i in range(1,n+1):
        j = (i-1)%p
        #(tf,uf)=rk.rungeKutta4(dt,t[i-1],u[i-1][0],u[i-1][1],u[i-1][2],u[i-1][3],key1=derX1,key2=derY1,key3=derX2,key4=derY2)
        (tf,uf)=rk.rungeKutta4(dt,tTemp[j],uTemp[j][0],uTemp[j][1],uTemp[j][2],uTemp[j][3],key1=derX1,key2=derY1,key3=derX2,key4=derY2)
        if(i%p == 0):
            # Values are added to final lists
            t.append(tf)
            u.append(uf)
            # We empty the temporary tables
            tTemp[:] = []
            uTemp[:] = []
        tTemp.append(tf)
        uTemp.append(uf)
            
        
    x1 = [i for i,j,k,l in u]
    y1 = [j for i,j,k,l in u]
    x2 = [k for i,j,k,l in u]
    y2 = [l for i,j,k,l in u]
    
    return t,x1,y1,x2,y2


def testEnergy(x1,y1,x2,y2):
    E = []
    T = []
    V = []
    
    for i in range(0,len(x1)):
        Ec = 0.5*(m1+m2)*l1**2*y1[i]**2 + 0.5*m2*l2**2*y2[i]**2 + m2*l1*l2*y1[i]*y2[i]*np.cos(x1[i]-x2[i])
        Ep = -g*l1*(m1+m2)*np.cos(x1[i]) - m2*l2*g*np.cos(x2[i])
        T.append(Ec)
        V.append(Ep)
        E.append(Ec+Ep)
    
    return T,V,E


def aniPenduleDouble(dt,n,t,x1,y1,x2,y2):
    xdata = []
    ydata = []
    
    labelx = r'x (m)'
    labely = r'y (m)'
    titre = "Double pendulum's motion (m1=m2,l1=l2=0.2 m)"
    
    fig,ax = plt.subplots()
    ax.set_xlim(-(l1+l2)-0.2,l1+l2+0.2)
    ax.set_ylim(-(l1+l2)-0.2,l1+l2)
    #ax.set_aspect('equal')
    ax.set_title(titre)
    ax.set_xlabel(labelx)
    ax.set_ylabel(labely)
    ax.grid()
    
    line, = ax.plot([], [], 'o-', lw=2)
    curve, = ax.plot(x2[0],y2[0],'lightgrey')
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
        
    def init():
        line.set_data([], [])
        curve.set_data(x2[0],y2[0])
        time_text.set_text('')
        return line, curve, time_text
       
    def animate(i):
        xdata.append(x2[i])
        ydata.append(y2[i])
        
        thisx = [0, x1[i],x2[i]]
        thisy = [0, y1[i],y2[i]]
    
        line.set_data(thisx, thisy)
        curve.set_xdata(xdata)
        curve.set_ydata(ydata)
        time_text.set_text(time_template % (i*dt))
        return line, curve, time_text
        
    ani = animation.FuncAnimation(fig,animate,range(1,len(y2)),interval=dt*1000,blit=True, init_func=init,repeat=False)
    plt.show()
    

if __name__ == "__main__":  
    # potential plot :
    #plotPotentiel()
    
    dt = 0.005
    n = 2000
    y0 = [0.66,0,0.03,0]
    y1 = [120*math.pi/180.,0,-10*math.pi/180.,0]
    t,x1,y1,x2,y2 = testRK4(y1,dt,n)
    Graph2D(x2,[y2],"x2","y2","y2(x2)").show()
    

    #T,V,E = testEnergy(x1,y1,x2,y2)
    #Graph2D(t,[V],"t","V","Potential energy").show()
    #Graph2D(t,[T],"t","T","Kinetic energy").show()
    #Graph2D(t,[E],"t","E","Total energy").show()

    x_1 = l1*np.sin(x1)
    y_1 = -l1*np.cos(x1)
    x_2 = l2*np.sin(x2)+x_1
    y_2 = -l2*np.cos(x2)+y_1
    v1 = np.multiply(l1,y1)
    v20 = np.multiply(l2,y2)
    v21 = np.multiply(2*l1*l2,np.multiply(np.cos(np.subtract(x1,x2)),np.multiply(y1,y2)))
    v2 = np.sqrt(np.square(v1)+np.square(v20)+v21)
    Graph2D(x_2,[v2],"x2","y2","Poincaré section (x2,y2)").show()
    #aniPenduleDouble(dt,n,t,x_1,y_1,x_2,y_2)
    
    
    