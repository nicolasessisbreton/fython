from ..config import *
from ..resolve import *

def whereruc(linecod):
	s = linecod

	b = s.i

	b != s.tbk_mark

	b != 'where ({:s})'.format(s.modifier_only_direct_production)
	b != s.newline

	s.indent

	s.tbk_mark_disable()

	for x in s.childcod_target:
		resolve(x)

	s.dedent		
	
	if not s.next_linecod_is_elwhere_or_else:
		b != 'end where'
		b != s.newline
		s.tbk_mark_enable()
		b != s.tbk_emark