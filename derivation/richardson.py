# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 02:32:29 2020

@author: moroo
"""

from math import atan

# extrapolation de taylor d'ordre 4 :
def richardson4(h,x,func):
  der = (8*func(x+h/4.)-8*func(x-h/4.)+func(x-h/2.)-func(x+h/2.))/(3*h)
  return der

def f(x):
  return atan(2*x)

#exemple du cours avec log néperien
def test():
  h = 0.05
  x = 1.5
  der = richardson4(h,x,f)
  print("der :", der, "exacte :", 2./(1+4.*x*x))


if __name__ == "__main__":
  test()
