from utilities import * # Includes ClosestInSet

class LearningModel:
    def __init__(self,LA={},d=np.linalg.norm,a=.12):
        self.LA = LA    # finite set of labels
        self.d = d      # setting distance metric - default is euclidean
        self.a = a      # learning rate#

class PrototypeLearningModel(LearningModel):
    "Simply moves prototypes around, nearest prototype is the category"
    def __init__(self,*args,**kw):
       super(PrototypeLearningModel,self).__init__(*args,**kw) # Funky stuff to keep the same init as the 'super' "LearningModel"
       self.coordsLA = {}

    def FindLabel(self,a):
        return ClosestInDict(a,self.LA)

    def AddLabel(self,name,a):
        self.LA[name]=a

    def GuessFrom(self,l,O):
        return ClosestInSet(self.LA[l],O)

    def Learn(self,f,o):
        # prototype += learningRate * difference ~~ do we want to play around with this learning rate?
        self.LA[f] += self.a*(o-self.LA[f]) # will need to gurantee these are np arrays
