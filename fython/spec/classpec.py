from ..config import *
from ..resolve import *

def classpec(linecod):
	s = linecod

	s.is_classpec = 1
	
	s.name = get_name(s)
	s.value = s.name.value

	s.parent = get_parent(s)

	s.inheritance_tree = get_inheritance_tree(s)
	s.mro = get_mro(s)

	s.attribute = get_attribute(s)
	treat_attribute(s)

	s.linecod = get_linecod(s)

	add_ast(s)
	add_name(s)

	s.type = Buffer()

	s.add_frame()
	s.ast = s.module.ast[s.level]	
	
	s.contains_disable

	s.set_klass(s)

	treat_linecod(s, s.linecod)

	mro_linecod = get_mro_linecod(s)
	treat_linecod(s, mro_linecod)
	s.linecod.extend(mro_linecod)

	treat_method(s)

	s.pop_frame()
	
	if s.is_temp_element:
		if s.is_solid_element:
			make_production(s)

	else:
		make_production(s)

	remove_pre_registration(s)

def add_ast(s):
	s.add_ast(s.value, s)

def add_name(s):
	s.add_name(s.value)

def get_name(s):
	n = s.modifier[-2]
	if n.is_namex:
		return n

	else:
		return n.funx
		# funbol

def get_parent(s):
	s.spec_parent = s.get_spec_parent()
	if s.spec_parent:
		return s.frame_ast[s.spec_parent]

	elif s.value in s.frame_ast:
		return s.frame_ast[s.value]

def get_inheritance_tree(s):
	if s.parent:
		r = []

		for b in s.parent.inheritance_tree:
			c = b.clone(s.module)
			r.append(c)

		return r

	else:
		n = s.modifier[-2]	
		if n.is_namex:
			return []

		else:
			return n.args

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
		for x in c.linecod:
			if not x.is_rout:
				r.append(x)

	r.extend(s.childcod_target)

	return r

def treat_attribute(s):
	s.pre = Buffer(', ', newline=', ')

	for m in s.attribute:
		if m.is_funbol:
			if m.value == 'spec':
				continue

			else:
				s.pre += m

		elif m.is_namex:
			if m.value in ['temp', 'template']:
				s.is_temp_element = 1
				
			else:
				s.pre += m

		else:
			s.pre += m

	s.pre.rreplace(', ', ' ')

def treat_linecod(s, linecod):
	for x in linecod:
		if x.is_rout:
			add_method(s, x)

		else:
			s.redirect = s.type
			resolve(x)
			s.redirect = 0

def treat_method(s):

	for x in s.linecod:
		if x.is_rout:
			if s.is_temp_element:
				if not s.is_solid_element:
					x.is_temp_element = 1
			s.method_buffer_enable
			resolve(x)
			s.method_buffer_disable

def make_production(s):
	b = s.b
	b != 'type '
	b != s.pre
	b != ':: '
	b += s.name

	b.indent
	b *= s.type
	b.dedent

	b += 'end type'

def get_mro(s):
	mro = [] 

	for b in s.inheritance_tree:
		b = b.targetted_ast
		mro.append(b)

	return mro

def get_mro_linecod(s):
	r = []
	for base in s.mro:
		for linecod in base.linecod:
			if linecod.is_rout:
				if linecod.rout_name not in s.frame_ast:
					x = linecod.clone(s.module)
					r.append(x)

			elif linecod.is_varpec:
				included = []
				for name in linecod.name:
					if name.value not in s.frame_ast:
						included.append(name.value)

				if included:
					v = linecod.clone(s.module)
					v.included_varpec_name = included
					r.append(v)

			else:
				s.throw(
					err.only_attribute_or_method_can_be_inherited,
					inheritance_target = xep(linecod),
				)
	return r

def add_method(s, method):
	x = Data()
	x.is_module = 0
	x.is_classpec = 0
	x.is_routpec = 1
	x.is_varpec = 0
	x.is_pget = method.has_pget_attribute
	x.is_pset = method.has_pget_attribute
	x.used_as_pget = x.is_pget
	x.used_as_pset = x.is_pset

	s.ast[method.rout_name] = x

def remove_pre_registration(s):
	r = []
	for key, item in s.ast.items():
		if isinstance(item, Data):
			r.append(key)

	for key in r:
		del s.ast[key]