from ..config import *
from ..resolve import *

def elwhereruc(linecod):
	s = linecod
	b = s.i

	b != 'else where ({:s})'.format(s.modifier_only_direct_production)
	b != s.newline

	s.indent

	for x in s.childcod_target:
		resolve(x)

	s.dedent		
	
	if not s.next_linecod_is_elwhere_or_else:
		b != 'end where'
		b != s.newline
		b != s.tbk_emark