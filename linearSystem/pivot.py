# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:33:05 2020

@author: moroo
"""
import numpy as np

def gauss(A,b):
    """
        Transform A matrix into a triangular one :
            - A : square matrix (n,n)
            - b : vector (n,1)
    """
    testMatrix(A)
    n = len(A)
    A0 = np.copy(A)
    b0 = np.copy(b)
    # pivot line used to suppress xk
    for k in range(0,n-1):
        for i in range(k+1,n):
            coeff = -A0[i][k]/A0[k][k]
            b0[i] += coeff*b0[k]
            for j in range(k,n):
                A0[i][j] += coeff*A0[k][j]
    
    x = np.zeros(n)
    x[n-1] = b0[n-1]/A0[n-1][n-1]
    for k in range(n-2,-1,-1):
        somme = 0
        for j in range(k+1,n):
            somme += A0[k][j]*x[j]
        x[k] = (b0[k]-somme)/A0[k][k]
    

    return A0,b0,x


def reducLU(A,b):
    U = gauss(A,b)[0]
    L = np.dot(A,np.linalg.inv(U))
    return L,U
    


def gaussJordan(A,b):
    """
        Goes further than the gauss method by transforming A into a diagonal
        matrix :
            - A : square matrix (n,n)
            - b : vector (n,1)
    """
    testMatrix(A)
    A0,b0,x = gauss(A,b)
    n = len(A)
    
    for k in range(n-1,0,-1):
        for i in range(k-1,-1,-1):
            coeff = -A0[i][k]/A0[k][k]
            b0[i] += coeff*b0[k]
            for j in range(k,n):
                A0[i][j] += coeff*A0[k][j]
                
    return A0,b0



def testMatrix(A):
    """
        Test if the given matrix contains the value 0.
            - A : square matrix or array
    """
    try:
        assert((A != 0).any())
    except AssertionError:
        print("0 value encountered.")
        return
    


if __name__ == "__main__":
    A = np.array([[1,2,1],[2,3,3],[-1,-3,1]])
    b = np.array([1,3,2])
    m =  np.amax(A,axis=1)
    km = np.argmax(A[2,:])
    print(km)

    L,U = reducLU(A,b)
    print("L : \n{}".format(L))
    print("U : \n{}".format(U))
    print("A = LU : \n{}".format(np.dot(L,U)))
    A1,b1,x = gauss(A,b)
    print("A1 : \n{}".format(A1))
    print("b1 : \n{}".format(b1))
    A1,b1 = gaussJordan(A,b)
    print("A1 : \n{}".format(A1))
    print("b1 : \n{}".format(b1))
    

    