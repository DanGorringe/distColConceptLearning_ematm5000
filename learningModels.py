from utilities import * # Includes ClosestInSet
import numpy as np
import qutip as q

class LearningModel:
    def __init__(self,LA={},a=.12,d=np.linalg.norm):
        self.LA = LA    # finite set of labels
        self.d = d      # setting distance metric - default is euclidean
        self.a = a      # learning rate

    def RemoveLabel(self,name):
        del self.LA[name]

class ExemplarLearningModel(LearningModel):
    "Simply moves Exemplars around, nearest Exemplar is the category"

    def __init__(self,*args,**kw):
       super(ExemplarLearningModel,self).__init__(*args,**kw) # Funky stuff to keep the same init as the 'super' "LearningModel"
       self.coordsLA = {} # this isn't used?

    def FindLabel(self,a):
        return ClosestInDict(a,self.LA)

    def FindLabelExemplar(self,l):
        return self.LA[l]

    def AddLabel(self,name,a):
        self.LA[name]=a

    def RemoveLabel(self,name):
        del self.LA[name]

    def GuessFrom(self,l,O):
        return ClosestInSet(self.LA[l],O)

    def Learn(self,f,o):
        # Exemplar += learningRate * difference ~~ do we want to play around with this learning rate?
        self.LA[f] += self.a*(o-self.LA[f]) # will need to gurantee these are np arrays

class BayesianPrototypeLearningModel(LearningModel):
    """Bayesiuan Prottpyes, centroids with varaince around"""

    def __init__(self, *args, **kwargs):
        self.a_sd = kwargs.pop('a_sd')
        super(BayesianPrototypeLearningModel, self).__init__(*args, **kwargs)

    def WeightedDistance(self,a,l):
        # return the weighted distance between a point o and label l:
        c = self.LA[l]['c']
        sd = self.LA[l]['sd']
        return np.exp(-np.square((self.d(a-c))/sd))

    def FindLabel(self,a):
        return MaxArgDict({l:self.WeightedDistance(a,l) for l in self.LA})

    def AddLabel(self,name,a,sd=0.1):
        self.LA[name] = {'c':a,'sd':sd}

    def GuessFrom(self,l,O):
        return np.fromstring(MaxArgDict({o.tostring():self.WeightedDistance(o,l) for o in O}))

    def Learn(self,f,o):
        cc = np.linalg.norm(o-self.LA[f]['c'])
        sdc = abs(self.LA[f]['sd']-self.LA[self.FindLabel(o)]['sd'])
        self.LA[f]['c'] += self.a*(o-self.LA[f]['c'])
        self.LA[f]['sd'] += self.a_sd * cc * sdc
        self.LA[self.FindLabel(o)]['sd'] -= self.a_sd * cc * sdc # hmm

class QuantumAgent(LearningModel):
    # Save iffy Density Matrix M = \sum{|sample><sample|}

    def __init__(self, *args, **kwargs):
        super(QuantumAgent, self).__init__(*args, **kwargs)
        # ReForm LA into density matrices
        for l in self.LA:
            x = self.f(self.LA[l])
            self.LA[l] = x*x.dag()
            self.NormRep(l)
            #self.LA[l] /= self.LA[l].tr() # New update rule
            #self.LA[l] /= self.LA[l].eigenenergies(sort='high')[0]

    def NormRep(self,l):
        #self.LA[l] /= self.LA[l].tr()
        self.LA[l] /= self.LA[l].eigenenergies(sort='high')[0]

    def f(self,x):
        # Convert rgb in to quantum rep
        x = rgb2hsv(x)
        x = hsv2q(x)
        return x

    def Measure(self,l,a):
        # This or stochastically return an eigenvector?
        a = self.f(a)
        M = self.LA[l]
        return (a.dag()*M*a).norm()

    def FindLabel(self,a):
        X = {l:self.Measure(l,a) for l in self.LA}
        return MaxArgDict(X)

    def AddLabel(self,name,a):
        x = self.f(a)
        self.LA[name] = x*x.dag()
        #self.LA[name] /= self.LA[name].eigenenergies(sort='high')[0]
        #self.LA[name] /= self.LA[name].tr() # New update rule
        self.NormRep(name)

    def GuessFrom(self,l,O):
        X = {a.tostring():self.Measure(l,a) for a in O}
        return np.fromstring(MaxArgDict(X))

    def Learn(self,f,o):
        o = self.f(o)
        self.LA[f] += self.a*(o*o.dag())
        #self.LA[f] /= self.LA[f].eigenenergies(sort='high')[0]
        #self.LA[f] /= self.LA[f].tr() # New update rule
        self.NormRep(f)

class QuantumAgent_dm(QuantumAgent):

    def NormRep(self,l):
        self.LA[l] /= self.LA[l].tr()


class QuantumAgent_2qbit(QuantumAgent):

    def f(self,x):
        # Convert rgb in to quantum rep
        x = rgb2hsv(x)
        x = hsv2qq(x)
        return x

class QuantumVectorAgent(LearningModel):
    # Save iffy Density Matrix M = \sum{|sample><sample|}

    def __init__(self, *args, **kwargs):
        super(QuantumVectorAgent, self).__init__(*args, **kwargs)
        # ReForm LA into density matrices
        for l in self.LA:
            x = self.f(self.LA[l])
            self.LA[l] = x

    def f(self,x):
        # Convert rgb in to quantum rep
        x = rgb2hsv(x)
        x = hsv2q(x)
        return x

    def Measure(self,l,a):
        a = self.f(a)
        x = self.LA[l]
        return (a.dag()*x).norm()

    def FindLabel(self,a):
        X = {l:self.Measure(l,a) for l in self.LA}
        return MaxArgDict(X)

    def AddLabel(self,name,a):
        self.LA[name] = self.f(a)

    def GuessFrom(self,l,O):
        X = {a.tostring():self.Measure(l,a) for a in O}
        return np.fromstring(MaxArgDict(X))

    def Learn(self,f,o):
        o = self.f(o)
        self.LA[f] = (1-self.a)*self.LA[f] + self.a*o
