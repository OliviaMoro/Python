# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:23:16 2019

@author: moroo
"""
import math
import matplotlib.pyplot as plt


def explicitEuler(pas,ti,*coord,**pente):
    """ 
        Computes one iteration of the explicit Euler's method with the
        given parameters :
            - pas : step of the iteration (float)
            - ti : initial time (float)
            - *coord : initial conditions's array
            - **pente : functions's dictionnary used to compute differential
        Doesn't work yet with numpy array
    """
    # Inital conditions in the form *(t,coord)
    tupleArgs = (ti,)+coord
    
    # slopes computation
    pentes = []
    for value in pente.values():
        pentes.append(value(*tupleArgs))  
    
    # new positions computation
    uf = []
    i = 0
    for pos in coord:
        uf.append(pos+pas*pentes[i])
        i += 1
    
    # update of time
    tf = ti + pas
    
    return tf,uf         


def regressiveEuler(pas,tf,*coord,**pente):
    """ 
        Computes one iteration of the explicit Euler's method with the
        given parameters :
            - pas : step of the iteration (float)
            - tf : final time (float)
            - *coord : initial conditions's array
            - **pente : functions's dictionnary used to compute differential
        Doesn't work yet with numpy array
    """
    
    # Inital conditions in the form *(t,coord)
    tupleArgs = (tf,)+coord
    
    # slopes computation
    pentes = []
    for value in pente.values():
        pentes.append(value(*tupleArgs))  
    
    # new positions computation
    ui = []
    i = 0
    for pos in coord:
        ui.append(pos-pas*pentes[i])
        i += 1
    
    # update of time
    ti = tf - pas
    
    return ti, ui 


if __name__ == "__main__":
    # Pendulum's example
    def smy(t,y,z):
        return z
    
    def smz(t,y,z):
        return -math.sin(y)
    
    n = 600
    t = []
    u = []
    
    t.append(0)
    u.append([0,0.2]) 
    
    
    for i in range(1,n+1):
        (tf,uf)= explicitEuler(0.05,t[i-1],u[i-1][0],u[i-1][1],key1=smy,key2=smz)
        t.append(tf)
        u.append(uf)
        
    y = [i for i,j in u]
    z = [j for i,j in u]
        
    # plot graph
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            }
    
    fig = plt.figure(1)
    plt.suptitle(r'Test simple pendulum',fontdict=font,fontsize=16)
    plt.plot(t,y)
    plt.xlabel(r'time',fontdict=font)
    plt.ylabel(r'position',fontdict=font)
    plt.grid(True)
    plt.show()
    