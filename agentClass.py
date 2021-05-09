import numpy as np

class Agent:
    # Simple agent (with one learningModel)
    def __init__(self,learningModel,pf=None):
        self.learningModel = learningModel # Agent given the learningModel
        self.pf = pf

    def GetLabels(self):
        return self.learningModel.LA

    def FindLabel(self,a):
        return self.learningModel.FindLabel(a)

    def FindLabelExemplar(self,l):
        return self.learningModel.FindLabelExemplar(l)

    def AddLabel(self,name,a):
        self.learningModel.AddLabel(name,a)

    def GuessFrom(self,l,O):
        return self.learningModel.GuessFrom(l,O)

    def Learn(self,f,o):
    # Update learning model based of the label of a topic o
        self.learningModel.Learn(f,o)

    def NotLearn(self,f,o):
        return None

class AgentMisraGries(Agent):

    def __init__(self,*args,**kw):
        self.k = kw.pop('k')
        super(AgentMisraGries,self).__init__(*args,**kw) # Funky stuff to keep the same init as the 'super' "Agent"
        self.LAK = {}
        for x in self.GetLabels():
            self.LAK[x] = 2

    def FindLabel(self,a):
        x = self.learningModel.FindLabel(a)
        #self.LAK[x] += 1 # Can't do this! use FindLabel outside of agent
        return x

    def AddLabel(self,name,a):
        # Misra Gries
        l = self.GetLabels()
        if len(l) < self.k:
            self.learningModel.AddLabel(name,a)
            self.LAK[name] = 1
        else:
            for x in self.GetLabels():
                if self.LAK[x] == 0:
                    print(self.LAK)
                    print(self.GetLabels().keys())
                #if np.random.random() < 1/self.LAK[x]:
                self.LAK[x] -= 1
            self.UpdateLabels()

    def UpdateLabels(self):
        deleteList = []
        for x in self.GetLabels():
            if self.LAK[x] <= 0:
                deleteList.append(x)
        for x in deleteList:
            self.learningModel.RemoveLabel(x)
            del self.LAK[x]

    def Learn(self,f,o):
    # Update learning model based of the label of a topic o
        #self.LAK[self.FindLabel(o)] -= 1 # funky add one in find label
        #self.LAK[f] += 1
        #self.UpdateLabels()
        self.learningModel.Learn(f,o)

    def NotLearn(self,f,o):
        self.LAK[f] += 1

class AgentTruther(Agent):

    def __init__(self, *args, **kwargs):
        self.l = kwargs.pop('l')
        self.RLA = kwargs.pop('RLA')
        self.Y = kwargs.pop('Y')
        super(AgentTruther, self).__init__(*args, **kwargs)

    def FindLabel(self,a):
        self.learningModel.LA = self.RLA(self.l,self.pf,r=1,Y=self.Y)
        return self.learningModel.FindLabel(a)

    def Learn(self,f,o):
        return None
