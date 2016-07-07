from fython.unit import *

class ParBol(Unit):
	unit = l.parbol
	
	def __init__(s, lparx):
		s.module = lparx.module
		s.lineno = lparx.lineno
		
		s.value = lparx.value
		
		s.raw = []
		s.lexem = []
		s.modifier = [lparx]

		s ^ lparx

	# &: add modifier
	def __and__(s, other):
		s ^ other
		s.modifier.append(other)
		return s

	def clone(s, module):
		lparx = s.raw[0].clone(module)

		k = ParBol(lparx)

		for m in s.raw[1:]:
			k & m.clone(module)

		return k

	def __str__(s):
		b = Buffer(newline='')
		for m in s.modifier:
			b += m
		return str(b)

