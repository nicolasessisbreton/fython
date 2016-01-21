from ..config import *

def privateruc(linecod):
	s = linecod
	b = s.b

	b != 'private :: '

	for t in s.atomic_target:
		b != t 
		b != ', '

	b.rstrip(', ')

	b != s.newline