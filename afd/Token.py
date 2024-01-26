class Token:
    def __init__(self, type, content, line):
        self.type = type
        self.content = content
        self.line = line

    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type

    def getContent(self):
        return self.content
    
    def setContent(self, content):
        self.content = content

    def __str__(self):
        return f"Token [type = {self.type}, content = {self.content}, line = {self.line}]"