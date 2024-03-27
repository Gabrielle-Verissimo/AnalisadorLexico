from Table import Table
from Token import Token
class Stack:
    def __init__(self):
        self.table = []  # Inicializa como uma lista vazia

    def push(self, flag, token):
        inputTable = Table(flag, token)
        self.table.append(inputTable)  # Adiciona uma instância de Table à lista

    def pop(self):
        if self.table:  # Verifica se a lista não está vazia
            return self.table.pop()  # Remove e retorna a última instância de Table da lista

    def top(self):
        if self.table:  # Verifica se a lista não está vazia
            flag = self.table[-1].getflag()
            token = self.table[-1].getToken()
            return flag, token # Retorna a última instância de Table da lista

    def isEmpty(self):
        return not bool(self.table)  # Retorna True se a lista estiver vazia, False caso contrário
    
    def searchToken(self, token):
        for table in reversed(self.table):  # Começa do topo da pilha
            if isinstance(table.getToken(), Token) and table.getToken().getContent() == token:
                return table
        return None
    
    def existId(self, id):
        for table in reversed(self.table):  # Começa do topo da pilha
            #print(table.getToken())
            if table.getToken() == '$': break
            if table.getToken() == id:
                return True
        return False
    
    def allElements(self):
        #for i in self.table: 
            #print(i.getFlag(), ',', i.getToken())
        return self.table  # Retorna a lista de todas as instâncias de Table


# p = Stack()
# p.push('hola', 'mi chica')
# p.push('katara', 'jaeger')
# p.push('nada', '$')
# p.push('katara', 'jaeger')
# print(p.searchToken('jaeger'))

# if(p.existId('jaeger')):
#     print("Deu ruim")
# else:
#     print("deu bom")
#p.allElements()