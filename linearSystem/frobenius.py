# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:39:08 2020

@author: moroo
"""
import numpy as np

def f(i,j,m,n):
    """
        Frobenius matrix construction given :
            - i : line index 
            - j : column index 
            - m : element value at (i,j)
            - n : matrix size
    """
    try:
        assert(i>j and isinstance(i,int) and isinstance(j,int))
    except AssertionError:
        print("Index aren't int or i < j.")
        return
    
    try:
        assert(i<n and j<n and isinstance(n,int))
    except AssertionError:
        print("The size must be an integer or i,j >= n.")
        return
    F = np.identity((n))
    F[i][j] = m
    return F



if __name__ == "__main__":
    L = f(3,2.,4,4)
    print(L)