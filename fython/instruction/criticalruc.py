from ..config import *
from ..resolve import *

def criticalruc(linecod):
	s = linecod
	b = s.i
	
	b != s.tbk_mark

	b != 'critical'
	b != s.newline

	s.indent

	for x in s.childcod_target:
		resolve(x)

	s.dedent
	
	b != 'end critical'
	b != s.newline
	b != s.tbk_emark