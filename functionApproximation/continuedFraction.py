# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:01:46 2020

@author: moroo
"""

from math import trunc, isclose, pi
import numpy as np

def develop(x):
    """
        Finds the 10 first ai coefficients of the continued fraction 
        approximating the x value 
    """
    
    i = 0
    ai = np.array([])
    stop = False
    
    while(not stop):
        y = 1./x
        a = trunc(y)
        ai = np.append(ai,a)
        print("y = 1/{} = {}, ai = {}".format(x,y,a))
        x = y - a
        i += 1
        if(i == 10):
            break
    
    return ai
    
    
if __name__ == "__main__":
    x = pi
    
    ai = develop(x)
    print(ai)