from ..config import *
from ..resolve import *

def errorruc(linecod):
	s = linecod
	b = s.i
	
	b != s.tbk_mark

	for m in s.modifier:
		b != m
		b != ' '

	b != s.newline

	b != s.tbk_emark