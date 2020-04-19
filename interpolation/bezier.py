# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:06:19 2020

@author: moroo
"""
import numpy as np
from scipy.special import binom


def bernstein(u,n,i):
    b = np.zeros(len(u))    

    for j in range(0,len(u)):
        b[j] = (u[j]**i)*(1-u[j])**(n-i)
        
    return b



def curve(u,xPoints,yPoints):
    n = len(xPoints)-1
    x = np.zeros(len(u))
    y = np.zeros(len(u))
    
    for i in range(0,n+1):
        C = binom(n,i)
        b = bernstein(u,n,i)
        x += xPoints[i]*C*b
        y += yPoints[i]*C*b
    
    return x,y
    
    
    
    
    