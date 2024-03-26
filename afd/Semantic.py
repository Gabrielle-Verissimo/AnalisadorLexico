from TokenType import TokenType

class Semantic:
    def __init__(self, parser):
        self.parser = parser
        self.stack = parser.stack

    def semantic(self):
        self.parser.syntax()
        self.type_checking()

    def type_checking(self):
        # Passamos por todos os elementos da pilha
        elements = self.stack.allElements()
        for element in elements:
            if element.getType() == 'assignment':
                self.check_assignment(element)
            elif element.getType() == 'arithmetic_operation':
                self.check_arithmetic_operation(element)

    def check_assignment(self, assignment):
        # Fazemos a verificação da compatibliidade de tipos para a atribuição
        variable_type = self.get_variable_type(assignment.getToken())
        value_type = self.get_expression_type(assignment.getNextToken())
        if variable_type != value_type:
            raise Exception(f"Incompatibilidade de tipos: Não é possível atribuir um valor do tipo '{value_type}' a uma variável do tipo '{variable_type}'")

    def check_arithmetic_operation(self, operation):
        # Verificamos se os tipos são compatíveis para operações artiméticas
        left_type = self.get_expression_type(operation.getLeftOperand())
        right_type = self.get_expression_type(operation.getRightOperand())

        # Verificamos se os tipos são inteiros ou reais 
        if left_type not in ['integer', 'real'] or right_type not in ['integer', 'real']:
            raise Exception(f"Incompatibilidade de tipos: As operações aritméticas devem ser realizadas apenas entre tipos numéricos (inteiro ou real)")

        # Verificamos se os tipos são compatíveis para a operação me especifico
        if left_type != right_type:
            raise Exception(f"Incompatibilidade de tipos: As operações aritméticas devem ser realizadas entre operandos do mesmo tipo (inteiro ou real)")

    def get_variable_type(self, variable_name):
        # Recuperamos o tipo da variável da pilha
        return self.stack.searchToken(variable_name)

    def get_expression_type(self, expression):
        # Recuperamos o tipo da expressão da pilha
        if expression == None:
            return None
        elif expression.getType() == TokenType.INTEGER:
            return 'integer'
        elif expression.getType() == TokenType.REAL:
            return 'real'
        elif expression.getType() == TokenType.BOOLEAN:
            return 'boolean'
        elif expression.getType() == TokenType.IDENTIFIER:
            return self.get_variable_type(expression.getContent())
