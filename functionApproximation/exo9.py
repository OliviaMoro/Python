# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:29:08 2020

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
    


def thMacLaurin8(x):
    """
        Mac Laurin's development up to the 8-th order for th
    """
    return x - 1/3.*x**3 + 2/15.*x**5 - 17/315.*x**7



def thPade3_4(x):
    """
        Padé's approximation R_{3,4} of th
    """
    num = x + 2/21.*x**3
    den = 1 + 3/7.*x**2 + 1/105.*x**4
    return num/den  


def exo9():
    n = 300
    x = np.linspace(-2,2,n)
    th = np.tanh(x)
    thPade = np.array([]); thML = np.array([])
    
    for i in range(0,n):
        thPade = np.append(thPade,thPade3_4(x[i]))
        thML = np.append(thML,thMacLaurin8(x[i]))
        
    Graph2D(x,[th,thPade,thML],"x","th(x)","exo9",["tanh","Pade","Mac Laurin"]).show()
        
    
    

if __name__ == "__main__":
    exo9()  