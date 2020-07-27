# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:34:02 2020

@author: moroo
"""
import numpy as np
from rayleigh import coef as R


def nPower(A,u,err,nmax=20):
    """
        The power method used to compute the largest eigenvalue of the
        A matrix with a first eigenvector approximation u.   
    """
    delta = 1
    coef = []
    lamb = []
    x = u
    i = 0
    coef.append(max(abs(u)))
    
    while(delta >= err and i < nmax):
        i += 1
        x = np.dot(A,x)
        coef.append(max(abs(x)))
        lamb.append(coef[-1]/(coef[-2]))
        if(i>=2):
            delta = abs(lamb[-1]-lamb[-2])
        

    return lamb[-1],x
        


def nPowerShift(A0,u,err,nmax=20):
    """
        The shifted power method used to compute the largest eigenvalue of 
        the A matrix with a first eigenvector approximation u.   
    """
    I = np.eye(len(A0))
    s = R(A0,u)
    delta = 1
    coef = []
    lamb = []
    x = u
    i = 0
    print("i : {}, s : {}".format(i,s))
    coef.append(max(abs(u)))
    
    while(delta >= err and i < nmax):
        A = np.copy(A0)-s*I
        i += 1
        x = np.linalg.solve(A,x)
        x /= np.linalg.norm(x)
        s = R(A0,x)
        print("i : {}, s : {}".format(i,s))
        coef.append(np.max(abs(x)))
        lamb.append(coef[-1]/(coef[-2]))
        if(i>=2):
            delta = abs(lamb[-1]-lamb[-2])

        

    return lamb[-1],x


    
if __name__ == "__main__":
    u = np.array([1,0])
    A = np.array([[2,-1],[-1,2]])
    err = 0.01
    lambda1,x = nPower(A,u,err)
    print("lambda : {}".format(lambda1))
    print("coef rayleight : {}".format(R(A,x)))
    
    
    u = np.array([1,1])
    A = np.array([[2/3.,1/3.],[1/3.,2/3.]])
    err = 0.01
    lambda1,x = nPower(A,u,err)
    print("lambda : {}".format(lambda1))
    print("coef rayleight : {}".format(R(A,x)))