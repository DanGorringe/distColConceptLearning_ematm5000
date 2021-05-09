import numpy as np
import colorsys
import qutip as q

def MinArgDict(D):
    return min(D,key=D.get,default=None)

def MaxArgDict(D):
    return max(D,key=D.get,default=None)

def ClosestInSet(a,B,d=np.linalg.norm):
    dL = {b.tostring():d(a-b) for b in B} # List of distances
    return np.fromstring(min(dL,key=dL.get,default=None))

def FurthestInSet(a,B,d=np.linalg.norm):
    dL = {b.tostring():d(a-b) for b in B} # List of distances
    return np.fromstring(max(dL,key=dL.get,default=None))

def ClosestInDict(a,B,d=np.linalg.norm): # Convinced there's a nicer way tow rite this but I can't figure it out atm
    dL = {b:d(a-B[b]) for b in B} # List of distances
    return min(dL,key=dL.get,default=None)

def FurthestVector(agent,xAvg,d):
    pf = agent.pf
    # of length
    p = [np.array([pf[0][i]+int(str(bin(j))[2:].zfill(len(pf[0]))[i])*pf[1][i] for i in range(len(pf[0]))])for j in range(2**len(pf[0]))]
    return FurthestInSet(xAvg,p,d)

def rgb2hsv(c):
    return colorsys.rgb_to_hsv(c[0],c[1],c[2])

def hsv2rgb(c):
    return colorsys.hsv_to_rgb(c[0],c[1],c[2])

def hsv2q(c):
    [h,s,v,] = c
    h = 2*np.pi*h
    theta_k = np.arcsin(s)
    #theta_k = s*np.pi # This is different to the representation suggested
    #theta_k = s*np.pi/2 # This is different to the representation suggested
    #theta_k = np.arcsin(s)
    #theta_k = np.arccos(1-s)
    return q.Qobj(np.array([np.cos(theta_k/2),np.exp(1j*h)*np.sin(theta_k/2)]))

def hsv2qq(c):
    [h,s,v,] = c
    q1 = hsv2q(c)
    q2 = q.Qobj(np.array([np.sqrt(v),np.sqrt(1-v)]))
    return q.tensor([q1,q2])
