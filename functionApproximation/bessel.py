# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:36:08 2020

@author: moroo
"""

def J0(x,n):
    """
        Evaluation of the zeroth order Bessel function at the value x from 
        its power series up to the n-th term
    """
    terme = 1
    somme = terme
    
    for i in range(1,n+1):
        terme = terme*-1*x*x/(4.*i*i)
        somme += terme
    return somme