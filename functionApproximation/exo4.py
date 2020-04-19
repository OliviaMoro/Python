# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 02:16:26 2020

@author: moroo
"""

import numpy as np
from bessel import J0

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'plotFunction')))
from plotMethods import Graph2D


def exo4():
    """
        Plot the Bessel function J0(x)
    """
    # Question b :
    n = 1
    err = 1
    while(err > 1e-6):
        n += 1
        err = err*10/(n-1)
        
    print("n : ",n)
    
    test = np.array([-0.1775967713, -0.2459357644, -0.0142244728])
    print("J0(5)-J0(5)test : ",J0(5.,n)-test[0])
    print("J0(10)-J0(10)test : ",J0(10.,n)-test[1])
    print("J0(15)-J0(15)test : ",J0(15.,n)-test[2])
    
    x = np.linspace(0,20,200)
    bessel0 = np.array([])
    for i in range(0,200):
        bessel0 = np.append(bessel0,J0(x[i],n))
        
    Graph2D(x,[bessel0],'x','J0(x)',"Bessel function J0").show()    


if __name__ == "__main__":
    exo4()      