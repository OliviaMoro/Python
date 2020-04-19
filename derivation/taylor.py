# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 01:44:33 2020

@author: moroo
"""

from math import log

def taylor1(h,x,func):
    """
        Computes the derivative of the 'func' function at x with a small
        enough h using a first order Taylor development
    """
    der = (func(x+h)-func(x))/h
    return der


def taylor1Mid(h,x,func):
    """
        Computes the derivative of the 'func' function at x (at the mid
        point) with a small enough h using a first order Taylor development 
    """
    der = (func(x+h)-func(x-h))/(2*h)
    return der



def taylorTest():
    """
        Above defined functions's test for the well known ln function
    """
    x = [0.159, 0.160, 0.161]
    #lnx = [-1.83885, -1.83258, -1.82635]
    #Ici h = 0.001
    h = 1e-3
    der1 = taylor1(h,x[1],log)
    der2 = taylor1Mid(h,x[1],log)
    print("der 1 :",der1, "der2 :", der2, "exact :", 1/x[1])


if __name__ == "__main__":
    taylorTest()