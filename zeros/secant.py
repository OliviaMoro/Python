# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:29:58 2020

@author: moroo
"""

from math import isclose


def intersect(xg,xd,f):
    yg = f(xg)
    yd = f(xd)
    xm = xd-yd*(xd-xg)/(yd-yg)
    return xm


def secant(x0,x1,f,tol,nMax):
    i = 0
    x = [x0,x1]
    xm = x1
    
    while(not isclose(f(xm),0,rel_tol=tol, abs_tol=0.0) and i <= nMax):
        xm = intersect(x[0],x[1],f)
        x = [x[1],xm]
        i += 1
    
    return xm
        