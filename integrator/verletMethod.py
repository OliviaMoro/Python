# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:31:12 2019

@author: moroo
"""
import math
import matplotlib.pyplot as plt


def velocityVerlet(pas,ti,pi,vi,accel):
    # Inital conditions in the form *(t,coord)
    tupleArgs = [ti,pi]
    
    # new positions computation
    pf = pi+pas*vi+0.5*pas*pas*accel(*tupleArgs)
        
    # new velocities computation
    tf = ti + pas
    tupleArgsf = [tf,pf]
    vf = vi+pas*(accel(*tupleArgs)+accel(*tupleArgsf))*0.5
    
    return tf, pf, vf



def leapFrog(pas,ti,pi,vi,accel):    
    # new positions computation
    pf = pi+pas*vi
        
    # new velocities computation
    tf = ti + pas
    tupleArgs = [tf,pf]
    vf = vi+pas*accel(*tupleArgs)
    
    return tf, pf, vf


if __name__ == "__main__":
    # Pendulum's example :
    def a(t,p):
        return -math.sin(p)
    
    n = 600
    t = [0]
    p = [0]
    v = [0.2]
    
    for i in range(1,n):
        (tf,pf,vf)=leapFrog(0.05,t[i-1],p[i-1],v[i-1],a)
        t.append(tf)
        p.append(pf)
        v.append(vf)
        
    #plot graph
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            }
    
    fig = plt.figure(1)
    plt.suptitle(r'Simple pendulum test',fontdict=font,fontsize=16)
    plt.plot(t,p)
    plt.xlabel(r'time',fontdict=font)
    plt.ylabel(r'position',fontdict=font)
    plt.grid(True)
    plt.show()
