# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 00:23:02 2020

@author: moroo
"""

from math import pi, sqrt
from elliptique import E, K

class LoopField:
    """
        Magnetic field's components computation of a current loop :
            - a : radius of the loop
            - I : current passing through the loop
    """
    mu0 = 1#4*pi*1e-7
    
    def __init__(self,a,I):
        self.a = a
        self.I = I
        self.B0 = self.mu0*I/(2*a)
        
    def cylCoord(self,r,z):
        rho = r/self.a
        eta = z/self.a
        Q = (1+rho)*(1+rho) + eta*eta
        k = sqrt(4*rho/Q)
        
        return rho,eta,Q,k
        
    
    def Bz(self,t,r,z):
        """
            B field's z component in the cylindrical coordinate's
            system
        """
        rho,eta,Q,k = self.cylCoord(r,z)
        num = 1 - rho*rho - eta*eta
        den = (1-rho)*(1-rho) + eta*eta
        
        return self.B0/(pi*sqrt(Q))*(E(k)*num/den + K(k)[0])
        
    
    def Br(self,t,r,z):
        """
            B field's r component in the cylindrical coordinate's
            system
        """
        rho,eta,Q,k = self.cylCoord(r,z)
        num = 1 + rho*rho + eta*eta
        den = (1-rho)*(1-rho) + eta*eta
        
        return self.B0*z/(r*pi*sqrt(Q))*(E(k)*num/den - K(k)[0])
        