from enum import Enum
from tkinter.tix import INTEGER
class TokenType(Enum):
	IDENTIFIER = 1
	INTEGER = 2
	REAL = 3
	REL_OP = 4
	ADD_OP = 5
	MULT_OP = 6
	DELIM = 7
	ASSIGN = 8
	WORD_RESERVED = 9
