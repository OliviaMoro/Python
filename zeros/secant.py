# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:29:58 2020

@author: moroo
"""

from math import isclose


def intersect(xg,xd,f):
    """
        Returns the abscissa where the (G,D) rope cut the x-axis. G = (xg,yg)
        and D = (xd,yd).
    """
    yg = f(xg)
    yd = f(xd)
    xm = xd-yd*(xd-xg)/(yd-yg)
    return xm


def secant(x0,x1,f,tol,nMax):
    """
        Search for the f function's zeros with a tolerance tol. nMax is the
        maximum number of step. x0 and x1 are the starting points.
    """
    i = 0
    x = [x0,x1]
    xm = x1
    
    while(not isclose(f(xm),0,rel_tol=tol, abs_tol=tol) and i <= nMax):
        xm = intersect(x[0],x[1],f)
        x = [x[1],xm]
        i += 1
        
    print("i secant : {}".format(i))
    
    return xm
        