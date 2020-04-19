# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:46:00 2020

@author: moroo
"""

from math import pi
import numpy as np


import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


def tan(x):
    """
        Continued fractions of tan(x) truncated up to the term 'x**2/9'
    """
    num = x*(945-105*x**2+x**4)
    den = 15*(63-28*x**2+x**4)
    return num/den


def exo7():
    """
        Plot the approximation versus the actual function
    """
    n = 100
    x = np.linspace(-pi,pi,n)    
    approx = np.array([])
    TAN = np.tan(x)

    
    for i in range(0,n):
        approx = np.append(approx,tan(x[i]))
    
    Graph2D(x,[TAN,approx],'x','tan(x)','exo7',['tan','fraction']).show()


if __name__ == "__main__":
    exo7() 