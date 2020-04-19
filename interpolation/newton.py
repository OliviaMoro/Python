# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:10:15 2020

@author: moroo
"""

import numpy as np

def diviseDifferences(x0,f):
    """
        computes the newton polynom differences f[x0,...,xn] of a function f 
        at the given points x0, the order is deduced from the length of x0 
        and f (which are the same) :
            - x0 : array of values
            - f : array of values
    """
    n = len(x0)
    tmp = np.zeros(n); diff = np.zeros(n)
    # Differences :
    for i in range(0,n):
        tmp[i] = f[i]
        
        for j in range(i-1,-1,-1):
            tmp[j] = (tmp[j+1]-tmp[j])/(x0[i]-x0[j])
        diff[i] = tmp[0]  
        #print("diff({}) : {}".format(i,diff[i]))
        
    return diff



def lateralDifferences(x0,f):
    """
        computes newton polynom coefficients given by the ascendant lateral
        differences method :
            - x0 : array of values
            - f : array of values
        Usefull for x0 of evenly spaced values
    """
    finite = diviseDifferences(x0,f)
    diff = np.zeros(len(finite))
    diff[0] = finite[0]
    facteur = 1
    h = abs(x0[1]-x0[0])
    #print("h : {}".format(h))
    #print("diff({}) : {}".format(0,diff[0]))
    
    for i in range(1,len(finite)):
        facteur *= h*i
        diff[i] = facteur*finite[i]
        #print("diff({}) : {}, facteur : {}".format(i,diff[i],facteur))
    
    return diff



def pDivise(x,x0,f):
    """
        computes the interpoling newton polynom for the set of points x with
        the interpoling points x0 of value f using the divised differences 
        method :
            - x0 : array of values
            - f : array of values
    """
    try:
        assert(len(x0)==len(f))
    except AssertionError:
        print("Given arrays aren't the same length.")
        return
    
    diff = diviseDifferences(x0,f)
    n = len(x0)
    poly = diff[n-1]
    
    for i in range(n-2,-1,-1):
        poly = np.multiply((x-x0[i]),poly)+diff[i]
    
    return poly



def pLateral(x,x0,f):
    """
        computes the interpoling newton polynom for the set of points x with
        the interpoling points x0 of value f using the lateral differences
        method :
            - x0 : array of values
            - f : array of values
    """
    try:
        assert(len(x0)==len(f))
    except AssertionError:
        print("Given arrays aren't the same length.")
        return
    
    diff = lateralDifferences(x0,f)
    h = abs(x0[1]-x0[0])
    mu = np.divide(x-x0[0],h)
    n = len(x0)
    poly = diff[n-1]
    
    for i in range(n-2,-1,-1):
        poly = np.multiply((mu-i)/(i+1),poly)+diff[i]
    
    return poly



def diviseTable(x0,f):
    """
        computes every divised differences for a given dataset f
    
    """
    n = len(x0)
    tmp = f
    diff = [f]
    k = 1
    
    while (len(tmp)>1):
        delta = []
        for i in range(0,n-k):
            delta.append((tmp[i+1]-tmp[i])/(x0[i+k]-x0[i]))
            #print("den : x0[{}]-x0[{}]".format(i+k,i))
        diff.append(delta)
        tmp = delta
        k += 1
        
    return diff



def lateralTable(f):
    """
        computes every lateral differences for a given dataset f
    
    """
    diff = [f]
    #print(len(diff[0]))
    tmp = diff[0]
    k = len(f)-1

    while (len(tmp) > 1):
        delta = []
        for i in range(1,k+1):
            delta.append(tmp[i]-tmp[i-1])
        diff.append(delta)
        tmp = delta
        k -= 1
        
    return diff


    
def printTable(x0,table):
    n = len(x0)

    head = ['i','xi     ','fi    ']
    for i in range(1,n):
        head.append('delta{}f'.format(i))
    print(*head)
    
    # init list
    lines = []
    blank = "    "
    for i in range(0,n):
        line = [i,'%.4f' %x0[i],'%.4f' %table[0][i]]
        lines.append(line)
        line = [' ',blank,blank]
        lines.append(line)
        
    # iteration over the difference order k   
    for k in range(1,n):
        j = 0
        i = 0
        while (j < len(table[k])):
            lines[k+i].append(blank)
            lines[k+i].append('%.4f' %table[k][j])
            j += 1
            i += 2          
        
    for line in lines :
        print(*line)

            


    
    
    


    
    
    
    