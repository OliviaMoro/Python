# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:49:41 2020

@author: moroo
"""

from math import cos, sin, pi, atan, sqrt
import numpy as np


def rotation(j,k,A):
    """
        Rotation matrix construction made from the A matrix in order to
        suppress de element at the j line and at the k column from A.
    """
    theta = pi/4.
    if (A[j][j] != A[k][k]):
        theta = 0.5*atan(2*A[j][k]/(A[k][k]-A[j][j]))
        
    R = np.eye(len(A))
    R[j][j] = cos(theta)
    R[k][k] = cos(theta)
    if (j < k):
        R[j][k] = sin(theta)
        R[k][j] = -sin(theta)
    elif (j > k):
        R[j][k] = -sin(theta)
        R[k][j] = sin(theta)
        
    return R



def jacobi(A0,imax=10):
    """
        A Jacobi method implementation used to compute the eigenvalues of a
        given matrix A0 :
            - A0 : must be a square matrix
    """
    tol = 1e-16
    n = len(A0)
    A = np.copy(A0)
    Ri = np.eye(n)
    i = 0
    
    while (i < imax):
        i += 1
        j,k = maxExtradiagElt(A,n)
        #print("(j,k) = ({},{})".format(j,k))
        R = rotation(j,k,A)
        #print("R:\n",R)
        A = np.dot(np.transpose(R),np.dot(A,R))
        A[abs(A) < tol] = 0.0
        #print("A:\n",A)
        Ri = np.dot(Ri,R)
        S = np.linalg.norm(A)**2-diagNorm(A)
        print(S)
    
    print(Ri)
        
    return A,Ri



def diagNorm(A0):
    """
        Frobenius norm of the given A0 matrix deprived of extra-diagonal
        elements. 
    """
    A = np.zeros((len(A0),len(A0)))
    for i in range(0,len(A0)):
        A[i][i] = A0[i][i]
        
    return np.linalg.norm(A)**2
    
    

def maxExtradiagElt(A0,n):
    """
        Search for the maximum extra-diagonal element in the A0 matrix :
            - A0 : matrix
            - n : len(A0)   
    """
    ajk = 0
    l,m = 0,0
    A = np.copy(A0)

    for j in range(0,n):
        A[j][j] = 0
        k = np.argmax(A[j,:])

        if (k != j and A[j][k]>ajk):
            l,m = j,k
            ajk = A[j][k]
            
    return l,m
   
    
    
if __name__ == "__main__":
    F = np.array([[1.0,1.,0.5],[1.0,1.,0.25],[0.5,0.25,2.0]])
    A,R = jacobi(F,4)
    c0 = R[0:3,0]
    c1 = R[0:3,1]
    c2 = R[0:3,2]
    d0 = np.dot(F,c0)
    print(np.divide(d0,c0)[0])
    d1 = np.dot(F,c1)
    print(np.divide(d1,c1)[0])
    d2 = np.dot(F,c2)
    print(np.divide(d2,c2)[0])
    