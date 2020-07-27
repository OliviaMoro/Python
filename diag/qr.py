# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 04:57:45 2020

@author: moroo
"""
import numpy as np
from householder import matrix


def factor(A0):
    """
        QR algorithm implementation :
            - A0 : given square matrix
            - Q : orthogonal matrix
            - A = R : upper triangular matrix 
        The purpose is to bring A0 to a tridiagonal form.      
    """
    tol = 1e-16
    
    A = np.copy(A0)
    n = len(A)
    #print("n : {}".format(n))
    V = np.zeros((n,n))
    for k in range(n-1):
        x = A[k:n,k]
        print("x : {}".format(x))
        v = matrix(x)[1]
        V[k:n,k] = v
        A[k:n,k:n] -= 2*np.outer(v,np.dot(np.transpose(v),A[k:n,k:n]))
        A[abs(A) < tol] = 0.0
        
    
    Q = np.eye(n)
    for k in range(0,n):
        Q -= 2*np.outer(np.dot(Q,V[0:n,k]),np.transpose(V[0:n,k]))     
        #Q[abs(Q) < tol] = 0.0
        
    return Q,A
        
        

if __name__ == "__main__":
    F0 = np.array([[1.,1.,0.5],[1.,1.,0.25],[0.5,0.25,2.]])
    S = np.eye(len(F0))
    
    for i in range(0,20):
        Q,R = factor(F0)
        F0 = np.dot(R,Q)
        S = np.dot(S,Q)
    
    print("F : \n {}".format(F0))
    print("S : \n {}".format(S))        