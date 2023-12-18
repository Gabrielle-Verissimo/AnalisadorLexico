from enum import Enum
class TokenType(Enum):
	IDENTIFIER = 1
	NUMBER = 2
	REL_OP = 3
	MATH_OP = 4
	BOOL_OP = 5
	DELIM = 6
	ASSIGN = 7
	WORD_RESERVED = 8
