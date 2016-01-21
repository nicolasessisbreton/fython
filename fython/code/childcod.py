from fython.unit import *
from fython.module import *

class ChildCod(Unit):
	unit = l.childcod
	
	def __init__(s, indentx):
		s.module = indentx.module
		s.lineno = indentx.lineno

		s.raw = []
		s.lexem = []

		s.linecod = []
	
		s ^ indentx	

	# +: add linecod
	def __add__(s, other):
		s ^ other

		if not other.is_dedentx:
			s.linecod.append(other)

			if s.nb_linecod > 1:
				a, b = s.linecod[-2:]
				a.next_linecod = b
				b.previous_linecod = a

		return s

	def clone(s, module):
		indentx = s.raw[0].clone(module)
		c = ChildCod(indentx)

		for n in s.raw[1:]:
			c + n.clone(module)

		return c
		
	def __repr__(s):
		if len(s.linecod) == 0:
			r = '{:s}({:d}, )'.format(
					s.cname,
					s.lineno,
			)

		elif len(s.linecod) == 1:
			r = '{:s}({:d}, {:s})'.format(
					s.cname,
					s.lineno,
					s.linecod[0].rep,
			)

		else:
			r = '{:s}({:d}, {:s}>{:s})'.format(
					s.cname,
					s.lineno,
					s.linecod[0].rep,
					s.linecod[-1].rep,
			)

		return r
