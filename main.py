from agentClass import *
from discriminationGame import *
from learningModels import *
import numpy as np

# Setting up agent A
labelsA = {'Left':np.array([1.0,1.0]),'Right':np.array([3.0,1.0])}
agentA = Agent(PrototypeLearningModel(LA=labelsA))

print(agentA.GetLabels())

# Testing prototypes work
print(agentA.FindLabel(np.array([0,1])))
print(agentA.FindLabel(np.array([4,1])))
print(agentA.FindLabel(np.array([2,1])))

# Setting up agent B
labelsB = {'Left':np.array([1.0,0.0]),'Right':np.array([3.0,2.0])}
agentB = Agent(PrototypeLearningModel(LA=labelsB))

# O = {L,L,R,L,L}
o = np.array([2.1,.1])
O = [np.array([1.0,1.0]),np.array([.1,1.0]),o,np.array([1,1.5]),np.array([1.6,1.2])]
print('finding labels for all values in O...')
for i in O:
    print(agentA.FindLabel(i))

print(np.isin(O,o))

# Check Where B starts
print('Labels for B:')
print(agentB.GetLabels())

# Do some learning
print('One round of discrimination game...')
discriminationGame(agentA,agentB,O,o)

print('Labels for B:')
print(agentB.GetLabels())
