class Table:
    def __init__(self, key, token):
        self.key = key
        self.token = token
    
    def getKey(self):
        return self.key
    
    def setKey(self, key):
        self.key = key
        
    def getToken(self):
        return self.token
    
    def setToken(self, token):
        self.token = token