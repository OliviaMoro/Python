# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:28:21 2020

@author: moroo
"""
import numpy as np
from math import exp, cos, sin, pi
from scipy.special import jv
from plotMethods import parametric,plotSurf, plotContour



def exo7():
    t = np.linspace(0,4,100)
    x = np.cos(2*pi*t)
    y = np.sin(2*pi*t)
    z = t
    parametric(x,y,z)
    
    
    
def exo8():
    v = np.linspace(0,12,12)
    x = np.linspace(0,20,100)
    v, x = np.meshgrid(v, x)
    besselj = jv(v,x)
    plotSurf(x,v,besselj,"x","n","Jn(x)","Exo 8")
    
    
    
def exo9():
    a = 1.
    x = np.linspace(-5.,5.,256)
    y = x
    x, y = np.meshgrid(x,y)
    
    den1 = np.sqrt(np.square(x-a) + np.square(y))
    den2 = np.sqrt(np.square(x+a) + np.square(y))
    U = np.divide(0.11,den1)-np.divide(0.11,den2)
    
    nivPos = [1e-2,5e-2,1e-1,5e-1,1,5,10]
    nivNeg = np.flipud(nivPos)
    nivNeg = -1*nivNeg
    niv = np.append(nivNeg,nivPos)

    plotContour(x,y,U,"x","y","Equipotentials",niv)
    


if __name__ == "__main__":
    #exo7()
    #exo8()
    exo9()