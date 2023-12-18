from Scanner import Scanner
from Token import Token
sc = Scanner('code.txt')
token = Token
while(token != None):
    token = sc.nextToken()
    print(token)
