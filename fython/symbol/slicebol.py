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
		
	# &: add modifier
	def __and__(s, other):
		s ^ other

		if other.unit not in [l.commax, l.rketx]:
			s.args.append(other)

		return s

	def clone(s, module):
		slicex = s.slicex.clone(module)
		
		c = SliceBol(slicex)

		for m in s.raw[1:]:
			c & m.clone(module)

		return c

	def __str__(s):
		b = Buffer()
		b != '{:s}('.format(s.slicex)

		for m in s.raw[1:]:
			b != m

		b.rreplace(']', ')')
		b.rreplace(',)', ')')

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
