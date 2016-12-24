from ..config import *

def make_read(p):
	p != 'read({unit:s}, {fmt:s} {iostat:s}) '.format(
		unit = p.unit,
		fmt = p.fmt,
		iostat = p.iostat,
	)

	for t in p.linecod.atomic_target:
		p != t
		p != ', '

	p.rstrip(', ')

	p != p.linecod.newline	