class Table:
    def __init__(self, type, token):
        self.type = type
        self.token = token
    
    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type
        
    def getToken(self):
        return self.token
    
    def setToken(self, token):
        self.token = token