# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 02:42:30 2020

@author: moroo
"""
import numpy as np
from random import random



def radioactivity(alpha,N,it):
    """
        Implements the radioactive decay of N A-particles into B-particules
        with the decay probability alpha :
            - alpha : float between 0 and 1
            - N : number of particles
            - it : number of iteractions
    """
    nB = np.zeros((it+1))
    nA0 = np.zeros((N))
    
    for i in range(0,it):
        for j in range(0,N):
            x = random()
            if (x <= alpha and nA0[j] == 0):
                nA0[j] = 1     
        nB[i+1] = np.sum(nA0)
    
    nA = N-nB
    return nA,nB



def radioactivity2(alpha,beta,N,it):
    """
        Implements the radioactive decay of N A-particles into B-particules
        and then into C-particles with the decay probabilities alpha and
        beta respectively :
            - beta : float between 0 and 1
    """
    nA = np.zeros((it))                                                        
    nB = np.zeros((it))
    nC = np.zeros((it))
    nA0 = np.zeros((N))
    
    for i in range(0,it):
        for j in range(0,N):
            x = random()
            if (x <= alpha and nA0[j] == 0):
                nA0[j] = 1     
            x = random()
            if (x <= beta and nA0[j] == 1):
                nA0[j] = 2   
                
        for j in range(0,N):
            nA[i] += 1 if (nA0[j] == 0) else 0
            nB[i] += 1 if (nA0[j] == 1) else 0
            nC[i] += 1 if (nA0[j] == 2) else 0
    
    return nA,nB,nC


