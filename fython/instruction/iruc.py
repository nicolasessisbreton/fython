from ..config import *

operator_inplace = {
	# bitwise
	'<<=' : 'lshift',
	'&='  : 'iand',
	'^='  : 'ieor',
	'|='  : 'ior',
	'>>=' : 'rshift',

	# min max
	'++=' : 'max',
	'--=' : 'min',
}

def iruc(linecod):
	s = linecod.modifier[0] # ibol
	b = s.i

	b != s.tbk_mark

	rest = Buffer()
	for m in s.rest:
		rest != m	

	iop = s.iop.value

	s.target.is_iruc_target = 1
	
	target = str(s.target)

	if s.target.is_klass_pset:
		if iop.startswith('='):
			if iop == '=>':
				s.throw(err.cannot_set_reference_with_a_property_setter)

			b != 'call {target:s}, {rest:s})'.format(
				target = target, 
				iop = iop, 
				rest = rest,
			)

		else:

			target_get = target.replace('_set_', '_get_') + ')'

			b != 'call {target_set:s}, {target_get:s} {op:s} ({rest:s}))'.format(
				target_set = target,
				target_get = target_get,
				op = iop[:-1],
				rest = rest,
			)

	else:
		if iop.startswith('='):
			b != '{target:s} {iop:s} {rest:s}'.format(
				target = target, 
				iop = iop, 
				rest = rest,
			)

		elif iop in operator_inplace:
			b != '{target:s} = {iop:s}({target:s}, {rest:s})'.format(
				target = target, 
				iop = operator_inplace[iop], 
				rest = rest,
			)

		else:

			b != '{target:s} = {target:s} {op:s} ({rest:s})'.format(
				target = target,
				op = iop[:-1],
				rest = rest,
			)

	b != s.newline
	
	b != s.tbk_emark