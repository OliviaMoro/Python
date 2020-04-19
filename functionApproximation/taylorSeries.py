# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:46:19 2020

@author: moroo
"""

from math import pi

def cos(x,tol):
    terme = 1.
    somme = terme
    k = 1
    while (abs(terme) > tol):
        terme = -1*x*x*terme/(2*k)
        somme += terme
        k += 1
    return somme


def sin(x,tol):
    terme = x
    somme = terme
    k = 1
    while (abs(terme) > tol):
        terme = -1*x*x*terme/(2*k+1)
        somme += terme
        k += 1
    return somme


def arctan(x,tol):
    terme = x
    somme = terme
    k = 1
    while (abs(terme) > tol):
        terme = -1*pow(x,2)*terme
        somme += terme/(2*k+1.) 
        k += 1
    return somme


def arctanBis(x):
    tol = 1e-5
    if (abs(x) <= 1):
        result = arctan(x,tol)
    elif (x > 1):
        result = pi/2. - arctan(1/x,tol)
    elif (x < -1):
        result = -pi/2 - arctan(1/x,tol)
    return result