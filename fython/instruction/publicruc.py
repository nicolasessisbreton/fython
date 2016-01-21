from ..config import *

def publicruc(linecod):
	s = linecod
	b = s.b

	b != 'public :: '

	for t in s.atomic_target:
		b != t 
		b != ', '

	b.rstrip(', ')

	b != s.newline