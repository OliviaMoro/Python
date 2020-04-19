# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:42:52 2020

@author: moroo
"""

import numpy as np
from bezier import curve

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


def test():
    xPoints = np.array([0,2,4,6])
    yPoints = np.array([1,4,1,4])
    u = np.linspace(0,1,50)
    x,y = curve(u,xPoints,yPoints)
    print("P0 : ({},{})".format(x[0],y[0]))
    print("P3 : ({},{})".format(x[-1],y[-1]))
    
    graph = Graph2D([xPoints,x],[yPoints,y],'x','y','test Bézier',['points','courbe'])
    graph.show()
    
    
if __name__ == "__main__":
    test()    