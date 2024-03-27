from Token import Token

class Table:
    def __init__(self, flag, token):
        self.flag = flag
        self.token = token
    
    def getFlag(self):
        return self.flag
    
    def setFlag(self, flag):
        self.flag = flag
        
    def getToken(self):
        return self.token
    
    def setToken(self, token):
        self.token = token