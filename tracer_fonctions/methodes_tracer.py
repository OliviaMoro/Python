# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 05:01:24 2020

@author: moroo
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, ticker, colors
import numpy as np

class Graph2D:

    def __init__(self,x,Y,x_label="x",y_label="y",title="",legend=[]):
        self.x = x
        self.Y = Y
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.legend = legend
        self.show_grid = True
        self.a = None
        self.b = None
        
    def ylimit(self,a,b):
        self.a = a
        self.b = b

    def show(self):
        fig, ax = plt.subplots()
        
        # Pour l'affichage de plusieurs courbes paramétrées sur un même
        # graphe
        if(len(self.x) > 1 and len(self.x) == len(self.Y)):
            for i in range(0,len(self.x)):
                if (len(self.legend) != 0):
                    ax.plot(self.x[i],self.Y[i],label=self.legend[i])
                    ax.legend(loc='upper right', shadow=True)
            else:
                ax.plot(self.x[i],self.Y[i])
        # Affichage de plusieurs courbes ou d'une seule pouvant être une
        # courbe d'équation paramétrique
        else:
            for i in range(0,len(self.Y)):
                if (len(self.legend) != 0):
                    ax.plot(self.x,self.Y[i],label=self.legend[i])
                    ax.legend(loc='upper right', shadow=True)
                else:
                    ax.plot(self.x,self.Y[i])
           
        if (self.a != None and self.b != None):
            plt.ylim(self.a,self.b)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()



def parametric(x,y,z,xlabel="x",ylabel="y",zlabel="z",titre="",label=[]):   
    plt.rcParams['legend.fontsize'] = 10
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            }
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    if (len(label) != 0):
        ax.plot(x,y,z,label)
        ax.legend()
    else:
        ax.plot(x,y,z)
        
    ax.set_xlabel(xlabel,fontdict=font)
    ax.set_ylabel(ylabel,fontdict=font)
    ax.set_zlabel(zlabel,fontdict=font)
    ax.set_title(titre,fontdict=font,fontsize=10)
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
    

    
def plotContour(x,y,z,labelx,labely,titre,niv=[]):
    fig,ax = plt.subplots(1,1)
    if (len(niv) != 0):
        cp = ax.contour(x,y,z,niv)      
    else :
        print("min : {}, max : {}".format(z.min(),z.max()))
        cp = ax.contour(x,y,z,locator=ticker.LogLocator())

    
    fig.colorbar(cp) # Add a colorbar to a plot
    ax.set_title(titre)
    ax.set_xlabel(labelx)
    ax.set_ylabel(labely)
    ax.clabel(cp, inline=1, fontsize=8)
    plt.show()
    

