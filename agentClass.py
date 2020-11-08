class Agent:
    # Simple agent (with one learningModel)
    def __init__(self,learningModel):
        self.learningModel = learningModel # Agent given the learningModel

    def GetLabels(self):
        return self.learningModel.LA

    def FindLabel(self,a):
        return self.learningModel.FindLabel(a)

    def AddLabel(self,name,a):
        self.learningModel.AddLabel(name,a)

    def GuessFrom(self,l,O):
        return self.learningModel.GuessFrom(l,O)

    def Learn(self,f,o):
    # Update learning model based of the label of a topic o
        self.learningModel.Learn(f,o)
