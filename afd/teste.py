buffer = ['a', 'b', 'c', 'd']

x = 0
while(x < len(buffer)):
    print(buffer[x])
    x +=  1
    
    # def store_tokens(self):
    #     t = Token
    #     while(t != None):
    #         t = self.scanner.nextToken()
    #         self.buffer.append(t)
    #         if(t == None): break
    
    # def read_token(self):
    #     if self.next < len(self.buffer):
    #         self.token = self.buffer[next]
    #         self.next += 1
    #         return self.token
    #     else:
    #         return None