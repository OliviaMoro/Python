# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:20:48 2020

@author: moroo
"""
import numpy as np
from math import isclose
from scipy.integrate import complex_ode, ode, odeint

from methodTir import tirRK



def system(n,y0,tf,f,args = []):
    """
        Integration of the differential system between t = 0 and tf :
            - n : number of step
            - y0 : initial(s) condition(s)
            - tf : endpoint
            - k : tested eigenvalue
            - f : defined differential system in scipy.integrate fashion
    """
        
    sol = complex_ode(f)
    # complex_ode doesn't accept args in set_f_params method
    sol.set_f_params(args,)
    sol.set_initial_value(y0,0)
    #sol.set_integrator('zvode', method='bdf')
    
    dt = tf/(n*1.)
    y = np.zeros((n,len(y0)))
    y[0] = y0
    
    for i in range(0,n):
        y[i] = sol.integrate(sol.t+dt)
        print("i : {}, y : {}".format(i,y))

    return y



def searchK(n,y0,cf,k1,k2,f,i=0,tol=1e-3,nmax=20,args=[]):
    """
        Search by dichotomy of an eigenmode between two values k1 and k2 :
            - k1, k2 : float
            - n : number of step of integration
            - y0 : initial(s) condition(s) array of flot
            - i : index apointing the used variable
            - cf : boundary condition to test 
    """
    delta = 1
    i = 0
    
    while (not isclose(delta,0,rel_tol=tol,abs_tol=tol) and i <= nmax):
        i += 1
        # The interval is cut in two
        k0 = (k1+k2)/2.
        
        k = k1
        y1 = f(n,y0,k,args)[i]
        k = k0 
        y2 = f(n,y0,k,args)[i]
        #print("k : {}".format(k))

        # root is in [a,x0] : the sign changed 
        if ((y1[-1]-cf)*(y2[-1]-cf) < 0 ):
            k2 = k0
        # root is in [x0,b] : sign unchanged  
        elif ((y1[-1]-cf)*(y2[-1]-cf) > 0):
            k1 = k0
        delta = y2[-1]-cf
        #print("y2[-1]-cf : {}".format(y2[-1]-cf))
            
            
    print("[k1,k2] = [{},{}], i = {}".format(k2,k1,i))
    return k0



def searchKRK(n,x0,y0,z0,k1,k2,xDer,yDer,tol=1e-3,nmax=20):
    """
        Modify integrator's functins to allow extra arguments
    """
    delta = 1
    i = 0
    
    while (not isclose(delta,0,rel_tol=tol, abs_tol=tol) and i <= nmax):
        i += 1
        # The interval is cut in two
        k0 = (k1+k2)/2.
        
        k = k1
        x,y1,z1 = tirRK(n,1,y0,z0,xDer,yDer,x0)
        k = k0 
        x,y2,z2 = tirRK(n,1,y0,z0,xDer,yDer,x0)
        print("k : {}".format(k))

        # root is in [a,x0] : the sign changed 
        if (y1[-1]*y2[-1] < 0 ):
            k2 = k0
        # root is in [x0,b] : sign unchanged  
        elif (y1[-1]*y2[-1] > 0):
            k1 = k0
        delta = y2[-1]
    
    print("[k1,k2] = [{},{}], i = {}".format(k2,k1,i))
    return k0

