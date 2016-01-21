from fython.unit import *

class SemiBol(Unit):
	unit = l.semibol
	
	def __init__(s, a, semix, b):
		s.module = a.module
		s.lineno = a.lineno		

		s.raw = []
		s.lexem = []

		s.modifier = []

		s & a & semix & b


	# &: add modifier
	def __and__(s, x):
		s ^ x

		if x.is_semibol:
			s.modifier.extend(x.modifier)

		elif not x.is_semix:
			s.modifier.append(x)

		return s
		
	def clone(s, module):
		a = s.raw[0].clone(module)
		semix = s.raw[1].clone(module)
		b = s.raw[2].clone(module)

		i = SemiBol(a, semix, b)

		for x in s.raw[3:]:
			i & x

		return i

