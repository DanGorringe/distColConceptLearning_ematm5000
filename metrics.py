import numpy as np
from utilities import *
from collections import Counter

def CompareAgentsExemplars(agents,d=np.linalg.norm,X=None):
    '''
    Find sum of variances between all unique labels used across agents
    '''
    s = 0
    labels = list(set([l for a in agents for l in a.GetLabels()])) # Unique labels used
    for l in labels:
        x = [a.FindLabelExemplar(l) for a in agents if l in a.GetLabels()] # list of co-ords of exemplars for l
        xAvg = np.mean(x,axis=0) # Calculate average, as this is probably more computationally efficient
        # Compensate for labels not in agents vocab, add extra points at maximal distance from xAvg
        x.extend([FurthestVector(a,xAvg,d) for a in agents if l not in a.GetLabels()])
        s += np.var([d(y-xAvg) for y in x]) # Increment by variance of distance from centroid
    return(s)

def RandomAccuracyMetric(agents,n=100,X=None):
    # Return average agreement percetnage
    p = 0
    labels = list(set([l for a in agents for l in a.GetLabels()])) # Unique labels used
    pf = agents[-1].pf
    for i in range(n): # n random elements
        x = np.random.uniform(pf[0],pf[1]) # Uniform random vector in field
        m = len(agents) - 1
        l = [a.FindLabel(x) for a in agents]
        l = l.count(max(set(l), key=l.count,default=1)) - 1 # number of most frequent element
        p += (1/n)*(l/m)
    return p

def TestingAccuracy(agents,X):
    # Reqiores a training set
    n = X.shape[0]
    m = len(agents)
    p = 0
    for x in X:
        trueLabel = x[-1]
        l = np.array([a.FindLabel(x[3:6]/255) for a in agents])
        #print([trueLabel,l])
        #print(trueLabel)
        #print(l)
        #print(np.where(l==trueLabel)[0])
        #print(len(np.where(l==trueLabel)[0]))
        p += len(np.where(l==trueLabel)[0])/m
    #print(p)
    return p/n

def MajorityTestingAccuracy(agents,X):
    # Reqiores a training set
    n = X.shape[0]
    p = 0
    for x in X:
        trueLabel = x[-1]
        l = np.array([a.FindLabel(x[3:6]/255) for a in agents])
        majorityLabel = Counter(l).most_common(1)
        majorityLabel = majorityLabel[0][0]
        print([trueLabel,majorityLabel])
        if trueLabel == majorityLabel:
            p += 1
    #print(p)
    return p/n
