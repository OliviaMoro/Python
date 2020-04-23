# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:49:37 2020

@author: moroo
"""

from math import isclose, log, floor 

def minIteration(a,b,tol):
    """
        Computes the iterations number needed for the dichotomy to 
        converge to a solution.
    """
    n = log((b-a)/(2*tol))/log(2)
    return floor(n)



def bissection(a,b,f,tol):
    """
        Search for the f function's zeros between a and b with a tolerance
        tol.
    """   
    i = 0
    n = minIteration(a,b,tol)
    # The interval is cut in two
    x0 = (b+a)/2.
    
    for i in range(0,n):
        i += 1
        x0 = (b+a)/2.
        
        # root is in [a,x0] : the sign changed 
        if (f(a)*f(x0) < 0 ):
            b = x0
        # root is in [x0,b] : sign unchanged  
        elif (f(a)*f(x0) > 0):
            a = x0
        # root finded 
        elif (isclose(f(a)*f(x0),0,rel_tol=tol, abs_tol=0.0)):
            break


    print("[a,b] = [{},{}], i = {}".format(a,b,i))
            
    return x0



    
    