from fython.unit import *

class EnumBol(Unit):
	unit = l.enumbol
	
	def __init__(s, colonx):
		s.module = colonx.module
		s.lineno = colonx.lineno		
		
		s.raw = []
		s.lexem = []

		s.modifier = []

		s ^ colonx

	# &: add modifier
	def __and__(s, other):
		s ^ other
		if other.is_semibol:
			s.modifier.extend(other.modifier)

		elif not other.is_newlinex:
			s.modifier.append(other)

		return s

	def clone(s, module):
		colonx = s.raw[0].clone(module)

		e = EnumBol(colonx)

		for m in s.raw[1:]:
			e & m.clone(module)

		return e