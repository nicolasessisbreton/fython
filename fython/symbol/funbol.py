from fython.unit import *

class FunBol(Unit):
	unit = l.funbol
	
	def __init__(s, funx):
		s.module = funx.module
		s.lineno = funx.lineno

		s.raw = []
		s.lexem = []

		s.funx = funx
		s.value = funx.value
		s.url_value = s.value
		s.args = []

		s ^ funx

		s.klass_arg = 0
		s.is_coarray_varpec = 0
		s.coarray_ketbol = []

	# &: add modifier
	def __and__(s, other):
		s ^ other

		if s.is_coarray_varpec:
			s.coarray_ketbol.append(other)

		else:
			if other.unit not in [l.commax, l.rparx, l.lpcax]:
				s.args.append(other)

			if other.is_lpcax:
				s.is_coarray_varpec = 1

		return s
		
	def clone(s, module):
		funx = s.funx.clone(module)
		f = FunBol(funx)

		for a in s.raw[1:]:
			f & a.clone(module)
		
		return f			
		
	def __str__(s):
		b = Buffer()
		b != '{:s}('.format(s.funx)

		if s.klass_arg:
			b != s.klass_arg
			b != ','
			
		for m in s.args:
			b != m
			b != ','

		b.rstrip(',')
		b != ')'
	
		if s.is_coarray_varpec:
			b != '['
			for m in s.coarray_ketbol:
				b != m	
			b.rreplace(',]', ']')
			
		return str(b)


	@property
	def targetted_ast(s):
		return s.get_ast(s.value)	

	@property
	def guid_override(s):
		pass

	@guid_override.setter
	def guid_override(s, value):
		s.funx.guid_overwrite = value

	@property
	def use_value_as_guid(s):
		s.funx.guid_overwrite = s.value