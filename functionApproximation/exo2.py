# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 05:37:08 2020

@author: moroo
"""

import numpy as  np
import matplotlib.pyplot as plt
from hermite import H, formHn

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


def exo2():
    """
        "physicists" Hermite polynomials computation
    """
    # question b :
    print("H5(0.5) :",H(5,0.5))
      
    min = -3
    max = 3
    N = 200
    x = np.linspace(min,max,N)

    #tracer  
    y = [formHn(0,min,max,N),formHn(1,min,max,N),formHn(2,min,max,N),
         formHn(3,min,max,N),formHn(4,min,max,N),formHn(5,min,max,N)]
    legend = ['H0','H1','H2','H3','H4','H5']
    graph = Graph2D(x,y,"x","Hn(x)","polynômes d'Hermite",legend)
    graph.ylimit(-50,50)
    graph.show()
      

if __name__ == "__main__":
    exo2()