# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:31:12 2019

@author: moroo
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def velocity_verlet(pas,ti,pi,vi,accel):
    #Mise sous forme de liste *(t,coord)
    tupleArgs = [ti,pi]
    
    #Actualisation des positions
    pf = pi+pas*vi+0.5*pas*pas*accel(*tupleArgs)
        
    #Actualisation des vitesses
    tf = ti + pas
    tupleArgsf = [tf,pf]
    vf = vi+pas*(accel(*tupleArgs)+accel(*tupleArgsf))*0.5
    
    return tf, pf, vf

def leap_frog(pas,ti,pi,vi,accel):    
    #Actualisation des positions
    pf = pi+pas*vi
        
    #Actualisation des vitesses
    tf = ti + pas
    tupleArgs = [tf,pf]
    vf = vi+pas*accel(*tupleArgs)
    
    return tf, pf, vf

if __name__ == "__main__":
    #Exemple du pendule:
    def a(t,p):
        return -math.sin(p)
    
    n = 600
    t = [0]
    p = [0]
    v = [0.2]
    
    for i in range(1,n):
        (tf,pf,vf)=leap_frog(0.05,t[i-1],p[i-1],v[i-1],a)
        t.append(tf)
        p.append(pf)
        v.append(vf)
        
    #plot graph
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            }
    
    fig = plt.figure(1)
    plt.suptitle(r'Test pendule simple',fontdict=font,fontsize=16)
    plt.plot(t,p)
    plt.xlabel(r'temps',fontdict=font)
    plt.ylabel(r'position',fontdict=font)
    plt.grid(True)
    plt.show()
