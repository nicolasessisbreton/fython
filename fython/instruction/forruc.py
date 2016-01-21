from ..config import *
from ..resolve import *

def forruc(linecod):
	s = linecod
	b = s.i

	counter = s.modifier[-4]
	ketbol = s.modifier[-2]

	b != s.tbk_mark
	b != 'do '

	for m in s.modifier[1:-4]:
		b != m
		b != ' '

	b != '{:s} = '.format(counter)
	for x in ketbol.modifier[1:-1]:
		b != x

	b != s.newline
	
	s.indent

	for x in s.childcod_target:
		resolve(x)

	s.dedent

	b += 'end do'
	
	b != s.tbk_emark