from Scanner import Scanner
from Token import Token
from TokenType import TokenType
from Table import Table
from Parser import Parser
class Semantic:
    parser = Parser
    def __init__(self, parser):
        self.parser = parser
    
    def semantic(self):
        self.parser.syntax()
        self.parser.stack.allElements()
