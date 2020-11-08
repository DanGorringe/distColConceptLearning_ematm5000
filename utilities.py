import numpy as np

def ClosestInSet(a,B,d=np.linalg.norm):
    dL = {b.tostring():d(a-b) for b in B} # List of distances
    return np.fromstring(min(dL,key=dL.get,default=None))

def ClosestInDict(a,B,d=np.linalg.norm): # Convinced there's a nicer way tow rite this but I can't figure it out atm
    dL = {b:d(a-B[b]) for b in B} # List of distances
    return min(dL,key=dL.get,default=None)
