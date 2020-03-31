# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 02:56:41 2020

@author: moroo
"""

def pointGauche(inf,sup,h,func):
  n = int(abs(sup-inf)/h)
  
  somme = 0
  x = inf
  for i in range(0,n):
    somme += func(x)*h
    x += h  
    
  return somme  
  
def pointDroite(inf,sup,h,func):
  n = int(abs(sup-inf)/h)
  
  somme = 0
  x = inf
  for i in range(0,n):
    somme += func(x+h)*h
    x += h
  
  return somme

def pointMileu(inf,sup,h,func):
  n = int(abs(sup-inf)/h)
  
  somme = 0
  x = inf
  for i in range(0,n): 
    somme += func(x+h/2.)*h
    x += h 
  
  return somme


def trapezes(inf,sup,h,func):
  n = int(abs(sup-inf)/h)
  
  somme = 0
  x = inf
  for i in range(0,n): 
    somme += (func(x+h)+func(x))*h/2.
    x += h 
  
  return somme

  
  
  
  