# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:28:45 2019

@author: moroo
"""
import math
import matplotlib.pyplot as plt



def rungeKutta2(pas,ti,*coord,**pente):
    """ 
        Computes one iteration of the 2-nd order Runge Kutta's method 
        with the following parameters :
            - pas : step of the iteration (float)
            - ti : initial time (float)
            - *coord : initial conditions's array
            - **pente : functions's dictionnary used to compute differential
        Doesn't work yet with numpy array
    """
    # Inital conditions in the form *(t,coord)
    tupleArgs = (ti,)+coord
    
    # slopes computation at ti : k1
    k1 = []
    for value in pente.values():
        k1.append(value(*tupleArgs))  
    
    # slopes computation at tf : k2
    tf = ti + pas
    k2 = []
    tupleArgs = [ti,]+[coord[i]+pas*k1[i] for i in range(0,len(coord))]
    for value in pente.values():
        k2.append(value(*tupleArgs))  
    
    # new positions computation
    uf = []
    i = 0
    for pos in coord:
        uf.append(pos+0.5*pas*(k1[i]+k2[i]))
        i += 1 
    
    return tf, uf
    
    

def rungeKutta4(pas,ti,*coord,**pente):
    """ 
        Computes one iteration of the 4-th order Runge Kutta's method 
        with the following parameters :
            - pas : step of the iteration (float)
            - ti : initial time (float)
            - *coord : initial conditions's array
            - **pente : functions's dictionnary used to compute differential
        Doesn't work yet with numpy array
    """
    # Inital conditions in the form *(t,coord)
    tupleArgs = (ti,)+coord
    
    # slopes computation at ti : k1
    k1 = []
    for value in pente.values():
        k1.append(value(*tupleArgs))  
    
    # slopes computation at ti+pas/2 : k2
    t = ti + pas/2.
    k2 = []
    tupleArgs = [t,]+[coord[i]+pas*0.5*k1[i] for i in range(0,len(coord))]
    for value in pente.values():
        k2.append(value(*tupleArgs))  
        
    # slopes computation at ti+pas/2 : k3
    k3 = []
    tupleArgs = [t,]+[coord[i]+pas*0.5*k2[i] for i in range(0,len(coord))]
    for value in pente.values():
        k3.append(value(*tupleArgs)) 
        
    # slopes computation at tf : k4
    tf = ti + pas
    k4 = []
    tupleArgs = [tf,]+[coord[i]+pas*k3[i] for i in range(0,len(coord))]
    for value in pente.values():
        k4.append(value(*tupleArgs)) 
    
    # new positions computation
    uf = []
    i = 0
    for pos in coord:
        uf.append(pos+pas*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6.)
        i += 1  
    
    return tf, uf

if __name__ == "__main__":
    # Pendulum's example :
    def smy(t,y,z):
        return z
    
    def smz(t,y,z):
        return -math.sin(y)
    
    
    n = 600
    t = []
    u = []
    
    t.append(0)
    u.append([3,0]) 
    
    
    for i in range(1,n+1):
        (tf,uf)=rungeKutta4(0.05,t[i-1],u[i-1][0],u[i-1][1],key1=smy,key2=smz)
        t.append(tf)
        u.append(uf)
        
    y = [i for i,j in u]
    z = [j for i,j in u]
        
    #plot graph
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            }
    
    fig = plt.figure(1)
    plt.suptitle(r'Simple pendulum test',fontdict=font,fontsize=16)
    plt.plot(t,y)
    plt.xlabel(r'time',fontdict=font)
    plt.ylabel(r'position',fontdict=font)
    plt.grid(True)
    plt.show()
    
