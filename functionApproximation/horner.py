# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 05:24:20 2020

@author: moroo
"""

def horner(coef,x):
    """ 
        Horner computation method of a polynomial :
            - coef : the polynomial coefficients array ordered by increasing
                exponent value
            - x : evaluation value
    """
    z = coef[-1]    # z0 : coefficient dominant du polynôme
    n = len(coef)   # degré du polynome
      
    for i in range(1,n):
        # Calcul des zk
        z = x*z + coef[-1-i]
        
    return z