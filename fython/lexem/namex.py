from fython.unit import *

class NameX(Unit):
	unit = l.namex

	def __init__(s, t, module=None):
		Unit.__init__(s, t, module)
		
		s.pre_interpolation_value = t.value.value
		s.klass_arg = 0

	def __str__(s):
		if s.guid_overwrite:
			r = s.guid_overwrite

		else:
			r = s.module.get_guid_tag(s.value)

		if s.klass_arg:
			if s.is_klass_pset:
				r += '({:s}'.format(s.klass_arg)

			else:
				r += '({:s})'.format(s.klass_arg)

		return r

	@property
	def targetted_ast(s):
		return s.get_ast(s.value)	

	@property
	def guid_override(s):
		pass

	@guid_override.setter
	def guid_override(s, value):
		s.guid_overwrite = value

	@property
	def use_value_as_guid(s):
		s.guid_overwrite = s.value