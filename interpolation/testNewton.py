# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:43:13 2020

@author: moroo
"""
import numpy as np
from newton import pLateral, pDivise, lateralTable, printTable

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D

def interpolExp():
    x0 = np.array([-1,0.5,1.5,2.])
    f = np.exp(x0)
    x = np.linspace(-2.3,50)
    poly = pDivise(x,x0,f)
    xExp = np.exp(x) 
    graph = Graph2D(x,[poly,xExp],'x','f(x)','Exp interpolation',[r'$p_{0123}}$','exp'])
    graph.xlimit(-2,3)
    graph.ylimit(-5,11)
    graph.show()
    
    
def interpolRac():
    x0 = np.linspace(1,2,10+1)
    rac = np.sqrt(x0)
    x = np.array([1.24,1.86])
    poly = pLateral(x,x0,rac)
    print(poly)
    table = lateralTable(rac)
    printTable(x0,table)
    


if __name__ == "__main__":
     interpolExp()
     #interpolRac()
    