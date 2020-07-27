# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 02:20:42 2020

@author: moroo
"""
from random import randint, random
import numpy as np

from methodTir import tirEuler
from potentials import V, V1, impurity, amorphous

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D 


a0 = 1    #0.529e-10 # Borh radius
Eh = 27.2 #to convert eV to hartree


"""
    We redefine the differential system as :
        y' = z                            - yDer
        z' = -2*(E-V(x))*y                - zDer
"""
def yDer(x,y,z):
    return z
    
    
def zDer(x,y,z):
    return -2*(E-V(x,nw))*y



def getA(nw,n):
    a = 4*a0+1.5*a0
    if (nw != 1):
        a = 4*a0+nw*1.5*a0+(nw-1)*0.5*a0
    return a


        
def testImpurity(nw,n):
    a = getA(nw,n)
    x = np.linspace(0,a,n+1)
    iw = randint(1,nw)
    v = [V(x[i],nw)+impurity(x[i],iw) for i in range(0,n+1)]
    #v = [impurity(x[i],iw) for i in range(0,n+1)]
    
    graph = Graph2D(x,[v],"x [a0]","V(x)","adding Impurity")
    graph.show()
    
    
    
def testAmorphous(nw,n):
    a = getA(nw,n)
    x = np.linspace(0,a,n+1)
    sizes = [1.5*a0*random() for i in range(0,nw)]
    #print("sizes : {}".format(sizes))
    v = [V(x[i],nw)+amorphous(x[i],nw,sizes) for i in range(0,n+1)]
    
    graph = Graph2D(x,[v],"x [a0]","V(x)","amorphous solid")
    graph.show()
    
    
    
def testVoltageStep(nw,n):
    a = getA(nw,n)
    x = np.linspace(0,a,n+1)
    v = [V(x[i],nw)+V1(x[i],a) for i in range(0,n+1)]
    
    graph = Graph2D(x,[v],"x [a0]","V(x)","Potential + voltage step")
    graph.show()
    
    

def testPotential(nw,n):
    a = getA(nw,n)
    x = np.linspace(0,a,n+1)
    v = [V(x[i],nw) for i in range(0,n+1)]
    
    graph = Graph2D(x,[v],"x [a0]","V(x)","Kronig Penney potential")
    graph.show()




def well():
    # potential well number 
    nw = 4         
    yd = 1; yg = 1; y0 = np.array([yg,yd])
    zd = 0; zg = 0; z0 = np.array([zg,zd])
    n = 300
    a = getA(nw,n)
    #testPotential(nw,n)
    
    global E
    E = -266.7709/Eh; E1 = E*Eh
    x,y1,z1 = tirEuler(n,a,y0,z0,yDer,zDer)
    y1 = y1/np.linalg.norm(y1)
    

    E = -3.98506/Eh; E2 = E*Eh
    x,y2,z2 = tirEuler(n,a,y0,z0,yDer,zDer)
    y2 = y2/np.linalg.norm(y2)
    
    
    legend = ["E = "+str(E1),"E = "+str(E2)]
    graph = Graph2D(x,[y1,y2],"x [a0]","Psi(x)","Potential well",legend)
    graph.show()
    


if __name__ == "__main__":
    nw = 4
    #testPotential(nw,100)
    #testImpurity(nw,100)
    #testAmorphous(nw,100)
    #testVoltageStep(nw,100)
    well()
    
    