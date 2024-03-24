from Scanner import Scanner
from Parser import Parser
from Semantic import Semantic

sc = Scanner('codes_example/Test4.pas')
parser = Parser(sc)
semantic = Semantic(parser)
try:
    semantic.semantic()
    #parser.syntax()
    print("Compilation Successful!")
except Exception as e:
    print(f"Erro: {e}")
    raise