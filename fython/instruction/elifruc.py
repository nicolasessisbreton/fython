from ..config import *
from ..resolve import *

def elifruc(linecod):
	s = linecod
	b = s.i
	
	b != 'else if ({:s}) then'.format(s.modifier_only_direct_production)
	b != s.newline

	s.indent

	for x in s.childcod_target:
		resolve(x)

	s.dedent

	if not s.next_linecod_is_elif_or_else:
		b != 'end if'
		b != s.newline
		b != s.tbk_emark