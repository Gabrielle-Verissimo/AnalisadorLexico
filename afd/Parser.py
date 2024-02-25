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
                    self.dcls_sub()
                    self.command_com()
                    self.token = self.scanner.nextToken()
                    if(self.token.getContent() == '.'):
                        return
                    else:
                        raise Exception(f"Erro sintatico: Espera-se o delimitador '.' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
                else:
                    raise Exception(f"Erro sintatico: Espera-se o delimitador ';' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
            else:
                raise Exception(f"Erro sintatico: Espera-se um identificador e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        else:
            raise Exception(f"Erro sintatico: Espera-se 'program' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
                    
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
                
    def list_id(self):
        self.token = self.scanner.nextToken()
        if(self.token.getType() == TokenType.IDENTIFIER):
            self.list_id_l()
    
    def list_id_l(self):
        self.token = self.scanner.nextToken()
        if(self.token.getContent() == ','):
            self.token = self.scanner.nextToken()
            if(self.token.getType() == TokenType.IDENTIFIER):
                self.list_id_l()
            else:
                raise Exception(f"Erro sintatico: e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        else:
            return
            
    def type(self):
        self.token = self.scanner.nextToken()
        if(self.token.getType() == TokenType.INTEGER or self.token.getType() == TokenType.REAL or self.token.getType() == TokenType.BOOLEAN):
            self.token = self.scanner.nextToken()
            if(self.token.getType() == ';'):
                return
 
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
                raise Exception(f"Erro sintatico: e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        else:
            return
        
    def list_param(self):
        self.list_id()
        self.token = self.scanner.nextToken()
        if self.token.getContent() == ':':
            self.type()
            self.list_param_l()
        else:
            raise Exception(f"Erro sintatico: e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
     
    def list_param_l(self):
        self.token = self.scanner.nextToken()
        if self.token.getContent == ';':
            self.list_id()
            self.token = self.scanner.nextToken()
            if self.token.getContent == ':':
                self.list_param_l()
        else:
            return
        
    def command_com(self):
        self.token = self.scanner.nextToken()
        if self.token.getContent == 'begin':
            self.optional_command()
            self.token = self.scanner.nextToken()
            if self.token.getContent == 'end':
                return
        else:
            raise Exception(f"Erro sintatico: Espera-se begin e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
            
    def optional_command(self):
        self.list_command()
        return

    def list_command(self):
        self.command()
        self.list_command_l()

    def list_command_l(self):
        self.token = self.scanner.nextToken()
        if self.token.getContent == ';':
            self.command()
            self.list_command_l()
        else:
            return
    
    def command(self):
        self.token = self.scanner.nextToken()
        if self.token.getType() == TokenType.IDENTIFIER:
            self.token = self.scanner.nextToken()
            if self.token.getType() == TokenType.ASSIGN:
                self.expression()
        else:
            self.procedure_activation()
            self.command_com()
            self.token = self.scanner.nextToken()
            if self.token.getContent() == 'if':
                self.expression()
                self.token = self.scanner.nextToken()
                if self.token.getContent() == 'then':
                    self.command()
                    self.part_else()
        
    def part_else(self):
        self.token = self.scanner.nextToken()
        if self.token.getContent == 'else':
            self.command()
        else:
            return
    
    def variable(self):
        self.token = self.scanner.nextToken()
        if self.token.getType() == TokenType.IDENTIFIER:
            return
        else:
            raise Exception(f"Erro sintatico: Espera-se uma variavel e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        
    def procedure_activation(self):
        self.token = self.scanner.nextToken()
        if self.token.getType == TokenType.IDENTIFIER:
            self.token = self.scanner.nextToken()
            if self.token.getContent() == '(':
                self.list_expression()
                self.token = self.scanner.nextToken()
                if self.token.getContent() == ')':
                    return
            else:
                return
        else:
            raise Exception(f"Erro sintatico: Espera-se uma variavel e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
            
    def list_expression(self):
        self.expression()
        self.list_expression_l()
    
    def list_expression_l(self):
        self.token = self.scanner.nextToken()
        if self.token.getContent() == ',':
            self.expression()
            self.list_expression_l()
        else:
            return       
    
    def expression(self):
        self.simple_expression()
        self.token = self.scanner.nextToken()
        if self.token.getType() == TokenType.REL_OP:
            self.simple_expression()
        else:
            return
    
    def simple_expression(self):
        self.term()
        self.signal()
        self.simple_expression()
        self.token = self.scanner.nextToken()
        if self.token.getType() == TokenType.ADD_OP:
            self.term()
        else:
            raise Exception(f"Erro sintatico: Espera-se um operador aditivo e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
    
    def term(self):
        self.factor()
        self.term()
        self.token = self.scanner.nextToken()
        if self.token.getType() == TokenType.MULT_OP:
            self.factor()
            return
        else:
            raise Exception(f"Erro sintatico: Espera-se um operador multiplicativo e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
         
    def factor(self):
        self.token = self.scanner.nextToken()
        if self.token.getType() == TokenType.IDENTIFIER:
            self.token = self.scanner.nextToken()
            if self.token.getContent() == '(':
                self.list_expression()
                self.token = self.scanner.nextToken()
                if self.token.getContent() == ')':
                    return
            elif self.token.getType() == TokenType.INTEGER or self.token.getType() == TokenType.REAL or self.token.getType() == TokenType.BOOLEAN:
                return
            return
        elif self.token.getContent() == '(': 
            self.expression()
            self.token = self.scanner.nextToken()
            if self.token.getContent() == ')':
                return
        elif self.token.getContent() == 'not':
            self.factor()
            
    def signal(self):
        self.token = self.scanner.nextToken()
        if not self.token.getType() == TokenType.ADD_OP:
            raise Exception(f"Erro sintatico: Espera-se um operador aditivo e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
