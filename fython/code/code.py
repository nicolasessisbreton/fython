from fython.unit import *

class Code(Unit):
	unit = l.code

	def __init__(s, bofx):
		s.module = bofx.module
		s.lineno = bofx.lineno
		
		s.raw = []
		s.lexem = []

		s.linecod = []
	
		s ^ bofx	

	# +: add linecod
	def __add__(s, other):
		s ^ other

		if not other.is_eofx:
			s.linecod.append(other)

			if s.nb_linecod > 1:
				a, b = s.linecod[-2:]
				a.next_linecod = b
				b.previous_linecod = a

		return s

	def clone(s, module):
		bofx = s.raw[0].clone(module)

		c = Code(bofx)

		for n in s.raw[1:]:
			c + n

		return c