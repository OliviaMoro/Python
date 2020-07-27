# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 03:08:12 2020

@author: moroo
"""
from math import pi, isclose
from scipy.integrate import complex_ode
import numpy as np

from methodTir import tirRK

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'functionPlot')))
from plotMethods import Graph2D 


P0 = 101325         # atmospheric pressure [Pa]
rho = 1.184         # density of dry air at 25°C [kg/m^3]
gamma = 5/3.        # gamma = Cp/Cv monoatomic ideal gas
A = rho/(gamma*P0)
L = 0.8             # pipe length [m]



def pressure(omg,A,L,S,derS,n,p0,q0):
    """
        Integration of : p'' + (S'/S)p' + omg^2*A*p = 0
        p' = q
        q' = -(S'/S)q -omg^2*A*p
    """
    def pDer(x,p,q):
        return q
        
        
    def qDer(x,p,q):
        return -derS(x)/S(x)*q-A*omg**2*p
    
    x,p,q = tirRK(n,L,p0,q0,pDer,qDer,opt=4)
    return x,p,q
    

    
def flow(omg,A,L,S,derS,n,u0,v0):
    """
        Integration of : U'' - (S'/S)U' + omg^2*A*U = 0
        U' = V
        V' = (S'/S)V -omg^2*A*U
    """
    def uDer(x,u,v):
        return v
        
        
    def vDer(x,u,v):
        return derS(x)/S(x)*v-A*omg**2*u

    x,U,V = tirRK(n,L,u0,v0,uDer,vDer,opt=4)
    return x,U,V



def system(omg,L,S,n,p0,u0):
    def pDer(x,p,u):
        return -1j*(omg*rho/S(x))*u
        
        
    def uDer(x,p,u):
        return -1j*(omg*S(x)/(gamma*P0))*p 
    

    def f(x,y):
        p,u = y
        dydt = [pDer(x,p,u),
                uDer(x,p,u)]
        return dydt
        
    y0 = np.array([p0,u0])
    sol = complex_ode(f)
    sol.set_initial_value(y0,0)
    #sol.set_integrator('zvode', method='bdf')
    
    dx = L/100.
    y = np.zeros((n,2))
    y[0] = y0
    
    for i in range(0,n):
        y[i] = sol.integrate(sol.t+dx)

    p = y[:,0]
    u = y[:,1]
    
    return p,u



def searchK(n,L,S,p0,u0,pf,uf,k1,k2,choice = 1):
    """
        choice : 1 = we test the boundary condition for p
                 2 = we test the boundary condition for u
    
    """
    delta = 1
    tol = 0.005
    nmax = 20
    i = 0
    
    while (not isclose(delta,0,rel_tol=tol, abs_tol=tol) and i <= nmax):
        i += 1
        # The interval is cut in two
        k0 = (k1+k2)/2.
        
        k = k1
        p1,u1 = system(k,L,S,n,p0,u0)
        k = k0 
        p2,u2 = system(k,L,S,n,p0,u0)
        #print("k : {}".format(k))

        if (choice == 1):
            # root is in [a,x0] : the sign changed 
            if ((p1[-1]-pf)*(p2[-1]-pf) < 0 ):
                k2 = k0
            # root is in [x0,b] : sign unchanged  
            elif ((p1[-1]-pf)*(p2[-1]-pf) > 0):
                k1 = k0
            delta = p2[-1]-pf
            #print("p2[-1]-pf : {}".format(p2[-1]-pf))
            
        elif (choice == 2):
            # root is in [a,x0] : the sign changed 
            if ((u1[-1]-uf)*(u2[-1]-uf) < 0 ):
                k2 = k0
            # root is in [x0,b] : sign unchanged  
            elif ((u1[-1]-uf)*(u2[-1]-uf) > 0):
                k1 = k0
            delta = u2[-1]-uf
            #print("u2[-1]-uf : {}".format(u2[-1]-uf))
            
    print("u2[-1]-uf : {}".format(u2[-1]-uf))
    print("[k1,k2] = [{},{}], i = {}".format(k2,k1,i))
    return k0
    

    
if __name__ == "__main__":
    n = 100
    a = 0.012
    L = 0.8 + 0.6*a
    
    def S(x):
        return pi*a**2*(1-x/L)**2
    
    def derS(x):
        return -2*pi*a**2*(1-x/L)/L
    
    
    # Question b :
    """
        Eigenmode for open-open boundaries conditions are : 
            w = p*987.5
        Eigenmode for open-close boundaries conditions are : 
            w = p*987.5/2  
    """
    w1 = 987.5
    w2 = 1975.
    w3 = 2962.5

    omg = 4500
    # open-open boundaries :
    u0 = 10; p0 = 0
    
    omg = searchK(n,L,S,p0,u0,p0,0,4000,4500,choice = 2)
    print("omg : {}".format(omg))
    
    p,u = system(omg,L,S,n,p0,u0)
    x = np.linspace(0,L,n)
    print("u[-1]-u0 : {}".format(u[-1]-u0))
    
    graphP = Graph2D(x,[p],"x","p","acoustic pressure")
    graphP.show()
    graphU = Graph2D(x,[u],"x","u","flow")
    graphU.show()
    
    
    # Question e :
    w1 = 1469.7265625
    w2 = 2938.4765625
    w3 = 4410.15625
    
    
