# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 05:01:24 2020

@author: moroo
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import animation
import numpy as np
from time import time

def plotGraph(x,y,labelx,labely,titre):    
    #plot graph
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            }
    
    #fig = plt.figure(1)
    plt.suptitle(titre,fontdict=font,fontsize=16)
    plt.plot(x,y)
    plt.xlabel(labelx,fontdict=font)
    plt.ylabel(labely,fontdict=font)
    plt.grid(True)
    plt.show()
    
def plot3DGraph(x,y,z,labelx,labely,labelz,titre):    
    #plot graph
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            }
    
    #fig = plt.figure(1)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    ax.plot(x,y,z,lw=0.5)
    ax.set_xlabel(labelx,fontdict=font)
    ax.set_ylabel(labely,fontdict=font)
    ax.set_zlabel(labelz,fontdict=font)
    ax.set_title(titre,fontdict=font,fontsize=16)
    plt.grid(True)
    plt.show()
    
    
    
    
def plotSurf(x,y,z,labelx,labely,labelz,titre):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=cm.viridis)
    #ax.plot_wireframe(x,y,z,rstride=5,cstride=5)     
    ax.set_title(titre)
    ax.set_xlabel(labelx)
    ax.set_ylabel(labely)
    ax.set_zlabel(labelz)
    plt.show()
    

    
def plotContour(x,y,z,labelx,labely,titre):
    fig,ax = plt.subplots(1,1)
    cp = ax.contourf(x,y,z)
    fig.colorbar(cp) # Add a colorbar to a plot
    ax.set_title(titre)
    ax.set_xlabel(labelx)
    ax.set_ylabel(labely)
    plt.show()
    
    

