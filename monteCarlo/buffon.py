# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 02:53:50 2020

@author: moroo
"""
import numpy as np
from math import pi, sin
from random import uniform



def lancerBuffon(N,a,l):
    """
        Implements Buffon needles's experience to compute pi with :
            - N : number of needles
            - a : needles length
            - l : parquet slat width
    """
    s = np.zeros((N))
    
    for i in range(0,N):
        y = uniform(0,l/2.)
        theta = uniform(0,pi/2.)
        
        if (a/2.*sin(theta) > y):
            s[i] = 1
        else:
            s[i] = 0

    p = np.sum(s)/N
    pi_approx = 2*a/(p*l)        
    return pi_approx