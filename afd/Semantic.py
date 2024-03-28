from Scanner import Scanner
from Token import Token
from TokenType import TokenType
from Table import Table
from Parser import Parser
from Stack import Stack
from PcT import PcT

class Semantic:
    def __init__(self, parser):
        self.parser = parser
        self.stack = parser.stack
        self.pct = parser.pct
    
    def semantic(self):
        self.parser.syntax()
        #self.pct.allElements()
        #if self.parser.counter == 1: print('aaaaaaaaaa')
        #self.teste()
        #self.pct.allElements()
        #self.parser.stack.allElements()

        #self.check_types()
    def teste(self):
        while(self.stack.top() != '$'):
            print(self.pct.searchToken(self.stack.top()))
            self.stack.pop()
    
    def check_types(self):
        # Percorremos a pilha de símbolos do parser
        for table_entry in self.parser.stack.allElements():
            # Verificamos se a entrada na tabela é uma variável
            if table_entry.getFlag() == 'var':
                # Obtemos o tipo da variável do PcT
                var_type = self.pct.searchToken(table_entry.getToken().getContent())
                if var_type is None:
                    # Se o tipo da variável não estiver na tabela de tipos, levantamos um erro
                    raise Exception(f"Erro semântico: Tipo da variável '{table_entry.getToken().getContent()}' não foi definido.")
                # Verificamos se o tipo da variável na tabela de símbolos corresponde ao tipo no PcT
                if table_entry.getFlag() != var_type:
                    raise Exception(f"Erro semântico: Tipo da variável '{table_entry.getToken().getContent()}' incompatível. Esperado '{var_type}', encontrado '{table_entry.getFlag()}'.")