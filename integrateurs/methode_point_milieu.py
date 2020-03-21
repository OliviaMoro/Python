# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:59:08 2019

@author: moroo
"""

import math
import matplotlib.pyplot as plt
import numpy as np


def point_milieu(pas,ti,*coord,**pente):
    #Mise sous forme de liste *(t,coord)
    tupleArgs = (ti,)+coord
    
    #Calcul des pentes à ti : k1
    k1 = []
    for value in pente.values():
        k1.append(value(*tupleArgs))  
    
    #Calcul des pentes à tf : k2
    t = ti + pas*0.5
    k2 = []
    tupleArgs = [t,]+[coord[i]+pas*0.5*k1[i] for i in range(0,len(coord))]
    for value in pente.values():
        k2.append(value(*tupleArgs))  
    
    #Calcul des nouvelles positions
    tf = ti + pas
    uf = []
    i = 0
    for pos in coord:
        uf.append(pos+pas*k2[i])
        i += 1 
    
    return tf, uf

if __name__ == "__main__":
    #Exemple du pendule:
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
        (tf,uf)=point_milieu(0.05,t[i-1],u[i-1][0],u[i-1][1],key1=smy,key2=smz)
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
    plt.suptitle(r'Test pendule simple',fontdict=font,fontsize=16)
    plt.plot(t,y)
    plt.xlabel(r'temps',fontdict=font)
    plt.ylabel(r'position',fontdict=font)
    plt.grid(True)
    plt.show()
    