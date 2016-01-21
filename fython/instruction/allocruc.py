from ..config import *

def allocruc(linecod):
	s = linecod
	b = s.i

	default_size = get_default_size(linecod)

	for t in s.atomic_target:
		b != t.tbk_mark

		b != 'allocate( {:s} )'.format( adjust(t, default_size) )

		b != t.newline

		b != t.tbk_emark


def get_default_size(linecod):
	s = linecod.modifier[0] # alloc

	if s.is_namex:
		return ''

	elif s.is_funbol:
		return s.args[0]

	else:
		s.throw(err.cannot_resolve_modifier)

def adjust(t, default_size):
	if default_size:
		if t.is_namex:
			return '{:s}({:s})'.format(t, default_size)

		elif t.unit in [l.slicebol, l.funbol]:
			return t

		else:
			t.throw(err.cannot_resolve_modifier)

	else:
		return t
