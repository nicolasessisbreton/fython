from ..config import *

intrinsic_subroutine = [
	'open',
	'close',
	'inquire',
]

def elementruc(linecod):
	s = linecod
	b = s.i

	b != s.tbk_mark
	
	m = s.modifier[0]
	ruc = str(m)

	if m.is_dotbol:
		if m.need_call:
			b != 'call '

	elif s.has_funbol:
		if s.modifier[0].value not in intrinsic_subroutine:
			b != 'call '

	b != ruc

	b != s.newline
	
	b != s.tbk_emark
