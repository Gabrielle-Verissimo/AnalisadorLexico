import re

# Define expressoes regulares para a identificacao de tokens
# Ver a API para entender a sintaxe das expressao regulares. Por exemplo, o que significa \d+?

wordsReserved = ["program", "var", "begin", "end", "if", "then", "else", "while", "do", "function", "procedure", "integer", "real", "boolean"]

patterns = [
    ('RESERVED_WORD_%s' % rw.upper(), r'\b%s\b' % rw) for rw in wordsReserved
] + [
    ('VARIABLE', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
    ('FLOAT', r'\b\d+\.\d+\b'),
    ('INTEGER', r'\b\d+\b'),      # Identificacao de inteiros
    #('NUMBER', r'[(\b\d+\.\d+\b)(\b\d+\b)]'),
    ('ADD_OP', r'[-\+]'),              # Identificacao do operador +
    ('MULT_OP', r'[/\*]'),
    ('ASSIGN', r'(:=)'),
    ('DELIM', r'[(),.;:]'),
    ('LBRACE', r'\{'),            # Identificação de chaves abertas
    ('RBRACE', r'\}'),            # Identificação de chaves fechadas
    ('REL_OP', r'[<>]'),                 # Identificação do sinal de maior
]

# Compilacao dos padores regex
token_regex = '|'.join('(?P<%s>%s)' % pair for pair in patterns)
lexer = re.compile(token_regex)

with open('code.txt', 'r') as file:
    input_file = file.read()

# Tokenizacao (separacao dos tokens) do string de entrada
tokens = []
for match in lexer.finditer(input_file):
    for name, pattern in patterns:
        token = match.group(name)
        if token:
            tokens.append((name, token))
            break

# Mostrar resultado
for token in tokens:
    print(token)