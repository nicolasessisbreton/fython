from ..config import *

def make_print(p):
	for t in p.linecod.atomic_target:
		if t.is_stringx:
			print_stringx(p, t)

		elif t.is_opbol:
			print_opbol(p, t)

		elif t.is_ibol:
			print_ibol(p, t)

		else:
			p.linecod.throw(err.cannot_resolve_modifier, modifier=t.rep)


def print_opbol(p, opbol):
	fmt = opbol.modifier[0].args
	args = opbol.modifier[2].args
	print_format_args(p, opbol, fmt, args)

def print_ibol(p, ibol):
	fmt = ibol.target.args
	args = ibol.rest[0].args
	print_format_args(p, ibol, fmt, args)
	
def print_format_args(p, s, fmt, args):
	p != s.tbk_mark

	p != 'write({:s}, '.format(p.unit)

	for f in fmt:
		p != f
		p != '//'

	p.rstrip('//')

	p != p.advance

	p != ') '

	for a in args:
		p != '{:s}, '.format(a)

	p.rstrip(', ')

	p != s.newline

	p != s.tbk_emark

def print_stringx(p, stringx):
	p != stringx.tbk_mark

	p != 'write({unit:s}, "(a)"{advance:s}) '.format(
		unit = p.unit, 
		advance = p.advance,
	)

	p != stringx

	p != stringx.newline

	p != stringx.tbk_emark