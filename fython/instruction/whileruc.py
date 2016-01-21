from ..config import *
from ..resolve import *

def whileruc(linecod):
	s = linecod

	b = s.i
	
	b != s.tbk_mark	

	b != 'do while ({:s})'.format(s.modifier_only_direct_production)
	b != s.newline

	s.indent

	for x in s.childcod_target:
		resolve(x)

	s.dedent

	b += 'end do'

	b != s.tbk_emark