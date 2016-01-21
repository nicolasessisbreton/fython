from ..config import *

def make_print(p):
	for t in p.linecod.atomic_target:
		if t.is_stringx:
			print_stringx(p, t)

		elif t.is_ibol:
			print_ibol(p, t)

		else:
			p.linecod.throw(err.cannot_resolve_modifier, modifier=t.rep)


def print_ibol(p, ibol):
	fmt = ibol.target.args
	args = ibol.rest[0].args

	p != ibol.tbk_mark

	p != 'write({:s}, '.format(p.unit)

	for f in fmt:
		p != f
		p != '//'

	p.rstrip('//')

	p != ') '

	for a in args:
		p != '{:s}, '.format(a)

	p.rstrip(', ')

	p != ibol.newline

	p != ibol.tbk_emark

def print_stringx(p, stringx):
	p != stringx.tbk_mark

	p != 'write({unit:s}, "(a)") '.format(
		unit = p.unit, 
	)

	p != stringx

	p != stringx.newline

	p != stringx.tbk_emark