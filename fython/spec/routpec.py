from ..config import *
from ..resolve import *

def routpec(linecod):
	s = linecod

	s.is_routpec = 1
	
	s.name = get_name(s)
	s.value = s.name.value

	s.parent = get_parent(s)

	s.attribute = get_attribute(s)
	treat_attribute(s)

	s.linecod = get_linecod(s)
	
	add_ast(s)
	add_name(s)

	s.body = Buffer()
	s.redirect = s.body

	s.add_frame()
	
	s.module.tbk_frame_rout[s.level] = s.value

	treat_linecod(s)

	s.pop_frame()

	s.redirect = 0
	
	if s.is_temp_element:
		if s.is_solid_element:
			make_production(s)

	else:
		make_production(s)

def get_parent(s):
	s.spec_parent = s.get_spec_parent()
	if s.spec_parent:
		return s.get_ast(s.spec_parent)

	elif s.klass:
		p = s.klass.parent
		if p:
			if s.value in p.ast:
				return p.ast[s.value]

	elif s.value in s.frame_ast:
		return s.frame_ast[s.value]

def make_production(s):
	b = s.b

	b != s.contains

	b != s.pre
	b != s.begin_tag

	if s.klass:
		b != s.klass.name
		b != '_'
		b != s.name

	else:
		b != s.name

	b != s.argument_prod

	b != s.post

	b != s.newline

	b.indent

	b != s.use_iso_c_binding

	b *= s.body

	b != s.tbk_eframe

	b.dedent

	b += s.end_tag

def get_attribute(s):
	r = []
	if s.parent:
		for m in s.parent.modifier_only_for_rout:
			c = m.clone(s.module)
			r.append(c)

	r.extend(s.modifier_only_for_rout)

	return r

def get_linecod(s):
	r = []

	if s.parent:
		c = s.parent.childcod.clone(s.module)
		r.extend(c.linecod)

	r.extend(s.childcod_target)

	return r

def treat_attribute(s):
	# pre post iso_c
	s.pre = Buffer(newline=' ')
	s.post = Buffer(' ', newline=' ')
	s.use_iso_c_binding = ''
	s.is_bindc = 0

	for m in s.attribute:
		if m.is_funbol:
			if m.value == 'iso':
				s.use_iso_c_binding = 'use iso_c_binding\n'
				s.post += 'bind(c)'
				s.is_bindc = 1

			elif m.value == 'bind':
				s.post += m
				s.is_bindc = 1

			elif m.value == 'spec':
				continue	

			else:
				s.pre += m

		elif m.is_namex:
			if m.value == 'pure':
				if s.release:
					s.pre += m

			elif m.value == 'elemental':
				s.pre += m
				if s.debug:
					s.pre += 'impure'

			elif m.value == 'temp':
				s.is_temp_element = 1
				
			elif m.value in ['pget', 'pset']:
				continue

			else:
				s.pre += m

		else:
			s.pre += m

def treat_linecod(s):
	s.argument = []
	s.argument_prod = Buffer('(', newline=',')
	s.result = 0
	s.is_wrappable = 1

	if s.klass:
		s.linecod[0].is_self = 1
		
	if s.is_pget or s.is_pset:
		s.is_wrappable = 0

	for x in s.linecod:
		resolve(x)
		
		if x.is_varpec:
			if x.is_self:
				n = x.name[0]	
				s.argument.append(n.value)
				s.argument_prod += n
				s.is_wrappable = 0

			elif x.is_argument:
				for n in x.name:
					s.argument.append(n.value)
					if n.is_namex:
						s.argument_prod += n
					else:
						s.argument_prod += n.funx

				if not x.is_wrappable:
					s.is_wrappable = 0

			elif x.is_result:
				n = x.name[0].value
				s.result = n
				s.post += 'result({:s})'.format(n)
				s.is_wrappable = 0

	s.argument_prod.rstrip(',')
	s.argument_prod != ')'

	if s.result:
		s.begin_tag = 'function '
		s.end_tag = 'end function'

	else:
		s.begin_tag = 'subroutine '
		s.end_tag = 'end subroutine'

	s.nb_argument = len(s.argument)	

def add_ast(s):
	s.add_ast(s.value, s)

def add_name(s):
	s.add_name(s.value)

def get_name(s):
	s.is_pget = 0
	s.is_pset = 0

	n = s.modifier[-2]

	if s.has_pget_attribute:
		if not n.value.startswith(getpfx):
			n.value = getpfx + n.value
		s.is_pget = 1

	elif s.has_pset_attribute:
		if not n.value.startswith(setpfx):
			n.value = setpfx + n.value
		s.is_pset = 1

	return n