# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:16:49 2020

@author: moroo
"""

import numpy as np
from numpy import real, imag
#from cmath import real, imag
from math import pi, cos, sin

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D


def circle(origin,radius):
    """ 
        Circle creation in complex coordinates with :
            - origin : O = ox + j* oy
            - radius : x*x + y*y = radius*radius
    """
    n = 700
    circle = np.array([])
    angle = np.linspace(0,2*pi,n)
    
    for i in range(0,n):
        x = origin.real + radius*cos(angle[i])
        y = origin.imag + radius*sin(angle[i])
        circle = np.append(circle,x+y*1j)
    
    return circle


def drawCircles():
    origin = 0.8+0.5j
    circle1 = circle(origin,0.75)
    circle2 = circle(origin,1)
    circle3 = circle(origin,1.25)
    
    x = np.array([circle1.real,circle2.real,circle3.real])
    y = np.array([circle1.imag,circle2.imag,circle3.imag])
    #Graph2D(x,y,'x','y','Cercles',['r=0.75','r=1','r=1.25']).show()
    
    w1 = 1/circle1
    w2 = 1/circle2
    w3 = 1/circle3
    
    X = np.array([w1.real,w2.real,w3.real])
    Y = np.array([w1.imag,w2.imag,w3.imag])
    #Graph2D(X,Y,'x','y','1/z',['r=0.75','r=1','r=1.25']).show()
    
    b = 1
    circle4 = circle(-0.25,1.25)
    wJ = circle4 + b*b/circle4
    graph = Graph2D(wJ.real,[wJ.imag],'x','y','Joukovsky')
    graph.setEqual()
    graph.show()
    
    
    
    
if __name__ == "__main__":
    drawCircles()  
    
    