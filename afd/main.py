from Scanner import Scanner
from Parser import Parser
from Semantic import Semantic

sc = Scanner('codes_example/code.txt')
parser = Parser(sc)
semantic = Semantic(parser)
try:
    parser.syntax()
    print("Compilation Successful!")
except Exception as e:
    print(f"Erro: {e}")
    raise