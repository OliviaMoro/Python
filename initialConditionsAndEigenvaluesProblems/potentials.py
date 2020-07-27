# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:18:09 2020

@author: moroo
"""


a0 = 1    #0.529e-10 # Borh radius
Eh = 27.2 #to convert eV to hartree

def getLists(nw):
    iList = [] # intervall list where V = -300eV
    pList = [] # discontinuities list where V = -150eV
    pList.append(2*a0)
    iList.append([2*a0,3.5*a0])
    if (nw != 1):
        for i in range(1,nw):
            inf = pList[-1]+1.5*a0
            pList.append(inf)
            sup = pList[-1]+0.5*a0
            pList.append(sup)
            iList.append([sup,sup+1.5*a0])
    return pList, iList
    

      
def checkValue(x,iList):
    ans = False
    for interval in iList:
        if (x > interval[0] and x < interval[1]):
            ans = True
            return ans
    return ans
    


def V(x,nw):
    """
        Kronig Penney potential defined from a given number of well nw at a 
        given x 
    """
    V = 0
    pList, iList = getLists(nw)
    #print("pList : {}".format(pList))
    #print("iList : {}".format(iList))
        
    if (checkValue(x,iList)):
        V = -300/Eh
    elif (x in pList):
        V = -150/Eh
    return V



def impurity(x,iw):
    """
        Impurity simulation to add to the Kronig Penney potential at the 
        iw'th well given x.
    """
    Vi = 0
    ai = 2*a0+iw*1.5*a0+0.5*(iw-1)*a0
    
    #Impurity size
    size = 0.25*1.5*a0
    if (x > ai-size and x < ai):
        Vi = 300/Eh
    elif(x == ai or x == ai-size):
        Vi = 150/Eh
        
    return Vi



def impurityBis(x,iw,size):
    """
        Impurity simulation to add to the Kronig Penney potential at the 
        iw'th well given x. The size of the impurity can be specified.
    """
    Vi = 0
    ai =2*a0+iw*1.5*a0+0.5*(iw-1)*a0
    
    if (x > ai-size and x < ai):
        Vi = 300/Eh
    elif(x == ai or x == ai-size):
        Vi = 150/Eh
        
    return Vi



def V1(x,a):
    """
        Simulation of an electric field through a potential which varies
        linearly from x = 0 to x = a.
    """
    v = -10/Eh + (20/(a*Eh))*x
    return v
    

    
def amorphous(x,nw,sizes):
    """
        Simulation of an amorphous solid defined from the Kronig Penney 
        potential by adding an impurity nw times to the wells. The sizes 
        of the impurities are randomly determined beforehand in the array
        'sizes'. 
    """
    v = 0
    
    for i in range(1,nw+1):
        v = impurityBis(x,i,sizes[i-1])
        
    return v