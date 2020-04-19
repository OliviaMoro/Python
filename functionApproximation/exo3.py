# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:16:47 2020

@author: moroo
"""

import horner
import numpy as np
from math import pow, pi

def arctan(x,n):
    """
        Evaluate arctan(x) using the power series formula up to the n-th 
        term for x between -1 and 1
    """
    terme = x
    somme = terme
    
    for i in range(1,n+1):
        terme = -1*pow(x,2)*terme
        somme += terme/(2*i+1.) 
    return somme


def atanHorner(x,n):
    """
        Attempt of evaluate the power series approximation of atan with the
        Horner method up to the n-th term for abs(x)<1
    """
    terme = 1 
    coef = np.array([0,terme])
    
    # On créer l'array contenant les coefficients du DSE
    for i in range(1,n+1):
        terme = -1*terme
        coef = np.append(coef,0)
        coef = np.append(coef,terme/(2*i+1))
    #print("array horner :",coef)
        
    # On utilise l'algorithme de Horner
    return horner.horner(coef,x) 
   
    
def arctanBis(x):
    """
        Evaluate arctan(x) using the arctan(x,n) function defined above for 
        x in the real axis
    """
    n = 25000
    if (abs(x) <= 1):
        result = arctan(x,n)
    elif (x > 1):
        result = pi/2. - arctan(1/x,n)
    elif (x < -1):
        result = -pi/2 - arctan(1/x,n)
    return result
    
    
def exo3():
    controle = pi/4.
    err = 1.
    n = 1
    x = 1.
    
    # Question b)
    while(err > 1e-5):
        somme = arctan(x,n)
        #somme = atanHorner(x,n)
        err = abs(somme - controle)
        n += 1
    print("n :",n,"atan(1) :",somme)
    
    # Question c
    print("arctan(2) :",arctanBis(2))
        

if __name__ == "__main__":
    exo3()        