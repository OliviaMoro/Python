# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 12:33:20 2020

@author: moroo
"""
import numpy as np
from math import exp, cos, sin, pi
from plotMethods import Graph2D



def exo1():
    a = 0.6; b = 7.; min = 0.; max = 5.; n = 150
    t = np.linspace(min,max,n)
    x = np.array([])
    y = np.array([])
    
    for i in range(0,n):
        x = np.append(x,exp(-a*t[i])*cos(b*t[i]))
        y = np.append(y,exp(-a*t[i])*sin(b*t[i]))
        
    yt = Graph2D(t,[x],"t","x")
    yx = Graph2D(x,[y],"x","y")
    tx = Graph2D(x,[t],"x","t")
    yt.show()
    yx.show()
    tx.show()
    
    
    
def exo2():
    t = np.array([0,1,2,3,4,5,10])
    N = np.array([1000,370,130,50,17,8,1])
    decroit = Graph2D(t,[N],"t","N(t)")
    decroit.show()
    
      
    
def exo3():
    L = 2; M = 4; N = 3; n = 200
    t = np.linspace(0,2*pi,n)
    x = np.array([]); y = np.array([])
    
    for i in range(0,n):
        x = np.append(x,sin(L*t[i])*cos(M*t[i]))
        y = np.append(y,sin(L*t[i])*sin(N*t[i]))
    
    yt = Graph2D(t,[x],"t","x")
    yx = Graph2D(x,[y],"x","y")
    tx = Graph2D(x,[t],"x","t")
    yt.show()
    yx.show()
    tx.show()
    
    
     
def exo4():
    min = -2*pi; max = 2*pi; n = 400
    t = np.linspace(min,max,n)
    x = np.array([])
    y = np.array([])
    
    for i in range(0,n):
        x = np.append(x,cos(t[i])*cos(t[i]/2.))
        y = np.append(y,sin(t[i])*cos(3.*t[i]))
        
    # period of x : 4*pi, period of y : pi     
    a = Graph2D(t,[x,y],"t","x","question a",["x","y"])
    a.show()
    
    # plot parametric curve
    b = Graph2D(x,[y],"x","y","question b")
    b.show()
    
    for i in range(0,n):
        # loop on the intervals satisfying 
        if (y[i] <= 1e-8 and abs(x[i]) <= 1 and abs(x[i]) >= 0.8):
            print("i :",i,"t :",t[i])
    
    
    
def exo5():
    valeur = np.array([0.5,1.,1.5])
    F = np.array([]); G = np.array([])
    n = 400
    t = np.linspace(-2*pi,2*pi,n)
    
    for a in valeur:
        f = np.array([]); g = np.array([])
        for i in range(0,n):
            f = np.append(f,t[i]-a*sin(t[i]))
            g = np.append(g,1-a*cos(t[i]))
        F = np.append(F,f)
        G = np.append(G,g)
        
    F = F.reshape((3,n))
    G = G.reshape((3,n))

    # Question a
    Graph2D(t,F,"t","f","f(t)",["0.5","1.","1.5"]).show()
    Graph2D(t,G,"t","g","g(t)",["0.5","1.","1.5"]).show()
    # Question b
    Graph2D(F,G,"f","g","question b",legend=["0.5","1.","1.5"]).show()
    # Question c
    for i in range(0,n):
        if(abs(G[2,i]) < 0.05): # intersection with the x-axis
            print("abscissa :",F[2,i],"i :",i,"t :",t[i])
        if(abs(F[2,i]) < 1e-3): # double point
            print("i :",i,"t :",t[i],"g :",G[2,i])
            
            
            
def exo6():
    min = -pi; max = 2*pi; n = 400
    t = np.linspace(min,max,n)
    
    # Question a
    terme0 = np.cos(t)         # 2*pi   periodic
    terme1 = -1/3.*np.cos(3*t) # 2*pi/3 periodic
    terme2 = 1/5.*np.cos(5*t)  # 2*pi/5 periodic
    Graph2D(t,[terme0,terme1,terme2],"t","f","question a").show()
    
    # Question b
    def Sn(n,t):
        terme = np.cos(t)
        somme = terme
        for i in range(1,n+1):
            terme = -1/(2*i+1)*np.cos((2*i+1)*t)
            somme += terme
        return somme
    
    y = [Sn(3,t),Sn(4,t),Sn(6,t),Sn(10,t)]
    legend = ["s3","s4","s6","s10"]
    Graph2D(t,y,"t","Sn","Partial sums",legend).show()
            
    

    

if __name__ == "__main__":
    #exo1()
    #exo2()
    #exo3()
    #exo4()
    #exo5()
    exo6()
    
        
    
    
    