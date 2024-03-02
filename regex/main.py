import re

wordsReserved = ["program", "var", "begin", "end", "if", "then", "else", "while", "do", "function", "procedure", "integer", "real", "boolean"]

patterns = [
    ('RESERVED_WORD_%s' % rw.upper(), r'\b%s\b' % rw) for rw in wordsReserved
] + [
    ('VARIABLE', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
    ('FLOAT', r'\b\d+\.\d+\b'),
    ('INTEGER', r'\b\d+\b'),      # Identificacao de inteiros
    ('ADD_OP', r'[-\+]'),              # Identificacao do operador +
    ('MULT_OP', r'[/\*]'),
    ('ASSIGN', r'(:=)'),
    ('DELIM', r'[(),.;:]'),
    ('COMMENT_INIT', r'\{'),            # Identificação de chaves abertas
    ('COMMENT_END', r'\}'),            # Identificação de chaves fechadas
    ('REL_OP', r'[<>]'),
    ('NEWLINE', r'\n|\r\n')# Identificação do sinal de maior
]

# Compilacao dos padores regex
token_regex = '|'.join('(?P<%s>%s)' % pair for pair in patterns)
lexer = re.compile(token_regex)

with open('regex/code.txt', 'r') as file:
    input_file = file.read()

# Tokenizacao (separacao dos tokens) do string de entrada
tokens = []
is_comment = False
column = 0
line = 1
qtd_tokens = 0
for match in lexer.finditer(input_file):
    for name, pattern in patterns:
        token = match.group(name)
        if token == '{' and is_comment == False:
            qtd_tokens = qtd_tokens + 1
            #qtd_tokens = match.end()
            is_comment = True
            break
        if token == '}' and is_comment:
            qtd_tokens = qtd_tokens + 1
            #qtd_tokens = match.end()
            is_comment = False
            break
        if token == '\n' or token == '\r':
            line = line + 1
            qtd_tokens = 0
            break
        if is_comment == False and token:
            qtd_tokens = qtd_tokens + 1
            column = match.end()
            tokens.append((name, token, line, column))
            break



# Mostrar resultado
for token in tokens:
    print(token)