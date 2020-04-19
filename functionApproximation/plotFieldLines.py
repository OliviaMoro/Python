# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:59:29 2020

@author: moroo
"""

import numpy as np
from numpy import pi, cos, sin
#from ..tracer_fonctions.methodes_tracer import Graph2D
from fieldLines import FieldLine
from currentLoopField import LoopField
try:
    import os
    import sys
    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    from functionPlot.plotMehods import Graph2D 
except Exception as e :
    print("somme modules ar missing : {}".format(e))
    

def fieldLines():  
    """
        plot field lines for a define set of initial conditions :
            - improve function
            - test for one
            - generalize later
    """
    pas = 0.5
    n = 200
    a = 2
    I = 1
    B = LoopField(a,I)
    Z0 = [1,1,1,1,1]
    R0 = [0.5,0.6,0.7,0.8,0.9]
    lines = []
    R = []; Z = []
    
    for i in range(0,len(Z0)):
        line = FieldLine(R0[i],Z0[i])
        line.timeEuler(pas,n,B.Br,B.Bz)
        lines.append(line)
        #print("Fin calcul ligne {}, n : {}".format(i,len(line.getLine()[0])))
        r = line.getLine()[0]
        z = line.getLine()[1]
        print("min r : {}, max r : {}".format(np.min(r),np.max(r)))
        print("min z : {}, max z : {}".format(np.min(z),np.max(z)))
        
    for i in range(0,len(Z0)):
        R.append(lines[i].getLine()[0])
        Z.append(lines[i].getLine()[1])
        

    graph = Graph2D(R,Z,'r','z')
    graph.show()
    

def testGraph2D():
    x = np.linspace(-pi,pi,50)
    y = np.linspace(-pi/2.,pi/2.,50)
    
    C = np.cos(x)
    S = np.sin(y)
    
    Graph2D([x,y],[C,S]).show()

        
if __name__ == "__main__":
    #testGraph2D()
    fieldLines()