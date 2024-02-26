from TokenType import TokenType
from Token import Token
class Scanner:
    wordsReserved = ["program", "var", "begin", "end", "if", "then", "else", "while", "do", "function", "procedure", "integer", "real", "boolean"]
    state = 0
    line = 1
    column = 0

    def __init__(self, fileName):
        self.arq = open(fileName, 'r')
        self.code = self.arq.read() + '\n'
        self.pos = 0

    def nextToken(self):
        currentChar = ''
        content = ""
        self.state = 0

        while(True):
            if(self.isEOF()): return None
            self.position(currentChar)
            currentChar = self.nextChar()
            match self.state:
                case 0:
                    if(self.isLetter(currentChar)):
                        content = content + currentChar
                        self.state = 1
                    elif(self.isUnderline(currentChar)):
                        content = content + currentChar
                        self.state = 1
                    elif(self.isDelim(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.DELIM, content, self.line, self.column)
                    elif(self.isPoint(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.DELIM, currentChar, self.line, self.column)
                    elif(self.isTwoPoint(currentChar)):
                        content = content + currentChar
                        self.state = 8
                    elif(self.isDigit(currentChar)):
                        content = content + currentChar
                        self.state = 2
                    elif(self.isAddOp(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.ADD_OP, content, self.line, self.column)
                    elif(self.isMultOp(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.MULT_OP, content, self.line, self.column)
                    elif(self.isEqual(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.REL_OP, content, self.line, self.column)
                    elif(self.isGreater(currentChar)):
                        content = content + currentChar
                        self.state = 4
                    elif(self.isLess(currentChar)):
                        content = content + currentChar
                        self.state = 4
                    elif(self.isParentheses(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.DELIM, content, self.line, self.column)
                    elif(self.isOpenComment(currentChar)):
                        self.state = 7
                    elif(self.isSpace(currentChar)):
                        self.state= 0
                case 1:
                    if(self.isLetter(currentChar) or self.isDigit(currentChar) or self.isUnderline(currentChar)):
                        content = content + currentChar
                        self.state = 1
                    else:
                        self.back()
                        if(self.isReserved(content)):
                            return Token(TokenType.WORD_RESERVED, content, self.line, self.column)
                        elif(content == "or"):
                            return Token(TokenType.ADD_OP, content, self.line, self.column)
                        elif(content == "and"):
                            return Token(TokenType.MULT_OP_OP, content, self.line, self.column)
                        elif(content == "True"):
                            return Token(TokenType.BOOLEAN, content, self.line, self.column)
                        elif(content == "False"):
                            return Token(TokenType.BOOLEAN, content, self.line, self.column)
                        return Token(TokenType.IDENTIFIER, content, self.line, self.column)
                case 2:
                    if(self.isDigit(currentChar)):
                        content = content + currentChar
                        self.state = 2
                    elif(self.isPoint(currentChar)):
                        content = content + currentChar
                        self.state = 5
                    elif(self.isLetter(currentChar)):
                        raise Exception("Erro lexico: Numero malformado. Linha " + str(self.line) + ", coluna " + str(self.column))
                    else:
                        self.back()
                        return Token(TokenType.INTEGER, content, self.line, self.column)
                case 3:
                    if(self.isEqual(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.REL_OP, content, self.line, self.column)
                    else:
                        self.back()
                        return Token(TokenType.ASSIGN, content, self.line, self.column)
                case 4:
                    if(self.isEqual(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.REL_OP, content, self.line, self.column)
                    elif(content == "<" and self.isGreater(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.REL_OP, content, self.line, self.column)
                    else:
                        self.back()
                        return Token(TokenType.REL_OP, content, self.line, self.column)
                case 5:
                    if(self.isDigit(currentChar)):
                        content = content + currentChar
                        self.state = 5
                    elif(self.isLetter(currentChar)):
                        raise Exception("Erro lexico: Numero malformado. Linha " + str(self.line) + ", coluna " + str(self.column))
                    else:
                        self.back()
                        return Token(TokenType.REAL, content, self.line, self.column)
                case 6:
                    if(currentChar == '\n' or currentChar == '\r'):
                        self.state = 0
                    else: self.state = 6
                case 7:
                    if(self.isCloseComment(currentChar)): 
                        self.state = 0
                    else:
                        self.state = 7
                case 8:
                    if(self.isEqual(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.ASSIGN, content, self.line, self.column)
                    else:
                        self.back()
                        return Token(TokenType.DELIM, content, self.line, self.column)

    def position(self, currentChar):
        self.column = self.column + 1
        if(currentChar == '\n' or currentChar == '\r'):
            self.line = self.line + 1
            self.column = 0; 
            
    def isEOF(self):
        if self.pos >= len(self.code): 
            return True
        return False

    def back(self):
        self.pos = self.pos - 1
        
    def nextChar(self):
        if self.pos < len(self.code):
            result = self.code[self.pos]
            self.pos += 1
            return result
        else:
            return None
    
    def isLetter(self, currentChar):
        if currentChar is None:
            return False
        if 'a' <= currentChar <= 'z' or 'A' <= currentChar <= 'Z':
            return True
        return False

    def isAddOp(self, currentChar):
        if currentChar is None:
            return False
        if currentChar in ['+', '-']:
            return True
        return False
    
    def isMultOp(self, currentChar):
        if currentChar is None:
            return False
        if currentChar in ['*', '/']:
            return True
        return False

    def isEqual(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == '=':
            return True
        return False
    
    def isLess(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == '<':
            return True
        return False
    
    def isGreater(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == '>':
            return True
        return False

    def isParentheses(self, currentChar):
        if currentChar is None:
            return False
        if currentChar in ['(', ')']:
            return True
        return False

    def isDigit(self, currentChar):
        if currentChar is None:
            return False
        if '0' <= currentChar <= '9':
            return True
        return False


    def isPoint(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == '.':
            return True
        return False
    
    def isTwoPoint(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == ':':
            return True
        return False
    
    def isDelim(self, currentChar):
        if currentChar is None:
            return False
        if currentChar in [';', ',']:
            return True
        return False
    
    
    def isSpace(self, currentChar):
        if currentChar is None:
            return False
        if currentChar in [' ', '\n', '\t', '\r']:
            return True
        return False

    def isUnderline(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == '_':
            return True
        return False

    def isOpenComment(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == '{':
            return True
        return False

    def isCloseComment(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == '}':
            return True
        return False
    
    def isReserved(self, content):
        for word in self.wordsReserved:
            if content == word:
                return True
        return False
