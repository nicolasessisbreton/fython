from ..config import *

def make_read(p):
	p != 'read({unit:s}, *) '.format(
		unit = p.unit,
	)

	for t in p.linecod.atomic_target:
		p != t
		p != ', '

	p.rstrip(', ')

	p != p.linecod.newline	