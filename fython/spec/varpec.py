from ..config import *

intrinsic_type = {
	'real' : 'real', 
	'int': 'integer',
	'char': 'character',
	'bool': 'logical',
	'complex': 'complex',

	# need for spec interpolation reintrospectio
	'integer': 'integer',
	'character': 'character',
	'logical': 'logical'
}

wrappable_type = [
	'real',
	'int',
	'char',
	# need for spec interpolation reintrospectio
	'integer',
	'character',
]

def varpec(linecod):
	s = linecod

	make_ast(s)

	add_ast(s)
	add_name(s)

	make_production(s)

def make_ast(s):
	s.is_varpec = 1
	
	s.typename = get_typename(s)
	if s.typename.value in intrinsic_type:
		s.is_intrinsic_type = 1
		tname = intrinsic_type[s.typename.value]
		s.typename.value = tname # good for namex
		
		if s.typename.is_funbol:
			s.typename.funx.value = tname

	else:
		s.is_intrinsic_type = 0

	s.is_parameter = 0
	s.is_argument = 0
	s.is_result = 0
	s.is_bindc = 0

	s.pre = Buffer(',', newline=',')
	
	if s.is_self:
		modifier = s.modifier[1:-1]

	else:
		modifier = s.modifier_only

	for m in modifier:
		if m.is_namex:
			if m.value == 'cons':
				s.is_parameter = 1
				s.pre += 'parameter'
				
			elif m.value in ['in', 'out', 'inout']:
				s.is_argument = 1
				s.pre += 'intent({:s})'.format(m.value)

			elif m.value == 'arg':
				s.is_argument = 1

			elif m.value == 'res':
				s.is_result = 1

			else:
				s.pre += m

		if m.is_funbol:
			if m.value == 'bind':
				s.is_bindc = 1
				s.pre += m

			else:
				s.pre += m

	s.pre.rstrip(',')

	s.is_wrappable = (
		s.typename.value in wrappable_type 
		and 
		not s.is_parameter
		and
		not s.is_bindc
	)
			
	# name
	if s.is_self:
		s.name = [s.modifier[0]]

	else:
		s.name = []
		for t in s.atomic_target_name_only:
			if s.included_varpec_name:
				if t.value in s.included_varpec_name:
					s.name.append(t)
					
			else:
				s.name.append(t)

def add_ast(s):
	for n in s.name:
		s.add_ast(n.value, s)

def add_name(s):
	for n in s.name:
		s.add_name(n.value)

def make_production(s):
	b = Buffer()

	if s.is_intrinsic_type:
		b != s.typename
	else:
		b != 'type({:s})'.format(s.typename)

	b != s.pre

	root = str(b)

	if s.is_self:
		target = s.name
		
	else:
		target = s.atomic_target
	
	prefix = ''
	if s.klass:
		if not s.module.method_buffer_enable:
			prefix = '{:s}_'.format(s.klass.name)

	b = s.b
	for t in target:
		b != '{root:s} :: {prefix:s}{varname:s}'.format(
			root = root, 
			prefix = prefix,
			varname = t,
		)

		if not t.is_ibol:
			b != t.newline

def get_typename(s):
	if s.is_self:
		return s.klass.name

	else:
		n = s.modifier[0]
		if n.value == 'self':
			return s.klass.name
		else:
			return n