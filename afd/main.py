from Scanner import Scanner
from Parser import Parser

sc = Scanner('Test3.pas')
parser = Parser(sc)

try:
    parser.syntax()
    print("Compilation Successful!")
except Exception as e:
    print(f"Erro: {e}")
    raise