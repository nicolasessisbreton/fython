from ..config import *

def make_read(p):
	p != 'read({unit:s}, * {iostat}) '.format(
		unit = p.unit,
		iostat = p.iostat,
	)

	for t in p.linecod.atomic_target:
		p != t
		p != ', '

	p.rstrip(', ')

	p != p.linecod.newline	