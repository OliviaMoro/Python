# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:28:16 2020

@author: moroo
"""
import numpy as np
from math import pi
from scipy.special import factorial


def product(x,pivot,index):
    try:
        assert(index >= 0 and index < len(pivot))
    except AssertionError:
        print("The index isn't accessible")
        return
    
    product = 1.
    for i in range(0,len(pivot)):
        if (i != index):
            product *= (x-pivot[i])/(pivot[index]-pivot[i])           
    return product



def polynome(x,pivot,values):
    """
        Compute Lagrange polynome for the values 'values' at the given 
        points 'pivot' at x 
    """
    try:
        assert(len(pivot)==len(values))
    except AssertionError:
        print("Given arrays aren't the same length.")
        return
    
    P = 0
    for i in range(0,len(pivot)):
        P += values[i]*product(x,pivot,i)
    return P            
    


def formPolynome(X,pivot,values):
    P = np.array([])
    
    for i in range(0,len(X)):
        P = np.append(P,polynome(X[i],pivot,values))
    return P



def polynomeWeight(x,pivot,values):
    n = len(pivot)
    weight = np.array([1])
    facteur = factorial(n)
    
    # Calcul des poids
    for i in range(1,n):
        weight = np.append(weight,weight[-1]/(i*(n-1)))
    weight = [weight[i]*facteur for i in range(1,n)]
    weight = np.concatenate(([0],weight),axis = None)
    
    
    # Calcul du polynome de Lagrange
    num = np.zeros(len(x))
    den = np.zeros(len(x))   
    
    for i in range(0,n):
        diff = x-pivot[i]
        den +=  np.divide(weight[i],diff)
        num +=  np.divide(weight[i]*values[i],diff)
    L = np.divide(num,den)
    return L



if __name__ == "__main__":
#    print("Exercice 2 :")
#    x = 5000
#    pivot = np.array([4861,5896])
#    values = np.array([1.6062,1.5923])
#    n = polynome(x,pivot,values)
#    print("a) indice de réfraction a 5000 A : {}".format(n))
#    
#    pivot = np.array([4358,4861,5896])
#    values = np.array([1.6174,1.6062,1.5923])
#    n = polynome(x,pivot,values)
#    print("b) indice de réfraction a 5000 A : {}".format(n))
    
#    print("Exercice 4:")
#    pivot = np.array([0,3,1])
#    values = np.array([1,2,3])
#    p2 = polynome(2,pivot,values)
#    print("p(2) : {}".format(p2))
    
    pivot = np.array([42,44,46,48])
    values = np.array([0.66913061,0.69465837,0.71933980,0.74314483])
    sin45 = polynomeWeight([pi/4.],pivot,values)
    print("sin(45) : {}".format(sin45))
    

    
    
    