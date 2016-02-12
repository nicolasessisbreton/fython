from ..config import *
from ..resolve import *

def elseruc(linecod):
	s = linecod
	b = s.i

	if s.previous_linecod_is_if_or_elif:
		b != 'else'
		b != s.newline
		end = 'end if'

	elif s.previous_linecod_is_where_or_elwhere:
		b != 'else where'
		b != s.newline
		end = 'end where'

	else:
		s.throw(err.else_without_if_elif_where_or_elwhere)	

	s.indent

	for x in s.childcod_target:
		resolve(x)

	s.dedent
	
	b != end
	b != s.newline

	b != s.tbk_emark