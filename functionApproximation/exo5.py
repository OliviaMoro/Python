# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 03:26:25 2020

@author: moroo
"""
from math import sqrt
import numpy as np


import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'plotFunction')))
from plotMethods import Graph2D


def f(x):
    terme = 1.
    somme = terme
    k = 1
    while (abs(terme) > 1e-7):
        terme = x*x*x*terme/(3*k-1)/(3*k)
        somme += terme
        k += 1
    return somme
    
    
def g(x):
    terme = x
    somme = terme
    k = 1
    while (abs(terme) > 1e-7):
        terme = x*x*x*terme/(3*k)/(3*k+1)        
        somme += terme
        k += 1
    return somme



def Ai(x):
    """
        Airy function of the first kind estimation at a given point x
    """
    c1 = 0.3550281
    c2 = 0.2588194
    return c1*f(x)-c2*g(x)



def Bi(x):
    """
        Airy function of the second kind estimation at a given point x
    """
    c1 = 0.3550281
    c2 = 0.2588194
    return (c1*f(x)+c2*g(x))*sqrt(3.)



def exo5():
    n = 200
    min = -10.
    max = 2.
    X = np.linspace(-10.,2.,n)
    A = np.array([])
    B = np.array([])
    x = -10.
    pas = (max-min)/n
    
    for i in range(0,n):
        A = np.append(A,Ai(x))
        B = np.append(B,Bi(x))
        x += pas
    
    graph = Graph2D(X,[A,B],'x','f(x)',"Airy Functions",['Ai','Bi'])
    graph.ylimit(-.5,1)
    graph.show()

    
    
    
if __name__ == "__main__":
    exo5()  