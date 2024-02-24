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
        #return self.token
        if self.token.getContent() == 'program':
            self.token = self.scanner.nextToken()
            if(self.token.getType() == TokenType.IDENTIFIER):
                self.token = self.scanner.nextToken()
                if(self.token.getContent() == ';'):
                    self.dcl_var()
                    self.dcls_sub()
                    self.command_com()
                    
    def dcl_var(self):
        self.token = self.scanner.nextToken()
        if(self.token.getContent() == 'var'):
            self.list_dcl_var()
        else:
            return
    
    def dcls_sub(self):
        
    def command_com(self):
    
    def list_dcl_var(self):
        self.list_id()
        self.token = self.scanner.nextToken()
        if self.token.getContent() == ':':
            self.type()
            self.token = self.scanner.nextToken()
            if self.token.getContent() == ';':
                self.list_dcl_var_l()

    def list_dcl_var_l(self):
        self.token = self.scanner.nextToken()
        # Se o próximo token não for um identificador, assumimos que chegamos ao fim da lista de declarações
        if self.token.getType() != TokenType.IDENTIFIER:
            return
        self.list_id()
        self.token = self.scanner.nextToken()
        if self.token.getContent() == ':':
            self.type()
            self.token = self.scanner.nextToken()
            if self.token.getContent() == ';':
                self.list_dcl_var_l()

    def list_id(self):
        self.token = self.scanner.nextToken()
        if(self.token == ':'):
            self.type()
            
    def type(self):
        self.token = self.scanner.nextToken()
        if(self.token.getType() == TokenType.INTEGER or self.token.getType() == TokenType.REAL):
            self.token = self.scanner.nextToken()
            if(self.token.getType() == ';'):
                return

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


#1. LISTA_DECLARACOES_VARIAVEIS -> LISTA_DE_IDENTIFICADORES : TIPO ; LISTA_DECLARACOES_VARIAVEIS_RESTO
#2. LISTA_DECLARACOES_VARIAVEIS_RESTO -> LISTA_DE_IDENTIFICADORES : TIPO ; LISTA_DECLARACOES_VARIAVEIS_RESTO | ε