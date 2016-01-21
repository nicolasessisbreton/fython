from fython.unit import *
from .strresolver import StrResolver

class DotBol(Unit):
	unit = l.dotbol
	
	def __init__(s, a, b, c=None):
		s.module = a.module
		s.lineno = a.lineno		

		s.raw = []
		s.lexem = []

		s.modifier = []
		s.args = []

		s & a & b
		if c:
			s & c

		s.is_klass_pset = 0
		s.is_iruc_target = 0		
		s.need_call = 0		

	# &: add modifier
	def __and__(s, other):
		s ^ other

		if other.is_dotbol:
			s.modifier.extend(other.modifier)
			s.args.extend(other.args)

		else:
			s.modifier.append(other)

			if not other.is_bdotx:
				s.args.append(other)

		return s

	def clone(s, module):
		a = s.raw[0].clone(module)
		b = s.raw[1].clone(module)

		d = DotBol(a, b)

		for m in s.raw[2:]:
			d & m.clone(module)

		return d


	@property
	def targetted_ast(s):
		ast = s.args[0].targetted_ast
		for t in s.args[1:]:
			alias = t.value
			if ast.is_module:
				ast = ast.ast[0][alias]
			else:
				ast = ast.ast[alias]

		return ast

	@property
	def url_value(s):
		r = ''
		for m in s.modifier:
			r += m.value
		return r

	def __str__(s):
		x = StrResolver(s)

		if x.target:
			return s.str_resolve(x)

		else:
			return s.str_fortran()

	def str_fortran(s):
		for a in s.args:
			a.use_value_as_guid

		b = Buffer(newline='')
		for a in s.args:
			b += a
			b += '%'
		b.rstrip('%')
		return str(b)

	def str_resolve(s, x):
		if x.ndx == x.n:
			x.b.rstrip('%')
			return str(x.b)

		elif x.target.is_module:
			is_main = 0
			a = x.args[x.ndx+1]
			if a.is_funbol:
				if a.value == 'main':
					if x.ndx+2 == x.n:
						is_main = 1

			if is_main:
				x.b = Buffer()
				x.b += 'call {:s}_main()'.format(x.target.module_guid)
				return str(x.b)

			else:
				x.module = x.target
				x.advance
				return s.str_resolve(x)

		elif x.target.is_routpec:
			s.need_call = 1
			
			if x.klass:
				x.cargs.use_value_as_guid

				x.b.rstrip('%')
				x.cargs.klass_arg = str(x.b)

				x.b = Buffer()
				x.b != x.module_name[x.klass.value]
				x.b != '_'

				if s.is_iruc_target:
					if x.target.used_as_pset:
						x.b != setpfx
						x.cargs.is_klass_pset = 1
						s.is_klass_pset = 1

				elif x.target.used_as_pget:
					x.b != getpfx


				x.b != x.cargs

			else:
				x.cargs.guid_override = x.module_name[x.alias]
				x.b += x.cargs
			
			x.ndx += 1
			if x.ndx == x.n:
				return s.str_resolve(x)

			else:
				s.throw(err.a_function_cannot_be_dotted)

		elif x.target.is_varpec:
			if x.klass:
				x.cargs.use_value_as_guid
				x.b != x.module_name[x.klass.value]
				x.b != '_'

			elif x.target.is_self:
				x.klass = x.module_ast[x.target.typename.value] 
				x.module = x.klass.module
				x.cargs.use_value_as_guid

			elif x.alias in x.module_name:
				x.cargs.guid_override = x.module_name[x.alias]
				
			else:
				x.cargs.use_value_as_guid

			x.b += x.cargs

			# next step 
			if x.target.is_intrinsic_type:
				x.ndx += 1
				if x.ndx == x.n:
					return s.str_resolve(x)

				else:
					s.throw(
						err.intrinsic_type_cannot_be_dotted,
						target = x.alias,
					)

			elif x.target.typename.value in x.module_ast: 
				x.klass = x.module_ast[x.target.typename.value]
				x.module = x.klass.module
				x.advance
				return s.str_resolve(x)

			else:
				# is either non-defined or in a template
				# abandonning resolution
				for i in range(x.ndx+1, x.n):
					x.args[i].use_value_as_guid
					x.b != x.args[i]
				x.b.rstrip('%')
				return str(x.b)


		else:	
			s.throw(err.invalid_url, url=s.url_value)