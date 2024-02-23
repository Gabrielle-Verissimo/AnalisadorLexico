from Scanner import Scanner
from Token import Token
from TokenType import TokenType

class Parser:
    scanner = Scanner
    def __init__(self, scanner):
        self.scanner = scanner
        self.token = Token
        
    def syntax(self):
        self.token = self.scanner.nextToken()
        if(self.token == None): return
        if self.token.getContent() == 'program':
            self.token = self.scanner.nextToken()
            if(self.token.getType() == TokenType.IDENTIFIER):
                self.token = self.scanner.nextToken()
                if(self.token.getContent() == ';'):
                    self.dcl_var()
                    self.dcl_sub()
                    self.command_com()
                    
    def dcl_var(self):
        self.token = self.scanner.nextToken()
        if(self.token.getContent() == 'var'):
            self.list_dcl_var()
        else:
            return
    def dcl_sub(self):
    def command_com(self):
    def list_dcl_var(self):
#1. LISTA_DECLARACOES_VARIAVEIS -> LISTA_DE_IDENTIFICADORES : TIPO ; LISTA_DECLARACOES_VARIAVEIS_RESTO
#2. LISTA_DECLARACOES_VARIAVEIS_RESTO -> LISTA_DE_IDENTIFICADORES : TIPO ; LISTA_DECLARACOES_VARIAVEIS_RESTO | ε

    #     if self.token.getType() == TokenType.IDENTIFIER or self.token.getType() == TokenType.NUMBER:
    #         self.token = self.scanner.nextToken()
    #         #if(self.token != None):
    #         self.op_add()
    #     return self.token
    
    # def op_add(self):
    #     if self.token.getType() == TokenType.ADD_OP: 
    #         self.token = self.scanner.nextToken()
    #         #if(self.token != None):
    #         self.fator()
    #     else:
    #         raise Exception("Erro sintatico: Expressão errada. Espera-se um operador. Recebeu-se: " + str(self.token.getType()) + " na linha: " + str(self.scanner.line) + " e coluna: " + str(self.scanner.column))
                    
    # def fator(self):
    #     if self.token.getType() != TokenType.IDENTIFIER and self.token.getType() != TokenType.NUMBER:
    #         raise Exception("Erro sintatico: Expressão errada. Espera-se um inteiro ou float. Recebeu-se: " + str(self.token.getType()) + " na linha: " + str(self.scanner.line) + " e coluna: " + str(self.scanner.column))
    #     else:
    #         return
