from Scanner import Scanner
from Token import Token
sc = Scanner('code.txt')
token = Token
try:
    while(token != None):
        token = sc.nextToken()
        if(token == None): break
        print(token)
except Exception as e:
    print(f"Erro: {e}")
    raise