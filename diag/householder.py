# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 02:44:45 2020

@author: moroo
"""

import numpy as np

def matrix(x):
    """
        Householder matrix construction from the x-array 
    """
    el = np.zeros_like(x)
    el[0] = 1
    I = np.eye(len(x))
    v = x + np.sign(x[0])*np.linalg.norm(x)*el
    v /= np.linalg.norm(v)
    P = I-2*np.outer(v,v)
    
    return P,v


if __name__ == "__main__":
    x = np.transpose(np.array([1.,-2.,3.,1.,-1.]))
    P = matrix(x)[0]
    print(P)