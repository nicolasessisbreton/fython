from .data import Data
from string import ascii_lowercase as alpha

ndx = -1

def x():
	global ndx
	ndx += 1
	return alpha[ndx]


class Verbose(Data):
	def __init__(s, level):
		s.level = level

	def __getattr__(s, name):
		if not s.level:
			return 0
			
		x = globals()[name]
		return x in s.level


# verbosity level
fml = x()
lex = x()
mark_newlinex = x()
source_with_invisible = x()
source_with_invisible_and_fml = x()
unsafe_interpolation_lexem = x()
yacc = x()

all = alpha[:ndx]


