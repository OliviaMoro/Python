# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:54:39 2020

@author: moroo
"""
import numpy as np
from math import sqrt

def cholesky(A):
    """
        Implementation of the Cholesky algorithm for a given square matrix
        A. Works better for a diagonally dominant matrix. Returns the result 
        of the decomposition G such as A = G*transpose(G).
    """
    n = len(A)
    G = np.zeros((n,n))
    # G triangular inferior matrix : G[i,j] = 0 si i<j

    for i in range(0,n):
        for j in range(0,i+1):
            somme = 0
            for k in range(0,j):     
                somme += G[i][k]*G[j][k]
            if (i == j):
                G[i][j] = sqrt(A[i][j]-somme)
            else:
                G[i][j] = (A[i][j]-somme)/G[j][j]   
            print("(i,j)=({},{}), Gij : {}".format(i,j,G[i][j]))
    return G
    

    
if __name__ == "__main__":
    A = np.array([[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]])
    print(A)
    G = cholesky(A)
    print(G)