from ..config import *

def ompruc(linecod):
	s = linecod
	b = s.i

	b != '!$omp'

	for t in s.modifier_and_atomic_target:
		if t.is_namex:
			if t.value == l.fork:
				b &= 'do'

			else:
				b &= t
				
		else:
			b &= t

	b != linecod.newline