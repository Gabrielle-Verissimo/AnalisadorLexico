from Scanner import Scanner

class Parser:
    scanner = ''
    token = ''
    def __init__(self, scanner):
        self.scanner = scanner
        
    def syntax(self):
        self.token = self.scanner.nextToken()
        return self.token