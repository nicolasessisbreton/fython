from fython.unit import *

class SliceBol(Unit):
	unit = l.slicebol
	
	def __init__(s, slicex):
		s.module = slicex.module
		s.lineno = slicex.lineno

		s.raw = []
		s.lexem = []

		s.slicex = slicex
		s.value = slicex.value
		s.args = []

		s ^ slicex

		s.is_klass_pset = 0

		s.is_coarray_varpec = 0
		s.has_coarray_ketbol = 0
		s.coarray_ketbol = []

	# &: add modifier
	def __and__(s, other):
		s ^ other

		if s.has_coarray_ketbol:
			s.coarray_ketbol.append(other)

		else:
			if other.unit not in [l.commax, l.rketx, l.lkcax]:
				s.args.append(other)

			if other.is_lkcax:
				s.has_coarray_ketbol = 1

		return s

	def clone(s, module):
		slicex = s.slicex.clone(module)
		
		c = SliceBol(slicex)

		for m in s.raw[1:]:
			c & m.clone(module)

		return c

	def __str__(s):
		if s.is_coarray:
			if s.coarray_ketbol:
				return s.coarray_with_ketbol_production
			else:
				return s.coarray_without_ketbol_production

		else:
			return s.array_production

	@property
	def array_production(s):
		b = Buffer()
		b != '{:s}('.format(s.slicex)

		for m in s.args:
			b != m
			b != ','


		b.rstrip(',')
		b != ')'

		return str(b)

	@property
	def coarray_with_ketbol_production(s):
		b = Buffer(s.array_production)

		b != '['

		for m in s.coarray_ketbol:
			b != m

		b.rreplace(',]', ']')
		
		return str(b)

	@property
	def coarray_without_ketbol_production(s):
		b = Buffer()
		b != '{:s}['.format(s.slicex)

		for m in s.raw[1:]:
			b != m

		b.rreplace(',]', ']')

		return str(b)

	@property
	def guid_override(s):
		pass

	@guid_override.setter
	def guid_override(s, value):
		s.slicex.guid_overwrite = value

	@property
	def use_value_as_guid(s):
		s.slicex.guid_overwrite = s.value

	@property
	def targetted_ast(s):
		return s.get_ast(s.value)	


	@property
	def is_coarray(s):
		if s.has_coarray_ketbol or s.is_coarray_varpec:
			return 1
		ast = s.ast_target

		if ast:
			return s.value in ast.coarray_names