from fython.unit import *
from fython.import_py import *

class LineCod(Unit):
	unit = l.linecod
	
	def __init__(s, linefeedx):
		s.module = linefeedx.module
		s.lineno = linefeedx.value
	
		s.raw = []	
		s.lexem = []
		
		s.modifier = []

		s ^ linefeedx	

		# helper
		s.is_module = 0
		s.is_classpec = 0
		s.is_varpec = 0
		s.is_routpec = 0
		
		s.next_linecod = None
		s.previous_linecod = None

		s.is_self = 0
		s.included_varpec_name = 0
		
		s.is_import_py = 0				
		
		s.used_as_pset = 0		
		s.used_as_pget = 0

		s.is_temp_element = 0
		s.is_solid_element = 0
		s.is_noprod_element = 0	
		
	# &: modifier added
	def __and__(s, other):
		s ^ other

		if other.is_terminal:
			s.modifier.append(other)
			
			if s.has_import:
				import_py(s)

		elif other.is_semibol:
			s.modifier.extend(other.modifier)

		else:
			s.modifier.append(other)

		return s

	def clone(s, module):
		linefeedx = s.raw[0].clone(module)

		c = LineCod(linefeedx)

		for m in s.raw[1:]:
			c & m.clone(module)

		return c
	
	# property	
	@property
	def is_elif_or_else(s):
		r = s.first_modifier_value in [l.elifk, l.elsek]
		return r

	@property
	def is_if_or_elif(s):
		r = s.first_modifier_value in [l.ifk, l.elifk]
		return r

	@property
	def is_elwhere_or_else(s):
		r = s.first_modifier_value in [l.elwhere, l.elsek]
		return r

	@property
	def is_where_or_elwhere(s):
		r = s.first_modifier_value in [l.where, l.elwhere]
		return r

	@property
	def next_linecod_is_elif_or_else(s):
		if s.next_linecod:
			return s.next_linecod.is_elif_or_else

	@property
	def next_linecod_is_elwhere_or_else(s):
		if s.next_linecod:
			return s.next_linecod.is_elwhere_or_else

	@property
	def previous_linecod_is_if_or_elif(s):
		if s.previous_linecod:
			return s.previous_linecod.is_if_or_elif

	@property
	def previous_linecod_is_where_or_elwhere(s):
		if s.previous_linecod:
			return s.previous_linecod.is_where_or_elwhere

	@property
	def next_linecod_is_packagebol(s):
		if s.next_linecod:
			return s.next_linecod.is_packagebol

	@property
	def is_packagebol(s):
		return s.modifier[0].unit == l.packagebol

	@property
	def is_rout(s):
		return s.lexem[1].value.value == l.defk

	@property
	def is_class(s):
		return s.lexem[1].value.value == l.classk

	def get_spec_parent(s):
		for m in s.modifier:
			if m.is_funbol:
				if m.value == 'spec':
					return m.args[0].value

	@property
	def has_spec_attribute(s):
		for m in s.modifier_only_for_rout:
			if m.is_funbol:
				if m.value == 'spec':
					return 1

	@property
	def rout_name(s):
		return s.modifier[-2].value

	@property
	def has_import(s):
		x = s.modifier[0]
		if x.is_namex:
			return x.value == l.importk

	@property
	def has_ibol(s):
		return s.modifier[0].is_ibol


	@property
	def has_funbol(s):
		return s.modifier[0].is_funbol

	@property
	def has_pget_attribute(s):
		for m in s.modifier_only_for_rout:
			if m.is_namex:
				if m.value == 'pget':
					return 1

	@property
	def has_pset_attribute(s):
		for m in s.modifier_only_for_rout:
			if m.is_namex:
				if m.value == 'pset':
					return 1

	@property
	def hash(s):
		return s.modifier[0].hash # packagebol

	@property
	def interpolation(s):
		return s.modifier[0].interpolation # packagebol

	@property
	def first_modifier_value(s):
		x = s.modifier[0]
		if x.is_opbol:
			return x.modifier[0].value

		elif x.unit in [l.namex, l.funbol, l.slicebol]:
			return x.value

		else:
			return ''

	# when fython.resolve.genericr finds its a ruc
	@property
	def adjust_opbol(s):
		if s.modifier[0].is_opbol:
			x = s.modifier[0].modifier.pop(0)
			s.modifier.insert(0, x)