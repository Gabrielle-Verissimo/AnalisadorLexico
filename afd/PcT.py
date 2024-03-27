from Table import Table
from TokenType import TokenType
class PcT:
    def __init__(self):
        self.pct = []
        
    def push(self, type, token):
        if type == TokenType.INTEGER: type = 'integer'
        elif type == TokenType.REAL: type = 'real'
        elif type == TokenType.BOOLEAN: type = 'boolean'
        inputTable = Table(type, token)
        self.pct.append(inputTable)
        
    def searchToken(self, token):
        for x in self.pct:  # Começa do topo da pilha
            if x.getToken() == token:
                return x.getFlag()
        return None
        
    def allElements(self):
        for i in self.pct: 
            print(i.getFlag(), ',', i.getToken())
        return self.pct
        