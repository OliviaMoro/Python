 # -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:33:41 2020

@author: moroo
"""

from math import sqrt, pi
import numpy as np

def K(k):
    """
        Estimate the first species complete elliptical function at a given k 
        following the Gauss arithmetic-geometrical average algorithm :
            - k : float
        Returns :
            - K(k) = pi/(2*an) : float
            - c : array containing cn values 
    """
    a0 = 1; b0 = sqrt(1-k*k); c0 = k
    c = np.array([c0])
    
    while(c[-1] > 1e-5):
        a = (a0+b0)/2.
        b = sqrt(a0*b0)
        c = np.append(c,(a0-b0)/2.)
        a0 = a
        b0 = b
        
    return pi/(2*a0),c


def E(k):
    """
        Estimate the second species complete elliptical function at a given k 
        following the Gauss arithmetic-geometrical average algorithm :
            - k : float
        Returns :
            - E(k) : float
    """
    C = K(k)[0]
    c = K(k)[1]
    somme = 0
    
    for i in range(0,len(c)):
        somme += pow(2,i)*c[i]*c[i]
    
    return C*(1-somme/2.)




if __name__ == "__main__":
    # Supposed to give roughly K(0.5) = 1.685750, E(0.5) = 1.467462
    print("K(0.5) : {} , E(0.5) : {} ".format(K(0.5)[0],E(0.5)))

