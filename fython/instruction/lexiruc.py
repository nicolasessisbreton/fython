from ..config import *
from ..module import *
from ..resolve import *
from ..yacc import *

def lexiruc(linecod):
	s = linecod

	ibol = s.modifier[-1]
	new_name = ibol.target
	funbol = ibol.rest[0]
	
	t = funbol.targetted_ast

	if not ( t.is_routpec or t.is_classpec ):
		s.throw(err.lexical_interpolation_is_only_on_routine_or_class)

	t = t.clone(s.module)

	interpolation = get_interpolation(funbol)

	m = FyModule(1)

	m.lexem = [s.module.lexem_raw[0]] + t.lexem + [s.module.lexem_raw[-1]]

	m.expanded_lexem = []
	m.interpolant = s.module.interpolant
	m.stack = s.module.stack
	m.verbose = s.module.verbose
	m.source = s.module.source
	m.source_lines = s.module.source_lines
	m.debug = s.module.debug
	m.release = s.module.release
	m.url = s.url
	m.line_offset = s.lineno
	m.value = s.module.value

	m.package_interpolation.add_lexiruc_interpolation(interpolation)
	yacc(m)
	m.package_interpolation.pop_lexiruc_interpolation()

	interpolated = m.code[0]
	change_name(s, interpolated, new_name)
	interpolated.is_solid_element = 1
	
	resolve(interpolated)

def change_name(s, t, new_name):
	if t.is_rout:
		t.modifier[-2] = new_name

	elif t.is_class:
		n = t.modifier[-2]

		if n.is_namex:
			t.modifier[-2] = new_name

		else:
			n.value = new_name.value	
			n.funx.value = new_name.value
			t.modifier[-2] = n

def get_interpolation(t):
	if t.is_namex:
		r = {}

	else:
		r = {}
		for a in t.args:
			x = a.modifier[0].pre_interpolation_value
			y = []
			for u in a.modifier[2:]:
				y.extend(u.lexem)

			r[x] = y

	return r