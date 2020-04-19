# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 05:55:35 2020

@author: moroo
"""
from __future__ import division
from math import isclose

def frame(x):
    """
        Frames the number x by two fractions of integers with a tolerance
        of 1e-5
    """
    a0 = 0; b0 = 1; a1 = 1; b1 = 0;
    f = 1
    i = 0
    
    while (not isclose(f,x,rel_tol=1e-5, abs_tol=0.0)): 
        i += 1
        #print("{}/{} < x < {}/{}".format(a0,b0,a1,b1)) 
        f = float(a0+a1)/float(b0+b1)
        #print("f = {} :({}+{})/({}+{})".format(f,a0,a1,b0,b1))
        
        if(f < x):     #approximation par défaut de x
            a0 += a1
            b0 += b1
        elif(f > x):   #approximation par excès de x
            a1 += a0
            b1 += b0
    return a0,b0,a1,b1,i
        
        
if __name__ == "__main__":
    x = 3.14159
    a0,b0,a1,b1,i = frame(x)
    # Finds the Adrien Metius's approximation of pi : 355/113
    print("{}/{} < x < {}/{}".format(a0,b0,a1,b1),"i = {}".format(i))