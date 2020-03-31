# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 01:44:33 2020

@author: moroo
"""

from math import log

# Utilise la formule de Taylor avec reste integral pour n = 1
def taylor1(h,x,func):
  der = (func(x+h)-func(x))/h
  return der

def taylor1Milieu(h,x,func):
  der = (func(x+h)-func(x-h))/(2*h)
  return der

#exemple du cours avec log néperien
def taylorTest():
  x = [0.159, 0.160, 0.161]
  #lnx = [-1.83885, -1.83258, -1.82635]
  #Ici h = 0.001
  h = 1e-3
  der1 = taylor1(h,x[1],log)
  der2 = taylor1Milieu(h,x[1],log)
  print("der 1 :",der1, "der2 :", der2, "exacte :", 1/x[1])


if __name__ == "__main__":
  taylorTest()