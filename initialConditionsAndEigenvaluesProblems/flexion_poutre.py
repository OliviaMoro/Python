# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 04:16:38 2020

@author: moroo
"""
import numpy as np

from methodTir import tirRK

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D 


################################ CONSTANTES ###################################
L = 3          # longueur poutre en mètre [m]
E = 10**10     # [N/m^2]
a = 5e-2       # [m] vertical side/section
b = 1e-1       # [m] horizontal section  
I = b*a**3  
mu = 4.2       # [kg/m]
g = 9.8        # 
T = 0          # [N]


def exact(x,I):
    """
        Exact solution of E*I*y'' = T*y - mu*g*x^2/2 with T = 0
        T being the applied force
    """
    A = mu*g/(24.*E*I)
    return A*x*(4*L**3-x**3)
    


def approx(T,I):
    """
        We redefine the differential system as :
            y' = z                         - yDer
            z' = (T/EI)y - (mu*g/2*EI)*x^2 - zDer
    """
    
    def yDer(x,y,z):
        return z
        
        
    def zDer(x,y,z):
        c1 = T/(E*I)
        c2 = mu*g/(2*E*I)
        return c1*y-c2*x**2
    
    n = 300
    y0 = 0
    z0 = mu*g*L**3/(6.*E*I)
    
    x,y,z = tirRK(n,L,y0,z0,yDer,zDer)
    print("y'(L) = {}, y(L) = {}".format(z[-1],y[-1]))
    arrow = mu*g*L**4/(8.*E*I)
    print("y0(L) = {}".format(arrow))
    
    return x,y,z
    
    

def questionC1():
    x,y,z = approx(T,I)
    
    #Exact Solution
    ye = [exact(xi,I) for xi in x]
    legend = ["exacte","approchée"]
    graph = Graph2D(x,[ye,y],"x","y","Déformation poutre",legend)
    graph.show()
    
    
    
def questionC2():
    T = 5000
    x,y,z = approx(T,I)
    
    ye = [exact(xi,I) for xi in x]
    legend = ["T = 0 N","T = 5000 N"]
    graph = Graph2D(x,[ye,y],"x","y","Déformation poutre",legend)
    graph.show()



def questionD():
    x = np.linspace(0,L,100)
    
    # a < b :
    b = 1e-1
    a = 5e-2
    I = b*a**3
    y1 = [exact(xi,I) for xi in x]
    
    # a > b :
    a = 1e-1
    b = 5e-2
    I = b*a**3  
    y2 = [exact(xi,I) for xi in x]

    legend = ["a < b","a > b"]
    graph = Graph2D(x,[y1,y2],"x","y","Déformation poutre",legend)
    graph.show()



def questionE():
    # Effet des forces de compressions
    T = -5000
    b = 1e-1
    a = 5e-2
    I = b*a**3  
    x,y,z = approx(T,I)
    
    ye = [exact(xi,I) for xi in x]
    legend = ["T = 0 N","T = -5000 N"]
    graph = Graph2D(x,[ye,y],"x","y","Déformation poutre",legend)
    graph.show()
    


if __name__ == "__main__":
    #questionC1()
    questionC2()
    #questionD()
    #questionE()