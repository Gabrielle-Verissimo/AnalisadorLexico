from Scanner import Scanner
from Token import Token
from Parser import Parser

sc = Scanner('code.txt')
token = Token
parser = Parser(sc)

try:
    while(token != None):
        token = parser.syntax()
        if(token == None): break
        print(token)
except Exception as e:
    print(f"Erro: {e}")
    raise
# try:
#     while(token != None):
#         token = sc.nextToken()
#         if(token == None): break
#         print(token)
# except Exception as e:
#     print(f"Erro: {e}")
#     raise