# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 01:23:20 2020

@author: moroo
"""

from math import exp
from newtonRaphson import newtonRaphson


# racine entre -1 et 1
def test1(x):
    return x**5 - 2*x**4 + 100*x**3 - 2

def der1(x):
    return 5*x**4 -8*x**3 + 300*x**2

# racine entre -2 et 0
def test2(x):
    return x + exp(x)

def der2(x):
    return 1 + exp(x)


if __name__ == "__main__":
    tol = 1e-5
    
    racine1 = newtonRaphson(0.5,tol,test1,der1)
    racine2 = newtonRaphson(-2,tol,test2,der2)
    print("racine1 : {}, racine2 : {}".format(racine1,racine2))