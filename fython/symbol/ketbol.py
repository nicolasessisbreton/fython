from fython.unit import *

class KetBol(Unit):
	unit = l.ketbol
	
	def __init__(s, lketx):
		s.module = lketx.module
		s.lineno = lketx.lineno

		s.raw = []		
		s.lexem = []

		s.modifier = [lketx]

		s ^ lketx

		s.is_array = 0

	# &: add modifier
	def __and__(s, other):
		s ^ other
		s.modifier.append(other)

		if other.is_commax:
			s.is_array = 1

		return s

	def clone(s, module):
		lketx = s.raw[0].clone(module)

		k = KetBol(lketx)

		for m in s.raw[1:]:
			k & m.clone(module)
			
		return k

	def __str__(s):
		b = Buffer(newline='')
		for m in s.modifier:
			b += m

		b = str(b)

		if not s.is_array:
			b = '({:s})'.format(b[1:-1])

		return b

