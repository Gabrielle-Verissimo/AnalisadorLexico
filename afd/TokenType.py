from enum import Enum
class TokenType(Enum):
	IDENTIFIER = 1
	INTEGER = 2
	REAL = 3
	REL_OP = 4
	ADD_OP = 5
	MULT_OP = 6
	DELIM = 7
	ASSIGN = 8
	BOOLEAN = 9
	WORD_RESERVED = 10
