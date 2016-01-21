from ..config import *
from ..resolve import *

def interfacepec(linecod):
	s = linecod
	b = s.b

	for m in s.modifier_only:
		b != m
		b != ' '

	b += 'interface'

	b.indent

	s.add_frame()

	s.contains_disable
	
	for x in s.childcod_target:
		resolve(x)
	
	s.pop_frame()

	b.dedent

	b += 'end interface'