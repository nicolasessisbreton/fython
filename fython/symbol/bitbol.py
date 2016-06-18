from fython.unit import *

bitwise_function = {
	'<<' : 'lshift',
	'&'  : 'iand',
	'^'  : 'ieor',
	'|'  : 'ior',
	'>>' : 'rshift',
}

class BitBol(Unit):
	unit = l.bitbol
	
	def __init__(s, left, op, right):
		s.module = left.module
		s.lineno = left.lineno
		s.value = ''		

		s.raw = [left, op, right]
		s.lexem = [left, op, right]
		s.modifier = [left, op, right]

		s.left = left
		s.op = op
		s.right = right

	def clone(s, module):
		return BitBol(s.left, s.op, s.right)

	def __str__(s):
		b = Buffer(newline='')

		b += bitwise_function[s.op.value]
		b += '('
		b += s.left
		b += ','
		b += s.right
		b += ')'

		return str(b)

