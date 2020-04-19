# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 02:56:41 2020

@author: moroo
"""

def leftPoint(inf,sup,h,func):
    """
        Rectangles's method using the first value of each interval used
        to estimate the 'func' function's integral between 'inf' and 'sup'
        with the step 'h'
    """
    n = int(abs(sup-inf)/h)
      
    somme = 0
    x = inf
    for i in range(0,n):
        somme += func(x)*h
        x += h  
        
    return somme  
  

def rightPoint(inf,sup,h,func):
    """
        Rectangles's method using the second value of each interval used
        to estimate the 'func' function's integral between 'inf' and 'sup'
        with the step 'h'
    """
    n = int(abs(sup-inf)/h)
      
    somme = 0
    x = inf
    for i in range(0,n):
        somme += func(x+h)*h
        x += h
      
    return somme


def midPoint(inf,sup,h,func):
    """
        Rectangles's method using the mid value of each interval used
        to estimate the 'func' function's integral between 'inf' and 'sup'
        with the step 'h'
    """
    n = int(abs(sup-inf)/h)
      
    somme = 0
    x = inf
    for i in range(0,n): 
        somme += func(x+h/2.)*h
        x += h 
      
    return somme


def trapezes(inf,sup,h,func):
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

  
  
  
  