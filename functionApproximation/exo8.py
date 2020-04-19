# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:57:47 2020

@author: moroo
"""

import numpy as np
try:
    import os
    import sys
    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    from functionPlot.plotMethods import Graph2D 
except Exception as e :
    print("somme modules ar missing : {}".format(e))


def argthPade(x):
    """
        Padé's approximation R3,4 of argth(x)
    """
    num = x*(105-55*x**2)
    den = 105 -100*x**2-9*x**4
    return num/den


def argthMacLaurin7(x):
    """
        Mac Laurin's development up to the 8-th order of the argth function
    """
    return x + 1/3.*x**3 + 1/5.*x**5 + 1/7.*x**7


def exo8():
    n = 200
    x = np.linspace(-0.9,0.9,n)
    f = np.arctanh(x)
    p = np.array([]); g = np.array([])
    
    for i in range(0,n):
        p = np.append(p,argthMacLaurin7(x[i]))
        g = np.append(g,argthPade(x[i]))
        
    Graph2D(x,[f,p,g],"x","argth(x)","exo8",["f","p","g"]).show()


if __name__ == "__main__":
    exo8()  