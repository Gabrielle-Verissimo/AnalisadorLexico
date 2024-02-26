from Scanner import Scanner
from Token import Token
from TokenType import TokenType

class Parser:
    scanner = Scanner
    buffer = []
    def __init__(self, scanner):
        self.scanner = scanner
        self.token = Token
        
    def nexToken(self):
        self.nexToken()
    
    def keep_buffer(self, token):
        self.buffer.append(token.getContent())
        
    def delete(self):
        self.buffer.pop()  
        
    def syntax(self):
        self.nexToken()
        if(self.token == None): return
        if self.token.getContent() == 'program':
            self.keep_buffer(self.token)
            print('buffer = ', self.buffer)
            self.nexToken()
            if(self.token.getType() == TokenType.IDENTIFIER):
                self.nexToken()
                if(self.token.getContent() == ';'):                    
                    self.dcl_var()
                    self.dcls_sub()
                    self.command_com()
                    self.nexToken()
                    if(self.token.getContent() == '.'):
                        return
                    else:
                        raise Exception(f"Erro sintatico: Espera-se o delimitador '.' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
                else:
                    raise Exception(f"Erro sintatico1: Espera-se o delimitador ';' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
            else:
                raise Exception(f"Erro sintatico: Espera-se um identificador e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        else:
            raise Exception(f"Erro sintatico: Espera-se 'program' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
                    
    def dcl_var(self):
        self.nexToken()        
        if(self.token.getContent() == 'var'):
            self.list_dcl_var()
        else:
            return
# list_dcl_var -> lista_de_identificadores:tipo;list_dcl_var_l
# list_dcl_var_l -> lista_de_identificadores:tipo;list_dcl_var_l|vazio
    def list_dcl_var(self):
        self.list_id()
        self.nexToken()
        if self.token.getContent() == ':':
            self.type()
            self.nexToken()
            if self.token.getContent() == ';':
                self.list_dcl_var_l()

    def list_dcl_var_l(self):
        self.list_id()
        self.nexToken()         
        if self.token.getContent() == ':':
            self.type()
            self.nexToken()
            if self.token.getContent() == ';':
                self.list_dcl_var_l()
        else:
            self.scanner.back()
            return
#list_id -> id list_id_l
#list_id_l -> ,id list_id | vazio             
    def list_id(self):
        self.nexToken()
        if(self.token.getType() == TokenType.IDENTIFIER):
            self.list_id_l()
    
    def list_id_l(self):
        self.nexToken()        
        if(self.token.getContent() == ','):
            self.nexToken()
            if(self.token.getType() == TokenType.IDENTIFIER):
                self.list_id_l()                
        else:
            self.scanner.back()            
            return
            
    def type(self):
        self.nexToken()
        if(self.token.getContent() == 'integer' or self.token.getContent() == 'real' or self.token.getContent() == 'boolean'):
            return
        else:
            raise Exception(f"Erro sintatico: Espera-se um tipo inteiro, real ou booleando e foi recebido '{self.token.getContent()}' do tipo '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")

#declarações_de_subprogramas → declaração_de_subprograma; declarações_de_subprogramas'
#declarações_de_subprogramas' → declaração_de_subprograma; declarações_de_subprogramas' | ε
    def dcls_sub(self):
        self.dcl_subprogram()
        self.nexToken()
        print('aqui: ', self.token)
        if self.token.getContent() == ';':
            self.dcls_sub_l()
        else:
            raise Exception(f"Erro sintatico2: Espera-se o delimitador ';' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")

    def dcls_sub_l(self):
        self.dcl_subprogram()
        self.nexToken()
        if self.token.getContent() == ';':
            self.dcls_sub_l()
        else:
            self.scanner.back()
            return
        
    def dcl_subprogram(self):
        self.nexToken()
        if(self.token.getContent() == 'procedure'):
            self.nexToken()
            if(self.token.getType() == TokenType.IDENTIFIER):
                self.arguments()
                self.nexToken()
                if(self.token.getContent() == ';'):
                    self.dcl_var()
                    self.dcls_sub()
                    self.command_com()
                else:
                    raise Exception(f"Erro sintatico3: Espera-se o delimitador ';' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")    
        else:
            print('else: ', self.token)
            self.scanner.back()
            return
                    
    def arguments(self):
        self.nexToken()
        if self.token.getContent() == '(':
            self.list_param()
            self.nexToken()
            if self.token.getContent() == ')':
                return
            else:
                raise Exception(f"Erro sintatico: espera-se o delimitador ')' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        else:
            self.scanner.back()
            return
#list_param -> list_id:tipo list_param_l
#list_param_l -> ;list_id:tipo list_param_l | vazio
    def list_param(self):
        self.list_id()
        self.nexToken()
        if self.token.getContent() == ':':
            self.type()
            self.list_param_l()
        else:
            raise Exception(f"Erro sintatico: espera-se o delimitador ':' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
     
    def list_param_l(self):
        self.nexToken()
        if self.token.getContent == ';':
            self.list_id()
            self.nexToken()
            if self.token.getContent == ':':
                self.type()
                self.list_param_l()
        else:
            self.scanner.back()
            return
        
    def command_com(self):
        self.nexToken()
        if self.token.getContent == 'begin':
            self.optional_command()
            self.nexToken()
            if self.token.getContent == 'end':
                return
            else:
                raise Exception(f"Erro sintatico: Espera-se 'end' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        else:
            raise Exception(f"Erro sintatico: Espera-se 'begin' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
            
    def optional_command(self):
        self.list_command()
        return
    
#lista_de_comandos → comando lista_de_comandos'
#lista_de_comandos' → ; comando lista_de_comandos' | ε
    def list_command(self):
        self.command()
        self.list_command_l()

    def list_command_l(self):
        self.nexToken()
        if self.token.getContent == ';':
            self.command()
            self.list_command_l()
        else:
            self.scanner.back()
            return
    
    def command(self):
        self.nexToken()
        if self.token.getType() == TokenType.IDENTIFIER:
            self.nexToken()
            if self.token.getType() == TokenType.ASSIGN:
                self.expression()
            else:
                raise Exception(f"Erro sintatico: Espera-se o sinal de atribuição ':=' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        else:
            self.procedure_activation()
            self.command_com()
            self.nexToken()
            if self.token.getContent() == 'if':
                self.expression()
                self.nexToken()
                if self.token.getContent() == 'then':
                    self.command()
                    self.part_else()
            elif self.token.getContent() == 'while':
                self.expression()
                self.nexToken()
                if self.token.getContent() == 'do':
                    self.command()
            else:
                raise Exception(f"Erro sintatico: Espera-se um 'if' ou um 'while' e foi recebido '{self.token.getContent()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        
    def part_else(self):
        self.nexToken()
        if self.token.getContent == 'else':
            self.command()
        else:
            self.scanner.back()
            return
    
    def variable(self):
        self.nexToken()
        if self.token.getType() == TokenType.IDENTIFIER:
            return
        else:
            raise Exception(f"Erro sintatico: Espera-se uma variavel e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
        
    def procedure_activation(self):
        self.nexToken()
        if self.token.getType == TokenType.IDENTIFIER:
            self.nexToken()
            if self.token.getContent() == '(':
                self.list_expression()
                self.nexToken()
                if self.token.getContent() == ')':
                    return
            else:
                self.scanner.back()
                return
        else:
            raise Exception(f"Erro sintatico: Espera-se uma variavel e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")

#lista_de_expressões → expressão lista_de_expressões'
#lista_de_expressões' → , expressão lista_de_expressões' | ε           
    def list_expression(self):
        self.expression()
        self.list_expression_l()
    
    def list_expression_l(self):
        self.nexToken()
        if self.token.getContent() == ',':
            self.expression()
            self.list_expression_l()
        else:
            self.scanner.back()
            return       
    
    def expression(self):
        self.simple_expression()
        self.nexToken()
        if self.token.getType() == TokenType.REL_OP:
            self.simple_expression()
        else:
            self.scanner.back()
            return

#expressão_simples → termo expressão_simples' | sinal termo expressão_simples'
#expressão_simples' → op_aditivo termo expressão_simples' | ε
    def simple_expression(self):
        self.term()
        self.simple_expression_l()  
        self.nexToken()
        if self.token.getContent() == '+' or self.token.getContent() == '-':
            self.term()
            self.simple_expression_l()
        else:
            self.scanner.back()
    
    def simple_expression_l(self):
        self.simple_expression_l()  
        self.nexToken()
        if self.token.getType() == TokenType.ADD_OP:
            self.term()
            self.simple_expression_l()
        else:
            self.scanner.back()
            return
        
    def term(self):
        self.factor()
        self.term()
        self.nexToken()
        if self.token.getType() == TokenType.MULT_OP:
            self.factor()
            return
        else:
            raise Exception(f"Erro sintatico: Espera-se um operador multiplicativo e foi recebido '{self.token.getType()}' na linha {self.scanner.line} e coluna {self.scanner.column}")
         
    def factor(self):
        self.nexToken()
        if self.token.getType() == TokenType.IDENTIFIER:
            self.nexToken()
            if self.token.getContent() == '(':
                self.list_expression()
                self.nexToken()
                if self.token.getContent() == ')':
                    return
            else:
                self.scanner.back()
                return
        elif self.token.getType() == TokenType.INTEGER or self.token.getType() == TokenType.REAL or self.token.getType() == TokenType.BOOLEAN:
            return
        elif self.token.getContent() == '(': 
            self.expression()
            self.nexToken()
            if self.token.getContent() == ')':
                return
        elif self.token.getContent() == 'not':
            self.factor()
