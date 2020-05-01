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
    i = 0
    
    while (abs(f(xi)) > tol and i <= nMax):
        #print("i : {}, x : {}, y : {}, y' : {}".format(i,'%.4f' %xi, '%.4f' %f(xi), '%.4f' %derf(xi)))
        i += 1
        x = xi - f(xi)/derf(xi)
        xi = x
        
    print("i : {}, x : {} ".format(i,'%.4f' %xi))
        
    return xi



def newtonRaphsonSimple(xi,tol,f,derf,nMax=20):
    """
        Looks for the roots of a function f around a close xi value 
        with a tolerance tol :
            - f : function of a real variable
            - derf : function derived from f
        This is a simplified version of th Newton Raphson algorithm.
    """
    x0 = xi
    i = 0
    
    while (abs(f(xi)) > tol and i <= nMax):
        #print("i : {}, x : {}, y : {}, y' : {}".format(i,'%.4f' %xi, '%.4f' %f(xi), '%.4f' %derf(xi)))
        i += 1
        x = xi - f(xi)/derf(x0)
        xi = x
        
    print("i : {}, x : {} ".format(i,'%.4f' %xi))
        
    return xi



def newtonRaphson2D(x,y,tol,f,g,fx,fy,gx,gy,nMax=20):
    """
        Looks for the closest root of the system f(x,y) = 0 and g(x,y) = 0
        with a tolerance tol :
            - f, g : function of a real variable
            - fx, gx : f and g derived with respect to x
            - fy, gy : f and g derived with respect to y
    """
    i = 0
    u = 1
    v = 1
    
    while (abs(u)>tol and abs(v)>tol and i<=nMax):
        i += 1
        delta = fx(x,y)*gy(x,y)-fy(x,y)*gx(x,y)
        u = (g(x,y)*fy(x,y)-f(x,y)*gy(x,y))/delta
        v = -(g(x,y)*fx(x,y)-f(x,y)*gx(x,y))/delta
        x += u
        y += v
        
    print("i : {}, (x,y) : ({},{}) ".format(i,'%.4f' %x,'%.4f' %y))
        
    return x,y
        
    