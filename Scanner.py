from TokenType import TokenType
from Token import Token
class Scanner:
    wordsReserved = ["if", "else", "int", "float", "print"]
    #code = ''
    state = 0
   # pos = 0
    line = 0
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
            currentChar = self.nextChar()
            match self.state:
                case 0:
                    if(self.isLetter(currentChar)):
                        content = content + currentChar
                        self.state = 1
                    elif(self.isUnderline(currentChar)):
                        content = content + currentChar
                        self.state = 1
                    elif(self.isDigit(currentChar)):
                        content = content + currentChar
                        self.state = 2
                    elif(self.isMathOp(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.MATH_OP, content)
                    elif(self.isAssignOp(currentChar)):
                        content = content + currentChar
                        self.state = 3
                    elif(self.isRelOp(currentChar)):
                        content = content + currentChar
                        self.state = 4
                    elif(self.isBoolOp(currentChar)):
                        content = content + currentChar
                        self.state = 7
                    elif(self.isParentheses(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.DELIM, content)
                    elif(self.isHash(currentChar)):
                        self.state = 6
                    elif(self.isSpace(currentChar)):
                        self.state= 0
                case 1:
                    if(self.isLetter(currentChar) or self.isDigit(currentChar) or self.isUnderline(currentChar)):
                        content = content + currentChar
                        self.state = 1
                    else:
                        self.back()
                        if(self.isReserved(content)):
                            return Token(TokenType.WORD_RESERVED, content)
                        return Token(TokenType.IDENTIFIER, content)
                case 2:
                    if(self.isDigit(currentChar)):
                        content = content + currentChar
                        self.state = 2
                    elif(self.isPoint(currentChar)):
                        content = content + currentChar
                        self.state = 5
                    elif(self.isLetter(currentChar)):
                        raise Exception("Erro")
                    else:
                        self.back()
                        return Token(TokenType.NUMBER, content)
                case 3:
                    if(self.isAssignOp(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.REL_OP, content)
                    else:
                        self.back()
                        return Token(TokenType.ASSIGN, content)
                case 4:
                    if(self.isAssignOp(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.REL_OP, content)
                    else:
                        self.back()
                        return Token(TokenType.REL_OP, content)
                case 5:
                    if(self.isDigit(currentChar)):
                        content = content + currentChar
                        self.state = 5
                    elif(self.isLetter(currentChar)):
                        raise Exception("Expected number")
                    else:
                        self.back()
                        return Token(TokenType.NUMBER, content)
                case 6:
                    if(currentChar == '\n' or currentChar == '\r'):
                        self.state = 0
                    else: self.state = 6
                case 7:
                    if(self.isBoolOp(currentChar)):
                        content = content + currentChar
                        return Token(TokenType.BOOL_OP, content)
                    else:
                        raise Exception("Operator booleano Malformed:")
                        
                    
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
            return None  # or some other way to handle the end of the string

    
    def isLetter(self, currentChar):
        if currentChar is None:
            return False
        if 'a' <= currentChar <= 'z' or 'A' <= currentChar <= 'Z':
            return True
        return False


    def isMathOp(self, currentChar):
        if currentChar is None:
            return False
        if currentChar in ['+', '-', '*', '/']:
            return True
        return False

    def isAssignOp(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == '=':
            return True
        return False

    def isRelOp(self, currentChar):
        if currentChar is None:
            return False
        if currentChar in ['>', '<', '!']:
            return True
        return False

    def isBoolOp(self, currentChar):
        if currentChar is None:
            return False
        if currentChar in ['&', '|']:
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

    def isHash(self, currentChar):
        if currentChar is None:
            return False
        if currentChar == '#':
            return True
        return False
    
    def isReserved(self, content):
        for word in self.wordsReserved:
            if content == word:
                return True
        return False
