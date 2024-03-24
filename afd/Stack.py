from Table import Table
class Stack:
    def __init__(self):
        self.table = []  # Inicializa como uma lista vazia

    def push(self, key, token):
        inputTable = Table(key, token)
        self.table.append(inputTable)  # Adiciona uma instância de Table à lista

    def pop(self):
        if self.table:  # Verifica se a lista não está vazia
            return self.table.pop()  # Remove e retorna a última instância de Table da lista

    def top(self):
        if self.table:  # Verifica se a lista não está vazia
            key = self.table[-1].getKey()
            token = self.table[-1].getToken()
            return key, token # Retorna a última instância de Table da lista

    def isEmpty(self):
        return not bool(self.table)  # Retorna True se a lista estiver vazia, False caso contrário

    def allElements(self):
        for i in self.table: 
            print(i.getKey(), ',', i.getToken())
        return self.table  # Retorna a lista de todas as instâncias de Table


# p = Stack()
# p.push('hola', 'mi chica')
# p.push('katara', 'jaeger')
# p.allElements()