from ..config import *
from ..resolve import *

def fopruc(linecod):
	s = linecod
	b = s.i

	counter = s.modifier[-4]
	ketbol = s.modifier[-2]

	b != s.tbk_mark
	b != 'do concurrent ({:s}={:s}:{:s})'.format(
		counter,
		ketbol.modifier[1],
		ketbol.modifier[3],
	)

	b != s.newline
	
	s.indent

	for x in s.childcod_target:
		resolve(x)

	s.dedent

	b += 'end do'
	
	b != s.tbk_emark