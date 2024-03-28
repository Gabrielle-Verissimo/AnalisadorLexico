from Scanner import Scanner
from Token import Token
from TokenType import TokenType
from Stack import Stack
from PcT import PcT
class Parser:
    scanner = Scanner
    buffer = []
    
    marked = []
    atual = []
    def __init__(self, scanner):
        self.scanner = scanner
        self.token = Token
        self.next = 0
        self.counter = 0
        self.stack = Stack()
        self.pct = PcT()
        self.store_tokens()
    
    def store_tokens(self):
        t = Token
        while(t != None):
            t = self.scanner.nextToken()
            if(t == None): break
            self.buffer.append(t)
    
    def read_token(self):
        if self.next < len(self.buffer):
            self.token = self.buffer[self.next]
            self.next += 1
            return self.token
        else:
            return None
        
    def back(self):
        self.next -= 1
        
    def syntax(self):    
        self.read_token()
        if(self.token == None): return
        if self.token.getContent() == 'program':
            self.stack.push('init_block', '$')
            self.read_token()
            if(self.token.getType() == TokenType.IDENTIFIER):
                self.stack.push('program_name', self.token)
                self.read_token()
                if(self.token.getContent() == ';'):
                    self.dcl_var()
                    self.dcls_subs()
                    self.command_com()
                    self.read_token()
                    if(self.token.getContent() == '.'):
                        return
                    else:
                        raise Exception(f"Erro sintatico: Esperava-se o final do programa com um '.', mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()}, coluna {self.token.getColumn()}. Certifique-se de que o programa esta corretamente finalizado.")
                else:
                    raise Exception(f"Erro sintatico: Esperava-se um ';' apos a declaracao de variavel, mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()}, coluna {self.token.getColumn()}. Insira o delimitador corretamente.")
            else:
                raise Exception(f"Erro sintatico: Apos 'program', esperava-se um identificador, mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()}, coluna {self.token.getColumn()}.")
        else:
            raise Exception(f"Erro sintatico: O arquivo deve começar com a palavra 'program', mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()}, coluna {self.token.getColumn()}.")
                    
    def dcl_var(self):
        self.read_token()        
        if(self.token.getContent() == 'var'):
            self.list_dcl_var()
            return
        else:
            self.back()
            return
# list_dcl_var -> lista_de_identificadores:tipo;list_dcl_var_l
# list_dcl_var_l -> lista_de_identificadores:tipo;list_dcl_var_l|vazio
    def list_dcl_var(self):
        self.list_id()
        self.read_token()
        if self.token.getContent() == ':':
            self.type()
            self.read_token()
            if self.token.getContent() == ';':
                self.list_dcl_var_l()
                return

    def list_dcl_var_l(self):
        self.read_token()
        if(self.token.getType() == TokenType.IDENTIFIER):
            self.back()
            self.list_id()
            self.read_token()             
            if self.token.getContent() == ':':
                self.type()
                self.read_token()
                if self.token.getContent() == ';':
                    self.list_dcl_var_l()
                    return
        else:
            self.back()
            return
#list_id -> id list_id_l
#list_id_l -> ,id list_id_l | vazio             
    def list_id(self):
        self.read_token()
        if(self.token.getType() == TokenType.IDENTIFIER):
            if(self.stack.existId(self.token.getContent())):
                raise Exception(f"Erro semântico: Já existe um identificador com o nome {self.token.getContent()}. Linha {self.token.getLine()} e coluna {self.token.getColumn()}")            
            self.stack.push('var', self.token)
            self.marked.append(self.token.getContent())
            self.list_id_l()
            return
        else:
            raise Exception(f"Erro sintatico: Espera-se uma variavel, mas foi encontrado '{self.token.getContent()}' do tipo '{self.token.getType()}' na linha {self.token.getLine()} e coluna {self.token.getColumn()}")               
            
    def list_id_l(self):
        self.read_token()        
        if(self.token.getContent() == ','):
            self.read_token()            
            if(self.token.getType() == TokenType.IDENTIFIER):
                if(self.stack.existId(self.token.getContent())):
                    raise Exception(f"Erro semântico: Já existe um identificador com o nome {self.token.getContent()}. Linha {self.token.getLine()} e coluna {self.token.getColumn()}")
                self.stack.push('var', self.token)
                self.marked.append(self.token.getContent())
                self.list_id_l()
                return
            else:
                raise Exception(f"Erro sintatico: Espera-se uma variavel, mas foi encontrado '{self.token.getContent()}' do tipo '{self.token.getType()}' na linha {self.token.getLine()} e coluna {self.token.getColumn()}")               
        else:
            self.back()            
            return
            
    def type(self):
        self.read_token()
        if(self.token.getContent() == 'integer' or self.token.getContent() == 'real' or self.token.getContent() == 'boolean'):
            for x in self.marked:
                self.pct.push(self.token.getContent(), x)
            self.marked = []
            return
        else:
            raise Exception(f"Erro sintatico: Tipo de dado invalido. Esperava-se 'integer', 'real' ou 'boolean', mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()}, coluna {self.token.getColumn()}.")

#declarações_de_subprogramas → declaração_de_subprograma; declarações_de_subprogramas'
#declarações_de_subprogramas' → declaração_de_subprograma; declarações_de_subprogramas' | ε
    def dcls_subs(self):
        self.dcl_subprogram()
        self.read_token()
        if self.token.getContent() == ';':
            self.dcls_subs_l()
        else:
            self.back()
            return

    def dcls_subs_l(self):
        self.dcl_subprogram()
        self.read_token()
        if self.token.getContent() == ';':
            self.dcls_subs_l()
        else:
            self.back()
            return
        
    def dcl_subprogram(self):
        self.read_token()
        if(self.token.getContent() == 'procedure'):
            self.read_token()
            if(self.token.getType() == TokenType.IDENTIFIER):
                if(self.stack.existId(self.token.getContent())):
                    raise Exception(f"Erro semântico: Já existe uma procedure com o nome {self.token.getContent()}. Linha {self.token.getLine()} e coluna {self.token.getColumn()}")
                self.stack.push('procedure_name', self.token)
                self.stack.push('init_block', '$')        
                self.arguments()
                self.read_token()
                if(self.token.getContent() == ';'):
                    self.dcl_var()
                    self.dcls_subs()
                    self.command_com()
                else:
                    raise Exception(f"Erro sintatico: Apos uma declaracao de subprograma, esperava-se ';', mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()}, coluna {self.token.getColumn()}.")
        else:
            self.back()
            return
                    
    def arguments(self):
        self.read_token()
        if self.token.getContent() == '(':
            self.list_param()
            self.read_token()
            if self.token.getContent() == ')':
                return
            else:
                raise Exception(f"Erro sintatico: Apos a lista de argumentos, esperava-se ')', mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()}, coluna {self.token.getColumn()}.")
        else:
            self.back()
            return
#list_param -> list_id:tipo list_param_l
#list_param_l -> ;list_id:tipo list_param_l | vazio
    def list_param(self):
        self.list_id()
        self.read_token()
        if self.token.getContent() == ':':
            self.type()
            self.list_param_l()
        else:
            raise Exception(f"Erro sintatico: esperava-se o delimitador ':', mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()} e coluna {self.token.getColumn()}. O delimitador é necessário para especificar o tipo da variável na declaração.")
     
    def list_param_l(self):
        self.read_token()
        if self.token.getContent() == ';':
            self.list_id()
            self.read_token()
            if self.token.getContent() == ':':
                self.type()
                self.list_param_l()
        else:
            self.back()
            return
        
    def command_com(self):
        self.read_token()
        if self.token.getContent() == 'begin':
            self.counter += 1
            self.optional_command()
            self.read_token()
            if self.token.getContent() == 'end':
                self.counter -= 1    
                return
            else:
                raise Exception(f"Erro sintatico: Esperava-se 'end' para finalizar um bloco 'begin', mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()}, coluna {self.token.getColumn()}.")
        else:
            raise Exception(f"Erro sintatico: Esperava-se 'begin' para iniciar um bloco, mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()} e coluna {self.token.getColumn()}")
            
    def optional_command(self):
        self.read_token()
        if self.token != 'end':
            self.back()
            self.list_command()
            return
        else:
            self.back()
            return
    
#lista_de_comandos → comando lista_de_comandos'
#lista_de_comandos' → ; comando lista_de_comandos' | ε
    def list_command(self):
        self.command()
        self.list_command_l()
        return

    def list_command_l(self):
        self.read_token() 
        if self.token.getContent() == ';':
            self.command()
            self.list_command_l()
        else:
            self.back()
            return
    
    def command(self):
        self.read_token()
        if self.token.getType() == TokenType.IDENTIFIER:
            tk = self.stack.searchToken(self.token.getContent())
            if(tk == None):
                raise Exception(f"Erro semântico: Identificador '{self.token.getContent()}' não encontrado. Linha {self.token.getLine()}, coluna  {self.token.getColumn()}.")
            if(tk == 'var'):
                self.atual = []
                self.atual.append(self.pct.searchToken(self.token.getContent()))
                self.atual.append(self.token.getContent())
            self.read_token()
            if self.token.getType() == TokenType.ASSIGN:                
                self.expression()
                return
            elif self.token.getContent() == '(':
                self.procedure_activation()
                return
            else:
                self.back()
        elif self.token.getContent() == 'if':
                self.expression()
                self.read_token()
                if self.token.getContent() == 'then':
                    self.command()
                    self.part_else()
        elif self.token.getContent() == 'while':
                self.expression()
                self.read_token()
                if self.token.getContent() == 'do':
                    self.command()
                    return
        elif self.token.getContent() == 'begin':
            self.back()
            self.command_com()
            return
        else:
            self.back()
            return
        
    def part_else(self): 
        self.read_token()
        if self.token.getContent() == 'else':
            self.command()
            return
        else:
            self.back()
            return
    
    def variable(self):  
        self.read_token()
        if self.token.getType() == TokenType.IDENTIFIER:
            return
        else:
            raise Exception(f"Erro sintatico: Espera-se uma variavel, mas foi encontrado '{self.token.getType()}' na linha {self.token.getLine()} e coluna {self.token.getColumn()}")
        
    def procedure_activation(self):
        self.list_expression()
        self.read_token()
        if self.token.getContent() == ')':
            return

#lista_de_expressões → expressão lista_de_expressões'
#lista_de_expressões' → , expressão lista_de_expressões' | ε           
    def list_expression(self):
        self.expression()
        self.list_expression_l()
    
    def list_expression_l(self): 
        self.read_token()
        if self.token.getContent() == ',':
            self.expression()
            self.list_expression_l()
        else:
            self.back()
            return       
    
    def expression(self):     
        self.simple_expression()
        self.read_token()
        if self.token.getType() == TokenType.REL_OP:
            self.simple_expression()
            return
        else:
            self.back()
            return

#expressão_simples → termo expressão_simples' | sinal termo expressão_simples'
#expressão_simples' → op_aditivo termo expressão_simples' | ε
    def simple_expression(self):  
        self.term()
        self.simple_expression_l()  
        self.read_token()
        if self.token.getContent() == '+' or self.token.getContent() == '-':
            self.term()
            self.simple_expression_l()
        else:
            self.back()
            return
    
    def simple_expression_l(self): 
        self.read_token()
        if self.token.getType() == TokenType.ADD_OP:
            self.term()
            self.simple_expression_l()
        else:
            self.back()
            return
        
#termo → fator termo'
#termo' → op_multiplicativo fator termo' | ε
    def term(self):  
        self.factor()
        self.term_l()
        return
    
    def term_l(self):
        self.read_token()
        if self.token.getType() == TokenType.MULT_OP:
            self.factor()
            self.term_l()
            return
        else:
            self.back()
            return

    def factor(self):
        self.read_token()
        if self.token.getType() == TokenType.IDENTIFIER:
            if(self.stack.searchToken(self.token.getContent()) == None):
                raise Exception(f"Erro semântico: Identificador '{self.token.getContent()}' não encontrado. Linha {self.token.getLine()}, coluna  {self.token.getColumn()}.")          
            if(self.pct.searchToken(self.token.getContent()) != self.atual[0]):
                raise Exception(f"Erro semântico: '{self.token.getContent()}' não é do mesmo tipo que '{self.atual[1]}'. Linha {self.token.getLine()}, coluna  {self.token.getColumn()}.")
            self.read_token()
            if self.token.getContent() == '(':
                self.list_expression()
                self.read_token()
                if self.token.getContent() == ')':
                    return
                else:
                    raise Exception(f"Espera-se fechamento de parênteses. Linha {self.token.getLine()}, coluna {self.token.getColumn()}")
            else:
                self.back()
                return
        elif self.token.getType() == TokenType.INTEGER:
            self.pct.push(self.token.getType(), self.token.getContent())
            if(self.atual[0] == 'real'): return         
            if(self.pct.searchToken(self.token.getContent()) != self.atual[0]):
                raise Exception(f"Erro semântico: '{self.token.getContent()}' não é do mesmo tipo que '{self.atual[1]}'. Linha {self.token.getLine()}, coluna  {self.token.getColumn()}.")
            return
        elif self.token.getType() == TokenType.REAL:
            self.pct.push(self.token.getType(), self.token.getContent())
            if(self.pct.searchToken(self.token.getContent()) != self.atual[0]):
                raise Exception(f"Erro semântico: '{self.token.getContent()}' não é do mesmo tipo que '{self.atual[1]}'. Linha {self.token.getLine()}, coluna  {self.token.getColumn()}.")
            return
        elif self.token.getType() == TokenType.BOOLEAN:
            self.pct.push(self.token.getType(), self.token.getContent())
            if(self.pct.searchToken(self.token.getContent()) != self.atual[0]):
                raise Exception(f"Erro semântico: '{self.token.getContent()}' não é do mesmo tipo que '{self.atual[1]}'. Linha {self.token.getLine()}, coluna  {self.token.getColumn()}.")
            return
        elif self.token.getContent() == '(':
            self.expression()
            self.read_token()
            if self.token.getContent() == ')':
                return
            else:
                raise Exception(f"Erro sintatico: Esperava-se o fechamento de parenteses ')', mas foi encontrado '{self.token.getContent()}' na linha {self.token.getLine()}, coluna {self.token.getColumn()}")
        elif self.token.getContent() == 'not':
            self.factor()
            return
        else:
            raise Exception (f"Erro semântico: expressão ilegal. Linha {self.token.getLine()} e coluna {self.token.getColumn()}")
            #raise Exception (f"Erro sintatico: Token inesperado '{self.token.getType()}' na linha {self.token.getLine()} e coluna {self.token.getColumn()}")
