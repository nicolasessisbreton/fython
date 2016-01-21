from ..config import *
from ..resolve import *

def ifruc(linecod):
	s = linecod
	b = s.i
	
	b != s.tbk_mark

	b != 'if ({:s}) then'.format(s.modifier_only_direct_production)
	b != s.newline

	s.indent

	for x in s.childcod_target:
		resolve(x)

	s.dedent
	
	if not s.next_linecod_is_elif_or_else:
		b != 'end if'
		b != s.newline
		b != s.tbk_emark