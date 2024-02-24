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
                    self.token = self.scanner.nextToken()
                    if(self.token.getContent() == '.'):
                        return
                    else:
                        raise Exception(f"Erro sintatico: Espera-se o delimitador '.' e foi recebido '{self.token.getContent()}' na linha {self.line} e coluna {self.column}")
                else:
                    raise Exception(f"Erro sintatico: Espera-se o delimitador ';' e foi recebido '{self.token.getContent()}' na linha {self.line} e coluna {self.column}")
            else:
                raise Exception(f"Erro sintatico: Espera-se um identificador e foi recebido '{self.token.getType()}' na linha {self.line} e coluna {self.column}")
        else:
            raise Exception(f"Erro sintatico: Espera-se 'program' e foi recebido '{self.token.getContent()}' na linha {self.line} e coluna {self.column}")
                    
    def dcl_var(self):
        self.token = self.scanner.nextToken()
        if(self.token.getContent() == 'var'):
            self.list_dcl_var()
        else:
            return
        
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
                
# lista_de_identificadores → id lista_de_identificadores_resto
# lista_de_identificadores_resto → , id lista_de_identificadores_resto | ε


    def list_id(self):
        self.token = self.scanner.nextToken()
        if(self.token.getType() == TokenType.IDENTIFIER):
            self.list_id_l()
            self.type()
    
    def list_id_l(self):
            
    def type(self):
        self.token = self.scanner.nextToken()
        if(self.token.getType() == TokenType.INTEGER or self.token.getType() == TokenType.REAL or self.token.getType() == TokenType.BOOLEAN):
            self.token = self.scanner.nextToken()
            if(self.token.getType() == ';'):
                return
# declarações_de_subprogramas → declaração_de_subprograma; declarações_de_subprogramas | ε
# lista_de_comandos → comando lista_de_comandos; | comando
# lista_de_expressões → expressão, lista_de_expressões | expressão
# expressão_simples → termo op_aditivo expressão_simples | sinal termo | termo
# termo → fator op_multiplicativo termo | fator  
    def dcls_sub(self):
        self.dcl_subprogram()
        self.token = self.scanner.nextToken()
        if self.token.getContent() == ';':
            self.dcls_sub()
        else:
            return
        
    def dcl_subprogram(self):
        self.token = self.scanner.nextToken()
        if(self.token.getContent() == 'procedure'):
            self.token = self.scanner.nextToken()
            if(self.token.getType() == TokenType.IDENTIFIER):
                self.arguments()
                self.token = self.scanner.nextToken()
                if(self.token.getContent() == ';'):
                    self.dcl_var()
                    self.dcls_sub()
                    self.command_com()
        else:
            return
                    
    def arguments(self):
        self.token = self.scanner.nextToken()
        if self.token.getContent() == '(':
            self.list_param()
            self.token = self.scanner.nextToken()
            if self.token.getContent() == ')':
                return
            else:
                raise Exception(f"Unexpected token: {self.token.getContent()}")
        else:
            return
    def list_param(self):
        self.list_id()
        
    def command_com(self):
    

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


