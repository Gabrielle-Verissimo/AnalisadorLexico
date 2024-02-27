from Scanner import Scanner
from Parser import Parser

sc = Scanner('code.txt')
parser = Parser(sc)

try:
    parser.syntax()
    print("Compilation Successful!")
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