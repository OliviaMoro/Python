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
    # integration de sqrt(x) sur un exemple élémentaire
    exact = 2/3.*(5**1.5 -1**1.5)
    # valeur calculée avec integrate.quad
    resultQuad = integrate.quad(lambda x: sqrt(x), inf, sup)
    # valeur calculée avec integrate.trapz
    x = np.linspace(inf, sup, int(abs(sup-inf)/h))
    y = np.sqrt(x)
    y_int = integrate.cumtrapz(y, x)
    
    pointGauche = crude.pointGauche(inf,sup,h,sqrt)
    pointDroit = crude.pointDroite(inf,sup,h,sqrt)
    pointMilieu = crude.pointMileu(inf,sup,h,sqrt)
    trapeze = crude.trapezes(inf,sup,h,sqrt)
    
    print("exact :",exact,"quad :",resultQuad,"cumtrapz :",y_int[-1])
    print("pointGauche :",pointGauche,"pointDroit :",pointDroit)
    print("trapeze :",trapeze,"pointMilieu :",pointMilieu)

def newtonCotes(inf,sup,h,func):
    # Test des algorithmes de nc
    nc1 = nc.trapeze(inf,sup,h,func)
    nc2 = nc.simpson_1_3(inf,sup,h,func)
    nc3 = nc.simpson_3_8(inf,sup,h,func)
    nc4 = nc.villarceau(inf,sup,h,func)
    print("trapeze :",nc1,"simpson 1/3 :", nc2)
    print("simpson 3/8 :",nc3,"villarceau :", nc4)
    
    # Utilisation de integrate
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
    
    
    
    
    
    