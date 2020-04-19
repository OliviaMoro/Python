# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:16:59 2020

@author: moroo
"""

from math import isclose

def intersect(xg,xd,f):
    yg = f(xg)
    yd = f(xd)
    xm = xd-yd*(xd-xg)/(yd-yg)
    return xm


def regulaFalsi(a,b,f,tol,nMax):
    """
        Recherche de zeros d'une fonction f à une variable
        sur l'intervalle [a,b] avec une tolérance tol
    """    
    i = 0
    xm = intersect(a,b,f)

    
    while(not isclose(f(xm),0,rel_tol=tol, abs_tol=0.0) and i<=nMax):  
        
        # root is in [a,xm] : the sign changed
        if (f(a)*f(xm) < 0 ):
            b = xm
        # root is in [xm,b] : sign unchanged   
        elif (f(a)*f(xm) > 0):
            a = xm
        # root finded with fairly good precision
        elif (isclose(f(xm),0,rel_tol=tol, abs_tol=0.0)):
            break
        
        i += 1
        xm = intersect(a,b,f)


    print("[a,b] = [{},{}], i = {}".format(a,b,i))
            
    return xm