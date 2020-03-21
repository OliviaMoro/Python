# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:23:16 2019

@author: moroo
"""
import math
import matplotlib.pyplot as plt


def euler_explicite(pas,ti,*coord,**pente):
    """ Calcul une itération de la méthode d'intégration d'euler explicite
    Paramètres nommés :
    pas -- pas de l'itération (réel)
    ti -- temps initial (réel)
    *coord -- jeu de conditions initiales (réels)
    **pente -- jeu de fonction (différentielle)
    
    """
    #Mise sous forme de liste *(t,coord)
    tupleArgs = (ti,)+coord
    
    #Calcul des pentes
    pentes = []
    for value in pente.values():
        pentes.append(value(*tupleArgs))  
    
    #Calcul des nouvelles positions
    uf = []
    i = 0
    for pos in coord:
        uf.append(pos+pas*pentes[i])
        i += 1
    
    #Mise à jour du temps
    tf = ti + pas
    
    return tf,uf         


def euler_retrograde(pas,tf,*coord,**pente):
    """ Calcul une itération de la méthode d'intégration d'euler rétrograde
    Paramètres nommés :
    pas -- pas de l'itération (réel)
    tf -- temps final (réel)
    *coord -- jeu de conditions initiales (réels)
    **pente -- jeu de fonction (différentielle)
    
    """
    #Mise sous forme de liste *(t,coord)
    tupleArgs = (tf,)+coord
    
    #Calcul des pentes
    pentes = []
    for value in pente.values():
        pentes.append(value(*tupleArgs))  
    
    #Calcul des nouvelles positions
    ui = []
    i = 0
    for pos in coord:
        ui.append(pos-pas*pentes[i])
        i += 1
    
    #Mise à jour du temps
    ti = tf - pas
    
    return ti, ui 


if __name__ == "__main__":
    #Exemple du pendule:
    def smy(t,y,z):
        return z
    
    def smz(t,y,z):
        return -math.sin(y)
    
    n = 600
    t = []
    u = []
    
    t.append(0)
    u.append([0,0.2]) 
    
    
    for i in range(1,n+1):
        (tf,uf)=euler_explicite(0.05,t[i-1],u[i-1][0],u[i-1][1],key1=smy,key2=smz)
        t.append(tf)
        u.append(uf)
        
    y = [i for i,j in u]
    z = [j for i,j in u]
        
    #plot graph
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            }
    
    fig = plt.figure(1)
    plt.suptitle(r'Test pendule simple',fontdict=font,fontsize=16)
    plt.plot(t,y)
    plt.xlabel(r'temps',fontdict=font)
    plt.ylabel(r'position',fontdict=font)
    plt.grid(True)
    plt.show()
    