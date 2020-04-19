# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 03:55:28 2020

@author: moroo
"""

import scipy.integrate as integrate
import crude
import newtonCotes as nc
from numpy import sqrt
import numpy as np


def testIntegration():
    inf = 1
    sup = 5
    h = 0.05
    # Integration of sqrt 
    exact = 2/3.*(5**1.5 -1**1.5)
    # value computed with integrate.quad
    resultQuad = integrate.quad(lambda x: sqrt(x), inf, sup)
    # value computed integrate.trapz
    x = np.linspace(inf, sup, int(abs(sup-inf)/h))
    y = np.sqrt(x)
    y_int = integrate.cumtrapz(y, x)
    
    leftPoint = crude.leftPoint(inf,sup,h,sqrt)
    rightPoint = crude.rightPoint(inf,sup,h,sqrt)
    midPoint = crude.midPoint(inf,sup,h,sqrt)
    trapeze = crude.trapezes(inf,sup,h,sqrt)
    
    print("exact :",exact,"quad :",resultQuad,"cumtrapz :",y_int[-1])
    print("leftPoint :",leftPoint,"rightPoint :",rightPoint)
    print("trapeze :",trapeze,"midPoint :",midPoint)


def newtonCotes(inf,sup,h,func):
    """
        nc's algorithms's tests 
    """
    nc1 = nc.trapeze(inf,sup,h,func)
    nc2 = nc.simpson_1_3(inf,sup,h,func)
    nc3 = nc.simpson_3_8(inf,sup,h,func)
    nc4 = nc.villarceau(inf,sup,h,func)
    print("trapeze :",nc1,"simpson 1/3 :", nc2)
    print("simpson 3/8 :",nc3,"villarceau :", nc4)
    
    # Use of integrate 
    somme = [0,0,0,0]
    x = inf
    N = int(abs(sup-inf)/h)
    for i in range(0,N):
        for n in range(1,5):
            y = np.linspace(x,x+h,n+1)
            an, B = integrate.newton_cotes(n, 1)
            dy = h/n
            quad = dy*np.sum(an*func(y))
            somme[n-1] += quad
        x += h
    
    for result in somme:
        print('{:10.9f}'.format(result))
        

    

if __name__ == "__main__":
    #testIntegration()
    newtonCotes(1,5,0.05,sqrt)
    
    
    
    
    
    