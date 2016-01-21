from fython.unit import *

class IBol(Unit):
	unit = l.ibol
	
	def __init__(s, element, iopx):
		s.module = element.module
		s.lineno = element.lineno
		
		s.raw = []
		s.lexem = []

		s.target = element
		s.iop = iopx
		s.rest = []

		s ^ element ^ iopx

	# &: add modifier
	def __and__(s, other):
		s ^ other
		s.rest.append(other)
		return s

	def clone(s, module):
		target = s.target.clone(module)
		iopx = s.iop.clone(module)

		i = IBol(target, iopx)

		for m in s.raw[2:]:
			i & m.clone(module)

		return i			
		
	def __str__(s):
		b = Buffer(newline=' ')
		b += str(s.target)	
		b += str(s.iop)

		for r in s.rest:
			b += str(r)

		b != s.newline

		return str(b)

	def __repr__(s):
		r = '{:s}({:d}, {:s}>{:s})'.format(
				s.cname,
				s.lineno,
				str(s.lexem[0].value.value),
				str(s.lexem[-2].value.value),
		)

		return r

	@property
	def url_value(s):
		t = s.target
		if not t.is_dotbol:
			s.throw(err.left_element_in_aliased_import_is_not_an_url)
		return t.url_value