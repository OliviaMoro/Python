# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:49:37 2020

@author: moroo
"""

from math import isclose, log, floor 

def minIteration(a,b,tol):
    """
        Calcule le nombre d'itération nécessaires pour que la dichotomie
        converge vers une solution
    """
    n = log((b-a)/(2*tol))/log(2)
    return floor(n)



def bissection(a,b,f,tol):
    """
        Recherche de zeros d'une fonction f à une variable
        sur l'intervalle [a,b] avec une tolérance tol
    """   
    i = 0
    n = minIteration(a,b,tol)
    # On découpe l'intervalle en deux    
    x0 = (b+a)/2.
    
    for i in range(0,n):
        i += 1
        x0 = (b+a)/2.
        
        # la racine est dans [a,x0]
        if (f(a)*f(x0) < 0 ):
            b = x0
        # la racine est dans [x0,b]    
        elif (f(a)*f(x0) > 0):
            a = x0
        # on a trouver la racine
        elif (isclose(f(a)*f(x0),0,rel_tol=tol, abs_tol=0.0)):
            break


    print("[a,b] = [{},{}], i = {}".format(a,b,i))
            
    return x0



    
    