# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:48:05 2020

@author: moroo
"""
#import numpy as np

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'integrator')))
from eulerMethod import explicitEuler

class FieldLine:
    """
        Builds a 2D field line with (u0,v0) as starting point
    """
 
    def __init__(self,u0,v0):
        # Initial conditions
        self.u0 = u0
        self.v0 = v0
        # line coordinztes
        self.u = [u0]
        self.v = [v0]
        
      
    def timeEuler(self,pas,n,Bu,Bv):
        """
            Compute u, v coordinates of the line given :
                - pas : pas d'integration
                - Bu : B field component along the u axis
                - Bv : B field component along the v axis
        """
        t = []
        t.append(0)
        u = []
        u.append([self.u0,self.v0])
        
        for i in range(1,n+1):
            (tf,uf)= explicitEuler(pas,t[i-1],u[i-1][0],u[i-1][1],key1=Bu,key2=Bv)
            t.append(tf)
            u.append(uf)
            
        self.u = [i for i,j in u]
        self.v = [j for i,j in u]
        
    def getLine(self):
        return self.u,self.v
        