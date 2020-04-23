# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:16:08 2020

@author: moroo
"""

import numpy as np
from newton import pLateral, pDivise, lateralTable, diviseTable, printTable
from undeterminedCoef import getCoef

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionApproximation')))
from horner import horner

sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


def exo5():
    # Interpolation of sqrt on [1,1.5]
    x0 = np.linspace(1,1.5,5+1)
    rac = np.sqrt(x0)
    table = lateralTable(rac)
    printTable(x0,table)


def exo6():
    # question b : polynomial's degree < 6 
    x0 = np.linspace(-2,3,6)
    p = np.array([-5,1,1,1,7,25])
    table = lateralTable(p)
    #printTable(x0,table)
    # answer : 3
    
    # question c : polynomial's determination with the undetermined 
    # coefficients method
    coef = getCoef(x0,p)
    x = np.linspace(-2,3,100)
    Pc = [horner(coef,xi) for xi in x]
    
    # question d : same as c), but with the Newton divised differences method
    Pd = pDivise(x,x0,p)
    table = diviseTable(x0,p)
    #printTable(x0,table)
    #Graph2D(x,[Pc,Pd],'x','p(x)','Interpolation',['c)','d)']).show()


if __name__ == "__main__":
    exo6()

    

