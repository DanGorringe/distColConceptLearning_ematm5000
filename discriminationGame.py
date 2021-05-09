from agentClass import *
from learningModels import *

def DiscriminationGame(A,B,O,o):
    # Agent A speaks
    # Agent B listens
    # Context O = {o_1,...o_n}
    # Topic o \in O

    # 1) Speaker tries to discriminate topic from context
    try:
        f = A.FindLabel(o) # Not sure about the context here - has to change for advanced games
        #print("A thinks "+str(o)+" is of label "+str(f))
    except: # If fail a new label is needed - is it? where would label come from?
        #print('Adding new label')
        #A.AddLabel('newName',o) # Need to rewrite this - how to develop new names?
        #print('A cant find label' +str(o))
        return 0

    # 2) Listener looks up f. Identifies topic in context from label
    if f in B.GetLabels():
        g = B.GuessFrom(f,O)
        #print("B thinks "+str(g)+" is most label "+str(f))
    elif f != None: # If don't know label then listener adds
        B.AddLabel(f,o)
        return 0
    else:
        return 0

    # 3) Listener 'learns' if g != o
    if not np.array_equal(g,o): # might need some less strict vesion of this for other models
        B.Learn(f,o)
    else:
        B.NotLearn(f,o)
