from Scanner import Scanner
from Token import Token
from TokenType import TokenType
from Table import Table
from Parser import Parser
from Stack import Stack

class Semantic:
    def __init__(self, parser):
        self.parser = parser
        self.stack = parser.stack
        self.pct = parser.pct
    def semantic(self):
        self.parser.syntax()