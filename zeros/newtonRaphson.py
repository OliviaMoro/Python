# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 01:12:26 2020

@author: moroo
"""

from math import isclose


def newtonRaphson(xi,tol,f,derf,nMax=20):
    """
        Looks for the roots of a function f around a close xi value 
        with a tolerance tol :
            - f : function of a real variable
            - derf : function derived from f
    """
    delta = 1
    i = 0
    
    while (not isclose(delta,0,rel_tol=tol, abs_tol=0.0) and i <= nMax):
        print("i : {}, x : {}, y : {}, y' : {}".format(i,'%.4f' %xi, '%.4f' %f(xi), '%.4f' %derf(xi)))
        i += 1
        x = xi - f(xi)/derf(xi)
        delta = abs(x-xi)
        xi = x
        
    print("i : {}, x : {} ".format(i,xi))
        
    return xi
        
    