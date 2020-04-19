# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 04:58:48 2020

@author: moroo
"""
import numpy as np
from . import horner

def exo1():  
  """ 
      evaluation of a given polynomial at a certain value with the horner 
      method
  """        
  # P1(x) = 2*x**3-3*x+1
  polynome1 = np.array([1,-3,0,2])
  result1 = horner(polynome1,2)
  print("result1 : ",result1)   
  result2 = horner(polynome1,1)
  print("result2 : ",result2)
  
  # P2(x) = 7*x**4+5*x**3-2*x**2+8
  polynome2 = np.array([8,0,-2,5,7])
  result3 = horner(polynome2,0.5) 
  print("result3 : ",result3)
  
if __name__ == "__main__":
  exo1()