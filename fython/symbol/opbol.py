from fython.unit import *

class OpBol(Unit):
	unit = l.opbol
	
	def __init__(s, a, b, c=None):
		s.module = a.module
		s.lineno = a.lineno
		s.value = ''		

		s.raw = []		
		s.lexem = []

		s.modifier = []

		s & a
		s & b
		if c:
			s & c

	# &: add modifier
	def __and__(s, other):
		s ^ other

		if other.is_opbol:
			s.modifier.extend(other.modifier)

		else:
			s.modifier.append(other)

		return s

	def clone(s, module):
		a = s.raw[0].clone(module)
		b = s.raw[1].clone(module)	

		o = OpBol(a, b)

		for m in s.raw[2:]:
			o & m.clone(module)

		return o

	def __str__(s):
		b = Buffer(newline='')
		for m in s.modifier:
			b += m
		return str(b)

