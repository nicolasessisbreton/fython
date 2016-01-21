from ..config import *
from ..resolve import *

def inlineruc(linecod):
	s = linecod

	set_inline_mode(s)	

	if not s.produce:
		return

	for t in s.atomic_target:
		t = t.targetted_ast
		code = get_code(t)	
		for x in code:
			x = x.clone(s.module)
			resolve(x)

def set_inline_mode(s):
	s.produce = 1
	for m in s.modifier_only:
		if m.is_namex:
			v = m.value
			if v == 'debug':
				s.module.has_mode_dependent_inline = 1
				s.produce = s.debug
				break

			elif v == 'release':
				s.module.has_mode_dependent_inline = 1
				s.produce = s.release
				break

def get_code(t):
	if t.is_module:
		r = t.code.linecod

	elif t.is_class:
		r = t.linecod

	elif t.is_rout:
		r = t.linecod

	else:
		r = [t]
		# varpec

	return r
