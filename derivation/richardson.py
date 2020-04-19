# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 02:32:29 2020

@author: moroo
"""

from math import atan


def richardson4(h,x,func):
    """
        Evaluates the derivative of the 'func' function at x with a small
        enough h using a fourth order Taylor's extrapolation
    """
    der = (8*func(x+h/4.)-8*func(x-h/4.)+func(x-h/2.)-func(x+h/2.))/(3*h)
    return der


def f(x):
    return atan(2*x)



def test():
    """
        Above defined functions's test for the f function
    """
    h = 0.05
    x = 1.5
    der = richardson4(h,x,f)
    print("der :", der, "exact :", 2./(1+4.*x*x))


if __name__ == "__main__":
    test()
