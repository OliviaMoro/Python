# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 05:09:08 2020

@author: moroo
"""


def trapeze(inf,sup,h,func):
    """
        Trapezes's method used to estimate the 'func' function's integral
        between 'inf' and 'sup' with the step 'h'
    """
    n = int(abs(sup-inf)/h)
    somme = 0

    x = inf
    for i in range(0,n):
        somme += (func(x+h)+func(x))*h/2.
        x += h 
        
    return somme


def simpson_1_3(inf,sup,h,func):
    """
        Newton-Cotes's method for n=2 used to estimate the 'func' function's 
        integral between 'inf' and 'sup' with the step 'h'
    """
    n = int(abs(sup-inf)/h)
    somme = 0

    x = inf
    for i in range(0,n):
        somme += h*(func(x)+4*func(x+h)+func(x+2*h))/6.
        x += h 
        
    return somme
    
    
def simpson_3_8(inf,sup,h,func):
    """
        Newton-Cotes's method for n=3 used to estimate the 'func' function's 
        integral between 'inf' and 'sup' with the step 'h'
    """
    n = int(abs(sup-inf)/h)
    somme = 0

    x = inf
    for i in range(0,n):
        somme +=  h*(func(x)+3*func(x+h)+3*func(x+2*h)+func(x+3*h))/8.
        x += h 
        
    return somme


def villarceau(inf,sup,h,func):
    """
        Newton-Cotes's method for n=4 used to estimate the 'func' function's 
        integral between 'inf' and 'sup' with the step 'h'
    """
    n = int(abs(sup-inf)/h)
    somme = 0

    x = inf
    for i in range(0,n):
        somme +=  h*(7*func(x)+32*func(x+h)+12*func(x+2*h)+32*func(x+3*h)+
                     7*func(x+4*h))/90.
        x += h 
    
    return somme
